# LocalAI stage replay

Verify `part3a-evidence.tar.gz` against `part3a-evidence.sha256`, extract into a
new directory, and run:

```bash
python3 verify_part3a.py --root /absolute/path/to/extracted
```

This checks manifest hashes, rebuilds complete packets from baseline/proposed
source using the frozen library, and verifies response bytes/usage, source-bound
receipt payloads and actual output hashes. It does not rerun tests or verify
historic MACs; private issuer keys are intentionally absent.

For genuine test replay, use the pinned image
`sha256:97b08c5ce375113809299fc8c5dd86ae60600f618158d15fe4ad5fc9d7f4b7ae`
if retained locally (the image itself is not distributed here). It contains
Python 3.14.9 and pytest 9.1.1. Mount an extracted `runs/ARM/turnN/remote-grade/source`
read-only at `/workspace`, network-none, UID1000, capabilities dropped, with
`PYTHONDONTWRITEBYTECODE=1`, and execute:

```text
python -m pytest -q -p no:cacheprovider /workspace/tests
```

For preservation, additionally mount extracted `baseline/tests` read-only over
`/workspace/tests`. Use a new container with no model/profile/credential/socket
mounts, one CPU, 1 GiB RAM and 90-second execution limit. Absolute bind paths must
refer to files on the Docker engine's local filesystem. The original source and
reference must each be tested separately; do not overwrite evidence snapshots.

For primary checks mount extracted `checks` read-only at `/checks` and run:

```text
python /checks/primary_localai.py /workspace bounded_replies PHASE
```

Use phase 0/1/2 matching the already-issued tasks. Future feature checks skip in
phases 0/1. The published checker retains the exact original Bound class; its
manifested extraction record documents removal of the unreleased XML class and
replacement of the entrypoint. Original baseline fails; a separate baseline copy
with `reference/localai/__init__.py` substituted passes the frozen primary checks.
That reference still fails the broader public-delivery cap property.

The supplemental checks use the same immutable original fixture and never reach
the models:

```text
python /checks/check_exact_fit_preservation.py /workspace
python /checks/check_public_delivery.py /workspace
```

The first checks 18 z-only complete-input cases. The second invokes the actual
opt-in public handler with a mocked provider and fake Nicotine dispatch, not a
live GUI/provider. Read `controls/supplemental-audit-registration.json` for the
posthoc timing and classification. Regression controls combine original code
with model-authored tests: inspect failure assertions, not just nonzero exits.

Critic requests/responses, seed/settings, actual packets, rendered token counts,
latency/caller records, complete proposed trees and genuine execution logs are
included per review. Do not rerun authenticated publication against these
completed arenas or treat replayed historical receipts as fresh authorization.
Native system/memory/profile, raw native API prompts, credentials and state DBs
are intentionally unavailable in public evidence; sanitized task hashes,
admission/lineage invariants and final model claims are provided instead.
