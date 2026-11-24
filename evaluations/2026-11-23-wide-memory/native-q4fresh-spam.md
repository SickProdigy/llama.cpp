# Adapted 27B Q4_K_M: fresh Spam workflow

Completed November 24, 2026. **All three requested stages pass independent source,
behavior, original-preservation and actual-publication audits in this fresh run.**
This closes the comparison gap left by the earlier [conditional recovery](native-q4-recovery.md).
It is one three-turn lineage, not an unattended-reliability result.

## Setup and actual execution

The [public file](q4fresh-download-verification.json) is pinned to
`netprojects/Qwen3.8-27B-hermes-adapted-GGUF` revision
`10fdf357f14825c61ad7eb42a932e1f1e4390e8f`, file
`Qwen3.8-27B-hermes-Q4_K_M.gguf`, 16,810,714,560 bytes, SHA256
`6512bb1c2595575fc0aed39b7d72a6aaf71084b1164b5d3749f87a6c2a3d3bf3`.
The downloader and supervisor independently checked the complete file hash.
Only the completed, owned GLM study weight was temporarily rotated to admit it;
all 29 original model entries were preserved.

The frozen layout reuses the actual successful Q4 native launch: 98,304 context,
56 GPU layers, q4 K/V cache, one slot, non-mapped loading, 512 MiB host prompt
cache, `--ctx-checkpoints 2`, and a **6656m / 6.5 GiB** backend cap with swap disabled.
The aggregate study guard remains 8 GiB including relevant cache and helpers.
The earlier 7 GiB prose is not the measured native configuration. The checkpoint
comparison and failed default 32 attempt remain preserved separately.

The runtime image is pinned to `b12627`, source
`225a5345bbb0e0c70859af5441ba922beb666fcf`. Native Hermes uses its full normal
policy/profile and scoped Gitea interface, temperature0.8, thinking disabled,
8192 output tokens, 60 iterations and a 10,800-second budget per coding turn.
Main/provider/stale call budgets are 5400 seconds. The future compression-timeout
proposal in MODEL-OPTIONS was not applied to this matched trial.

Before calls, 70 code fingerprints and 1007 profile-file fingerprints were frozen.
The selected upstream and conversation were new; no draft, recovered session,
read-control conversation, grader feedback or corrective reminder was resumed.
All arenas start from the same40-file frozen baseline.

## Coding and independent quality

| Stage | Native time | Project tests | Immutable originals | Source/behavior/publication result |
|---|---:|---:|---:|---|
| Initial enforcement repair | 50.40 min | 86 pass +2 subtests | 83 pass +2 subtests | Correct next-qualifying-message action; issue/fork/commit/PR created |
| README followup | 14.27 min | 86 pass +2 subtests | 83 pass +2 subtests | Only plugin README changes; correct documentation and updated contribution |
| Rule-alert cooldown | 50.93 min | 96 pass +2 subtests | 83 pass +2 subtests | Requested feature, original repair and preservation checks pass; followup published |

Total coding time is **115.60 minutes**. All native exits are0 without external
timeout or repetition termination. At every stage, all 40 actual published source
files match the captured local files. Green model-authored tests are not the
basis for this conclusion: source inspection, frozen behavior checks, immutable
original tests, separate callback controls and independent forge readbacks agree.

The initial repair separates log-only `_triggered` state from `_enforced` action
state. A prior log-only detection therefore cannot suppress the next qualifying
enforcement action. Both states clear on episode expiry, cleanup and reset.
Existing exemptions, window and scope behavior are preserved.

The README followup changes only `autospamignore/README.md`; code and tests are
byte-identical to the initial stage. Independent callbacks verify the rate,
country and phrase transitions, actual local/desktop notice counts, ignored-user
guard and no automatic unignore. Its attribution of non-delivery to Nicotine is
not a live network-delivery proof; source Markdown was inspected without a
browser-rendering test.

The final feature implements `rule_alert_cooldown_seconds`, default 60, clamped
to1–3600. Timestamps are keyed by rule, room and user. A missing timestamp uses
`None`, so the first alert works at monotonic zero; exact expiry is inclusive.
Enforcement bypasses the log-only cooldown. Selected reset preserves other users'
timestamps, global reset clears suppression, and normal cleanup retains a long
unexpired cooldown even after the shorter rate window elapses. Rate-episode
deduplication remains separate, as the task requested only country/phrase cooldowns.

Separate actual callback controls verify first-alert/boundary behavior, the same
user and room under different rules, room/user isolation, original country-before-
phrase priority, reset isolation, enforcement, actual bounded-setting integration
and ordinary cleanup at a high clock. All observed cases pass. These use immutable
original fake peers, not live Soulseek or GUI/network integration.

## Test adequacy and claims

The initial stage adds three tests. Keeping those exact tests while restoring the
original implementation produces 84 passes and2 failures on the actual missing
ignore action. The two failures overlap the toggle scenario; the third case
already passes the old source. Original test ASTs remain unchanged.

The feature adds **10 test methods and one non-test helper**, producing 27 plugin
tests and96 workspace tests. The generic added-functions inventory contains11
callables; that does not contradict the model's test count. Applied to the prior
README-stage implementation, the retained tests produce 92 passes and4 failures:
three missing re-alert behaviors and the new status output. Six cases already
pass prior source. The authored bounds test exercises an existing utility;
independent callback controls additionally verify the actual setting integration.

During development, one newly authored test wrongly expected both country and
phrase processing after the existing country-first early return. The model
corrected its test setup without changing that implementation priority. Its
corrected case varies both user and rule, so the independent control separately
holds user/room fixed while changing the matching rule. An intermediate failed
own-test run is not treated as the final outcome or hidden from the audit.

Final claimed counts, public issue/PR paths, README blob prefix, changed-file
counts and PR diffstat match independent records. The final title/body include
the cooldown followup and current 96-test result. Gitea reports283 additions;
its diff alignment is the reference for that claim, rather than an alternative
Python diff alignment.

## Actual Gitea contribution

Upstream `chatgpt-codex/hermes-wide-q4fresh-20261124`, personal fork
`hermes-agent/hermes-wide-q4fresh-20261124`, fork parent independently verified.

- Issue1 is created in the upstream by `hermes-agent` and **closed after testing**.
- PR2 targets upstream `main` from `wide-spam-q4fresh-enforcement-toggle` in the
  personal fork. It remains open and unmerged for audit.
- Initial commit: `93f8ff8cdc2ffb76a4cd2b8c6af4bf24c50c6fcc`.
- Documentation commit: `6bc37a70bcdd16b05d7eaa9f6d0a3fde23646449`.
- Feature commit: `30a8bdbf4e801f9a6ad62027ec0b3b9d24968464`.
- Upstream and fork `main` remain `4c88d7324eab6bc448d87badacd17a80016e4fa7`.

Connected upstream PR/issue/commit/file/branch reads verify publication. The
connector cannot see the private actor fork directly; scoped actor-authenticated
read-only metadata/branch GETs verify its parent/head. Credentials passed through
stdin only and were never persisted or printed.

## Context, memory and restoration

A separate read-only control takes384.79 seconds and successfully calls Gitea
repository-info. Its detailed plugin summary is not an exhaustive source audit.
Coding starts fresh; its first request reports **zero cached tokens**. Some older
candidates reused a warm first prefix, so native times are not controlled cold-
start comparisons.

Last completed primary requests26/33/54 contain40,777 /50,544 /77,347 prompt
tokens. The final request retains all three full tasks in user messages. No native
compaction occurs in this lineage. Literal retention does not prove attention.
Saved pretty-JSON hashes and original wire-body hashes are separately bound.

| Measurement | Observed value |
|---|---:|
| Aggregate samples / errors / guards | 696 /0 /0 |
| Peak sampled study cgroups, including charged cache/helpers | 7.044 GiB |
| Peak sampled study process PSS | 4.977 GiB |
| Peak GPU device usage | 15,456 MiB |
| Study swap | 0 |
| Global swap-in / swap-out delta | 129,231 /246,516 pages, unattributed |
| Lowest host MemAvailable | 32.50 GiB |
| Complete HTTP captures / all captures | 54 /54 |
| Completed backend HTTP latency min / median / max | 23.43 /80.62 /930.54 seconds |
| Maximum completed prompt | 77,347 tokens |

HTTP timings include prompt processing and response generation, not isolated
decode throughput. Sampling is not continuous whole-host attribution; global
swap activity cannot be assigned to the model. File size or readiness alone is
not used as fit or quality proof.

Independent restoration verifies original service IDs/images/configuration and
running state, original Vibe alias/98k context, four profile hashes, all 29 original
model metadata entries, owner HEAD/pending edits/ignored instructions and unchanged
Hermes-Codex container state/uptime. Owned workload containers/network are absent.
The Q4 file is [retained with the original 29](retained-models.json), with over111 GiB
free and no study-prefixed partial downloads. [All six study issues are closed](test-issue-cleanup.json).

## Reproducible evidence

[Summary](native-q4fresh-spam-summary.json), [archive](native-q4fresh-spam-evidence.tar.gz),
[SHA256](native-q4fresh-spam-evidence.sha256), [validation](native-q4fresh-spam-validation.json),
[verifier controls](native-q4fresh-spam-verifier-controls.json), and
[privacy scan](native-q4fresh-spam-privacy.json).

```sh
python3 verify_q4fresh_native_observed.py q4fresh spam_enforcement
python3 verify_q4fresh_negative_controls.py
```

The positive artifact is accepted. Three coherently rehashed corruptions are
rejected at the intended checks: wrong manual-audit source, wrong authored-test
control source and wrong saved context request. Unchanged legacy Devstral/GLM
observed evidence remains accepted. These are artifact-consistency tests, not
additional model trials or private behavior reexecution.

Full source, raw requests/responses, native databases, profiles, tasks, hidden
checks and receipt keys remain private. The public bundle binds recorded outputs
and hashes; reproducing the whole workflow requires the retained local inputs.
The [final comparison](comparison.md) keeps the earlier conditional recovery and
small-sample limitations explicit.
