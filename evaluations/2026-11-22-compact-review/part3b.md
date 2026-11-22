# Fresh XML workflow: faster review, incomplete or incorrect publication

Both fresh families are complete: twelve native turns across four three-turn
workflows. **None meets the complete task contract.** This is a small diagnostic
sample, not an estimate of autonomous reliability. The XML full-review arm fixes
the behavior but never opens the requested PR; the documentation-control arm
opens a PR with the wrong failure predicate and a genuine no-result regression.

## Conditions and actual interface

The same frozen library, 27B IQ3_XXS checkpoint, P100, 98,304 context, q4 KV,
1,024-token critic cap, 240-second caller, sampler and 32 KiB/10k-token bounds
apply as in [Part 3a](part3a.md). Full runs first, control second. Order, cache,
actor randomness and different trajectories prevent a causal speed/quality win.
Each arm receives the same symptom-led initial request, README followup and
wrong-XML-root feature request in one persistent logical session. No private
checks, corrective operator hints or future feature task reaches either actor
before the corresponding turn. Native discard clears admission state between
turns, returns zero and preserves each transcript; no force unlock or task replay.

Both arms use native Hermes CLI, file/terminal tools, persistence and memory/skill
approval policy, plus experimental focused Gitea 0.1.6, workspace publisher 0.1.3
and selected-project 0.1.0 plugins. Their wrappers make real MCP calls, including
commits from actual files. The normal full native MCP toolset is disabled in the
isolated profiles. This is not an unmodified production-tool-interface test.
All four profiles' 33 wire tool schemas match. Six executable/descriptor files
match the pre-fresh public commit `9dc41e4`; plugin hashes were audited posthoc,
not pre-registered in the native protocol. Two README variants differ only in
nonexecutable documentation. Sanitized configuration/schema/source proofs and
actual plugin sources accompany the archive; private profiles do not.

Every publication proposal requires actual project tests and immutable original
preservation tests, source-bound signed receipts, then external documentation
review. Control withholds behavioral/coverage findings; full enforces all review
findings. This common safety baseline is not an unassisted control. The four
review-per-turn allowance is fixed. Private primary checks run independently.

## XML results

| Result | Documentation control | Full review |
|---|---|---|
| Initial / README / feature turn, seconds | 1134.87 / 248.30 / 446.08 | 2718.46 / 293.59 / 496.39 |
| Critic calls / admitted / blocked | 5 / 4 / 1 | 6 / 5 / 1 |
| Primary local and remote snapshots | All six fail | All six pass |
| Project and preservation suites | All pass | All pass |
| Provider-error/no-result distinction | Wrong | Correct |
| Wrong-root followup | Correct | Correct |
| Actual XML upstream PR | #4, open, unmerged | Absent |
| Issue #3 after cleanup | Closed | Closed |

All eleven critic responses are complete and delivered in 70.81–108.75 seconds;
there are no critic timeouts. Inputs span 12,970–21,470 bytes and 4,975–7,663
rendered tokens. Nine publications are admitted. Native elapsed time includes
agent work and reviews, not just inference. Full initial turn hits the outer
2700-second guard plus shutdown grace despite process exit zero. Its final
assistant stop response existed before that guard and honestly reports that the
PR remains blocked. The remaining live process's cause is not established;
this is not a caught functional defect or a completed workflow.

Control checks `success='false'` instead of `error='true'`. For the genuine
no-result input `<queryresult error="false" success="false"/>`, original code
returns `NO_RESULT`, while published code returns a new failure sentence.
Conversely, `error='true'` without success is missed. The primary checker expects
`WolframError`, an implementation-specific oracle: exception choice alone would
not establish a wrong solution. The wrong attribute and changed ordinary
no-result behavior independently violate the actual request. Added tests largely
reinforce the mistaken success predicate; on original source two fail because
the newly named constant is absent. Nonzero baseline tests alone are not proof
of a meaningful provider-error regression test. README changes describe the
wrong predicate accurately, demonstrating that source/prose agreement can still
misstate the intended behavior.

Full checks the requested error flag before pods and uses the existing generic
provider failure channel. Four genuine initial assertions fail original code;
normal rendering, privacy, no-result preservation and later invalid-root checks
pass independently. Its project suite grows from 83 tests plus two subtests to
94 plus two; control ends at 90 plus two. Green counts do not rank correctness.

## Publication and review findings

Control really opens upstream PR #4 from its personal fork; the full fork holds
five commits but no XML PR, even after dependent followups. Both reuse forks
created in Part 3a, so XML receives no fresh fork-creation credit. Independent
upstream list readback confirms full has only its earlier LocalAI PR #2; a generic
cleanup flag saying PRs were preserved is not proof an XML PR exists. No PR is
merged or original repository changed. Final claims and actual publication
metadata are archived separately.

Full initially publishes two identical conftest bootstraps and a placeholder
file. A later PR review says approve but includes two real cleanup findings;
the gate correctly blocks nonempty findings. These are supported patch-quality
observations, not detection of the requested functional bug. Initial review had
approved the same source, but publication metadata differs between requests.
The agent comments out remote artifacts through direct Gitea edits, consumes
all four review slots and cannot open its PR. Native full-read/write and deletion
approval guards also affect this trajectory; no production guard is bypassed.

Crucially, its next workspace publication resends stale local copies and
**overwrites the remote cleanup of two files**. Snapshot hashes and actual Git
clones prove the local/remote drift; it is not inferred from an untracked-file
status. The functional correction remains intact. The next critic approves
without flagging restored artifacts. Current review packets compare cumulative
changes with pristine baseline, omitting incremental prior-remote changes and
previous finding state. A future state-preservation check should address that
before publication; this audit does not silently change the frozen experiment.

Control's one block requests missing README coverage. It fixes that coverage,
but no reviewer identifies its wrong failure/no-result distinction. A supported
documentation objection is not functional detection credit.

## Coverage controls and actual cache evidence

Four registered posthoc feature mutations run only after all fresh model calls
and restoration, with no feedback to models and no publication. Forcing the
LocalAI worker to ignore marker-disabled settings survives full-arm project
and original tests (92 plus two), while the independent setting assertion fails.
Original published worker code is correct: this is a coverage gap, not an actual
published defect. Control's worker test catches the same mutation. Both XML
suites catch disabled root validation with genuine assertion failures; control's
already-failing earlier predicate is distinguished from the newly failing target.
All four source/diff/log/receipt payload sets are archived. These controls are
not fresh critic detection scores.

The actual actor prefix also survives self-review: a subsequent 42,310-token
main request reports 41,710 cached tokens after a 92.31-second critic call.
Its 161.22-second backend duration includes 1,240 output tokens; it is not
observed cold prefill. This extends the earlier synthetic 19K cache observation,
not a guarantee for every full-window request. Sanitized numeric metrics for all
103 native calls are included without raw native prompts.

## Preservation, replay and remaining work

Original Hermes and VibeForged 98,304-context runtime are restored. Container
IDs/images/configuration and four profile hashes match, all 29 model inventory
entries and the owner's five pending files/ignored instructions are unchanged.
Hermes-Codex's entire snapshot matches, including its original start time.
124.01 GiB remains free; no model was downloaded or deleted. Exact owned test
containers/supervisor/internal network are removed; unrelated nonempty image
volumes are retained, with no global prune. See [preservation](part3b-preservation.json).

The [archive hash](part3b-evidence.sha256), [artifact validation](part3b-artifact-validation.json),
[summary](part3b-summary.json), [turns](part3b-turns.csv), [reviews](part3b-reviews.csv)
and [replay instructions](part3b-replay.md) provide the evidence. Public receipt
payloads verify source/log consistency; private historical signatures were
checked before export, but keys/MACs are intentionally omitted.

The goal remains active for one registered four-request posthoc context
comparison: minimal packets versus complete changed production modules, using
already-completed LocalAI proposals and fresh genuine paired receipts. It is a
bounded diagnosis of missing context, not a new qualification sample. Wider
P100 plus 8 GiB RAM candidates are recorded separately in MODEL-OPTIONS.md and
have not been loaded under that new budget. Faster reviews, additional RAM and
higher precision do not yet establish a trustworthy correctness gate.
