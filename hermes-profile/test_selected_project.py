import importlib.util,json,pathlib,subprocess,tempfile,unittest
p=pathlib.Path(__file__).parent/'selected-project/__init__.py'
spec=importlib.util.spec_from_file_location('selected_project',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Checks(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=pathlib.Path(self.tmp.name)
  self.git('init','-b','main');self.git('config','user.name','Evaluation');self.git('config','user.email','eval@invalid.example');self.git('commit','--allow-empty','-m','baseline')
 def git(self,*args):return subprocess.check_output(['git','-C',str(self.root),*args],stderr=subprocess.DEVNULL).decode().strip()
 def test_actual_root_branch_and_remote(self):
  self.git('remote','add','origin','https://gitea.example/owner/project.git')
  data=json.loads(m.SelectedProject(self.root).context()['context'].split('\n',1)[1])
  self.assertEqual(data['cwd'],str(self.root));self.assertEqual(data['branch'],'main');self.assertEqual(data['head'],self.git('rev-parse','HEAD'));self.assertEqual(data['remotes']['origin'],'https://gitea.example/owner/project.git')
 def test_metadata_refreshes_each_turn(self):
  project=m.SelectedProject(self.root);self.git('checkout','-b','fix');self.assertIn('"branch": "fix"',project.context()['context'])
 def test_credentials_never_in_context(self):
  self.git('remote','add','origin','https://user:private-test-token@gitea.example/owner/project.git?access_token=other-secret#fragment')
  result=m.SelectedProject(self.root).context()['context'];self.assertNotIn('private-test-token',result);self.assertNotIn('other-secret',result);self.assertNotIn('fragment',result);self.assertIn('https://gitea.example/owner/project.git',result)
 def test_scp_and_ipv6(self):
  self.assertEqual(m.public_remote('git@gitea.example:owner/project.git'),'ssh://gitea.example/owner/project.git')
  self.assertEqual(m.public_remote('ssh://git@[::1]:2222/owner/project.git'),'ssh://[::1]:2222/owner/project.git')
 def test_missing_or_nested_root_not_injected(self):
  sub=self.root/'sub';sub.mkdir();self.assertIsNone(m.SelectedProject(sub).context());self.assertIsNone(m.SelectedProject(self.root/'missing').context())
  with self.assertRaises(ValueError):m.SelectedProject('')
 def test_local_remotes_not_reported_as_forge(self):
  self.assertIsNone(m.public_remote('/srv/local/project'));self.assertIsNone(m.public_remote('file:///srv/local/project'));self.assertIsNone(m.public_remote('https://host:bad/owner/project'))
if __name__=='__main__':unittest.main(verbosity=2)
