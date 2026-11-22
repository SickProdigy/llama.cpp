# Fresh LocalAI workflow — stage 3a

Six native turns completed, with actual upstream issues, personal forks and PRs.
All primary checks passed, but **neither arm met the complete delivered-message
contract**. Eight timely critic approvals produced no findings. The original
runtime is restored and verified. The second fresh family is still required;
this is a completed part, not completion of the full goal.

## Results

| Measure | Documentation control | Full review |
|---|---:|---:|
| Native turns, same logical session | 3 | 3 |
| Native elapsed, including common review/test work | 40.11 min | 38.32 min |
| Critic requests | 4 | 4 |
| Critic backend time, included above | 4.87 min | 4.62 min |
| Primary checks, local / actual fork snapshots | 3 / 3 pass | 3 / 3 pass |
| Introduced exact-fit preservation regression | Yes | No |
| Public delivered-message cap satisfied | No | No |
| Useful reviewer findings / review timeouts | 0 / 0 | 0 / 0 |

Across eight proposals: packets **11,121–21,071 bytes**, actual rendered inputs
**4,126–6,844 tokens**, critic time **62.66–96.34 seconds**. All responses were
complete, stopped normally and arrived before the fixed 240-second deadline.
The output cap was 1,024. The [runtime measurements](part3a-runtime.json) record
the 27B IQ3XXS at 98,304 q4 KV, peak 12,932 MiB, readiness 61.44 seconds and
first native API response 157.49 seconds (13,659 input tokens, zero cache).
Disk-cache state was uncontrolled; these are not cold-start measurements. Native elapsed is one run per arm, with order, cache and
sampling differences; the107-second difference is not a causal review benefit.
The control also pays for genuine execution and an external documentation check;
it is not a no-review latency baseline.

[Measurements](part3a-reviews.csv), [turns](part3a-turns.csv),
[summary](part3a-summary.json), [evidence archive](part3a-evidence.tar.gz),
[archive hash](part3a-evidence.sha256), [replay](part3a-replay.md).

## Protocol and publication prerequisites

The same frozen symptom-led bug request, README followup and optional-marker
feature followup reached each arm in order. Only already-issued tasks reached
the actor/reviewer. No private grader, reference implementation or operator
correction was supplied. Normal native Hermes CLI used an actual checkout,
isolated profile, memory/skill tools and persistent logical session. All six
raw user-task prefixes and frozen query hashes match; both lineages have one
session node. Before followups, native `sessions discard SID --yes` returned 0
with an exact conversation-hash invariant. This is a disclosed harness lifecycle
control, not forced unlocking or task replay.

Part 2 qualified no reviewer. The selected 27B self-review path avoids swaps and
retained the measured actor prefix in calibration; it is not an accuracy winner
or a production default. Native main requests retain the normal 8,192-token cap
and backend-default seed; only the critic seed is fixed. Static class declaration
context is a generic, source-backed addition, frozen before fresh inference.
The eight library modules and controller remain unchanged for the next family.

The trusted adapter materializes the actual cumulative MCP publication payload.
Before every commit/PR, it genuinely runs the project suite and mounts immutable
original tests over the candidate tests directory for a second run. Environment
identity includes the pinned image and original-test digest. Test containers
have no network, credentials, actor profile, private grader or Docker socket.
Private per-arm keys remain outside model/test mounts. Independent audit verified
all eight admitted proposals' source, MACs, output hashes and execution-before-review
ordering. A negative control passed rewritten tests but failed the untouched
original assertion; it was blocked before a critic call or publication.

The 31 framework checks plus 20 subtests pass in the pinned Python 3.14.9 image.
These controls establish authentic prerequisites, not semantic correctness.

## What the independent audit found

**Exact-fit regression in the control.** Its code reserves a marker character
unconditionally on the final permitted chunk, losing text even when the answer
fits exactly. Nine of eighteen supplemental complete-input properties fail in
every published phase. A new test explicitly expects the erroneous marker.
The full-review arm instead trims only when leftover text exists; all eighteen
properties pass. That implementation was already present before its first
review, so the difference cannot be credited to a reviewer correction.

**Delivered length remains wrong in both arms.** The opt-in public handler adds
`reader: ` after chunk sizing. A probe through the actual handler, with a mocked
300-character provider answer and fake Nicotine dispatch, delivers208 characters
at a200-character setting in all six published snapshots. The original delivers209;
the reference fix delivers208. Thus the reference and primary grader also miss
this path. Both READMEs' universal delivered-message cap claims overstate behavior.
This probe is not a live provider or GUI acceptance test.

**Tests and documentation need interpretation.** On original code, the control's
initial test set has one genuine overflow failure and one erroneous exact-fit
expectation. The full arm has two genuine overflow failures. Neither is an import
failure. Feature tests also fail on absent settings/signatures, which demonstrates
feature dependence rather than exhaustive coverage. The control README's blanket
exact-limit statement varies incorrectly with chunk count and marker mode.
Its issue/PR claim that configuring 80 yields 81 also ignores the worker's 200–1000
clamp: a direct helper 80 test is valid, but is not configured-delivery evidence.

The frozen primary checks passed all twelve local/actual-remote snapshots and
all eight attempted proposals. They validate the original helper/worker symptom
and feature but are not a complete oracle. Supplemental probes were registered
**after inspecting control phases 0/1, before the full arm started**, then executed
after runtime restoration. They are explicitly posthoc source-audit findings,
not newly predeclared detection scores or corrective model feedback.

Actual project counts were 88/93 for initial/feature control snapshots and 87/92
for full review, each plus 2 subtests. Immutable suites had 83 passes plus 2 subtests.
LocalAI module counts were 13/18 and 12/17 respectively. The full arm's initial
summary calls 12 the full suite, but its native command ran the LocalAI module;
that wording is imprecise, not evidence of invented execution. Authentic gate
logs establish the separate whole-project runs.

## Real forge and runtime checks

Each arm opened issue 1 upstream, created its personal fork, published three
commits on one feature branch and maintained upstream PR 2. Actual fork clones
match PR head SHAs/trees, expected upstream parent/base and local source digests.
Only the intended code, tests and later README changed, with regular file modes.
Independent connected Gitea readback confirms both issues closed and both PRs
open/unmerged. No merges or upstream default-branch edits occurred.

[Preservation checks](part3a-preservation.json) confirm original container
IDs/images/configuration, all four profile hashes, all 29 model-file metadata,
owner pending edits and ignored instructions. Hermes-Codex's complete runtime
snapshot is unchanged. Original VibeForged alias/context 98,304 is restored; model
disk reserve is 123.86 GiB. The isolated test containers/network and stopped
supervisor were removed. Nonempty unused image volumes were preserved rather
than globally pruned. No models were downloaded, deleted, trained or quantized.

The allowlisted archive has 1,260 manifest entries plus the manifest.
[Offline verification](part3a-artifact-validation.json) rebuilds all eight exact
packets and checks captures and twelve source-bound grades. Native system/memory,
profiles, credentials, issuer keys/MACs and unreleased XML tasks/checker/reference
are excluded. Published LocalAI primary checks are an exact class extraction
with a disclosed entrypoint transform and original private-file hash. Historic
MAC authentication was checked privately; public replay cannot authenticate
historic MACs without those private keys.

This stage demonstrates working, bounded publication plumbing and faster reviews
than the prior timeout-heavy pilot. It does not demonstrate reliable mistake
detection, unattended operation, or a need to buy hardware. The next family tests
a different bug path with dependent followups under the same frozen code.
