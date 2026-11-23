"""Scripted OpenAI-compatible responses through the real native CLI and persistence."""
from pathlib import Path
import os,sys,json,time,threading,subprocess,sqlite3,hashlib,re
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
sys.path.insert(0,'/opt/hermes')
import hermes_yaml as yaml
O=Path('/results');home=Path('/tmp/glm-history-home');home.mkdir();work=Path('/tmp/glm-history-work');work.mkdir()
alias='glm-4.7-flash-q4k';requests=[];lock=threading.Lock()
class Handler(BaseHTTPRequestHandler):
 def log_message(self,*args):pass
 def answer(self,body):
  data=json.dumps(body).encode();self.send_response(200);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
 def do_GET(self):self.answer({'object':'list','data':[{'id':alias,'object':'model'}]})
 def do_POST(self):
  body=json.loads(self.rfile.read(int(self.headers['Content-Length'])))
  with lock:
   requests.append(body);number=len(requests);(O/('request-'+str(number)+'.json')).write_text(json.dumps(body,indent=2))
  if number==1:
   delta={'role':'assistant','reasoning_content':'control-reasoning-tool-one','tool_calls':[{'index':0,'id':'call_history_control_1','type':'function','function':{'name':'terminal','arguments':json.dumps({'command':'printf hermes-glm-history-control','timeout':10})}}]};finish='tool_calls'
  elif number==2:
   delta={'role':'assistant','reasoning_content':'control-reasoning-final-one','content':'Control one complete.'};finish='stop'
  else:
   delta={'role':'assistant','reasoning_content':'control-reasoning-final-two','content':'Control two complete.'};finish='stop'
  if body.get('stream'):
   chunks=[{'id':'history-control','object':'chat.completion.chunk','created':0,'model':alias,'choices':[{'index':0,'delta':delta,'finish_reason':None}]},{'id':'history-control','object':'chat.completion.chunk','created':0,'model':alias,'choices':[{'index':0,'delta':{},'finish_reason':finish}],'usage':{'prompt_tokens':100,'completion_tokens':10,'total_tokens':110}}]
   data=(''.join('data: '+json.dumps(v)+'\n\n' for v in chunks)+'data: [DONE]\n\n').encode();self.send_response(200);self.send_header('Content-Type','text/event-stream');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
  else:self.answer({'id':'history-control','object':'chat.completion','created':0,'model':alias,'choices':[{'index':0,'message':delta,'finish_reason':finish}],'usage':{'prompt_tokens':100,'completion_tokens':10,'total_tokens':110}})
server=ThreadingHTTPServer(('127.0.0.1',0),Handler);threading.Thread(target=server.serve_forever,daemon=True).start();url='http://127.0.0.1:'+str(server.server_port)+'/v1';extra={'temperature':.7,'top_p':1,'top_k':0,'min_p':0,'repeat_penalty':1,'presence_penalty':0,'max_tokens':16384,'chat_template_kwargs':{'enable_thinking':True,'clear_thinking':False}}
config={'model':{'default':alias,'provider':'custom:wide','base_url':url,'api_key':'local-history-control','context_length':98304,'max_tokens':16384},'custom_providers':[{'name':'wide','base_url':url,'api_key':'local-history-control','model':alias,'extra_body':extra}],'providers':{'custom:wide':{'request_timeout_seconds':30,'stale_timeout_seconds':30}},'plugins':{'enabled':[]},'mcp_servers':{},'tools':{'tool_search':{'enabled':'off'}},'terminal':{'backend':'local','cwd':str(work),'timeout':10},'platform_toolsets':{'cli':['terminal']},'memory':{'enabled':False},'title_generation':{'enabled':False,'model_upgrade_enabled':False},'compression':{'threshold':.85},'agent':{'max_turns':5,'run_budget_seconds':90,'gateway_timeout':150}}
(home/'config.yaml').write_text(yaml.safe_dump(config));env=dict(os.environ,HOME=str(home),HERMES_HOME=str(home),HERMES_WRITE_SAFE_ROOT=str(work)+':'+str(home/'cache/scratch'),PYTHONDONTWRITEBYTECODE='1')
first='Run the harmless terminal history control, then finish.';follow='Confirm the previous control has completed.'
def cli(query,sid=None):
 argv=['/opt/hermes/bin/hermes','chat','--cli','--oneshot','-Q','--query-file','-','--in',str(work),'--accept-hooks','--max-turns','5','--run-budget','90']
 if sid:argv+=['--resume',sid]
 z=subprocess.run(argv,input=query,capture_output=True,text=True,env=env,timeout=120);(O/('cli-'+('second'if sid else'first')+'.log')).write_text(z.stdout+z.stderr);assert z.returncode==0,(z.stdout+z.stderr)[-1500:]
cli(first)
db=sqlite3.connect(home/'state.db');row=db.execute("select session_id from messages where role='user'and content=? order by id desc limit 1",(first,)).fetchone();assert row;sid=row[0];before=repr(db.execute('select * from messages order by id').fetchall());db.close()
z=subprocess.run(['/opt/hermes/bin/hermes','sessions','discard',sid,'--yes'],capture_output=True,text=True,env=env,timeout=60);assert z.returncode==0,z.stderr[-700:]
db=sqlite3.connect(home/'state.db');assert repr(db.execute('select * from messages order by id').fetchall())==before;db.close();cli(follow,sid)
def visible(v):
 if isinstance(v,str):return v
 if isinstance(v,list):return '\n'.join(visible(x)for x in v)
 if isinstance(v,dict):return visible(v.get('text',v.get('content','')))
 return ''
def reasoning(m):
 value=m.get('reasoning_content')
 if isinstance(value,str):return value
 content=visible(m.get('content'))
 return content.split('</think>')[0].split('<think>')[-1]if'</think>'in content else ''
assert len(requests)==3,len(requests)
same=' '.join(reasoning(m)for m in requests[1]['messages']if m['role']=='assistant')
prior=[]
for m in requests[2]['messages']:
 if m['role']=='user'and follow in visible(m.get('content')):break
 if m['role']=='assistant':prior.append(reasoning(m))
checks={'same_turn_reasoning_retained':'control-reasoning-tool-one'in same,'cross_user_tool_reasoning_retained':any('control-reasoning-tool-one'in v for v in prior),'cross_user_final_reasoning_retained':any('control-reasoning-final-one'in v for v in prior),'real_terminal_result_seen':any(m['role']=='tool'and'hermes-glm-history-control'in visible(m.get('content'))for m in requests[1]['messages']),'GLM_template_kwargs_serialized':all(v.get('chat_template_kwargs')==extra['chat_template_kwargs']for v in requests),'output_cap_16384_serialized':all(v.get('max_tokens',v.get('max_completion_tokens'))==16384 for v in requests)}
out={'passed':all(checks.values()),'checks':checks,'native_CLI_processes':2,'requests':len(requests),'model_inference':False,'scripted_responses':True,'actual_forge_actions':False,'normal_native_discard_preserved_history':True,'not_actual_model_template_or_hardware_compatibility_or_quality':True,'scope':'Minimal terminal-only no-inference CLI integration control; full normal-profile scored trials remain separate.'};(O/'result.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));server.shutdown()
