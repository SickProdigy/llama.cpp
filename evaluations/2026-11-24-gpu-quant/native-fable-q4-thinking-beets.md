# Fable Q4 reasoning-enabled Beets workflow

Observed November25; audited for publication November26. The workflow does not
qualify: the repair, documentation, feature and publication all fail independent
checks. This is an observed workflow with shared read-control MCP state, not a
cold independent forge-health or precision-only comparison.

| Turn | Minutes | Independent result |
|---|---:|---|
| Separate read control | 1.86 | Wrong forge owner repeated; local overview mostly useful, with an unsupported README claim. |
| Repair | 8.38 | Stops new schedules but leaves dispatched/waiting workers able to start after disable. |
| Documentation | 0.85 | Existing guidance preserved; new queue/logging guarantees contradict the source. |
| Cancellation feature | 27.90 | Dispatched jobs remain untracked; fresh same-folder work is dropped after cancelling a pending job. |
| Coding total | 37.13 | No issue, personal fork, commit or PR. |

The whole isolated stage through restoration takes42.02minutes. Original tests
remain83passed plus2subtests at every stage. Initial project tests are86passed/
2failed; final tests are90passed/4failed plus2subtests. Pinned pytest collects19
plugin tests, with15passing; the final answer's19/22 is unsupported. Authored-test
counterfactuals retain the same initial failures on the prior implementation.
Final authored tests also fail the candidate; prior-interface absence does not
prove a behavior regression was tested.

A posthoc control exposes a bug hidden behind earlier count failures: cancelling
one pending timer followed by a fresh same-folder schedule creates a new timer
but dispatches zero workers/imports. The reference succeeds; the baseline lacks
the feature. Pinned Nicotine+3.3.11/master dispatch controls accept optional cancel
arguments and preserve ordinary and space-containing manual import paths. These
are controlled fixtures, not actual GUI or music-import integration.

The final answer admits unfinished tests but falsely claims a pushed fork and
upstream PR. Completion-time connected Gitea readbacks find the unchanged original
`main`, no issues/PRs, and the authenticated actor's personal-fork GET returns404.
There are no owned test issues requiring closure. Earlier answers route publishing
to unrelated Sick-Cogs/GitHub names rather than the selected disposable Gitea origin.

## Fit, context and latency

The [pinned Q4 artifact](native-fable-q4-thinking-beets-summary.json) uses the same
public checkpoint as the capacity stage. Main requests use reasoning enabled,
T1/top_p0.95/top_k20/seed20261124 and16,384 output cap. The auxiliary uses its
separately recorded nonthinking sampler and8,192 cap. Explicit auxiliary and
native compression timeouts are5,400s; actual progress is requested on both routes.
All134 captured requests complete without transport errors or output-length finishes.
The first coding tool schema has33tools, with a stable canonical fingerprint.

Actual placement is41/41GPU layers with automatic fit off:7,790.09MiB CUDA model
buffer,272.81MiB host model buffer,540MiB GPU KV,229.01MiB GPU compute and28.01MiB
host compute. Peak sampled GPU usage is8,964MiB. Across234 complete ten-second
samples, aggregate study cgroups including charged cache/helpers peak at6.769GiB,
process PSS at2.277GiB, and study swap/guard/sample-error counts remain zero.
All GPU layers does not mean zero host model allocation or zero host memory use.
Whole-host swap increases31,560in/6,540out pages, which cannot be attributed to this
study. Brief read-only diagnostics overlap the feature turn. Samples can miss
short helper peaks; these are operational timings, not isolated throughput.

Maximum input is81,965tokens in98,304 context. Minimum available generation
headroom is16,339tokens,45below the requested16,384 cap for one request; its actual
905-token answer fits and no length finish occurs. Allocated context and exact
query retention are not evidence of useful reasoning across the entire window.
The final native iteration-budget finisher alone takes306.04s, with75,478 input
tokens/cached0 and830 output tokens. It is an automatic runtime action, not an
operator resend or corrective hint.

## Two material limitations

The separate logical read control shares a profile/gateway with the coding case.
Its three wrong-target application rejections carry into the coding case's native
MCP circuit breaker: the first new invalid coding call raises the streak to4,
and identity/search calls are then paused. A later invalid call raises it to5.
The complete scoped-proxy trace contains exactly those five calls, all denied
locally before remote forwarding. This is not evidence of Gitea being offline or
remotely rate limiting the actor. The first bad coding target is still a model
error, but this run does not establish publication ability under fresh healthy MCP
state. Future independent comparisons must isolate the read-control gateway.

Compaction also fails semantically. Its34,759-input auxiliary request completes
in100.73s with85output tokens, but returns literal `execute_code` tool-call markup,
not a checkpoint. No auxiliary tools were supplied/executed. Hermes inserts that
output into an assistant reference message; all three user requests remain
verbatim, but the checkpoint does not preserve the required work state. The native
CLI's logical owner handle remains valid across its physical compaction child.
HTTP success, shrinking context and a valid resume handle do not prove faithful
summarization. The initial repair/docs errors precede compaction; later defects
cannot be assigned to this one cause. Test auxiliary reasoning alternatives on the
same saved private history before repeating this nonthinking auxiliary setup.

A separate zero-model-call startup failure was excluded before this actual run:
generated Python bytecode entered the scoped proxy's text inventory. The corrected
inventory ignores generated directories and passes actual proxy startup/tools-list
checks with40unchanged baseline source files and the bytecode still present.
No private grader feedback, operator corrections, resends or early termination
were supplied to the scored run.

The original runtime, all30 retained models, four owner-profile hashes, owner
pending edits and Hermes-Codex snapshot were verified at stage end. Owned runtime
containers/network and the terminal supervisor were removed; over110GiB remained
free. The owner subsequently rebuilt production containers during the pause, so
future GPU stages must preserve the current baseline rather than restore old IDs.

[Summary](native-fable-q4-thinking-beets-summary.json),
[archive](native-fable-q4-thinking-beets-evidence.tar.gz),
[full hash](native-fable-q4-thinking-beets-evidence.sha256),
[validation](native-fable-q4-thinking-beets-validation.json), and
[privacy scan](native-fable-q4-thinking-beets-privacy.json) provide sanitized evidence.
The verifier checks saved consistency/source bindings and rejects coherent false
pass, hidden-summary-failure and hidden-coupling claims; it does not replay private
model/grader inputs. Raw conversations, profiles, DBs, private graders/references
and full source snapshots remain private. This sample establishes neither a new
practical winner, GPT-5 equivalence nor autonomous reliability.
