# Bounded workflow evaluator components

`bounded_guard.py` admits exact manifested upstream issue/PR writes and fork
branch/file changes. Required manifest fields include the fork name, branch,
original/expected file contents, issue title/body and PR title/body template.
The default source is the approved nicotineplus-plugins fixture; explicit
upstream owner/repo and fork owner fields support separate held-out fixtures.
There is no credential handling or transport in this module.

`retry_ledger.py` blocks an identical rejected model call while the known remote
state has not changed. Only a confirmed successful native mutation advances its
epoch. A read of a missing feature branch can legitimately succeed after branch
creation; successful reads and failed writes do not reset rejection history.
Write idempotency remains separate: progress must never release an ambiguous
or successful create for blind retry.

The dated evidence retains the actual full AIAgent runner, native argument
traces, manifests, profiles' public hashes and external verification. Controls,
fresh runs, resumed stages and evaluator errors must be reported separately.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s evaluations/harness -p 'test_*.py'
```
