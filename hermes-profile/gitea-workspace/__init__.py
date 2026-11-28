"""Publish a model-edited Git workspace through the configured Gitea MCP service."""
from pathlib import Path, PurePosixPath
import hashlib,json,subprocess,re
PREFIX='mcp__mcp_gitea_hermes__'
TOOLSET='gitea-workspace'

def decode(value):
 for _ in range(6):
  if isinstance(value,str):
   try:value=json.loads(value);continue
   except ValueError:return value
  if isinstance(value,dict) and ('error' in value or value.get('isError')):raise RuntimeError(str(value))
  if isinstance(value,dict) and set(value)=={'result'}:value=value['result'];continue
  return value
 raise RuntimeError('Unexpected nested MCP result')

class Publisher:
 def __init__(self,root,baseline_ref,transport,allowed_upstreams,allowed_paths,public_url='https://gitea.rcs1.top',allowed_path_prefixes=(),explicit_object_ids=False):
  self.root=Path(root).resolve();self.baseline=baseline_ref;self.transport=transport;self.allowed=frozenset(allowed_upstreams);self.paths=frozenset(allowed_paths);self.public=public_url.rstrip('/');self.last=None
  self.prefixes=tuple(allowed_path_prefixes or ())
  if type(explicit_object_ids) is not bool:raise ValueError('explicit_object_ids must be a boolean')
  self.explicit_object_ids=explicit_object_ids
  for prefix in self.prefixes:
   if not isinstance(prefix,str) or not prefix.endswith('/') or PurePosixPath(prefix).is_absolute() or not PurePosixPath(prefix).parts or '..' in PurePosixPath(prefix).parts or '.git' in PurePosixPath(prefix).parts or chr(92) in prefix or prefix!=str(PurePosixPath(prefix))+'/':raise ValueError('Allowed path prefixes must be normalized relative directory paths ending in /')
 def git(self,*args):return subprocess.check_output(['git','-C',str(self.root),*args])
 def native(self,name,args):return decode(self.transport(PREFIX+name,args))
 def tree_ref(self,owner,repo,branch):
  if len(branch)!=40:return branch
  return self.branch_commit(owner,repo,branch)
 def branch_commit(self,owner,repo,branch):
  previous=None
  for page in range(1,51):
   rows=self.native('branch_read',{'method':'list','owner':owner,'repo':repo,'per_page':100,'page':page})
   if not isinstance(rows,list):raise ValueError('Missing branch metadata for tree lookup')
   signature=tuple(row.get('name') for row in rows)
   if rows and signature==previous:raise ValueError('Branch pagination did not advance')
   previous=signature
   for row in rows:
    if row.get('name')!=branch:continue
    commit=row.get('commit');sha=row.get('commit_sha') or (commit.get('sha') or commit.get('id') if isinstance(commit,dict) else None)
    if not isinstance(sha,str) or not re.fullmatch(r'[0-9a-fA-F]{40}',sha):raise ValueError('Missing branch commit SHA')
    return sha
   if len(rows)<100:break
  raise ValueError('Branch not found for tree lookup: '+branch)
 def tree(self,owner,repo,branch,*,resolved_ref=None):
  tree_ref=self.tree_ref(owner,repo,branch) if resolved_ref is None else resolved_ref
  if resolved_ref is not None and not re.fullmatch(r'[0-9a-fA-F]{40}',resolved_ref):raise ValueError('Invalid resolved commit SHA')
  files={};seen=0;previous=None
  for page in range(1,51):
   value=self.native('get_repository_tree',{'owner':owner,'repo':repo,'tree_sha':tree_ref,'recursive':True,'per_page':100,'page':page})
   if not isinstance(value,dict) or not isinstance(value.get('tree'),list):raise ValueError('Missing remote tree metadata')
   entries=value['tree'];signature=tuple((e.get('path'),e.get('sha')) for e in entries)
   if entries and signature==previous:raise ValueError('Remote tree pagination did not advance')
   previous=signature;seen+=len(entries)
   for entry in entries:
    if entry.get('type')=='blob':
     if not isinstance(entry.get('path'),str) or not entry.get('sha'):raise ValueError('Invalid remote blob metadata')
     files[entry['path']]={'sha':entry['sha']}
   total=value.get('total_count')
   if type(total) is int:
    if seen>=total:return files
    if not entries:raise ValueError('Incomplete remote tree pagination')
   elif len(entries)<100 and not value.get('truncated'):return files
  raise ValueError('Remote tree exceeds the small-task publisher limit of 5000 entries')
 def publish(self,fork_owner,fork_repo,branch_name,commit_message):
  if not commit_message or not branch_name:raise ValueError('Branch and commit message are required')
  actual=Path(self.git('rev-parse','--show-toplevel').decode().strip()).resolve()
  if actual!=self.root:raise ValueError('Workspace root must be the selected Git repository root')
  me=self.native('get_me',{})
  if fork_owner!=me.get('login'):raise ValueError('Fork owner must be the authenticated automation account')
  info=self.native('repo_read',{'method':'get','owner':fork_owner,'repo':fork_repo});parent=info.get('parent');parent=parent.get('full_name') if isinstance(parent,dict) else parent
  if not info.get('fork') or parent not in self.allowed:raise ValueError('Unapproved fork parent')
  if branch_name==info.get('default_branch'):raise ValueError('Never publish into the fork default branch')
  names=set(self.git('diff','--name-only','--no-renames','-z',self.baseline).decode().strip('\0').split('\0'))
  names.update(self.git('ls-files','--others','--exclude-standard','-z').decode().strip('\0').split('\0'));names.discard('')
  if not names:raise ValueError('No workspace changes to publish')
  if len(names)>20:raise ValueError('Too many files for the selected small-task publisher')
  before=self.tree(fork_owner,fork_repo,branch_name)
  files=[];expected={}
  for name in sorted(names):
   path=PurePosixPath(name);local=self.root/name
   if path.is_absolute() or '..' in path.parts or '.git' in path.parts or '\\' in name:raise ValueError('Invalid workspace path')
   if name not in self.paths and not any(name.startswith(prefix) for prefix in self.prefixes) and not (name.startswith('tests/') and name.endswith('.py')):raise ValueError('File outside the configured task scope: '+name)
   if any(self.root.joinpath(*path.parts[:i]).is_symlink() for i in range(1,len(path.parts)+1)) or not local.resolve().is_relative_to(self.root):raise ValueError('Symlink/outside-workspace file is not publishable')
   remote=before.get(name);entry={'path':name}
   if remote is not None:
    if not isinstance(remote,dict) or not remote.get('sha'):raise ValueError('Missing remote file SHA')
    entry['sha']=remote['sha']
   if local.exists():
    if not local.is_file():raise ValueError('Only regular files may be published')
    data=local.read_bytes()
    if len(data)>200000:raise ValueError('File too large')
    entry['content']=data.decode('utf-8');expected[name]=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
   else:
    if remote is None:raise ValueError('Deleted file is already absent remotely')
    entry['delete']=True;expected[name]=None
   files.append(entry)
  fingerprint=hashlib.sha256(json.dumps([fork_owner,fork_repo,branch_name,expected],sort_keys=True).encode()).hexdigest()
  if fingerprint==self.last:raise ValueError('These exact workspace changes were already published')
  result=self.native('create_or_update_file',{'owner':fork_owner,'repo':fork_repo,'branch_name':branch_name,'message':commit_message,'files':files});verified=[]
  verified_commit=None
  if self.explicit_object_ids:
   try:verified_commit=self.branch_commit(fork_owner,fork_repo,branch_name)
   except (ValueError,RuntimeError) as error:raise RuntimeError('Write returned but remote commit metadata could not be verified: '+str(error)) from error
  after=self.tree(fork_owner,fork_repo,branch_name,resolved_ref=verified_commit) if self.explicit_object_ids else self.tree(fork_owner,fork_repo,branch_name)
  for name,sha in expected.items():
   remote=after.get(name)
   if sha is None:
    if remote is not None:raise RuntimeError('Commit returned but deletion verification failed: '+name)
   elif not isinstance(remote,dict) or remote.get('sha')!=sha:raise RuntimeError('Commit returned but blob verification failed: '+name)
   verified.append({'path':name,'verified':True,('blob_sha' if self.explicit_object_ids else 'sha'):sha,'url':self.public+'/'+fork_owner+'/'+fork_repo+'/src/branch/'+branch_name+'/'+name})
  self.last=fingerprint
  if self.explicit_object_ids:return {'ok':True,'verified_commit_sha':verified_commit,'commit_url':self.public+'/'+fork_owner+'/'+fork_repo+'/commit/'+verified_commit,'result':result,'files':verified,'checks_executed_by_this_tool':False}
  return {'ok':True,'result':result,'files':verified,'checks_executed_by_this_tool':False}
 def handle(self,args):
  try:return json.dumps(self.publish(**args),ensure_ascii=False)
  except (ValueError,RuntimeError,subprocess.CalledProcessError,UnicodeError) as e:return json.dumps({'error':str(e)})

def register(ctx):
 from tools.registry import registry
 root=ctx.get_config('workspace_root','');baseline=ctx.get_config('baseline_ref','')
 if not root or not baseline:raise ValueError('gitea-workspace requires an explicit selected workspace root and baseline ref')
 p=Publisher(root,baseline,registry.dispatch,ctx.get_config('allowed_upstream_repositories',[]),ctx.get_config('allowed_paths',[]),ctx.get_config('public_url','https://gitea.rcs1.top'),allowed_path_prefixes=ctx.get_config('allowed_path_prefixes',[]),explicit_object_ids=ctx.get_config('explicit_object_ids',False))
 schema={'name':'gitea_commit_workspace','description':'Commit the selected local Git workspace changes to an existing personal-fork feature branch through Gitea MCP. Includes committed and uncommitted changes since the frozen baseline. Verifies remote blob hashes. Does not run tests: execute appropriate checks before publishing.','parameters':{'type':'object','properties':{k:{'type':'string','minLength':1} for k in ['fork_owner','fork_repo','branch_name','commit_message']},'required':['fork_owner','fork_repo','branch_name','commit_message'],'additionalProperties':False}}
 ctx.register_tool(name=schema['name'],toolset=TOOLSET,schema=schema,handler=p.handle)
