import importlib.util,json,pathlib,unittest
p=pathlib.Path(__file__).parent/'gitea-focused/__init__.py';spec=importlib.util.spec_from_file_location('focused',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
UP='sickprodigy/nicotineplus-plugins';FORK='fixture'
class Native:
 def __init__(self):self.calls=[];self.parent=UP;self.login='hermes-agent';self.error=None
 def __call__(self,name,args):
  self.calls.append((name.removeprefix(m.PREFIX),args));op=self.calls[-1][0]
  if self.error:return json.dumps({'error':self.error})
  value={'get_me':{'login':self.login,'email':'do-not-return@example.test'},'repo_read':{'full_name':'hermes-agent/'+FORK,'fork':True,'default_branch':'main','parent':self.parent},'get_repository_tree':{'sha':'abc'},'branch_write':'Branch Created','create_or_update_file':'Committed 1 file(s) to branch feature','pull_request_write':{'number':11,'html_url':'http://gitea:3000/'+UP+'/pulls/11'},'issue_write':{'number':10},'get_file_contents':{'content':json.dumps([{'line':1,'content':'# Title'},{'line':2,'content':'body'}])}}
  return json.dumps({'result':json.dumps(value.get(op,[]))})
class Focused(unittest.TestCase):
 def setUp(self):self.native=Native();self.b=m.Bridge(self.native,[UP]);self.f={'fork_owner':'hermes-agent','fork_repo':FORK,'branch_name':'feature'}
 def call(self,op,**args):return self.b.invoke(op,args)
 def pr(self,**override):
  args={'upstream_owner':'sickprodigy','upstream_repo':'nicotineplus-plugins','fork_owner':'hermes-agent','fork_repo':FORK,'head_branch':'feature','base_branch':'main','title':'Fix docs','body':'Refs #10'};args.update(override);return self.call('create_pull_request',**args)
 def test_create_fields_are_required(self):
  s=m.schemas()
  for op in ['create_issue','fork_repository','create_branch','edit_file','create_pull_request']:
   schema=s['gitea_'+op]['parameters'];self.assertEqual(set(schema['required']),set(schema['properties']));self.assertFalse(schema['additionalProperties'])
  self.assertNotIn('method',s['gitea_create_pull_request']['parameters']['properties'])
 def test_missing_head_never_reaches_transport(self):
  self.assertIn('error',self.call('create_pull_request',upstream_owner='sickprodigy'));self.assertEqual(self.native.calls,[])
 def test_wrong_upstream_blocked(self):
  self.assertIn('error',self.call('create_issue',upstream_owner='nicotineplus',upstream_repo='nicotineplus-plugins',title='title',body='body'));self.assertEqual(self.native.calls,[])
 def test_default_is_deny_writes(self):
  self.assertIn('error',m.Bridge(self.native,[]).invoke('create_issue',{'upstream_owner':'sickprodigy','upstream_repo':'nicotineplus-plugins','title':'t','body':'b'}));self.assertEqual(self.native.calls,[])
 def test_branch_required_name_maps_to_native(self):
  out=self.call('create_branch',**self.f,base_branch='main');self.assertTrue(out['ok']);self.assertEqual(self.native.calls[-1],('branch_write',{'method':'create','owner':'hermes-agent','repo':FORK,'branch':'feature','old_branch':'main'}))
 def test_upstream_file_write_blocked(self):
  self.assertIn('error',self.call('create_branch',fork_owner='sickprodigy',fork_repo='nicotineplus-plugins',branch_name='feature',base_branch='main'));self.assertFalse(any(n=='branch_write' for n,a in self.native.calls))
 def test_default_branch_write_blocked(self):
  self.assertIn('error',self.call('edit_file',fork_owner='hermes-agent',fork_repo=FORK,branch_name='main',path='README.md',old_text='old',new_text='new',commit_message='docs'));self.assertFalse(any(n=='create_or_update_file' for n,a in self.native.calls))
 def test_wrong_fork_parent_blocks_pr(self):
  self.native.parent='other/repo';self.assertIn('error',self.pr());self.assertFalse(any(n=='pull_request_write' for n,a in self.native.calls))
 def test_parent_dict_supported(self):
  self.native.parent={'full_name':UP};self.assertEqual(self.pr()['number'],11)
 def test_exact_edit_no_branch_creation_or_rewrite(self):
  out=self.call('edit_file',**self.f,path='README.md',old_text='old',new_text='new',commit_message='docs');self.assertTrue(out['ok']);name,args=self.native.calls[-1];self.assertEqual(name,'create_or_update_file');self.assertEqual(args['edits'],[{'old_string':'old','new_string':'new'}]);self.assertNotIn('new_branch_name',args);self.assertNotIn('files',args);self.assertNotIn('content',args)
 def test_head_uses_owner_not_fork_name(self):
  out=self.pr();self.assertEqual(out['html_url'],'https://gitea.rcs1.top/'+UP+'/pulls/11');name,args=self.native.calls[-1];self.assertEqual(name,'pull_request_write');self.assertEqual(args['head'],'hermes-agent:feature');self.assertEqual(args['owner'],'sickprodigy');self.assertEqual(args['base'],'main')
 def test_fork_never_sends_personal_username_as_org(self):
  self.call('fork_repository',upstream_owner='sickprodigy',upstream_repo='nicotineplus-plugins',fork_name='fixture');self.assertNotIn('org',self.native.calls[-1][1])
 def test_line_json_is_returned_as_readable_text(self):
  out=self.call('read_file',owner='sickprodigy',repo='nicotineplus-plugins',path='README.md',ref='main');self.assertEqual(out['text'],'1: # Title\n2: body');self.assertEqual(self.native.calls[-1][1]['end_line'],160)
 def test_direct_native_names_are_blocked(self):
  self.assertEqual(m.block_direct_native(m.PREFIX+'issue_write',{})['action'],'block')
  self.assertIsNone(m.block_direct_native('gitea_create_issue',{}))
  self.assertIsNone(m.block_direct_native('terminal',{}))
 def test_handler_contract_is_serialized_json(self):
  result=self.b.handle('identity',{});self.assertIsInstance(result,str);self.assertEqual(json.loads(result)['login'],'hermes-agent')
 def test_identity_does_not_return_email(self):self.assertNotIn('email',self.call('identity'))
 def test_native_errors_not_hidden_or_retried(self):
  self.native.error='request failed with status 409';out=self.pr();self.assertIn('409',out['error']);self.assertEqual(len(self.native.calls),1)
 def test_unknown_args_not_ignored(self):
  self.assertIn('error',self.call('identity',org='hermes-agent'));self.assertEqual(self.native.calls,[])
 def test_boolean_not_accepted_as_issue_number(self):
  self.assertIn('error',self.call('read_issue',owner='sickprodigy',repo='nicotineplus-plugins',issue_number=True));self.assertEqual(self.native.calls,[])
if __name__=='__main__':unittest.main()
