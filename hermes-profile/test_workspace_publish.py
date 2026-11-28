import importlib.util,pathlib,tempfile,subprocess,hashlib,json,unittest
P=pathlib.Path(__file__).parent/'gitea-workspace/__init__.py';spec=importlib.util.spec_from_file_location('workspace_publish',P);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def blob(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
class Publication(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=pathlib.Path(self.tmp.name);(self.root/'code.py').write_text('old\n');self.run_git('init','-b','main');self.run_git('config','user.name','Eval');self.run_git('config','user.email','eval@invalid.example');self.run_git('add','.');self.run_git('commit','-m','base');self.base=self.run_git('rev-parse','HEAD').strip();self.remote={'code.py':b'old\n'};self.calls=[];self.bad_hash=False
  self.p=m.Publisher(self.root,self.base,self.transport,['owner/up'],['code.py','README.md'])
 def tearDown(self):self.tmp.cleanup()
 def run_git(self,*args):return subprocess.check_output(['git','-C',str(self.root),*args],stderr=subprocess.DEVNULL).decode()
 def transport(self,name,args):
  self.calls.append((name,args));n=name.removeprefix(m.PREFIX)
  if n=='get_me':return {'login':'agent'}
  if n=='repo_read':return {'fork':True,'default_branch':'main','parent':{'full_name':'owner/up'}}
  if n=='get_repository_tree':
   entries=[{'type':'blob','path':p,'sha':'bad' if self.bad_hash else blob(data)} for p,data in sorted(self.remote.items())];start=(args.get('page',1)-1)*args.get('per_page',100)
   return {'tree':entries[start:start+args.get('per_page',100)],'total_count':len(entries)}
  if n=='create_or_update_file':
   for f in args['files']:
    if f.get('delete'):self.remote.pop(f['path'])
    else:self.remote[f['path']]=f['content'].encode()
   return 'Committed files'
  raise AssertionError(name)
 def publish(self,**overrides):return self.p.publish(**({'fork_owner':'agent','fork_repo':'fork','branch_name':'fix','commit_message':'fix'}|overrides))
 def test_existing_and_new_files_are_published_and_verified(self):
  (self.root/'code.py').write_text('new\n');(self.root/'tests').mkdir();(self.root/'tests/test_code.py').write_text('test\n');r=self.publish();self.assertTrue(r['ok']);self.assertEqual(len(r['files']),2);self.assertTrue(all(f['verified'] for f in r['files']));self.assertFalse(r['checks_executed_by_this_tool']);writes=[a for n,a in self.calls if n.endswith('create_or_update_file')];self.assertEqual(writes[0]['files'][0]['sha'],blob(b'old\n'))
  self.assertNotIn('verified_commit_sha',r);self.assertTrue(all('sha' in f and 'blob_sha' not in f for f in r['files']));self.assertFalse(any(n.endswith('branch_read') for n,a in self.calls))
 def enable_explicit_ids(self,branch='fix',missing=False):
  original=self.transport
  def transport(name,args):
   if name.endswith('branch_read'):
    self.calls.append((name,args))
    if missing:return []
    return [{'name':branch,'commit':{'id':('b' if any(n.endswith('create_or_update_file') for n,a in self.calls) else 'a')*40}}]
   return original(name,args)
  self.p=m.Publisher(self.root,self.base,transport,['owner/up'],['code.py','README.md'],explicit_object_ids=True)
 def test_explicit_ids_separate_verified_commit_from_file_blob(self):
  self.enable_explicit_ids();(self.root/'code.py').write_text('new\n');r=self.publish()
  self.assertEqual(r['verified_commit_sha'],'b'*40);self.assertEqual(r['commit_url'],'https://gitea.rcs1.top/agent/fork/commit/'+'b'*40)
  self.assertNotEqual(r['verified_commit_sha'],blob(b'new\n'));self.assertEqual(r['files'][0]['blob_sha'],blob(b'new\n'));self.assertNotIn('sha',r['files'][0])
  self.assertEqual([a['tree_sha'] for n,a in self.calls if n.endswith('get_repository_tree')],['fix','b'*40])
  self.assertEqual(len([n for n,a in self.calls if n.endswith('branch_read')]),1)
 def test_explicit_ids_keep_forty_character_branch_resolution(self):
  branch='feature-'.ljust(40,'x');self.enable_explicit_ids(branch);(self.root/'code.py').write_text('new\n');r=self.publish(branch_name=branch)
  self.assertEqual(r['verified_commit_sha'],'b'*40);self.assertEqual([a['tree_sha'] for n,a in self.calls if n.endswith('get_repository_tree')],['a'*40,'b'*40])
 def test_missing_postwrite_head_never_becomes_a_blob_commit_link(self):
  self.enable_explicit_ids(missing=True);(self.root/'code.py').write_text('new\n')
  r=json.loads(self.p.handle({'fork_owner':'agent','fork_repo':'fork','branch_name':'fix','commit_message':'fix'}))
  self.assertIn('Write returned but remote commit metadata could not be verified',r['error']);self.assertNotIn('ok',r);self.assertNotIn('commit_url',r)
  self.assertEqual(self.remote['code.py'],b'new\n')
 def test_explicit_ids_pin_verification_when_branch_moves(self):
  self.enable_explicit_ids();original=self.p.transport;snapshot=None
  def transport(name,args):
   nonlocal snapshot
   result=original(name,args)
   if name.endswith('branch_read'):
    snapshot=dict(self.remote);self.remote['code.py']=b'concurrent change\n'
   elif name.endswith('get_repository_tree') and snapshot is not None:
    if args['tree_sha']=='b'*40:return {'tree':[{'type':'blob','path':p,'sha':blob(data)}for p,data in snapshot.items()],'total_count':len(snapshot)}
   return result
  self.p.transport=transport;(self.root/'code.py').write_text('new\n');r=self.publish()
  self.assertEqual(r['verified_commit_sha'],'b'*40);self.assertEqual(r['files'][0]['blob_sha'],blob(b'new\n'));self.assertEqual(self.remote['code.py'],b'concurrent change\n')
 def test_explicit_ids_report_deletion_without_inventing_blob(self):
  self.enable_explicit_ids();(self.root/'code.py').unlink();r=self.publish();self.assertIsNone(r['files'][0]['blob_sha']);self.assertEqual(r['verified_commit_sha'],'b'*40)
 def test_explicit_ids_require_a_boolean_setting(self):
  for value in ['false',1,None]:
   with self.assertRaises(ValueError):m.Publisher(self.root,self.base,self.transport,['owner/up'],[],explicit_object_ids=value)
 def test_forty_character_branch_resolves_fresh_sha_before_and_after_commit(self):
  branch='feature-'.ljust(40,'x');original=self.transport
  def transport(name,args):
   if name.endswith('branch_read'):
    self.calls.append((name,args));return [{'name':branch,'commit_sha':('b' if any(n.endswith('create_or_update_file') for n,a in self.calls) else 'a')*40}]
   if name.endswith('get_repository_tree'):self.assertNotEqual(args['tree_sha'],branch)
   return original(name,args)
  self.p.transport=transport;(self.root/'code.py').write_text('new\n')
  self.assertTrue(self.publish(branch_name=branch)['ok'])
  refs=[a['tree_sha'] for n,a in self.calls if n.endswith('get_repository_tree')]
  self.assertEqual(refs,['a'*40,'b'*40])
 def test_missing_forty_character_branch_blocks_publication(self):
  original=self.transport
  self.p.transport=lambda name,args:[] if name.endswith('branch_read') else original(name,args)
  (self.root/'code.py').write_text('new\n')
  with self.assertRaises(ValueError):self.publish(branch_name='feature-'.ljust(40,'x'))
  self.assertFalse(any(n.endswith('create_or_update_file') for n,a in self.calls))
 def test_forty_character_branch_pagination_and_nested_commit_metadata(self):
  branch='feature-'.ljust(40,'x');original=self.transport
  def transport(name,args):
   if name.endswith('branch_read'):
    self.calls.append((name,args))
    return [{'name':'other'+str(i)} for i in range(100)] if args['page']==1 else [{'name':branch,'commit':{'id':'a'*40}}]
   return original(name,args)
  self.p.transport=transport;(self.root/'code.py').write_text('new\n');self.assertTrue(self.publish(branch_name=branch)['ok'])
  self.assertEqual(len([a for n,a in self.calls if n.endswith('branch_read') and a['page']==2]),2)
 def test_three_new_files_never_probe_missing_file_endpoints(self):
  (self.root/'tests').mkdir()
  for i in range(3):(self.root/f'tests/test_new{i}.py').write_text('new test\n')
  self.assertTrue(self.publish()['ok']);self.assertFalse(any(n.endswith('get_file_contents') for n,a in self.calls));self.assertEqual(len([n for n,a in self.calls if n.endswith('get_repository_tree')]),2)
 def test_remote_tree_pagination_keeps_existing_sha(self):
  self.remote.update({f'a{i:03}.py':b'untouched' for i in range(140)});(self.root/'code.py').write_text('new\n');self.assertTrue(self.publish()['ok'])
  self.assertTrue(any(a.get('page')==2 for n,a in self.calls if n.endswith('get_repository_tree')))
 def test_multiple_deletions_do_not_need_404_verification(self):
  for name in ['tests/a.py','tests/b.py','tests/c.py']:
   path=self.root/name;path.parent.mkdir(exist_ok=True);path.write_text('old\n');self.remote[name]=b'old\n'
  self.run_git('add','.');self.run_git('commit','-m','more baseline files');self.p.baseline=self.run_git('rev-parse','HEAD').strip()
  for name in ['tests/a.py','tests/b.py','tests/c.py']:(self.root/name).unlink()
  self.assertTrue(self.publish()['ok']);self.assertFalse(any(n.endswith('get_file_contents') for n,a in self.calls))
 def test_explicit_directory_scope_allows_new_module_and_data(self):
  self.p.prefixes=('booksearch/','tests/')
  (self.root/'booksearch').mkdir();(self.root/'booksearch/response.py').write_text('new helper\n');(self.root/'tests').mkdir();(self.root/'tests/data.json').write_text('{}')
  self.assertTrue(self.publish()['ok']);self.assertIn('booksearch/response.py',self.remote);self.assertIn('tests/data.json',self.remote)
 def test_directory_scope_does_not_allow_sibling_prefix(self):
  self.p.prefixes=('booksearch/',);(self.root/'booksearch-other').mkdir();(self.root/'booksearch-other/response.py').write_text('x')
  with self.assertRaises(ValueError):self.publish()
 def test_parent_symlink_rejected_even_if_within_repository(self):
  self.p.prefixes=('booksearch/',);(self.root/'booksearch').symlink_to(self.root,target_is_directory=True)
  original_git=self.p.git
  self.p.git=lambda *args:b'booksearch/code.py\0' if args[0]=='diff' else b'' if args[0]=='ls-files' else original_git(*args)
  with self.assertRaises(ValueError):self.publish()
 def test_invalid_directory_scope_rejected(self):
  for prefix in ['/','../','booksearch/../','booksearch-other','./booksearch/','./','booksearch'+chr(92)+'nested/']:
   with self.assertRaises(ValueError):m.Publisher(self.root,self.base,self.transport,['owner/up'],[],allowed_path_prefixes=[prefix])
 def test_locally_committed_change_is_not_lost(self):
  (self.root/'code.py').write_text('new\n');self.run_git('add','.');self.run_git('commit','-m','local fix');self.assertTrue(self.publish()['ok'])
 def test_deletion_verified(self):
  (self.root/'code.py').unlink();self.assertTrue(self.publish()['ok']);self.assertNotIn('code.py',self.remote)
 def test_default_branch_rejected_before_write(self):
  (self.root/'code.py').write_text('new')
  with self.assertRaises(ValueError):self.publish(branch_name='main')
  self.assertFalse(any(n.endswith('create_or_update_file') for n,a in self.calls))
 def test_other_owner_rejected(self):
  with self.assertRaises(ValueError):self.publish(fork_owner='owner')
 def test_symlink_rejected(self):
  (self.root/'code.py').unlink();(self.root/'code.py').symlink_to('/etc/passwd')
  with self.assertRaises(ValueError):self.publish()
 def test_unexpected_file_rejected(self):
  (self.root/'token.env').write_text('not a real secret')
  with self.assertRaises(ValueError):self.publish()
 def test_duplicate_publish_rejected(self):
  (self.root/'code.py').write_text('new');self.publish()
  with self.assertRaises(ValueError):self.publish()
 def test_failure_to_verify_is_not_reported_success(self):
  (self.root/'code.py').write_text('new');self.bad_hash=True
  with self.assertRaises(RuntimeError):self.publish()
 def test_handler_accepts_registry_argument_dict(self):
  (self.root/'code.py').write_text('new');r=json.loads(self.p.handle({'fork_owner':'agent','fork_repo':'fork','branch_name':'fix','commit_message':'fix'}));self.assertTrue(r['ok'])
if __name__=='__main__':unittest.main()
