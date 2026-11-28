"""Required-field Gitea tools over the existing authenticated Hermes MCP transport.

No credentials, HTTP client, shell, implicit retries or model-specific defaults.
Native tools remain registered for transport but should be hidden by toolset config.
"""
from functools import partial
import json,re
from pathlib import PurePosixPath

PREFIX = 'mcp__mcp_gitea_hermes__'
TOOLSET = 'gitea-focused'
SPECS = {
 'identity': ('Get the authenticated Gitea account.', {}, {}),
 'search_repositories': ('Search configured Gitea repositories; returns default branches and full names.', {'query':'string'}, {}),
 'repository_info': ('Read exact repository metadata, including its upstream parent if it is a fork.', {'owner':'string','repo':'string'}, {}),
 'list_branches': ('List branches of this exact Gitea repository.', {'owner':'string','repo':'string'}, {}),
 'list_directory': ('List a directory at an explicit branch or commit. For the repository root use path "" or "."; never repeat the repository name as the path.', {'owner':'string','repo':'string','path':'string','ref':'string'}, {}),
 'read_file': ('Read bounded source text at an explicit branch or commit. Output preserves total_lines and truncated when supplied by MCP; use next_start_line to continue a truncated excerpt. Use the fork branch to verify edits.', {'owner':'string','repo':'string','path':'string','ref':'string'}, {'start_line':'integer','end_line':'integer'}),
 'list_issues': ('List upstream issues before creating a duplicate.', {'owner':'string','repo':'string'}, {'state':'string'}),
 'read_issue': ('Read an upstream issue by number.', {'owner':'string','repo':'string','issue_number':'integer'}, {}),
 'list_pull_requests': ('List pull requests in their destination upstream repository.', {'owner':'string','repo':'string'}, {}),
 'read_pull_request': ('Read a pull request in its destination upstream repository.', {'owner':'string','repo':'string','pull_number':'integer'}, {}),
 'create_issue': ('Create an issue in the UPSTREAM repository specified by the user, not in its working fork.', {'upstream_owner':'string','upstream_repo':'string','title':'string','body':'string'}, {}),
 'update_issue': ('Correct the title and body of an existing allowed upstream issue; does not change its state.', {'upstream_owner':'string','upstream_repo':'string','issue_number':'integer','title':'string','body':'string'}, {}),
 'update_pull_request': ('Correct the title and body of an existing allowed upstream PR; does not merge or close it.', {'upstream_owner':'string','upstream_repo':'string','pull_number':'integer','title':'string','body':'string'}, {}),
 'fork_repository': ('Create a personal fork of the specified upstream using the authenticated account. If a fork exists, inspect and reuse it instead. There is no organization argument.', {'upstream_owner':'string','upstream_repo':'string','fork_name':'string'}, {}),
 'create_branch': ('Create a new feature branch in the authenticated account\'s existing fork. All branch names are required.', {'fork_owner':'string','fork_repo':'string','branch_name':'string','base_branch':'string'}, {}),
 'edit_file': ('Commit one exact text replacement to an EXISTING feature branch in the working fork. Does not create another branch or rewrite the whole file.', {'fork_owner':'string','fork_repo':'string','branch_name':'string','path':'string','old_text':'string','new_text':'string','commit_message':'string'}, {}),
 'create_pull_request': ('Open a PR in UPSTREAM from an existing branch in the authenticated account\'s verified fork. Pass owner/repo/branch separately; the MCP head reference is constructed for you. Leave the PR open.', {'upstream_owner':'string','upstream_repo':'string','fork_owner':'string','fork_repo':'string','head_branch':'string','base_branch':'string','title':'string','body':'string'}, {}),
}

def schemas():
 result={}
 for operation,(description,required,optional) in SPECS.items():
  props={}
  for key,typ in {**required,**optional}.items():
   props[key]={'type':typ}
   if typ=='string' and key not in ('path','new_text'):props[key]['minLength']=1
   if typ=='integer':props[key]['minimum']=1
  if operation=='list_issues':props['state']['enum']=['open','closed','all']
  result['gitea_'+operation]={'name':'gitea_'+operation,'description':description+' Uses the configured Gitea MCP connection.','parameters':{'type':'object','properties':props,'required':list(required),'additionalProperties':False}}
 return result

class MCPFailure(RuntimeError):
 pass

def decode(value):
 # The native bridge wraps the MCP text payload in {result: JSON string}.
 for _ in range(5):
  if isinstance(value,str):
   try:value=json.loads(value);continue
   except (ValueError,TypeError):return value
  if isinstance(value,dict) and ('error' in value or value.get('isError')):raise MCPFailure(str(value.get('error',value)))
  if isinstance(value,dict) and set(value)=={'result'}:value=value['result'];continue
  return value
 raise MCPFailure('Unexpected nested MCP response')

class Bridge:
 def __init__(self,transport,allowed_upstream_repositories,public_url='https://gitea.rcs1.top',explicit_reference_numbers=False):
  self.transport=transport
  self.allowed=frozenset(allowed_upstream_repositories)
  self.public_url=public_url.rstrip('/')
  if not self.public_url.startswith(('https://','http://')):raise ValueError('public_url must be an HTTP(S) origin')
  if type(explicit_reference_numbers) is not bool:raise ValueError('explicit_reference_numbers must be a boolean')
  self.explicit_reference_numbers=explicit_reference_numbers
 def handle(self,operation,args):
  # Hermes tool handlers require a serialized result, not a bare dict.
  return json.dumps(self.invoke(operation,args),ensure_ascii=False)
 def native(self,name,args):
  return decode(self.transport(PREFIX+name,args))
 def upstream(self,owner,repo):
  if owner+'/'+repo not in self.allowed:raise ValueError('Upstream is outside the operator-configured write allowlist: '+owner+'/'+repo)
 def tree_ref(self,owner,repo,ref,branch_required=False):
  # Gitea's tree endpoint interprets a 40-character ref as an object ID.
  if len(ref)!=40 or (not branch_required and re.fullmatch(r'[0-9a-fA-F]{40}',ref)):return ref
  previous=None
  for page in range(1,51):
   rows=self.native('branch_read',{'method':'list','owner':owner,'repo':repo,'per_page':100,'page':page})
   if not isinstance(rows,list):raise ValueError('Missing branch metadata for tree lookup')
   signature=tuple(row.get('name') for row in rows)
   if rows and signature==previous:raise ValueError('Branch pagination did not advance')
   previous=signature
   for row in rows:
    if row.get('name')!=ref:continue
    commit=row.get('commit');sha=row.get('commit_sha') or (commit.get('sha') or commit.get('id') if isinstance(commit,dict) else None)
    if not isinstance(sha,str) or not re.fullmatch(r'[0-9a-fA-F]{40}',sha):raise ValueError('Missing branch commit SHA')
    return sha
   if len(rows)<100:break
  raise ValueError('Branch not found for tree lookup: '+ref)
 def fork(self,owner,repo,branch=None):
  me=self.native('get_me',{})
  if owner!=me.get('login'):raise ValueError('Working fork owner must be the authenticated Gitea account: '+str(me.get('login')))
  info=self.native('repo_read',{'method':'get','owner':owner,'repo':repo})
  parent=info.get('parent');parent=parent.get('full_name') if isinstance(parent,dict) else parent
  if not info.get('fork') or parent not in self.allowed:raise ValueError('Working repository is not a verified fork of an allowed upstream')
  if branch is not None and branch==info.get('default_branch'):raise ValueError('Use a feature branch, not the fork default branch')
  return info,parent
 def urls(self,value):
  if isinstance(value,dict):return {k:self.urls(v) for k,v in value.items()}
  if isinstance(value,list):return [self.urls(v) for v in value]
  if isinstance(value,str) and value.startswith('http://gitea:3000/'):return self.public_url+value[len('http://gitea:3000'):]
  return value
 def reference_numbers(self,operation,value):
  if not self.explicit_reference_numbers:return value
  kinds={'create_issue':'issue_number','update_issue':'issue_number','read_issue':'issue_number','list_issues':'issue_number',
         'create_pull_request':'pull_number','update_pull_request':'pull_number','read_pull_request':'pull_number','list_pull_requests':'pull_number'}
  key=kinds.get(operation)
  if key is None:return value
  def row(item):
   if not isinstance(item,dict) or type(item.get('number')) is not int or item['number']<1:
    raise ValueError('Gitea response lacks a public repository reference number; read the upstream before retrying a mutation')
   # Keep the original public number and all prose/state. A database primary
   # key is not accepted by these tools' issue_number/pull_number arguments.
   return {key:item['number'],**{k:v for k,v in item.items()if k not in ('id',key)}}
  if operation.startswith('list_'):
   if not isinstance(value,list):raise ValueError('Gitea reference list response must be a list')
   return [row(item)for item in value]
  return row(value)
 def invoke(self,operation,args):
  try:
   required=SPECS[operation][1];optional=SPECS[operation][2]
   missing=[k for k in required if k not in args]
   if missing:raise ValueError('Required arguments missing: '+', '.join(missing))
   extra=set(args)-set(required)-set(optional)
   if extra:raise ValueError('Unknown arguments: '+', '.join(sorted(extra)))
   for key,typ in {**required,**optional}.items():
    if key not in args:continue
    value=args[key]
    if typ=='string' and (not isinstance(value,str) or (key not in ('path','new_text') and not value)):raise ValueError(key+' must be a nonempty string')
    if typ=='integer' and (not isinstance(value,int) or isinstance(value,bool) or value<1):raise ValueError(key+' must be a positive integer')
   a=dict(args);owner=a.get('owner');repo=a.get('repo');target={'owner':owner,'repo':repo}
   if operation=='identity':value=self.native('get_me',{});value={k:value.get(k) for k in ['login','html_url']}
   elif operation=='search_repositories':value=self.native('search_repos',{'query':a['query'],'per_page':30})
   elif operation=='repository_info':value=self.native('repo_read',{'method':'get',**target})
   elif operation=='list_branches':value=self.native('branch_read',{'method':'list',**target,'per_page':50})
   elif operation=='list_directory':
    if a['path'] in ('','.','/','./'):
     value=self.native('get_repository_tree',{**target,'tree_sha':self.tree_ref(owner,repo,a['ref']),'recursive':False,'per_page':100})
    else:value=self.native('get_dir_contents',{**target,'path':a['path'],'ref':a['ref']})
   elif operation=='read_file':
    start=a.get('start_line',1);end=a.get('end_line',start+159)
    if end<start or end-start>=300:raise ValueError('Read a range of at most 300 lines')
    value=self.native('get_file_contents',{**target,'path':a['path'],'ref':a['ref'],'with_lines':True,'start_line':start,'end_line':end})
    if not isinstance(value,dict) or 'content' not in value:raise ValueError('Path is not a readable file; use list_directory for directories')
    text=value['content']
    if isinstance(text,str):
     try:lines=json.loads(text)
     except ValueError:lines=None
     if isinstance(lines,list) and all(isinstance(x,dict) and 'line' in x and 'content' in x for x in lines):text='\n'.join(str(x['line'])+': '+x['content'] for x in lines)
    source=value
    value={'owner':owner,'repo':repo,'path':a['path'],'ref':a['ref'],'text':text,'url':self.public_url+'/'+owner+'/'+repo+'/src/branch/'+a['ref']+'/'+a['path']}
    for key in ('start_line','end_line','total_lines','truncated'):
     if key in source:value[key]=source[key]
    last=source.get('end_line');total=source.get('total_lines')
    if source.get('truncated') is True and type(last) is int and type(total) is int and 0<last<total:
     value['next_start_line']=last+1
   elif operation=='list_issues':value=self.native('list_issues',{**target,'state':a.get('state','open'),'per_page':50})
   elif operation=='read_issue':value=self.native('issue_read',{'method':'get',**target,'issue_number':a['issue_number']})
   elif operation=='list_pull_requests':value=self.native('list_pull_requests',{**target,'state':'open','per_page':50})
   elif operation=='read_pull_request':value=self.native('pull_request_read',{'method':'get',**target,'pull_number':a['pull_number']})
   elif operation=='create_issue':
    self.upstream(a['upstream_owner'],a['upstream_repo'])
    value=self.native('issue_write',{'method':'create','owner':a['upstream_owner'],'repo':a['upstream_repo'],'title':a['title'],'body':a['body']})
   elif operation in ('update_issue','update_pull_request'):
    self.upstream(a['upstream_owner'],a['upstream_repo'])
    number_key='issue_number' if operation=='update_issue' else 'pull_number'
    value=self.native('issue_write' if operation=='update_issue' else 'pull_request_write',{'method':'update','owner':a['upstream_owner'],'repo':a['upstream_repo'],number_key:a[number_key],'title':a['title'],'body':a['body']})
   elif operation=='fork_repository':
    self.upstream(a['upstream_owner'],a['upstream_repo'])
    value=self.native('repo_write',{'method':'fork','owner':a['upstream_owner'],'repo':a['upstream_repo'],'name':a['fork_name']})
   elif operation=='create_branch':
    self.fork(a['fork_owner'],a['fork_repo'],a['branch_name'])
    value=self.native('branch_write',{'method':'create','owner':a['fork_owner'],'repo':a['fork_repo'],'branch':a['branch_name'],'old_branch':a['base_branch']})
    value={'ok':True,'fork':a['fork_owner']+'/'+a['fork_repo'],'branch':a['branch_name'],'result':value}
   elif operation=='edit_file':
    self.fork(a['fork_owner'],a['fork_repo'],a['branch_name']);path=PurePosixPath(a['path'])
    if not a['path'] or path.is_absolute() or '..' in path.parts:raise ValueError('path must be a relative repository file path')
    value=self.native('create_or_update_file',{'owner':a['fork_owner'],'repo':a['fork_repo'],'branch_name':a['branch_name'],'path':a['path'],'message':a['commit_message'],'edits':[{'old_string':a['old_text'],'new_string':a['new_text']}]})
    value={'ok':True,'fork':a['fork_owner']+'/'+a['fork_repo'],'branch':a['branch_name'],'path':a['path'],'result':value}
   elif operation=='create_pull_request':
    self.upstream(a['upstream_owner'],a['upstream_repo']);_,parent=self.fork(a['fork_owner'],a['fork_repo'],a['head_branch'])
    if parent!=a['upstream_owner']+'/'+a['upstream_repo']:raise ValueError('PR upstream does not match this fork\'s parent')
    self.native('get_repository_tree',{'owner':a['fork_owner'],'repo':a['fork_repo'],'tree_sha':self.tree_ref(a['fork_owner'],a['fork_repo'],a['head_branch'],True),'recursive':False,'per_page':1})
    value=self.native('pull_request_write',{'method':'create','owner':a['upstream_owner'],'repo':a['upstream_repo'],'head':a['fork_owner']+':'+a['head_branch'],'base':a['base_branch'],'title':a['title'],'body':a['body']})
   else:raise ValueError('Unknown operation')
   return self.urls(self.reference_numbers(operation,value))
  except (ValueError,MCPFailure) as e:return {'error':str(e)}

def block_direct_native(tool_name='', args=None, **kwargs):
 # Model-facing calls must use the focused policy. Internal bridge transport
 # dispatches directly through the registry and does not run model tool hooks.
 if tool_name.startswith(PREFIX):
  return {'action':'block','message':'Use the registered gitea_* focused tools for this profile; direct native Gitea tools are disabled.'}
 return None

def register(ctx):
 from tools.registry import registry
 workspace_only=ctx.get_config('workspace_publication_only',False)
 if type(workspace_only) is not bool:raise ValueError('workspace_publication_only must be a boolean')
 ctx.register_hook('pre_tool_call',block_direct_native)
 bridge=Bridge(registry.dispatch,ctx.get_config('allowed_upstream_repositories',[]),ctx.get_config('public_url','https://gitea.rcs1.top'),explicit_reference_numbers=ctx.get_config('explicit_reference_numbers',False))
 for name,schema in schemas().items():
  if workspace_only and name=='gitea_edit_file':continue
  ctx.register_tool(name=name,toolset=TOOLSET,schema=schema,handler=partial(bridge.handle,name[len('gitea_'):]))
