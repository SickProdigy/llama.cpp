"""Synthetic loopback transport control using the actual current Hermes SDK/classifier."""
from pathlib import Path
import sys,os,json,time,threading,subprocess,urllib.request,urllib.error,hashlib
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
sys.path.insert(0,'/opt/hermes');os.environ['HERMES_HOME']='/tmp/synthetic-hermes-home';Path(os.environ['HERMES_HOME']).mkdir(exist_ok=True)
from openai import OpenAI,APIStatusError
from agent.error_classifier import classify_api_error
status=200
class Backend(BaseHTTPRequestHandler):
 def log_message(self,*a):pass
 def do_GET(self):self.reply()
 def do_POST(self):
  request=json.loads(self.rfile.read(int(self.headers.get('Content-Length',0))));self.reply(request.get('stream',False))
 def reply(self,stream=False):
  if status==400:body={'error':{'code':'context_length_exceeded','type':'invalid_request_error','message':'request (98346 tokens) exceeds the available context size (98304 tokens), try increasing it'}}
  elif status>=400:body={'error':{'code':'synthetic_'+str(status),'message':'synthetic backend failure '+str(status)}}
  else:body={'id':'synthetic','object':'chat.completion','created':0,'model':'synthetic','choices':[{'index':0,'message':{'role':'assistant','content':'transport-ok'},'finish_reason':'stop'}],'usage':{'prompt_tokens':8,'completion_tokens':2,'total_tokens':10}}
  raw=json.dumps(body).encode();content_type='application/json'
  if status==200 and stream:
   events=[{'id':'synthetic','object':'chat.completion.chunk','created':0,'model':'synthetic','choices':[{'index':0,'delta':{'role':'assistant','content':'transport-stream-ok'},'finish_reason':None}]},{'id':'synthetic','object':'chat.completion.chunk','created':0,'model':'synthetic','choices':[{'index':0,'delta':{},'finish_reason':'stop'}],'usage':{'prompt_tokens':8,'completion_tokens':2,'total_tokens':10}}]
   raw=(''.join('data: '+json.dumps(e)+'\n\n'for e in events)+'data: [DONE]\n\n').encode();content_type='text/event-stream'
  self.send_response(status);self.send_header('Content-Type',content_type);self.send_header('Content-Length',str(len(raw)));self.send_header('Retry-After','7');self.end_headers();self.wfile.write(raw)
backend=ThreadingHTTPServer(('127.0.0.1',11430),Backend);threading.Thread(target=backend.serve_forever,daemon=True).start();results=[]
try:
 for version in ['llm_proxy.py','llm_proxy_transparent.py']:
  root=Path('/tmp')/version;root.mkdir();env={**os.environ,'PILOT_LLM_RECORDS':str(root),'PILOT_LLM_BACKEND':'http://127.0.0.1:11430','PILOT_ALIAS':'synthetic'}
  child=subprocess.Popen([sys.executable,'/state/harness/'+version],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  try:
   status=200
   for _ in range(100):
    assert child.poll()is None,'Recorder process exited'
    try:urllib.request.urlopen('http://127.0.0.1:11431/health',timeout=.2).read();break
    except OSError:time.sleep(.05)
   else:raise AssertionError('Recorder did not become ready')
   client=OpenAI(base_url='http://127.0.0.1:11431/v1',api_key='synthetic-not-a-credential',max_retries=0,timeout=5)
   reply=client.chat.completions.create(model='synthetic',messages=[{'role':'user','content':'synthetic request'}],max_tokens=16)
   assert reply.choices[0].message.content=='transport-ok';rows=[]
   stream_reply=list(client.chat.completions.create(model='synthetic',messages=[{'role':'user','content':'synthetic stream'}],max_tokens=16,stream=True,stream_options={'include_usage':True}))
   assert ''.join(c.delta.content or ''for part in stream_reply for c in part.choices)=='transport-stream-ok'
   assert stream_reply[-1].usage.total_tokens==10
   for code in [400,429,503]:
    status=code
    for stream in [False,True]:
     try:client.chat.completions.create(model='synthetic',messages=[{'role':'user','content':'synthetic request'}],max_tokens=16,stream=stream)
     except APIStatusError as error:
      verdict=classify_api_error(error,provider='custom',model='synthetic',approx_tokens=98346,context_length=98304,num_messages=201,base_url='http://127.0.0.1:11431/v1')
      row={'backend_status':code,'SDK_status':error.status_code,'SDK_exception':type(error).__name__,'stream':stream,'native_reason':verdict.reason.value,'native_should_compress':verdict.should_compress}
      if version.endswith('_transparent.py'):
       assert error.status_code==code
       assert error.response.headers['retry-after']=='7'
       assert isinstance(error.body,dict)and error.body.get('code')==('context_length_exceeded'if code==400 else 'synthetic_'+str(code)),error.body
       if code==400:assert verdict.reason.value=='context_overflow'and verdict.should_compress
      else:assert error.status_code==502 and not verdict.should_compress
      rows.append(row)
     else:raise AssertionError('Expected backend error')
   # GET status/body must also survive.
   try:urllib.request.urlopen('http://127.0.0.1:11431/health',timeout=5)
   except urllib.error.HTTPError as error:assert error.code==(503 if version.endswith('_transparent.py')else 502)
   status=200
   time.sleep(.1);metrics=[json.loads(p.read_text())for p in root.glob('*.metrics.json')];assert len(metrics)==8
   if version.endswith('_transparent.py'):
    assert sorted(m.get('backend_http_status')for m in metrics if m.get('backend_http_status'))==[400,400,429,429,503,503]
    assert all(m.get('backend_error_response_sha256')for m in metrics if m.get('backend_http_status'))
    for m in metrics:
     if m.get('backend_http_status'):assert hashlib.sha256((root/(str(m['id']).zfill(5)+'.response.txt')).read_bytes()).hexdigest()==m['backend_error_response_sha256']
   results.append({'recorder':version,'source_sha256':hashlib.sha256(Path('/state/harness',version).read_bytes()).hexdigest(),'successful_JSON_response_preserved':True,'successful_SSE_content_and_usage_preserved':True,'GET_error_verified':True,'cases':rows})
  finally:child.terminate();child.wait(timeout=10)
finally:backend.shutdown();backend.server_close()
print(json.dumps({'passed':True,'actual_current_Hermes_SDK_and_error_classifier':True,'model_calls':0,'forge_mutations':0,'synthetic_loopback_only':True,'results':results}))
