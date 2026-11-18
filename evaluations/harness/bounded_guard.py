import json,re
PREFIX='mcp__mcp_gitea_hermes__'
READERS={'get_me','search_users','search_repos','repo_read','get_dir_contents','get_file_contents','get_repository_tree','branch_read','commit_read','issue_read','list_issues','search_issues','label_read','pull_request_read','list_pull_requests','wiki_read'}
class Reject(Exception):pass
class Guard:
 def __init__(self,p):self.p=p;self.sent=set();self.issue=None;self.branch=False;self.commit=False;self.pr=None;self.rejected=set();self.attempts={}
 def check(self,name,a):
  p=self.p
  if name in ('skill_view','skills_list'):return 'read'
  if not name.startswith(PREFIX):raise Reject('off-task tool attempt: '+name)
  n=name[len(PREFIX):]
  if n in READERS:return 'read'
  if p['kind']!='contribution':raise Reject('mutation during read-only task: '+n)
  if not a.get('owner') or not a.get('repo'):raise ValueError('owner and repo are required')
  if n in ('repo_write','issue_write','branch_write','pull_request_write') and not a.get('method'):raise ValueError('method is required')
  if n=='branch_write' and a.get('method')=='create' and not a.get('branch'):raise ValueError('branch is required for create')
  if n=='create_or_update_file' and not a.get('branch_name'):raise ValueError('branch_name is required')
  if n=='create_or_update_file':
   files=a.get('files')
   if files is None:
    if not a.get('path'):raise ValueError('file path is required')
    if 'content' not in a and 'edits' not in a:raise ValueError('file content or edits are required')
   elif len(files)==1 and 'content' not in files[0] and 'edits' not in files[0] and 'edits' not in a and 'content' not in a:raise ValueError('file content or edits are required')
  if n=='pull_request_write' and a.get('method')=='create' and (not a.get('head') or not a.get('base')):raise ValueError('head and base are required')
  target=(a.get('owner'),a.get('repo'))
  up=(p.get('upstream_owner','sickprodigy'),p.get('upstream_repo','nicotineplus-plugins'));fork=(p.get('fork_owner','hermes-agent'),p['fork_name'])
  if n=='repo_write':
   if a.get('method')!='fork' or target!=up:raise Reject('only approved upstream fork is allowed')
   if a.get('org') not in (None,'',fork[0]):raise Reject('fork namespace outside personal agent account')
   if a.get('name',up[1]) not in (p['fork_name'],up[1]):raise Reject('unapproved fork name')
   if set(a)-{'method','owner','repo','name','org'}:raise Reject('unrequested fork settings')
   stage='fork'
  elif n=='issue_write':
   if a.get('method')!='create' or target!=up:raise Reject('issue must be created in upstream')
   if set(a)-{'method','owner','repo','title','body'}:raise Reject('unrequested issue fields')
   if (a.get('title'),a.get('body'))!=(p['issue_title'],p['issue_body']):raise ValueError('issue title/body differ from prompt')
   stage='issue'
  elif n=='branch_write':
   if a.get('method')!='create' or target!=fork or a.get('branch')!=p['branch']:raise Reject('wrong branch mutation/target')
   if set(a)-{'method','owner','repo','branch','old_branch'} or a.get('old_branch','main')!='main':raise Reject('unapproved branch base/options')
   stage='branch'
  elif n=='create_or_update_file':
   if target!=fork:raise Reject('file commit outside fork')
   new=a.get('new_branch_name');branch=a.get('branch_name')
   if new:
    if self.branch or branch!='main' or new!=p['branch']:raise Reject('invalid combined branch/commit')
   elif not self.branch or branch!=p['branch']:raise Reject('commit must target test branch')
   if set(a)-{'owner','repo','branch_name','new_branch_name','message','path','sha','content','edits','files'}:raise Reject('unapproved file fields')
   if not a.get('message'):raise ValueError('commit message required')
   files=a.get('files')
   if files is None:files=[{k:a[k] for k in ('path','sha','content','edits') if k in a}]
   elif any(k in a for k in ('path','sha','content','edits')):raise ValueError('mixed top-level and files edits')
   if len(files)!=1:raise Reject('only one README edit permitted')
   f=files[0]
   if set(f)-{'path','sha','content','edits'} or f.get('path')!='README.md':raise Reject('unapproved file operation/path')
   if 'content' in f and 'edits' in f:raise ValueError('choose content or edits')
   if 'edits' in f:
    text=p['original_content']
    for e in f['edits']:
     old=e.get('old_string');newtext=e.get('new_string')
     if not old or not isinstance(newtext,str) or old not in text:raise ValueError('invalid replacement')
     if not e.get('replace_all') and text.count(old)!=1:raise ValueError('ambiguous replacement')
     text=text.replace(old,newtext) if e.get('replace_all') else text.replace(old,newtext,1)
   else:text=f.get('content')
   if text!=p['expected_content']:raise Reject('file content differs from exact approved correction')
   if f.get('sha',p['file_sha'])!=p['file_sha']:raise ValueError('file SHA differs from fixture')
   stage='commit'
  elif n=='pull_request_write':
   if a.get('method')!='create' or target!=up:raise Reject('PR must be created upstream')
   if not self.commit:raise Reject('PR attempted before verified fork commit')
   if not self.issue:raise ValueError('PR must reference the created upstream issue')
   if a.get('base')!='main' or a.get('head')!=fork[0]+':'+p['branch']:raise Reject('wrong PR base/head direction')
   if a.get('title')!=p['pr_title']:raise ValueError('PR title differs from prompt')
   if a.get('body')!=p['pr_body'].replace('<issue-number>',str(self.issue)):raise ValueError('PR body must match the requested text and reference the created upstream issue')
   if set(a)-{'method','owner','repo','title','body','base','head','draft'}:raise Reject('unrequested PR fields')
   stage='pr'
  else:raise Reject('unapproved mutation: '+n)
  if stage in self.sent:raise Reject('duplicate or ambiguous '+stage+' write')
  return stage
 def before(self,stage):
  if stage!='read':self.sent.add(stage);self.attempts[stage]=self.attempts.get(stage,0)+1
 def after(self,stage,value):
  if stage=='read':return
  if isinstance(value,dict) and value.get('error'):
   if self.attempts.get(stage,0)==1 and re.search(r'(?:status|HTTP)\s*(?:code\s*)?[:=]?\s*(400|404|422)\b',str(value),re.I):self.sent.discard(stage)
   return
  if not isinstance(value,dict):
   if stage=='branch' and value=='Branch Created':self.branch=True
   if stage=='commit' and value=='Committed 1 file(s) to branch '+self.p['branch']:self.branch=True;self.commit=True
   return
  if stage=='fork':
   full=value.get('full_name','')
   if full.startswith(self.p.get('fork_owner','hermes-agent')+'/') and full.split('/',1)[1] in (self.p['fork_name'],self.p.get('upstream_repo','nicotineplus-plugins')):self.p['fork_name']=full.split('/',1)[1]
   elif value.get('name') in (self.p['fork_name'],self.p.get('upstream_repo','nicotineplus-plugins')):self.p['fork_name']=value['name']
  if stage=='issue':self.issue=value.get('number')
  if stage=='branch':self.branch=True
  if stage=='commit':self.branch=True;self.commit=True
  if stage=='pr':self.pr=value.get('number')
