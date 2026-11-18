import unittest
from bounded_guard import Guard,Reject,PREFIX
p={'kind':'contribution','fork_name':'fixture','branch':'test','issue_title':'title','issue_body':'body','pr_title':'pr','pr_body':'Refs #<issue-number>','original_content':'old\n','expected_content':'new\n','file_sha':'abc'}
class Tests(unittest.TestCase):
 def setUp(self):self.g=Guard(p.copy())
 def check(self,n,a):return self.g.check(PREFIX+n,a)
 def test_upstream_issue(self):self.assertEqual(self.check('issue_write',{'method':'create','owner':'sickprodigy','repo':'nicotineplus-plugins','title':'title','body':'body'}),'issue')
 def test_issue_in_fork_blocked(self):
  with self.assertRaises(Reject):self.check('issue_write',{'method':'create','owner':'hermes-agent','repo':'fixture'})
 def test_missing_branch_can_retry(self):
  self.g.issue=4
  with self.assertRaises(ValueError):self.check('branch_write',{'method':'create','owner':'hermes-agent','repo':'fixture'})
  self.assertEqual(self.check('branch_write',{'method':'create','owner':'hermes-agent','repo':'fixture','branch':'test'}),'branch')
 def test_fork_before_issue_still_within_write_scope(self):
  self.assertEqual(self.check('repo_write',{'method':'fork','owner':'sickprodigy','repo':'nicotineplus-plugins'}),'fork')
 def test_allowed_fork(self):
  self.g.issue=4
  self.assertEqual(self.check('repo_write',{'method':'fork','owner':'sickprodigy','repo':'nicotineplus-plugins'}),'fork')
 def test_fork_response_target(self):
  self.g.after('fork',{'name':'nicotineplus-plugins','full_name':'hermes-agent/nicotineplus-plugins'})
  self.assertEqual(self.g.p['fork_name'],'nicotineplus-plugins')
 def test_wrong_fork_namespace(self):
  self.g.issue=4
  with self.assertRaises(Reject):self.check('repo_write',{'method':'fork','owner':'sickprodigy','repo':'nicotineplus-plugins','org':'other'})
 def test_settings_blocked(self):
  with self.assertRaises(Reject):self.check('repo_write',{'method':'update','owner':'hermes-agent','repo':'fixture'})
 def test_terminal_blocked(self):
  with self.assertRaises(Reject):self.g.check('terminal',{'command':'true'})
 def test_upstream_code_blocked(self):
  self.g.issue=1
  with self.assertRaises(Reject):self.check('create_or_update_file',{'owner':'sickprodigy','repo':'nicotineplus-plugins','branch_name':'main','path':'README.md','message':'docs','content':'new\n'})
 def test_native_branch_success_string(self):
  self.g.before('branch');self.g.after('branch','Branch Created');self.assertTrue(self.g.branch)
 def test_native_commit_success_string(self):
  self.g.before('commit');self.g.after('commit','Committed 1 file(s) to branch test');self.assertTrue(self.g.commit)
 def test_missing_file_path_gets_validation(self):
  with self.assertRaises(ValueError):self.check('create_or_update_file',{'owner':'hermes-agent','repo':'fixture','branch_name':'test','message':'docs'})
 def test_missing_file_payload_gets_validation(self):
  with self.assertRaises(ValueError):self.check('create_or_update_file',{'owner':'hermes-agent','repo':'fixture','branch_name':'test','message':'docs','path':'README.md'})
 def test_exact_edit(self):
  self.g.issue=1;self.g.branch=True
  self.assertEqual(self.check('create_or_update_file',{'owner':'hermes-agent','repo':'fixture','branch_name':'test','path':'README.md','message':'docs','edits':[{'old_string':'old','new_string':'new'}]}),'commit')
 def test_extra_edit_blocked(self):
  self.g.issue=1;self.g.branch=True
  with self.assertRaises(Reject):self.check('create_or_update_file',{'owner':'hermes-agent','repo':'fixture','branch_name':'test','path':'README.md','message':'docs','content':'bad'})
 def test_combined_commit(self):
  self.g.issue=1
  self.assertEqual(self.check('create_or_update_file',{'owner':'hermes-agent','repo':'fixture','branch_name':'main','new_branch_name':'test','message':'docs','path':'README.md','content':'new\n'}),'commit')
 def test_definitive_fork_argument_failure_can_retry(self):
  self.g.before('fork');self.g.after('fork',{'error':'request failed with status 404'})
  self.assertNotIn('fork',self.g.sent)
  self.g.before('fork');self.g.after('fork',{'error':'request failed with status 404'})
  self.assertIn('fork',self.g.sent)
 def test_ambiguous_write_cannot_retry(self):
  self.g.before('fork');self.g.after('fork',{'error':'connection timed out'})
  self.assertIn('fork',self.g.sent)
 def test_duplicate_blocked(self):
  self.g.sent.add('issue')
  with self.assertRaises(Reject):self.test_upstream_issue()
 def test_pr_direction(self):
  self.g.issue=4;self.g.commit=True
  a={'method':'create','owner':'sickprodigy','repo':'nicotineplus-plugins','base':'main','head':'hermes-agent:test','title':'pr','body':'Refs #4'}
  self.assertEqual(self.check('pull_request_write',a),'pr');a['head']='test'
  with self.assertRaises(Reject):self.check('pull_request_write',a)
 def test_merge_blocked(self):
  with self.assertRaises(Reject):self.check('pull_request_write',{'method':'merge','owner':'sickprodigy','repo':'nicotineplus-plugins'})
 def test_read_only(self):
  self.g.p['kind']='read'
  with self.assertRaises(Reject):self.test_upstream_issue()
if __name__=='__main__':unittest.main()
