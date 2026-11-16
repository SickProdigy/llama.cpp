import unittest,importlib.util,pathlib
p=pathlib.Path(__file__).parent/'gitea-readable-defaults/__init__.py'
spec=importlib.util.spec_from_file_location('readable',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
T=m._TOOL
class ReadDefaults(unittest.TestCase):
 def test_missing_flags_become_bounded_text(self):
  original={'owner':'o','repo':'r','path':'README.md'};result=m.readable_defaults(T,original)
  self.assertEqual(result,{'action':'modify','args':{'with_lines':True,'start_line':1,'end_line':160}});self.assertNotIn('with_lines',original)
 def test_explicit_raw_binary_other_tools_unchanged(self):
  for tool,args in [(T,{'with_lines':False,'path':'README.md'}),(T,{'path':'image.PNG'}),('mcp__other__get_file_contents',{'path':'README.md'}),(T,{'with_lines':'false'})]:self.assertIsNone(m.readable_defaults(tool,args))
 def test_explicit_range_preserved_and_start_respected(self):
  self.assertIsNone(m.readable_defaults(T,{'with_lines':True,'start_line':161,'end_line':200}))
  self.assertEqual(m.readable_defaults(T,{'with_lines':True,'start_line':161})['args'],{'end_line':320})
 def test_invalid_start_not_silently_repaired(self):
  self.assertEqual(m.readable_defaults(T,{'start_line':-1})['args'],{'with_lines':True})
if __name__=='__main__':unittest.main()
