# Fresh adapted27B Q3 Announcer workflow

Completed, restored and independently audited November24,2026. **The initial
repair and cancellation feature pass scoped independent source/behavior checks
on the published code. Documentation and reporting have qualifications, so this
is not an unqualified whole-workflow pass.** The same model's [Spam repair fails](native-q3-spam.md).
These are two fresh families with dependent followups, not a reliability rate.

The [pinned Q3 resource layout](resource-q3.md) is retained: 98,304 context,
requested `-ngl 99`, non-mapped loading, q4K/V, one slot, prompt cache512MiB and
two context checkpoints. Backend cap6.5GiB/no swap; aggregate guard8GiB.
Main/compression output reserve8,192, temperature0.8, thinking off. Normal native
memory/approval/persistence policy and scoped forge tools remain in place, with
a visible project-test publication gate. The read-only control is separate from
the fresh coding conversation; three coding stages share one native lineage.
No private grader feedback or corrective audit hints reach the actor.

| Stage | Actor time | Project / immutable original | Independent outcome |
|---|---:|---:|---|
| Send-time disabled check | 9.90 min | 85 / 83 | Source/behavior and remote equality pass |
| README followup | 1.19 min | 85 / 83 | Only README changes; re-enable wording qualification |
| Scoped pending cancellation | 9.56 min | 89 / 83 | Source/behavior and remote equality pass |

Two immutable-original subtests pass at every stage. All frozen local/remote
independent checker exits are0. These checks and manual source/test/documentation
review are separate from the actor's green tests and the saved-evidence verifier.
They do not establish live Nicotine+ GUI/network correctness or autonomous reliability.

## Source, preservation and authored tests

The initial patch adds a boolean send-time guard before the joined-room check,
preserving preview, scheduling, duplicate cooldown, pending-entry removal and
completion. Both new tests reject original source. The before-first-send case
is a genuine regression; the between-room test manually fires callback0 and
then replays it through the fake runner, confounding an exactly-once sequence.
Separate frozen checks dispatch callbacks correctly and pass. Existing test AST
is initially unchanged apart from the additions.

The feature stores `(event_id, target_room)` consistently, strips/casefolds the
requested room, removes only matching pending entries, and cancels the real
event IDs. Surviving jobs retain replies and complete normally; a fully cancelled
scoped job replies immediately. No-argument cancellation preserves the old
cancel-all behavior. Already-fired entries cannot be selected, and posted
messages are never retracted. The send-time guard remains effective.

Four added feature tests all fail pre-feature source with assertions, not
missing-method errors. One asserts the documented immediate completion reply
for full scoped cancellation, rather than a separate old defect. The fake runner
is improved to skip cancelled IDs; existing test-function AST is unchanged,
although the helper AST changes. The earlier callback-replay caveat remains.
The immutable original83 independently pass with their original helper.
Manual source checks and frozen tests cover selective/case-insensitive and
multiple-job cancellation, unknown rooms/counts, surviving work, prior send-time
guards and no-argument behavior.

The README's cancellation paragraph accurately describes pending-only selection,
case-insensitive matching and completion. Its earlier stable-off paragraph says
none of the remaining sends post after switching off. A control using the same
immutable fixture as the Q4 documentation audit shows the needed qualification:
**re-enabling before a pending callback allows that room to send**. Turning off
is not permanent cancellation; skipped callbacks are not retried. That wording
remains in the final publication and is not corrected by the evaluator.

## Actual Gitea publication and claims

The actor opens upstream issue3 and PR4 and reuses its already-verified personal
fork `hermes-agent/hermes-wide-q3-20261123` on branch
`wide-queue-q3-announcer-queued-disable`. Reuse is not credited as a second fork
creation. Three commits are independently fetched with equal local/remote bytes.
Final head is `341f029c84d6d100de0c19794f620a6ea435cbfa`; upstream main remains
`93f7d0429ce3acd9479e47fefd2563a76ffc5181`. Independent connected readbacks verify
issue3 closed and PR4 open/unmerged after completion.

Initial/final answers label10/14 plugin-file tests as the full suite; actual
project counts are85/89. The PR body correctly scopes its initial10 to the plugin
test file, but the title/body stay on the original fix and omit the cancellation
feature. The same PR-edit tool was available. Reported issue/fork/branch/PR and
publication claims otherwise match the independent readbacks. No wrong-host URL
or incorrect published-commit claim is present in these answers.

## Resource observations and restoration

All39 HTTP bodies complete without transport errors; largest completed prompt
is **39,532 tokens**. Across153 complete samples, peak charged experiment
cgroups are **6.598GiB**, all-process PSS **2.377GiB**, and GPU **14,946MiB**.
Own swap, measurement-error samples and resource-guard events are zero. Do not
sum independent peak columns. Global swap counters increase14,595pages in and
9,953out, which cannot be attributed to this no-swap experiment. These samples
do not prove a continuous entire-host allocation bound; transient helper and
shared/cache accounting have limits.

Coding actor time totals **20.65minutes**, excluding the separate228.68s read
control. First coding HTTP is143.06s for13,730prompt tokens; HTTP median23.80s,
maximum147.78s, including prompt processing and generation. These are not
isolated decode or cold-cache benchmarks. Q3 and Q4 generate different
trajectories/context sizes; their public calibration metadata differs. Do not
attribute this timing difference solely to bit precision or infer a quality
ranking from the shorter run.

Original service IDs/images/configurations, four profile hashes, all29 original
model metadata, owner pending files/instructions and the entire Hermes-Codex
snapshot are independently verified restored/preserved. The five owned stage
container names and empty internal network are independently verified absent.
Minimum observed disk reserve is110.65GiB; after restoration110.65GiB remains.

After both Q3 families finish their audits and restoration, only the newly
downloaded Q3 study weight is full-hash/ownership verified and temporarily rotated,
with a matching pinned public prefix checked before removal. Original29 entries
remain unchanged. This admits Devstral while retaining100GiB reserve and one
additional large study weight at a time; it is not a claim that Q3 is useless.
Selected weights can be restored from the recorded public pins at the end;
see the [rotation records](study-weight-rotations.json).

## Evidence and remaining scope

[Summary](native-q3-queue-summary.json), [sanitized archive](native-q3-queue-evidence.tar.gz),
[SHA256](native-q3-queue-evidence.sha256), [privacy scan](native-q3-queue-privacy.json)
and [validation](native-q3-queue-validation.json) retain numerical measurements,
source fingerprints, project/original-suite logs and scoped independent audits
and publication projections. Raw native prompts/responses, profiles/databases,
full private project source, primary graders, independent grader logs and
credentials remain local.

```sh
python3 evaluations/2026-11-23-wide-memory/verify_candidate_native.py q3 queued_announcements
```

The verifier checks saved consistency, not private behavior reexecution or overall
correctness. Q3 fixes this family's code while failing the other family's initial
repair; its documentation/reporting qualifications remain. Devstral and GLM
still require actual resource and native quality evaluation. No model winner or
autonomous-reliability conclusion is established.
