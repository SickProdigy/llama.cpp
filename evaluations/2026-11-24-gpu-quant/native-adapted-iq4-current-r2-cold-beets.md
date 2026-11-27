# Current adapted 27B IQ4_XS: fits mostly on GPU, published workflow fails

November 27: the fresh operational retry completes three dependent Beets tasks
in **110.58 coding minutes / 114.69 supervisor wall minutes**, but fails the
requested repair, documentation and cancellation workflow. The actor creates
the correct upstream issue, personal fork and PR. Its published patch breaks
ordinary import dispatch, omits `/beetscancel`, and publishes no new tests.
This is one workflow, not three independent reliability samples.

The [first attempt](native-adapted-iq4-current-interrupted.md) remains a separate
disk-reserve interruption without a quality score. This retry used a new
fixture, profile, process and conversation after the
[owned Q8 retirement](study-owned-q8-retirement.md). It received the
[same three literal requests](beets-natural-task-queries.json), no preliminary
model read, no private grader feedback and no operator repair or resume.

| Turn | Minutes | Actual published project / originals | Independent behavior |
|---|---:|---|---|
| Lifecycle repair | 51.92 | 83 / 83 pass, plus 2 subtests each | Fail |
| Documentation | 5.03 | 83 / 83 pass, plus 2 subtests each | Fail |
| Cancellation feature | 53.63 | 83 / 83 pass, plus 2 subtests each | Fail |

All CLI exits are zero, without external timeout. The final turn ends on the
native repeated-read guard after five unproductive `read_file` calls; its last
model response is a tool call, not a final successful coding answer. The local
final project suite has **5 failures / 92 passes / 2 subtests**. Local edits and
their tests differ from the actual published tree and cannot substitute for it.

The published `_timer_elapsed` passes `(folder, activation)` to an unchanged
worker accepting only `folder`. Ordinary thread dispatch raises `TypeError`
before the worker body runs. The worker has no activation/stop check, the
schedule method has no stopping guard, and the published tests remain identical
to baseline. The PR nevertheless claims a worker check, stopping-aware
scheduling, removal of `_stop_timers` and five added tests. The final README
also promises waiting-worker cancellation and completion logging after disable
that the published code does not implement. `_report_result` suppresses logging
while stopping; that documentation mismatch also exists in the local patch.

The local first-turn patch passes the registered initial behavior checks but
fails one immutable original test that directly calls the worker's old private
signature. That gate requires private-interface compatibility in addition to
observable behavior. Its rejection alone is not proof of a public regression;
the actual published dispatch failure is. No gate-free causal ablation was run,
so the gate cannot be declared the cause of incomplete publication. The first
workspace-publication read denial has a different cause: the actor supplied
`wide-beets-abandon-queued` instead of its created trial-prefixed branch.
Correct-branch reads subsequently succeeded; this was not a 40-character-ref bug.

The five local authored initial tests offer limited coverage. Two never create
the stale queued work their names claim to test, the cleanup test does not
assert that a waiting worker never starts, and the edited original reporting
test removes the invocation-count assertion. None is published. Actual-source
test transplantation at turns 0 and 2 finds no added or changed tests; candidate,
prior and reference suites all pass. Those green suites do not detect the
dispatch defect.

Supplemental observations use the actual Nicotine+ **3.3.11 PluginHandler** in
an isolated, network-disabled container. The pinned core source and candidate
hashes match; baseline behavior matches the expected negative controls and the
correct reference passes all four cases. The IQ4 publication fails ordinary
fresh-instance dispatch with the argument mismatch, cannot reach the
instrumented waiting-worker lock, and has no registered cancel command. These
failures mostly expose one dispatch defect, not four independent model errors.
Fake timers, deferred workers and a fake import boundary are used: no GUI,
music files, real beets process or owner settings are touched. Separate
same-object reload controls remain supplemental API stress, not GUI proof.
The prior Q4 publication is also checked: fresh-instance timer handling passes,
but old dispatched/waiting work still runs after disable and cancellation is
unregistered. These observations do not change historical model-call scores.

All **67/67** backend requests complete without HTTP/transport errors or length
finishes. The largest actual coding input is **81,911 tokens**, with substantial
cached input. Native compression uses 35,054 uncached input tokens and 3,311
output tokens, finishing normally in **19.24 minutes**. The first resumed main
request uses 38,158 uncached input tokens and takes **11.59 minutes**. Together
they consume **30.83 minutes** of the final feature turn. All three literal user
tasks remain in the resumed and final main requests. The helper summarizes an
older prefix; recent PR and documentation records remain outside that prefix in
retained main history. Its superseded historical state is not, by itself, a
compression failure. Structural/task retention does not prove complete semantic
fidelity or successful task recovery.

The selected [measured capacity layout](resource-adapted-iq4-current.md) is
98,304 context, 63/66 GPU layers, ubatch 64, q4_0 K/V, one slot, two cache
checkpoints, 512 MiB cache RAM, load mode `none` and automatic fit off. The
sampler is temperature 0.8, top-p 1, top-k/min-p 0, repeat penalty 1, presence
penalty 0, thinking off, seed 20261124; main and auxiliary output caps are 8,192.
The current owner-derived evaluator is image
`c9b40eb8dea441cba7ded2e6589e5c011545ffc1ec76a0dc736f8e399d8f947b`;
llama.cpp is `fee4289628e7ba09f6fbf62d6ce4325aebb2531ffde2154d41276fe4acc58da3`.
The evaluator's pytest/shim qualification and execution/scope gates are
experimental production differences, not weight tuning or a production rollout.

Across 634 ten-second samples, GPU memory peaks at **15,926 MiB**, with about
349 MiB free in the recorded layout. CUDA model buffers are 13,122.69 MiB;
host model buffers are **1,250.63 MiB**, GPU KV 1,728 MiB and GPU compute
451.91 MiB. This is explicitly a mostly-GPU layout. Aggregate charged cgroups
peak at 7,219,105,792 bytes and process PSS at 3,342,588,928 bytes, including
recorded helpers/cache. No study swap, resource guards or measurement errors
are observed; both disk reserves stay above 100 GiB. Sampling can miss peaks,
and timings share an active host rather than an isolated benchmark machine.

The exact public artifact is `Qwen3.8-27B-hermes-IQ4_XS.gguf`, 15,321,491,104 bytes,
SHA256 `d25b50a2bfdfba157c2baf959f298d706d70083255bab95232ffcd40fbafcaba`, from
[netprojects revision 10fdf357](https://huggingface.co/netprojects/Qwen3.8-27B-hermes-adapted-GGUF/tree/10fdf357f14825c61ad7eb42a932e1f1e4390e8f).
Full length/hash were checked before inference. Its importance-matrix metadata
records `imatrix.gguf`, `calib-train.txt`, 496 entries and 104 chunks; Q4 records
no such metadata. Header shapes/templates match, but equal unquantized weights
or calibration are not proven. Q4 uses 56/66 GPU layers and ubatch 128, so this
is a practical artifact/layout comparison, not a precision-only experiment.

Authenticated final readback verifies the fork parent, unchanged 40-blob
upstream and PR #2 open/unmerged at
`8ffd43eb0f02aaca5abd870f02cc4b5931050e9c` against baseline
`f9980ddc8aa6809e2f98f3ee95436bdb368e7a3d`. A single connected-MCP issue read
confirms owned issue #1 closed; an empty issue-list response is not used as
absence or closure proof. Private signed test receipts match the actual
published tree for four commits and the PR; keys are excluded from the export.

Original model alias/context, container identities/images/configurations,
four profile hashes, all 30 retained model records and owner pending edits pass
independent preservation checks. Exact study containers, the empty owned network
and the supervisor's exclusively attached anonymous volume are removed; staged
IQ4 is preserved. **The strict restoration check failed:** Hermes-Codex's start
timestamp changed during the run, although its ID/image/configuration/running
state/health/restart count match. The cause is unknown; retained Docker events
do not establish it. The original failure is retained, a separate qualified
reconciliation records the exception, and no uninterrupted Codex-preservation
claim is made. Post-control free space is 103.75 GiB on original-model storage
and 115.28 GiB on staging.

The [archive with 42 manifested files](native-adapted-iq4-current-r2-cold-beets-evidence.tar.gz)
includes actual published source snapshots, full source-hash indexes and curated
numeric/audit evidence. The [summary](native-adapted-iq4-current-r2-cold-beets-summary.json),
[validation](native-adapted-iq4-current-r2-cold-beets-validation.json) and
[privacy scope/result](native-adapted-iq4-current-r2-cold-beets-privacy.json) are
separate. Profiles, credentials, signing keys, private graders/reference code,
actor conversations and unpublished local source are excluded.

From the repository root, verify the saved measurements, source hashes and
static dispatch mismatch without inference or behavior replay:

```sh
python3 evaluations/2026-11-24-gpu-quant/verify_current_iq4_r2_native.py evaluations/2026-11-24-gpu-quant/native-adapted-iq4-current-r2-cold-beets-evidence.tar.gz
(cd evaluations/2026-11-24-gpu-quant && sha256sum -c native-adapted-iq4-current-r2-cold-beets-evidence.sha256)
```

IQ4 does not become a practical workflow recommendation from this sample.
Earlier correct slower Q4 workflows remain measured overnight-use tradeoffs;
this slower failed workflow supplies no equivalent correctness benefit. The
[retained IQ3 current-runtime reference](resource-adapted-iq3-current.md) now passes
capacity admission; coding remains untested.
No new weight download, local quantization, GPU purchase or production model
replacement is part of this stage. No GPT-5 equivalence or autonomous reliability
is established.
