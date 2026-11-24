# Devstral Small 2 24B: fresh Announcer workflow

Completed November 24, 2026. **The initial fix passes locally; the complete
workflow does not.** The new room-cancellation feature leaves stale reply state
when it empties a job, the README needs a qualification, and no contribution is
published. Original behavior is preserved in the unchanged test suite.

| Stage | Actor minutes | Project suite | Unchanged original suite | Independent outcome | Publication |
|---|---:|---|---|---|---|
| Initial send-time fix | 65.31 | 85 pass | 83 pass | Initial callback/completion checks pass locally | None |
| README followup | 3.23 | 85 pass | 83 pass | Source unchanged; re-enable wording qualification | None |
| Room cancellation | 36.11 | 88 pass | 83 pass | Raw metadata assertion fails; separate dispatch control finds cleanup defect | None |

Each suite also passes two subtests. Total coding time is **104.65 minutes**,
excluding the separate 3.73-minute read control. These are dependent turns in
one fresh native conversation, not independent reliability trials. No private
grades, corrected code or corrective prompts are supplied to the actor.

## Initial repair and authored-test adequacy

The callback gains a send-time disabled branch and makes the joined-room check
an `elif`. Pending-entry removal and end-of-job cleanup still execute after a
skipped send. Independent checks verify switching off before all callbacks and
between callbacks, keeping already-sent messages and completing the queue.
Preview, cooldown, scheduling and other original behavior remain unchanged.

Both added tests reject the baseline queued-send bug. However, both switch off
before **any** scheduled callback runs. The test named and described as testing
mid-flight switching does not exercise that case. Independent checks cover it;
the model's authored-coverage claim is inaccurate. Existing tests are preserved.

The README-only turn changes only `announcer/README.md`. Its claim that switching
off cancels pending sends needs a qualification: each callback checks the current
setting. An identical immutable-fixture control used on Q3/Q4 skips Linux while
off, then permits still-pending Books after re-enabling. This is not permanent
cancellation of every remaining target.

## Feature behavior and a grader qualification

The final code stores timer/room pairs, matches room names with `casefold`,
cancels matching pending timers and leaves other targets scheduled. Global
cancellation unpacks timer IDs correctly and clears all job reply state.
Already-fired entries are absent from the pending map. The original suite passes.

**The frozen feature checker exits1 at missing command-parameter metadata. That
assertion does not prove that the room argument is rejected.** The plugin declares
support for Nicotine+3.3.11+. Pinned [3.3.11 dispatcher source](https://raw.githubusercontent.com/nicotine-plus/nicotine-plus/f6897dc860769203923a6943e8e9b5d0fae6ee7d/pynicotine/pluginsystem.py)
and [current dispatcher source](https://raw.githubusercontent.com/nicotine-plus/nicotine-plus/2a1eb32037a52718bf1ebd72c64092307ffcc960/pynicotine/pluginsystem.py)
pass arguments to the callback without requiring that optional metadata. Missing
metadata and the unchanged cancel-all help description are discoverability gaps.
The original grader and its recorded failure remain unchanged.

A separate posthoc control executes those exact dispatcher methods with immutable
fake peers and the captured candidate source. For all three compared candidates,
the room argument is accepted and a surviving Linux target runs after canceling
Books. **Devstral retains one `_job_replies` entry when canceling the job's only
pending target.** No future callback remains to clear that entry. This establishes
a separate lifecycle defect, rather than deriving task failure from the metadata
assertion. This control is not full GUI/network integration.

| Final source | Room argument accepted | Reply entries after canceling last target |
|---|---|---:|
| Adapted Q3 | Yes | 0 |
| Adapted Q4 | Yes | 0 |
| Devstral | Yes | 1 |

The [matched posthoc comparison](announcer-dispatch-cleanup-comparison.json)
uses the same control and pinned dispatchers on retained final snapshots, with
source fingerprints checked against their existing evidence archives. A particular
completion-message string is observed but is not the cleanup criterion. No actor
sees these findings. Two initial posthoc helper-adapter errors were corrected
(echo tuple shape and dispatcher registry naming); failed attempts and source
versions remain local and are not counted as model failures.

The three new feature tests preserve existing test AST. Two reject prior cancel-all
behavior; the no-argument test also passes the prior implementation. They do not
run surviving callbacks or check reply cleanup when a job becomes empty. The
model correctly reports88 project tests but claims11 Announcer tests; the actual
Announcer file has13 after both initial and feature additions. The scheduled-values
type annotation also still describes integers instead of the new pairs.

## Actual forge actions and claims

The task explicitly requests a selected-upstream issue, personal fork and upstream
PR; actual Git facts include the correct Gitea remote. The actor attempts to fork
the original `SickProdigy/nicotineplus-plugins` instead. The local tool allowlist
rejects that target **before forwarding a forge mutation**. Both profile allowlist
entries and the scoped proxy correctly name the selected evaluation upstream.
This rejection is a configured safety boundary, not a Gitea service outage or
hardware incompatibility. No allowlist or task is changed to rescue the attempt.

The initial answer says the upstream is inaccessible and hands draft issue/PR
text to the user. Connected readbacks show the selected upstream exists, with no
issues/PRs and only unchanged `main` at
`2fa2670df71b1c2f2629372f5a0c4dd6455e9d4e`. The local checkout HEAD also stays at
that baseline. The captured forwarded ledger contains only reads. Across all
three turns there is no actual issue, contribution branch, commit or PR; no remote
source grade exists. No test issues require closure. No successful publication
URL or commit is claimed; required publication remains incomplete.

## Resource observations and restoration

The [public pin and measured layout](resource-devstral.md) are unchanged: pinned
b12627 backend, 98,304 context, non-mapped loading, requested32 GPU layers with
CPU spill, q4 K/V, one slot, 512 MiB prompt cache, two context checkpoints, eight
CPU threads, batch512/ubatch128 and temperature0.15. Output budgets are8,192;
native turns allow10,800 seconds and60 turns, with5,400-second call/stale budgets.
No timeout, forced restart, OOM or resource guard ends this workflow.

All **68 HTTP captures** complete without transport errors, reaching **73,156
prompt tokens**. Across **619 complete samples**, peak charged cgroups are
**6.974 GiB**, all-process PSS **5.725 GiB**, and GPU **14,880 MiB**. Separate peaks
must not be summed. Experiment swap, guard violations and measurement errors
are zero. Global swap counters rise203,515 pages in and655,871 out; those
whole-host changes cannot be attributed to this no-swap experiment. Charged
memory includes relevant cache/shared buffers and labelled helpers, but samples
do not prove continuous additional whole-host allocation bounds.

Median HTTP latency is37.25 seconds, maximum466.39 seconds. Requests mix prefill,
generation and different sizes. The first coding HTTP takes5.87 seconds for12,624
tokens with12,422 cached. Its fresh conversation reuses a warm backend prefix;
this is not a cold-start speed comparison. Repeated debugging calls are retained
in the record. Slow useful work is allowed; elapsed time alone is not failure.

Afterward, independent audits verify original service IDs/images/configuration,
four profile hashes, all29 original model entries, owner pending files/instructions,
original Vibe alias/98k context and the entire unchanged Hermes-Codex snapshot.
Owned Announcer containers and network are absent;115.44 GiB is free at the
restoration audit. No original model is deleted. Later study-weight rotation and
GLM inference have separate admission and restoration obligations.

## Evidence

[Summary](native-devstral-queue-summary.json), [archive](native-devstral-queue-evidence.tar.gz),
[SHA256](native-devstral-queue-evidence.sha256), [privacy scan](native-devstral-queue-privacy.json)
and [validation](native-devstral-queue-validation.json) retain numerical samples,
source fingerprints, project/original logs, posthoc source pins/controls and
independent audit summaries. Private source, raw native conversations, profiles,
session databases, task/primary-grade inputs and credentials remain excluded.
Legacy control fields named `published` contain the explicitly labelled local
draft, not a published contribution.

```sh
python3 evaluations/2026-11-23-wide-memory/verify_candidate_native_observed.py devstral queued_announcements
python3 evaluations/2026-11-23-wide-memory/verify_announcer_dispatch_cleanup.py
```

These verify saved observations and fingerprints, not private behavior or inference.
A negative tooling control recomputes valid archive/manifest hashes after changing
the posthoc source fingerprint and confirms rejection. The full private workflow
cannot be recreated from this bundle alone. Neither this family nor green tests
establish autonomous reliability; GLM and the final comparison remain required.
