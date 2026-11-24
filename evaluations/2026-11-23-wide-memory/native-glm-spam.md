# GLM-4.7-Flash Q4_K: fresh Spam workflow

Completed and independently audited November 24, 2026. The requested initial
next-message repair works locally, but notification preservation and the new
cooldown feature fail. The actor creates the correct upstream issue and personal
fork, then leaves push/PR work to the user. No code is published. This is a
task-quality failure, not a loading failure or speed rejection.

| Turn | Actor seconds | Project / unchanged original suite | Independent outcome | Publication |
|---|---:|---|---|---|
| Initial repair | 1,398.27 | Both 82 pass / 1 fail, plus 2 subtests | Next-message checks pass; repeated rate notices and extra cleanup regression | Real issue 1/fork 34331; no branch, commit or PR |
| README followup | 305.64 | Both 82 pass / 1 fail, plus 2 subtests | Source/tests unchanged; README correctly says next qualifying message | No contribution update |
| Cooldown feature | 3,396.26 | Both 81 pass / 2 fail, plus 2 subtests | Feature exit1: four failure records across five methods/subtests; original next-message checks still pass | No branch, commit or PR |

The three coding turns share one fresh native lineage, separate from the
read-only control. No private grades or corrective hints are given to the actor.
The actor stops normally in every turn, without an external timeout.

## Source, tests and claims

Removing the old rate-trigger set makes the next qualifying message enforce in
both scopes. It also repeats log-only rate notifications; the unchanged original
test observes two notices instead of one. Existing tests are not weakened.
The initial cleanup additionally clears rule suppression when an ordinary rate
counter expires. A separate chat-event control reproduces a repeated phrase
notice against the original fixture; the baseline retains suppression.

The feature adds the default 60 setting with correct 1..3600 bounds and per-rule,
room and user keys, but leaves the old permanent rule-suppression check in place.
A first alert at clock 10000 logs; another at 10061 still does not, despite the
elapsed default cooldown. A missing timestamp defaults to 0, which also suppresses
a first alert at low clock values. The high-clock control shows that the feature
failure is not solely an artifact of synthetic startup timing.

Selected-user reset and ordinary expired-counter cleanup assign a set to the
timestamp dictionary. Subsequent log-only handling raises AttributeError when
it calls the dictionary lookup. The cleanup control uses a 3600-second cooldown
with only 120 seconds elapsed, so it does not mistake legitimate cooldown expiry
for a regression. Enforcement bypass works in the independent control. Global
reset from an intact dictionary clears it; the demonstrated type defects are
selected reset and counter cleanup.

Eight initial and eleven feature test methods are written to
autospamignore/tests.py, outside normal project-suite discovery. Explicit
collection in the prepared image fails to import pynicotine. Thus no working
new regression coverage is demonstrated. The original test fixture remains
unchanged. The final claim of 18 new/26 total comprehensive tests is wrong:
the file contains 11 new/19 total methods. The README's expiring cooldown and
safe-reset claims contradict actual behavior. Its next-qualifying-message
explanation is accurate, while some final answers omit that qualification.

## Actual configured Gitea

Independent reads confirm issue 1 belongs to the selected disposable upstream,
and fork 34331 is hermes-agent/hermes-wide-glm-20261123 with the correct parent.
Both attempted feature-branch creations are rejected locally for omitting the
experiment's required prefix. That prefix was already present in the original
and later request context. These are scope-guard rejections, not Gitea server
outages. The scoped wrappers and branch lease are limitations of this setup;
the independent code failures do not depend on the branch rule.

At completion both upstream and fork have only unchanged main at
e703b9e32748cbd930c47b523fa4225dbf70691b. There is no published commit, remote
code grade or PR. The final answer again delegates pushing and opening the PR
to the user, with extra local summary documents. Issue 1 is independently
verified closed; no unrelated issues are changed.

The separate read control takes 234.15 seconds and claims verification through Gitea after
only listing local files and reading the README. That claim is unsupported.
Actual coding later uses Gitea correctly for discovery, issue and fork.
The first coding request contains only system plus fresh task, with 18 focused
Gitea tools available. Its first response takes 14.47 seconds and uses 13,234 cached tokens of 13,419:
separate conversations do not imply a cold backend.

Final requests retain the original issue/fork/PR instruction and expected
dependent task texts at 37,173 / 40,784 / 72,426 prompt tokens. Text presence does
not prove attention, but dropped task text does not explain this observed handoff.

## Capacity, latency and preservation

The pinned [public file and runtime](resource-glm.md) use the measured 98,304
context, requested 99 GPU layers / 12 CPU expert layers, matching q4_0 caches,
non-mapped loading, one slot, 512 MiB prompt cache and two checkpoints.
Temperature 0.7, thinking enabled, clear_thinking false, main/compression
output cap 16,384, per-turn 10,800-second budget and 60 turns remain fixed.

Coding takes 85.00 minutes, excluding the read control. All 58 HTTP captures
complete without transport errors. HTTP latency median 49.73 seconds and
maximum 577.60 seconds include prompt processing and output, not isolated decode.

Across 514 complete samples: GPU peak 15,336 MiB, charged host peak 6.556 GiB,
all-process PSS peak 5.389 GiB, experiment swap 0, guard/error samples 0.
Independent peaks must not be summed. Backend cap is 6.5 GiB and aggregate guard
8 GiB, including charged cache and sampled helpers. Minimum sampled host
available memory is 35.61 GiB and disk free 111.63 GiB. Whole-host swap counters
rise 1,305,985 pages in / 1,369,390 out; these are not attributed to the model.
Sampling does not prove continuous entire-host allocation bounds.

Original runtime IDs/images/configuration, four profile hashes, owner pending
files, all 29 original model entries, original Vibe 98k alias and unchanged
Hermes-Codex are independently verified after this GPU stage. Five owned
containers and the owned network are absent. The subsequent fresh Announcer
stage has separate restoration obligations and remains under evaluation.

## Evidence and limits

[Summary](native-glm-spam-summary.json), [archive](native-glm-spam-evidence.tar.gz),
[hash](native-glm-spam-evidence.sha256), [validation](native-glm-spam-validation.json)
and [privacy scan](native-glm-spam-privacy.json) retain observed outcomes,
source/log fingerprints, controls and restoration/publication audits. Full private
source, prompts, graders, sessions and credentials are excluded.

The [format controls](native-glm-spam-verifier-controls.json) reject altered
feature-source and context-request fingerprints even after coherent audit,
manifest and archive hashes are recomputed. Legacy Devstral evidence remains
accepted. These checks verify evidence consistency, not model correctness.

```sh
python3 evaluations/2026-11-23-wide-memory/verify_candidate_native_observed.py glm spam_enforcement
python3 evaluations/2026-11-23-wide-memory/verify_glm_native_negative_controls.py
```

One fresh family with dependent turns is not an autonomous-reliability sample.
Fake-peer/source/unit checks do not replace live Nicotine+ GUI/network testing.
GLM Announcer remains required. A fresh matched Q4 Spam trial is registered
after both GLM families finish: its earlier Spam result was conditional recovery,
and will not be ranked as an equivalent fresh primary.

