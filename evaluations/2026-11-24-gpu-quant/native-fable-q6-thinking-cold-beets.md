# Fable Q6 reasoning with a cold coding gateway

November26: the fresh reasoning-enabled Q6 trial fails repair, documentation,
cancellation and publication checks in13.16 coding minutes. Its final source
passes91 project tests plus2 subtests, and the immutable original suite passes.
Passing those tests does not cover the independently observed defects.

| Dependent turn | Coding seconds | Actual outcome |
|---|---:|---|
| Lifecycle repair |274.98|No source changes; project/original suites pass, independent lifecycle check fails |
| Documentation followup |81.46|No source changes; requested documentation not produced |
| Cancellation feature |433.14|Plugin, README and tests changed;91 tests/2 subtests pass; independent feature check fails |

The final patch adds8 Beets test methods while preserving the8 original methods
and all unrelated source. It leaves the lifecycle functions unchanged: dispatched
workers waiting for the serialization lock can still import after disable or
shutdown. Cancellation tracks only pending timers, not those dispatched/waiting
workers. An empty `/beetscancel` argument returns usage instead of cancelling all;
it requires an unrequested `--all` flag. Named cancellation validates the current
filesystem folder before removing queued work. The independent feature suite has
6 registered methods with8 failure records including subcases. The README falsely
claims no-argument cancellation works, while documenting some other limitations
honestly. Original setup/command guidance remains present.

Publication fails independently: after completion, authenticated readbacks
verify all40 upstream baseline blobs unchanged, zero issues, zero PRs and HTTP404
for the actor's fork. No issue needs closing. The scoped proxy records11 calls,
8 denied for repositories outside this trial. The final answer asks the user to
fork/push through GitHub and replace the evaluation checkout, despite the exact
Gitea remote already being included in the initial Git-facts context. A local
commit and green authored tests do not establish a remote contribution.

This trial starts directly with coding in a fresh native profile/process and
scoped gateway; no preliminary read control can contaminate native connection
health. Actual configured-MCP identity, repository lookup and tree reads pass
separate read-only admission. The initial fixture is independently verified
unchanged with no existing actor fork. The first setup attempt fails on a local
profile-directory permission before actor calls; a new writable task directory
resolves it without changing prior profiles or service settings.

Main generation is temperature1.0/top_p0.95/top_k20/thinking enabled, seed20261124,
16,384 output cap and98,304 context, with q4_0 K/V. Current llama.cpp is pinned
b12723-abca69200; the experimental Hermes runtime retains its prior pinned image.
All109 frozen source fingerprints verify. There are81 completed backend requests,
no auxiliary compression requests or length finishes, and maximum completed input
64,066tokens. Context exhaustion/compaction does not explain these failures.
The earlier Q4 reasoning run used an older backend and shared preliminary read
state; the [same-method cold Q4 cell](native-fable-q4-thinking-cold-beets.md) also fails.
Both use an older experimental Hermes runtime, distinct from the rebuilt owner
image; future current-runtime cells require separate qualification.

Full file SHA256 and actual41/41 GPU placement are verified. Peak sampled GPU is
11,566MiB; GPU model buffer10,392.38MiB, host model buffer397.85MiB and GPU KV540MiB.
Across86 samples, with a10-second pause between collections, no measurement errors,
guards or study swap are observed. Charged cgroups peak at7,445,458,944bytes and
process PSS at2,243,700,736bytes. Sampling can miss transient peaks; whole-host swap
is not attributed. All original services/alias/context,30 retained model metadata
entries, four owner profile hashes, pending owner edits and Codex are preserved.
Owned terminal supervisor/backend/helpers/network are removed. Disk reserve is
106.69GiB afterward. No download, quantization, deletion or production policy change.

The [sanitized summary](native-fable-q6-thinking-cold-beets-summary.json),
[SHA256](native-fable-q6-thinking-cold-beets-summary.sha256) and
[validation receipt](native-fable-q6-thinking-cold-beets-validation.json) bind saved
numeric observations and curated audits. Private messages, full source, grader
outputs and credentials remain local. This is development evidence from one
lineage, not an autonomous-reliability estimate or a GPT-5 equivalence claim.
