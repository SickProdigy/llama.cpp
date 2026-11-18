"""Reject no-progress repetitions without rejecting valid retries after a write.

Write idempotency remains the bounded guard's responsibility: an ambiguous or
successful create must never be retried merely because another write advanced
this ledger. Only confirmed successful native mutations advance its epoch.
"""
import json

class RetryLedger:
    def __init__(self):
        self.epoch = 0
        self.rejected = set()

    def key(self, name, args):
        return str(self.epoch) + ':' + name + ':' + json.dumps(args, sort_keys=True)

    def reject(self, name, args):
        self.rejected.add(self.key(name, args))

    def advance_after_write(self, *, succeeded):
        if succeeded:
            self.epoch += 1
