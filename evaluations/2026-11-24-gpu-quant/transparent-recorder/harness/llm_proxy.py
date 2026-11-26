"""Fixed-destination model transport recorder. Never records authentication headers."""
import os,json,time,pathlib,threading,urllib.request,urllib.error,hashlib
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
ROOT=pathlib.Path(os.environ.get('PILOT_LLM_RECORDS','/records'));ROOT.mkdir(parents=True,exist_ok=True)
BACKEND=os.environ.get('PILOT_LLM_BACKEND','http://llama-pilot:11430').rstrip('/');ALIAS=os.environ.get('PILOT_ALIAS','qwen3.8-27b-hermes-adapted-iq3xxs');counter=0;counter_lock=threading.Lock();slot=threading.Lock()
class H(BaseHTTPRequestHandler):
 def log_message(self,*a):pass
 def do_GET(self):
  if self.path not in ('/v1/models','/health'):self.send_error(404);return
  try:
   with urllib.request.urlopen(BACKEND+self.path,timeout=10) as r:b=r.read();ct=r.headers.get('Content-Type','application/json')
   self.send_response(200);self.send_header('Content-Type',ct);self.end_headers();self.wfile.write(b)
  except Exception:self.send_error(502)
 def do_POST(self):
  global counter
  if self.path!='/v1/chat/completions':self.send_error(404);return
  size=int(self.headers.get('Content-Length',0))
  if not 0<size<=8*1024**2:self.send_error(413);return
  data=self.rfile.read(size)
  try:body=json.loads(data);assert body.get('model')==ALIAS
  except Exception:self.send_error(400);return
  with counter_lock:counter+=1;number=counter
  prefix=ROOT/(str(number).zfill(5));prefix.with_suffix('.request.json').write_text(json.dumps(body,ensure_ascii=False));record={'id':number,'purpose':self.headers.get('X-Pilot-Purpose','native-main-or-auxiliary'),'received_epoch':time.time(),'request_sha256':hashlib.sha256(data).hexdigest()};chunks=[];begun=False
  try:
   with slot:
    record['backend_start_epoch']=time.time();req=urllib.request.Request(BACKEND+self.path,data=data,headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=5400) as r:
     if not body.get('stream'):
      # Preserve the complete non-streaming response before touching a possibly
      # disconnected caller. This changes observation only, not critic timeout.
      chunks.append(r.read())
      self.send_response(r.status);self.send_header('Content-Type',r.headers.get('Content-Type','application/json'));self.end_headers();begun=True
      self.wfile.write(chunks[0]);self.wfile.flush()
     else:
      # Keep streaming cancellation behavior unchanged: do not drain cancelled
      # generation in pursuit of usage telemetry.
      self.send_response(r.status);self.send_header('Content-Type',r.headers.get('Content-Type','application/json'));self.end_headers();begun=True
      while True:
       b=r.read1(8192)
       if not b:break
       chunks.append(b);self.wfile.write(b);self.wfile.flush()
  except Exception as e:
   record['transport_error']=type(e).__name__+': '+str(e)
   if not begun:
    try:self.send_error(502)
    except OSError:pass
  finally:
   record['end_epoch']=time.time();raw=b''.join(chunks);prefix.with_suffix('.response.txt').write_bytes(raw)
   try:
    if body.get('stream'):
     events=[json.loads(line[6:]) for line in raw.decode().splitlines() if line.startswith('data: ') and line[6:]!='[DONE]'];record['usage']=next((e['usage'] for e in reversed(events) if e.get('usage')),None);record['finish_reasons']=[c.get('finish_reason') for e in events for c in e.get('choices',[]) if c.get('finish_reason')]
    else:
     reply=json.loads(raw);record['usage']=reply.get('usage');record['finish_reasons']=[c.get('finish_reason') for c in reply.get('choices',[])]
   except Exception:record['response_parse_failed']=True
   prefix.with_suffix('.metrics.json').write_text(json.dumps(record,indent=2))
ThreadingHTTPServer(('0.0.0.0',11431),H).serve_forever()
