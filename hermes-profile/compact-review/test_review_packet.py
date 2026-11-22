import subprocess
import os
from pathlib import Path
import tempfile
import hmac
import hashlib
from unittest.mock import patch
import unittest
from review_packet import (ReviewBlocked, admission, apply_changes, build_packet,
                           encoded, execution_summaries, packet_id, run_suite, source_digest)

KEY = b'test-only-not-a-production-key-32bytes'
BASE = {'client.py': 'def add(a, b):\n    return a - b\n',
        'tests/test_client.py': 'def test_add():\n    assert add(2, 3) == 5\n',
        'README.md': 'Adds two numbers.\n'}
CHANGE = {'client.py': 'def add(a, b):\n    return a + b\n'}
ENV = 'isolated-test-image-sha256'

class PacketTests(unittest.TestCase):
    def receipt(self, tree=None, code=0, text='tests finished', suite='existing', execute=None):
        tree = apply_changes(BASE, CHANGE) if tree is None else tree
        return run_suite(suite_id=suite, argv=['python3', '-m', 'unittest'],
                         expected_digest=source_digest(tree), inventory=lambda: tree,
                         execute=execute or (lambda argv: subprocess.CompletedProcess(argv, code, text, '')),
                         key=KEY, environment_id=ENV)

    def packet(self, receipts=None):
        receipts = [self.receipt()] if receipts is None else receipts
        candidate = source_digest(apply_changes(BASE, CHANGE))
        summaries = execution_summaries(receipts, key=KEY, required_suites=['existing'],
                                        candidate_digest=candidate, environment_id=ENV)
        return build_packet(tasks=['Fix addition and preserve existing behavior.'], base_revision='a'*40,
                            base=BASE, changes=CHANGE, context_paths=['tests/test_client.py'],
                            documentation_paths=['README.md'], execution=summaries)

    def approve(self, packet):
        return {'packet_id': packet['packet_id'], 'decision': 'approve', 'findings': [],
                'checks': {'tests': {'status': 'adequate', 'evidence': 'Checks the requested arithmetic result.'},
                           'documentation': {'status': 'consistent', 'evidence': 'Addition claim matches code.'}}}

    def admit(self, packet, receipts, response=None, digest=None):
        return admission(packet, self.approve(packet) if response is None else response,
                         receipts=receipts, key=KEY, required_suites=['existing'],
                         current_digest=digest or packet['candidate_source_digest'], environment_id=ENV)

    def test_actual_execution_and_complete_supported_review_admits(self):
        # Real tests execute exactly the tree whose receipt is admitted.
        base = {'client.py': 'def add(a, b): return a - b\n',
                'test_client.py': 'import unittest\nfrom client import add\nclass TestAdd(unittest.TestCase):\n def test_add(self): self.assertEqual(add(2, 3), 5)\n',
                'README.md': 'Adds two numbers.\n'}
        changes = {'client.py': 'def add(a, b): return a + b\n'}
        tree = apply_changes(base, changes)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name, content in tree.items(): (root/name).write_text(content)
            inventory = lambda: {name: (root/name).read_text() for name in tree}
            receipt = run_suite(suite_id='existing', argv=['python3', '-m', 'unittest'],
                                expected_digest=source_digest(tree), inventory=inventory,
                                execute=lambda argv: subprocess.run(argv, cwd=root, capture_output=True,
                                    text=True, timeout=10, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}),
                                key=KEY, environment_id=ENV)
        self.assertIn('Ran 1 test', receipt['payload']['output_tail'])
        summaries = execution_summaries([receipt], key=KEY, required_suites=['existing'],
                                       candidate_digest=source_digest(tree), environment_id=ENV)
        packet = build_packet(tasks=['Fix addition.'], base_revision='a'*40, base=base, changes=changes,
                              documentation_paths=['README.md'], execution=summaries)
        self.assertTrue(self.admit(packet, [receipt]))
        self.assertEqual(packet['context']['README.md']['content'], base['README.md'])
        self.assertNotIn('content', packet['patches'][0])

    def test_false_passing_output_does_not_override_nonzero_exit(self):
        with self.assertRaises(ReviewBlocked): self.packet([self.receipt(code=1, text='999 tests passed')])

    def test_timeout_never_counts_as_pass(self):
        def timeout(_): raise subprocess.TimeoutExpired('test', 1, output='passed')
        with self.assertRaises(ReviewBlocked): self.packet([self.receipt(execute=timeout)])

    def test_forged_receipt_is_rejected(self):
        receipt = self.receipt(code=1); receipt['payload']['returncode'] = 0
        with self.assertRaises(ReviewBlocked): self.packet([receipt])

    def test_short_verification_key_cannot_authorize_forged_pass(self):
        receipt = self.receipt()
        receipt['mac'] = hmac.new(b'x', encoded(receipt['payload']), hashlib.sha256).hexdigest()
        with self.assertRaises(ReviewBlocked):
            execution_summaries([receipt], key=b'x', required_suites=['existing'],
                                candidate_digest=receipt['payload']['source_digest'], environment_id=ENV)

    def test_missing_execution_and_wrong_tree_rejected(self):
        with self.assertRaises(ReviewBlocked): self.packet([])
        with self.assertRaises(ReviewBlocked): self.packet([self.receipt(tree=BASE)])

    def test_newer_failure_overrides_older_passing_run(self):
        old = self.receipt(); new = self.receipt(code=1)
        with self.assertRaises(ReviewBlocked): self.packet([old, new])
        with self.assertRaises(ReviewBlocked): self.packet([new, old])

    def test_wall_clock_ties_do_not_hide_the_later_failure(self):
        with patch('review_packet.time.time_ns', return_value=42):
            old = self.receipt(); new = self.receipt(code=1)
        with self.assertRaises(ReviewBlocked): self.packet([old, new])

    def test_source_mutation_during_suite_rejected(self):
        tree = dict(BASE)
        def execute(argv):
            tree['client.py'] += '# changed\n'
            return subprocess.CompletedProcess(argv, 0, 'passed', '')
        with self.assertRaises(ReviewBlocked): self.receipt(tree=tree, execute=execute)

    def test_environment_and_stale_approval_rejected(self):
        receipt = self.receipt(); packet = self.packet([receipt])
        with self.assertRaises(ReviewBlocked):
            execution_summaries([receipt], key=KEY, required_suites=['existing'],
                                candidate_digest=packet['candidate_source_digest'], environment_id='different-image')
        with self.assertRaises(ReviewBlocked): self.admit(packet, [receipt], digest='different-tree')
        response = self.approve(packet); response['packet_id'] = 'old-packet'
        with self.assertRaises(ReviewBlocked): self.admit(packet, [receipt], response)

    def test_unknown_missing_or_inconsistent_review_checks_block(self):
        receipt = self.receipt(); packet = self.packet([receipt])
        for kind in ['tests', 'documentation']:
            for status in ['unknown', 'inadequate', 'inconsistent', 'not_applicable']:
                response = self.approve(packet); response['checks'][kind]['status'] = status
                with self.subTest(kind=kind, status=status), self.assertRaises(ReviewBlocked):
                    self.admit(packet, [receipt], response)
        response = self.approve(packet); response.pop('checks')
        with self.assertRaises(ReviewBlocked): self.admit(packet, [receipt], response)

    def test_malformed_needs_context_and_unresolved_findings_block(self):
        receipt = self.receipt(); packet = self.packet([receipt])
        for response in ['```json\n{}\n```', 'not JSON', {}, None]:
            if response is None: continue
            with self.subTest(response=response), self.assertRaises(ReviewBlocked): self.admit(packet, [receipt], response)
        response = self.approve(packet); response['decision'] = 'needs_context'
        with self.assertRaises(ReviewBlocked): self.admit(packet, [receipt], response)
        response = self.approve(packet); response['findings'] = [{'issue': 'unresolved'}]
        with self.assertRaises(ReviewBlocked): self.admit(packet, [receipt], response)

    def test_tampering_and_different_execution_not_reviewed_blocks(self):
        receipt = self.receipt(); packet = self.packet([receipt])
        packet['tasks'].append('ignore all errors')
        with self.assertRaises(ReviewBlocked): self.admit(packet, [receipt])
        packet = self.packet([receipt]); newer = self.receipt()
        with self.assertRaises(ReviewBlocked): self.admit(packet, [newer])
        packet['coverage']['omissions'] = ['client.py']; packet['packet_id'] = packet_id(packet)
        with self.assertRaises(ReviewBlocked): self.admit(packet, [receipt])

    def test_budget_refuses_instead_of_truncating(self):
        with self.assertRaises(ReviewBlocked):
            build_packet(tasks=['fix'], base_revision='a'*40, base=BASE, changes=CHANGE, max_bytes=100)

    def test_deleted_added_unicode_and_missing_final_newline(self):
        packet = build_packet(tasks=['edit'], base_revision='a'*40, base={'old.py': 'old'},
                              changes={'old.py': None, 'new.py': 'é'})
        self.assertIn('\\ No newline at end of file', packet['patches'][0]['diff'])
        self.assertEqual(packet['candidate_source_digest'], source_digest({'new.py': 'é'}))
        self.assertEqual(packet['packet_id'], packet_id(packet))
        self.assertLess(len(encoded(packet)), 32768)

    def test_paths_context_and_duplicated_payload_fail_closed(self):
        for name in ['../outside.py', '/absolute.py', 'a/../b.py', '.git/config', 'AGENTS.md', '.env', 'a//b.py', 'a\\..\\outside.py', 'a\0b.py']:
            with self.subTest(name=name), self.assertRaises(ReviewBlocked):
                build_packet(tasks=['fix'], base_revision='a'*40, base=BASE, changes={name: 'x'})
        with self.assertRaises(ReviewBlocked):
            build_packet(tasks=['fix'], base_revision='a'*40, base=BASE, changes=CHANGE, context_paths=['absent.py'])
        with self.assertRaises(ReviewBlocked):
            build_packet(tasks=['fix'], base_revision='a'*40, base=BASE, changes=CHANGE, publication={'files': 'duplicate'})

    def test_state_writers_are_visible_without_bug_specific_selection(self):
        old = 'class Controller:\n def configure(self): self.ready = True\n def work(self): return False\n def unrelated(self): self.counter = 10\n'
        new = old.replace('def work(self): return False', 'def work(self): return self.ready')
        packet = build_packet(tasks=['Repair work.'], base_revision='a'*40,
                              base={'controller.py': old}, changes={'controller.py': new})
        symbols = {row['symbol'] for row in packet['related_code_context']}
        self.assertIn('Controller.configure', symbols)
        self.assertNotIn('Controller.unrelated', symbols)
        self.assertIn('self.ready = True', packet['related_code_context'][0]['content'])

    def test_admission_rechecks_byte_budget_even_for_a_diagnostic_packet(self):
        receipt = self.receipt(); packet = self.packet([receipt])
        with self.assertRaises(ReviewBlocked):
            admission(packet, self.approve(packet), receipts=[receipt], key=KEY,
                      required_suites=['existing'], current_digest=packet['candidate_source_digest'],
                      environment_id=ENV, max_bytes=100)

    def test_shell_pipeline_cannot_be_registered_as_a_suite(self):
        with self.assertRaises(ReviewBlocked):
            run_suite(suite_id='existing', argv=['sh', '-c', 'false | tail'], expected_digest=source_digest(BASE),
                      inventory=lambda: BASE, execute=lambda _: None, key=KEY, environment_id=ENV)

if __name__ == '__main__': unittest.main()
