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
 def test_update_prose_only_maps_to_correct_native_number(self):
  for op,tool,key in [('update_issue','issue_write','issue_number'),('update_pull_request','pull_request_write','pull_number')]:
   self.call(op,upstream_owner='sickprodigy',upstream_repo='nicotineplus-plugins',title='Correction',body='Actual checks',**{key:10})
   self.assertEqual(self.native.calls[-1],(tool,{'method':'update','owner':'sickprodigy','repo':'nicotineplus-plugins',key:10,'title':'Correction','body':'Actual checks'}))
 def test_prose_update_rejects_unallowed_upstream_and_state(self):
  self.assertIn('error',self.call('update_issue',upstream_owner='other',upstream_repo='repo',issue_number=10,title='x',body='y'))
  self.assertIn('error',self.call('update_issue',upstream_owner='sickprodigy',upstream_repo='nicotineplus-plugins',issue_number=10,title='x',body='y',state='closed'))
  self.assertEqual(self.native.calls,[])
 def test_missing_head_never_reaches_transport(self):
  self.assertIn('error',self.call('create_pull_request',upstream_owner='sickprodigy'));self.assertEqual(self.native.calls,[])
 def test_forty_character_branch_uses_commit_sha_for_pr_tree(self):
  branch='feature-'.ljust(40,'x');original=self.native
  def transport(name,args):
   if name.endswith('branch_read'):
    self.native.calls.append(('branch_read',args));return [{'name':branch,'commit_sha':'a'*40}]
   return original(name,args)
  self.b.transport=transport
  self.assertEqual(self.pr(head_branch=branch)['number'],11)
  tree=next(a for n,a in self.native.calls if n=='get_repository_tree')
  self.assertEqual(tree['tree_sha'],'a'*40)
  self.assertEqual(self.native.calls[-1][1]['head'],'hermes-agent:'+branch)
 def test_forty_character_root_branch_resolved_but_commit_is_unchanged(self):
  branch='feature-'.ljust(40,'x');original=self.native
  self.b.transport=lambda name,args:[{'name':branch,'commit':{'id':'b'*40}}] if name.endswith('branch_read') else original(name,args)
  self.call('list_directory',owner='hermes-agent',repo=FORK,path='',ref=branch)
  self.assertEqual(self.native.calls[-1][1]['tree_sha'],'b'*40)
  self.call('list_directory',owner='hermes-agent',repo=FORK,path='',ref='c'*40)
  self.assertEqual(self.native.calls[-1][1]['tree_sha'],'c'*40)
 def test_missing_forty_character_branch_never_opens_pr(self):
  out=self.pr(head_branch='feature-'.ljust(40,'x'))
  self.assertIn('error',out);self.assertFalse(any(n=='pull_request_write' for n,a in self.native.calls))
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
 def test_root_directory_aliases_use_repository_tree(self):
  for path in ('', '.', '/', './'):
   self.call('list_directory',owner='sickprodigy',repo='Sick-Cogs',path=path,ref='main');self.assertEqual(self.native.calls[-1],('get_repository_tree',{'owner':'sickprodigy','repo':'Sick-Cogs','tree_sha':'main','recursive':False,'per_page':100}))
  self.call('list_directory',owner='sickprodigy',repo='Sick-Cogs',path='folder',ref='main');self.assertEqual(self.native.calls[-1][1]['path'],'folder')
 def test_line_json_is_returned_as_readable_text(self):
  out=self.call('read_file',owner='sickprodigy',repo='nicotineplus-plugins',path='README.md',ref='main');self.assertEqual(out['text'],'1: # Title\n2: body');self.assertEqual(self.native.calls[-1][1]['end_line'],160)
 def test_direct_native_names_are_blocked(self):
  self.assertEqual(m.block_direct_native(m.PREFIX+'issue_write',{})['action'],'block')
  self.assertIsNone(m.block_direct_native('gitea_create_issue',{}))
  self.assertIsNone(m.block_direct_native('terminal',{}))
 def test_partial_read_retains_mcp_pagination_metadata(self):
  payload={'content':json.dumps([{'line':160,'content':'last returned line'}]),'start_line':1,'end_line':160,'total_lines':400,'truncated':True}
  bridge=m.Bridge(lambda name,args:json.dumps({'result':json.dumps(payload)}),[UP])
  out=bridge.invoke('read_file',{'owner':'sickprodigy','repo':'nicotineplus-plugins','path':'README.md','ref':'main'})
  self.assertEqual(out['total_lines'],400);self.assertTrue(out['truncated']);self.assertEqual(out['next_start_line'],161);self.assertEqual(out['text'],'160: last returned line')
 def test_complete_read_does_not_offer_another_page(self):
  payload={'content':'last page','start_line':301,'end_line':350,'total_lines':350,'truncated':False}
  bridge=m.Bridge(lambda name,args:payload,[UP])
  out=bridge.invoke('read_file',{'owner':'sickprodigy','repo':'nicotineplus-plugins','path':'README.md','ref':'main','start_line':301,'end_line':350})
  self.assertFalse(out['truncated']);self.assertNotIn('next_start_line',out);self.assertEqual(out['end_line'],350)
 def test_missing_metadata_does_not_invent_file_length_or_continuation(self):
  out=self.call('read_file',owner='sickprodigy',repo='nicotineplus-plugins',path='README.md',ref='main')
  self.assertNotIn('total_lines',out);self.assertNotIn('truncated',out);self.assertNotIn('next_start_line',out)
 def test_handler_contract_is_serialized_json(self):
  result=self.b.handle('identity',{});self.assertIsInstance(result,str);self.assertEqual(json.loads(result)['login'],'hermes-agent')
 def test_identity_does_not_return_email(self):self.assertNotIn('email',self.call('identity'))
 def test_native_errors_not_hidden_or_retried(self):
  self.native.error='request failed with status 409';out=self.pr();self.assertIn('409',out['error']);self.assertEqual(len(self.native.calls),1)
 def test_unknown_args_not_ignored(self):
  self.assertIn('error',self.call('identity',org='hermes-agent'));self.assertEqual(self.native.calls,[])
 def test_boolean_not_accepted_as_issue_number(self):
  self.assertIn('error',self.call('read_issue',owner='sickprodigy',repo='nicotineplus-plugins',issue_number=True));self.assertEqual(self.native.calls,[])
 def test_public_reference_format_is_opt_in(self):
  raw={'id':1623,'number':1,'title':'Fix','body':'Details','state':'open'}
  self.assertIs(self.b.reference_numbers('create_issue',raw),raw)
  explicit=m.Bridge(self.native,[UP],explicit_reference_numbers=True)
  result=explicit.reference_numbers('create_issue',raw)
  self.assertEqual(list(result)[0],'issue_number');self.assertEqual(result['issue_number'],1)
  self.assertNotIn('id',result);self.assertEqual(raw['id'],1623)
  self.assertEqual({k:result[k]for k in raw if k!='id'},{k:v for k,v in raw.items()if k!='id'})
 def test_explicit_issue_result_does_not_rewrite_native_write_or_retry(self):
  calls=[]
  def transport(name,args):
   calls.append((name,args));return json.dumps({'result':json.dumps({'id':1623,'number':1,'html_url':'http://gitea:3000/'+UP+'/issues/1'})})
  bridge=m.Bridge(transport,[UP],explicit_reference_numbers=True)
  args={'upstream_owner':'sickprodigy','upstream_repo':'nicotineplus-plugins','title':'Fix','body':'Details'}
  result=json.loads(bridge.handle('create_issue',args))
  self.assertEqual(result['issue_number'],1);self.assertNotIn('id',result)
  self.assertEqual(result['html_url'],'https://gitea.rcs1.top/'+UP+'/issues/1')
  self.assertEqual(calls,[(m.PREFIX+'issue_write',{'method':'create','owner':'sickprodigy','repo':'nicotineplus-plugins','title':'Fix','body':'Details'})])
 def test_explicit_reference_lists_preserve_prose_and_public_numbers(self):
  bridge=m.Bridge(self.native,[UP],explicit_reference_numbers=True)
  for operation,key in [('list_issues','issue_number'),('list_pull_requests','pull_number')]:
   raw=[{'id':1623,'number':1,'body':'Keep #7 context','comments':[{'body':'Comment'}]},{'id':1710,'number':2}]
   result=bridge.reference_numbers(operation,raw)
   self.assertEqual([r[key]for r in result],[1,2]);self.assertEqual(result[0]['comments'],raw[0]['comments'])
   self.assertEqual(result[0]['body'],raw[0]['body']);self.assertTrue(all('id'not in r for r in result))
   self.assertEqual(bridge.reference_numbers(operation,[]),[])
 def test_explicit_references_never_fall_back_to_database_id(self):
  bridge=m.Bridge(self.native,[UP],explicit_reference_numbers=True)
  for value in [None,True,0,-1,'1']:
   with self.subTest(value=value),self.assertRaises(ValueError):bridge.reference_numbers('read_issue',{'id':1623,'number':value})
  for operation in ['create_issue','update_issue','read_issue','create_pull_request','read_pull_request','update_pull_request']:
   with self.subTest(operation=operation),self.assertRaises(ValueError):bridge.reference_numbers(operation,{'id':1623})
  with self.assertRaises(ValueError):bridge.reference_numbers('read_issue',[])
  with self.assertRaises(ValueError):bridge.reference_numbers('list_issues',{'id':1623,'number':1})
 def test_explicit_pr_number_and_normal_permissions_remain(self):
  self.b=m.Bridge(self.native,[UP],explicit_reference_numbers=True)
  self.assertEqual(self.pr()['pull_number'],11)
  self.assertEqual(self.native.calls[-1][1]['head'],'hermes-agent:feature')
  self.assertIn('error',self.pr(fork_owner='other'))
 def test_explicit_mode_does_not_change_other_metadata(self):
  bridge=m.Bridge(self.native,[UP],explicit_reference_numbers=True);raw={'id':3,'number':10}
  self.assertIs(bridge.reference_numbers('repository_info',raw),raw)
  self.assertEqual(bridge.reference_numbers('create_issue',{'id':1623,'number':1,'issue_number':1623})['issue_number'],1)
 def test_explicit_reference_config_requires_real_boolean(self):
  for value in ['false',1,None]:
   with self.subTest(value=value),self.assertRaises(ValueError):m.Bridge(self.native,[UP],explicit_reference_numbers=value)
if __name__=='__main__':unittest.main()
