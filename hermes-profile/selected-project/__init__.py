"""Supply selected-checkout Git facts through Hermes's native context hook."""
import json,re,subprocess
from pathlib import Path
from urllib.parse import urlsplit,urlunsplit

def public_remote(value):
 """Keep repository identity, dropping credentials, query and fragment."""
 value=value.strip()
 if '://' not in value:
  match=re.fullmatch(r'(?:[^@\s]+@)?([^:\s]+):(.+)',value)
  if match:return 'ssh://'+match[1]+'/'+match[2].lstrip('/')
  return None  # Local filesystem remotes are not forge identities.
 try:
  parts=urlsplit(value)
  if parts.scheme not in {'http','https','ssh','git'} or not parts.hostname:return None
  host=parts.hostname
  if ':' in host:host='['+host+']'
  if parts.port:host+=':'+str(parts.port)
  return urlunsplit((parts.scheme,host,parts.path,'',''))
 except ValueError:return None

class SelectedProject:
 def __init__(self,root):
  if not root:raise ValueError('selected-project requires an explicit workspace_root')
  self.root=Path(root).resolve()
 def git(self,*args):
  return subprocess.check_output(['git','-C',str(self.root),*args],stderr=subprocess.DEVNULL,timeout=2).decode().strip()
 def context(self,**kwargs):
  try:
   if Path(self.git('rev-parse','--show-toplevel')).resolve()!=self.root:return None
   facts={'cwd':str(self.root),'branch':self.git('branch','--show-current'),'head':self.git('rev-parse','HEAD'),'remotes':{}}
   for remote in ['origin','upstream']:
    try:url=public_remote(self.git('remote','get-url',remote))
    except subprocess.CalledProcessError:continue
    if url:facts['remotes'][remote]=url
   return {'context':'Selected repository workspace (Git facts):\n'+json.dumps(facts,ensure_ascii=False,indent=2)}
  except (OSError,subprocess.SubprocessError,UnicodeError):return None

def register(ctx):
 project=SelectedProject(ctx.get_config('workspace_root',''))
 ctx.register_hook('pre_llm_call',project.context)
