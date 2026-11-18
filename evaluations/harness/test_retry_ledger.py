import unittest
from retry_ledger import RetryLedger
from bounded_guard import Guard, Reject, PREFIX

class Retries(unittest.TestCase):
    def test_identical_failed_read_without_progress_stays_blocked(self):
        r=RetryLedger();args={'repo':'fixture','ref':'not-yet-created'}
        r.reject('read_file',args)
        self.assertIn(r.key('read_file',args),r.rejected)
        r.advance_after_write(succeeded=False)
        self.assertIn(r.key('read_file',args),r.rejected)

    def test_read_becomes_eligible_after_branch_creation(self):
        r=RetryLedger();args={'repo':'fixture','ref':'feature'}
        r.reject('read_file',args);r.advance_after_write(succeeded=True)
        self.assertNotIn(r.key('read_file',args),r.rejected)
        r.reject('read_file',args)
        self.assertIn(r.key('read_file',args),r.rejected)

    def test_argument_order_does_not_evade_repeat_detection(self):
        r=RetryLedger();r.reject('read_file',{'repo':'r','owner':'o'})
        self.assertIn(r.key('read_file',{'owner':'o','repo':'r'}),r.rejected)

    def test_corrected_arguments_are_eligible_without_mutation(self):
        r=RetryLedger();r.reject('read_file',{'ref':'wrong'})
        self.assertNotIn(r.key('read_file',{'ref':'main'}),r.rejected)

    def test_progress_does_not_release_ambiguous_create(self):
        p={'kind':'contribution','fork_name':'fixture','branch':'feature',
           'issue_title':'title','issue_body':'body'}
        g=Guard(p);g.before('issue');g.after('issue',{'error':'network timed out'})
        r=RetryLedger();r.advance_after_write(succeeded=True)
        with self.assertRaises(Reject):
            g.check(PREFIX+'issue_write',{'method':'create','owner':'sickprodigy',
                    'repo':'nicotineplus-plugins','title':'title','body':'body'})

if __name__=='__main__':unittest.main()
