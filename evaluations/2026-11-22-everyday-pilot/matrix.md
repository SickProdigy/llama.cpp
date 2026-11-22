# Everyday Hermes pilot — final matrix

Candidate: public Qwen3.8-27B-hermes IQ3_XXS, 98,304 context on P100 16 GiB.
Three bug families × two arms × three dependent turns = 18 captured turns.
**No full workflow passed.** These six trials are not a reliability estimate.

| Family | Arm | Final local frozen checks | Actual personal-fork delivery | Why the full workflow fails |
|---|---|---:|---|---|
| Beets queued import | Unassisted | 4/5 | Initial fix + README, upstream issue 1 and PR 2; final feature unpublished | Old waiting worker can run after disable/reload; README overstates lifecycle guarantee; feature deadline |
| Beets queued import | Automatic review | 4/5 | No code commit, issue or PR | Same reload gap; local cancellation improvement remains unpublished; all three turns reach guard |
| Announcer comma room | Unassisted | 6/6 | Three commits, upstream issue 3 and PR 4 | Collapses internal spaces in valid literal room names, changes empty-default status, breaks default root pytest collection |
| Announcer comma room | Automatic review | 6/6 | Local commits only; no remote code, issue or PR | Actual contribution never reaches Gitea; local primary success does not establish publication |
| Arr credential redirects | Unassisted | 3/5 | Initial fix + README, upstream issue 5 and PR 6; final feature unpublished | Rejects valid relative same-origin redirects/chains; README falsely gives50-hop default; feature deadline |
| Arr credential redirects | Automatic review | 5/5 | No code commit, issue or PR | HTTPS redirects raise uncaught AttributeError; final root suite still has one mock-signature failure; no publication |

Issue/PR numbers refer to separate disposable `hermes-pilot-plain-20261122`
and `hermes-pilot-review-20261122` arenas, not the owner's working repository.
The three created issues are closed; PRs remain open and unmerged as evidence.
The actual published Arr branch passes2/5 final checks because its feature was
never published. The unassisted Announcer passes its new nested tests separately,
but that is not a passing combined repository-root test run.

The review arm has15 real review calls, all exceeding the 240-second caller
limit. No semantic decision reaches the actor. Late outputs include one grounded
packaging concern, soft suggestions, false findings, malformed JSON and missing
capture. See [finding audit](review-findings.md). Blocking on timeout is not a
successful defect detection or demonstrated review benefit.

[Full interpretation](investigation.md), [18-turn measurements](measurements.md),
[CSV](measurements.csv), [protocol](protocol.md), and [replay](REPLAY.md).

## Initial request latency

| Workflow | First recorded native model request s | First persisted native tool receipt from turn start s |
|---|---:|---:|
| plain-announcer | 121.518 | 144.140 |
| plain-arrrequests | 117.079 | 140.525 |
| plain-beetsbridge | 116.226 | 136.744 |
| review-announcer | 139.351 | 173.973 |
| review-arrrequests | 128.933 | 152.715 |
| review-beetsbridge | 111.025 | 137.375 |

These are request/receipt timings, not first correct Gitea write or completed repair.
See [provenance](first-call-measurements.json); startup and adopted-turn coverage
limitations still apply.

## Actual published heads

| Workflow | Upstream PR | Personal-fork final commit | Commits | Closed issue |
|---|---|---|---:|---:|
| plain-announcer | [PR #4](http://gitea:3000/chatgpt-codex/hermes-pilot-plain-20261122/pulls/4) | `030711d3f3f0e35021c525cd86183d0b60bd4fdb` | 3 | 3 |
| plain-arrrequests | [PR #6](http://gitea:3000/chatgpt-codex/hermes-pilot-plain-20261122/pulls/6) | `b3edc939e47f1b0ee4c12e4b5d7da804eeb3b724` | 2 | 5 |
| plain-beetsbridge | [PR #2](http://gitea:3000/chatgpt-codex/hermes-pilot-plain-20261122/pulls/2) | `09f2d2df087e63b962c6e5e8f17ddec59687ef72` | 2 | 1 |

The review branches were independently cloned at their unchanged initial base;
zero successful model commits is confirmed by remote Git trees, not inferred
solely from missing tool receipts.
