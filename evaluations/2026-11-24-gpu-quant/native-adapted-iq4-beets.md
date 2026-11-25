# Public adapted27B IQ4_XS: local repair succeeds, full workflow fails

This fresh, explicitly trusted native trial does **not** qualify the model for
the complete coding/Gitea workflow. The initial lifecycle repair passes; the
README overstates disabled-state reporting, cancellation has counting and stale
callback bugs, and no issue, personal fork, commit or PR is published.

| Dependent task | Independent result | Actor elapsed |
|---|---|---:|
| Disable/shutdown lifecycle repair | Dispatched/waiting work abandoned across re-enable; running import finishes; original behavior preserved |1052.55s /17.54min |
| README follow-up | Existing setup/safety guidance preserved; state descriptions mostly correct; exit-status logging claim inaccurate |192.98s /3.22min |
| Optional-folder cancellation | Running work counted as cancelled; repeated-folder jobs undercounted; cancelled callback can revive against newly queued work |3899.73s /65.00min |

Coding totals **85.75 minutes**; separate read control takes 4.75 minutes.
Launch through verified restoration takes 94.13 minutes, including setup and
independent grading. These are operational wall times, not isolated quantization
or decode-throughput measurements. No operator hints, resends, continuation or
stop are supplied. A conditional stop consideration is withdrawn when native
fallback makes progress; the original run completes unchanged.

## Source, behavior and tests

The final project suite has 92 passing tests plus 2 subtests. All 83 immutable
original tests plus 2 subtests pass at every phase. Three initial and six feature
test methods are added without changing pre-existing test functions. Green tests
do not establish correctness:

- The registered feature checks fail when cancellation reports2 not-started
  imports with 1 running and 1 waiting. The running import does finish; this is
  not evidence that it was killed.
- Additional **posthoc** timer-entrypoint controls show 2 dispatched jobs for the
  same folder counted as 1, and an old cancelled callback running after new work
  for that folder is dispatched. Both cases pass the reference and fail the
  baseline missing the feature. These checks are distinct from the registered
  grade and were never supplied to the actor.
- Initial authored tests on the prior implementation fail on the new private
  activation field rather than the target behavior. Feature tests on the prior
  implementation fail on absent feature fields/callbacks and private worker
  arity. This does not prove comprehensive behavioral regression coverage. The
  sleep-based running test does not force cancellation during an active import.
- Actual result-handler controls confirm normal completion logs 1 result,
  completion while disabled logs 0, and completion after re-enable logs 1.
  README's claim of normal reporting after disable remains inaccurate.

The pinned Nicotine+3.3.11/master dispatchers accept the optional command syntax
and preserve normal/space-containing manual import paths with automation off.
These are isolated fake-peer/runner tests, not live GUI or real music imports.
The model's17/17 count describes its Beets unittest module; the independent
project runner separately collects92. Its earlier four-added-tests claim counts
an unchanged test; the actual initial additions number three.

## Configured Gitea and retained context

The actor repeatedly treats source attribution to `SickProdigy/nicotineplus-plugins`
as the required upstream despite the selected checkout's disposable Gitea origin.
Wrong-target fork and issue attempts are blocked before remote writes. It finds
the selected origin, reads Git remotes and cached Gitea results, but still asks
for a permitted owner. This is routing failure, not proof that the actual
fixture lacks permission. Independent connected and own-actor reads confirm
no issues/PRs, original upstream `main` unchanged and personal fork404. No owned
issue needs closure.

There are 66 HTTP records: 64 complete and 2 failed native summary requests.
The failed summaries have identical inputs. The actual agent log confirms a
**300-second compression inactivity guard**, despite main-provider 5400-second
settings. Auxiliary compression is configured 120s, floored to 300s; the host
resolves idle 300/ceiling 600. The custom recorder endpoint is not recognized as
Hermes-managed and actual requests lack `return_progress`. This separates a
runtime/configuration limitation from intrinsic model quality.

After the first failure, a main request processes 57,002 input tokens with zero
cached tokens:979.04 backend seconds plus81.31 seconds queued, 504 output tokens.
After the second failure Hermes commits its deterministic fallback, reducing
101 messages to 31 without an LLM-generated summary. The next main request uses
32,673 tokens, zero cached,497.78 backend seconds. Failed intervals remain in
phase/total wall time and are retained separately in the evidence.

Actual CLI output and SQLite ancestry verify the stable CLI receipt-owner
handle and distinct compressed child. Initial repair and current feature
requests remain verbatim; the middle README request does not. The fallback
preserves the active request, tool-cache links and admits unknown active state;
complete semantic preservation is not established. Existing files, source
correctness and documentation are independently audited. Routing and README
errors predate compression, so cannot be blamed solely on it. No whole-window
reasoning claim follows from retained tokens or a successful native handoff.

Scratch-copy getter controls confirm the 300/600 budgets and that explicit 5400 s
auxiliary/host settings resolve correctly without changing the owner profile.
They make no model calls and **do not** prove backend progress compatibility or
successful slow native compression; those controls remain the next runtime gate.

## Fit, accounting and preservation

At 65,536 context, ubatch 64, q4_0 KV, fit off, verbose placement confirms 66/66
layers on GPU. Native peak sampled device use is 15,788 MiB. Initial buffers are
13,729.18 MiB CUDA model,644.14 MiB host model,1,152 MiB GPU KV,149.62 MiB recurrent
state,4.25 MiB rotation,276.50 MiB GPU compute,13 MiB host compute and0.95 MiB host
output. All-GPU layers do not mean zero host allocations. No CPU transformer-layer
fallback is used. The earlier98k allocation failures remain in the
[capacity evidence](resource-adapted-iq4.md).

All 530 samples have complete accounting: peak aggregate charged cgroups 6.883 GiB,
process PSS 2.440 GiB, zero study swap, no measurement errors or guard triggers.
Charged cache/helpers are included when sampled; short 1 GiB-limited test helpers
can finish between 10-second samples. Separate peaks must not be summed and are
not continuous whole-host guarantees. Global swap moves without attribution.
Both actual filesystems retain over 100 GiB reserve. A bounded privacy helper
runs during the separate read control, and read-only source diagnostics run
during the compression failure; timings are not isolated throughput evidence.

Original service identities/images/configuration/default 98k alias, four profile
hashes, all 30 retained model metadata entries, owner pending edits and the Codex
container snapshot pass independent restoration checks. Exact owned runtime
containers/network are removed. The new IQ4 artifact stays in its owned volume.

## Evidence and limits

[Summary](native-adapted-iq4-beets-summary.json),
[archive](native-adapted-iq4-beets-evidence.tar.gz),
[SHA256](native-adapted-iq4-beets-evidence.sha256),
[validation](native-adapted-iq4-beets-validation.json) and
[coherent negative controls](native-adapted-iq4-beets-verifier-controls.json)
retain source/audit bindings, failed requests, native fallback and host buffers.
Run from this directory:

```bash
sha256sum -c native-adapted-iq4-beets-evidence.sha256
python3 verify_iq4_native.py native-adapted-iq4-beets-evidence.tar.gz
python3 verify_iq4_native_controls.py native-adapted-iq4-beets-evidence.tar.gz
```

These check saved consistency, not rerun private behavior tests. Credentials,
session databases, full source snapshots, private graders and raw primary/auxiliary
conversations stay local. [Public production differences](adapted-quant-production.md)
include calibration/tensor mixes. The actual 33-tool schema matches trusted Vibe
Q4/Q6; different checkpoints, samplers, context/placement, trajectories and
calibration prevent precision-only attribution. This is one fresh lineage, no
new everyday selection, GPT-5-equivalence or autonomous-reliability claim.
