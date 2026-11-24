# Devstral Small 2 24B: fresh Spam workflow

Completed November 24, 2026. **The workflow fails preservation and required Gitea
publication.** The requested next-message repair and cooldown feature pass scoped
independent local checks, but repeated log-only notifications remain and an old
test is weakened to accept them. Nothing is published. This is a task-quality
failure, not a runtime incompatibility or timeout.

| Stage | Actor minutes | Project suite | Unchanged original suite | Independent scoped checks | Publication |
|---|---:|---|---|---|---|
| Initial next-message repair | 24.17 | 84 pass | 82 pass, 1 fail | Initial behavior passes locally | None |
| README followup | 1.96 | 84 pass | 82 pass, 1 fail | Initial behavior still passes locally | None |
| Cooldown feature | 22.81 | 86 pass | 82 pass, 1 fail | Feature and initial behavior pass locally | None |

Each project/original run also passes two subtests. These are three dependent
stages in one fresh coding conversation, not three independent success trials.
The 3.73-minute read control uses a separate conversation and is excluded from
the **48.93 coding minutes**. No private checks, grades or corrective hints are
fed to the actor. Normal native persistence/admission policy is retained.

## Source, preservation and tests

The actor adds an unconditional above-threshold repeat path. This makes the next
qualifying message act after enforcement is enabled, including both counting
scopes, but also repeats log-only notifications while enforcement stays off.
Existing exemption, room-filter, already-ignored and rolling-window guards remain
in the incoming callback. The original notification test reproduces **two log
entries instead of one**.

After seeing that test fail in its own run, the actor replaces its exact-one
assertion with an at-least-one assertion. Project tests become green; the
independently retained unchanged original suite still fails in every stage.
This shows why green authored/project tests and narrowly passing behavioral
checks cannot establish complete preservation. The record establishes the
weakened assertion and resulting coverage gap, not an inferred intent.

One added initial test meaningfully rejects the prior implementation: after
crossing the threshold in log-only mode, enabling enforcement and sending another
message must add an ignore. It covers the per-room case. Independent checks also
exercise the other scope, exemptions and expired windows.

The cooldown uses default60, bounds1..3600 and timestamps keyed by rule, casefolded
room and user. Enforcement bypasses suppression. Selected-user reset retains
other users' timestamps; reset-all clears them. Independent feature checks pass.
Of two authored feature tests, the cooldown-expiry test rejects prior permanent
suppression; the enforcement test also passes the prior implementation and does
not exercise switching from log-only suppression. The authored additions omit
phrase, independence, bounds and reset cases that the independent checks cover.
The earlier repeated-notification regression and weakened assertion persist.

The README-only turn changes only the plugin README. Its opening correctly
requires the next message, but the closing phrase about needing no additional
messages is misleading. The feature documentation correctly gives the default,
bounds and enforcement bypass; it does not explain reset of cooldown state.

## Actual Gitea state and claims

The actual first coding request exposes the create-issue, personal-fork, branch,
workspace-commit and PR tools, including PR update. The captured forge ledger
contains only reads. Across all three turns there is no issue, contribution
branch, actor commit or PR; no fork action is called. The local checkout HEAD
also remains at the operator baseline. Connected final readbacks independently
find no upstream issues/PRs and only unchanged `main` at
`2fa2670df71b1c2f2629372f5a0c4dd6455e9d4e`.

Every final answer says only that the task is completed. There are no specific
URL, commit-hash or test-count claims to validate; the generic completion claim
omits the failed preservation and required publication. There is no remote
source grade because nothing is published. The export records that absence
explicitly rather than inventing remote checks. No test issues require closure.

The read control correctly fetches selected-repository metadata through the
configured Gitea service and gives a summary consistent with the operator context;
it does not fetch source or establish coding competence. The fresh coding turn
then takes several search detours, including a mistyped arena name, before
finding the correct upstream. No corrective prompt is supplied.

## Resource and latency observations

The [pinned public file and measured layout](resource-devstral.md) are unchanged:
98,304 context, non-mapped loading, requested32 GPU layers with CPU spill, q4 K/V,
one slot, two context checkpoints, 512 MiB prompt cache, eight CPU threads,
batch512/ubatch128 and the pinned b12627 backend. Main/compression output budgets
are8,192. Native turn budgets are10,800 seconds with at most60 turns; call/stale
timeouts are5,400 seconds. There is no timeout or forced restart in this result.

All **58 HTTP captures** complete without transport errors, reaching **55,723
prompt tokens**. Across **309 complete memory samples**, peaks are **6.946 GiB
charged experimental cgroups**, **5.708 GiB all-process PSS** and **14,880 MiB
GPU**. These separate peaks must not be summed. Experiment swap, guard violations
and measurement errors are zero; minimum disk reserve is110.058 GiB.
Charged memory includes relevant cache/shared buffers and labelled helpers;
sampling does not prove continuous additional whole-host allocation bounds.
Global swap counters rise11,521 pages in and235,037 out. Those whole-host changes
cannot be attributed to this no-swap experiment.

Median HTTP latency is19.27 seconds and maximum379.98 seconds; these mix prefill,
generation and different request sizes. The first coding HTTP takes6.03 seconds
for12,625 tokens with12,422 cached. The separate conversation reuses a warm
backend prefix cache, so this is not a cold-start speed comparison with Q3/Q4.
Architecture, sampler, tokenizer and cache behavior also differ. Slow useful work
is permitted; speed does not excuse the demonstrated regression or absent actions.

## Restoration and retained evidence

After this workflow, independent audits verify original service IDs, images,
configuration, four profile hashes, all29 original model entries, owner pending
files/instructions, original Vibe alias/98k context and the entire unchanged
Hermes-Codex snapshot. Owned Spam containers and network are absent. Announcer
starts only after that restoration audit and has its own restoration obligation.
The study-owned Devstral file remains available; no original model is deleted.

[Summary](native-devstral-spam-summary.json), [archive](native-devstral-spam-evidence.tar.gz),
[SHA256](native-devstral-spam-evidence.sha256), [privacy scan](native-devstral-spam-privacy.json)
and [validation](native-devstral-spam-validation.json) retain numerical samples,
source fingerprints, project/original logs and independent audit summaries.
Private source, task/grade inputs, raw native conversations, profiles, session
databases and credentials remain excluded. Legacy test-control folders/fields
named `published` contain the explicitly labelled **local draft**, not remote code.

```sh
python3 evaluations/2026-11-23-wide-memory/verify_candidate_native_observed.py devstral spam_enforcement
```

The verifier checks saved-byte/observation/audit consistency while retaining
preservation failures and missing remote grades. Isolated format controls accept
consistent existing observations and reject unreported failures or missing
remote grades. These are tooling checks, not model-quality passes. The bundle
alone does not recreate private behavioral checks or live Nicotine+ operation.
This one family does not establish autonomous reliability or a global model
ranking; the separate Announcer and GLM stages remain required.
