# GLM-4.7-Flash Q4_K: fresh Announcer workflow

Completed November 24, 2026. **Partial repair, failed complete workflow.**
All three coding turns ended at Hermes's repetition detector with an incomplete-turn
notice and discarded partial response. No issue, code branch, commit or PR was
published for this family. This is a task-quality failure with a separately
identified compression-timeout confound, not a loading or CUDA compatibility failure.

## Protocol and quality

The same pinned public model, runtime, 98,304 context, CPU expert spill and q4 KV
layout described in [resource evidence](resource-glm.md) were used. One fresh native
coding lineage received the frozen natural initial task and two dependent followups.
A separate read-only conversation is not a coding result. Actors received no grader
feedback, corrective hints or additional continuation prompts.

| Stage | Actual coding time | Original suite | Project suite | Independent observations |
|---|---:|---:|---:|---|
| Initial repair | 54.07 min | 83 pass | 85 pass, 1 fail | Disabled callbacks do not send, but removing the whole job reply loses the completion notification when another callback survives |
| README followup | 14.15 min | 83 pass | 85 pass, 1 fail | Claims disabling immediately cancels all queued jobs; a later callback can send after re-enabling. Leaves a DEBUG print |
| Room cancellation | 147.08 min | 83 pass | 91 pass, 1 fail | Case-insensitive pending-room cancellation works, but loses surviving-job completion replies and retains completed/cancelled room bookkeeping |

Total coding time was **215.29 minutes**. Each native exit was 1 without external
timeout; none exhausted the registered 180-minute turn budget. Green original tests
do not cover the independently established new defects. The initial scoped checker
passes; the frozen feature checker fails first at command `parameters` metadata.
The actual pinned Nicotine+ 3.3.11 and current dispatcher methods accept the room
argument without that metadata. That assertion is retained but is not evidence of
argument rejection. Separate actual controls establish the behavioral failures.

The feature pops `_job_replies` for the whole job while another room remains pending.
The surviving callback posts but cannot report completion. Its new `_scheduled_rooms`
map is not cleared by normal completion, cancel-all or shutdown: four completed
two-room jobs leave eight entries while pending and reply maps are empty. Cancelling
the final remaining target specifically does clear its target and reply; this is
different from Devstral's orphaned last-target reply defect.

Three initial and six additional feature tests were authored; original test ASTs
were preserved. The inherited re-enable test invokes the immutable fake scheduler's
retained callbacks twice and fails on that replay; this does not prove the real
scheduler duplicates callbacks. A new feature test explicitly expects the reply map
to be empty while a room remains pending, codifying the lost-completion defect.
The new tests never execute those surviving callbacks or check room-map cleanup.
README remains unchanged in the feature turn, so the new room argument is undocumented
and the earlier immediate-cancel claim remains wrong.

The same initial off/reenable callback control was actually run on saved Q3, Q4,
Devstral and GLM initial sources. All skip the disabled first callback, send only
Books after re-enabling and clear pending/reply state. Q3/Q4/Devstral retain one
finished notification; GLM retains zero. The bundle binds each source/result to
prior unchanged public archives. This compares one interleaving, not reliability.

## Forge and claim audit

Native session records show two wrong-target write attempts: issue creation and
fork creation against `hermes-agent/wide-glm-20261123`, rather than configured
`chatgpt-codex/hermes-wide-glm-20261123`. The focused plugin rejected both before
proxy transport. Proxy-only ledgers therefore undercount attempts. No new forge
write attempts occur in later turns. Registered profile/proxy routing remained
correct; this is not evidence of a Gitea outage.

Independent connected upstream and scoped read-only actor-authenticated fork
readbacks show only the pre-existing Spam fork/main and closed Spam issue 1.
Upstream and fork main remain `e703b9e32748cbd930c47b523fa4225dbf70691b`;
there is no Announcer issue, branch, commit or PR. Final actor messages explicitly
say the turns did not complete; no successful PR/commit/test-count final claim is
inferred from unfinished console activity.

## Large context, latency and compression limitation

Last fully completed primary requests per coding phase are 51, 62 and 120:
49,041 / 55,681 / 49,330 prompt tokens. The subsequent primary requests 52, 63
and 121 have incomplete response captures after repetition interruption. Separately,
primary 95 actually completes at **84,237 prompt / 603 completion tokens**.
The final context audit binds both saved JSON and wire-body hashes to exported
metrics; it does not mistake the two distinct hashes for each other.

Auxiliary compression requests 94 and 96 return no complete usage or finish reason.
Hermes's separate 300-second no-output guard interrupts them while P100 prefill
progresses. The operator extended main/provider timeouts but missed these separate
compression settings. Hermes then commits a deterministic fallback checkpoint;
this is **not successful model-generated summarization**. All three literal tasks
remain in subsequent primary requests, but the README task is in an assistant
checkpoint, while original/current tasks retain user roles. Presence does not prove
attention. Earlier initial/README defects and repetition preceded compression;
the guard limitation cannot explain every quality failure.

A source-verified future timeout proposal is recorded in [MODEL-OPTIONS.md](../../MODEL-OPTIONS.md),
explicitly untested and unapplied. It does not retroactively change this trial.

| Measurement | Observed value |
|---|---:|
| Aggregate memory samples / errors / guards | 1,267 / 0 / 0 |
| Peak study cgroups, including charged cache/helpers | 6.833 GiB |
| Peak study process PSS | 5.909 GiB |
| Peak GPU | 15,336 MiB |
| Peak study swap | 0 |
| Global swap-in / swap-out delta | 438,426 / 23,372 pages, unattributed |
| Complete HTTP captures / all captures | 116 / 121 |
| Completed backend HTTP latency min / median / max | 4.87 / 37.66 / 3,011.64 seconds |

Backend-start latency excludes prior proxy waiting; primary95 end-to-end HTTP time
was 3,446.83 seconds. Neither measure is isolated decoding speed. Sampling does not
prove continuous peaks or attribute all whole-host activity to the model.

Original service IDs/images/configuration, four profiles, all29 original model
metadata entries, owner HEAD/pending edits/ignored instructions and the entire
Hermes-Codex snapshot were independently preserved. Original Vibe 98k runtime is
ready; owned stage containers/network are absent. Restoration free disk was
111.52 GiB. No Announcer issue needed closing; the prior Spam issue remains closed.

## Evidence and limits

[Summary](native-glm-queue-summary.json), [archive](native-glm-queue-evidence.tar.gz),
[hash](native-glm-queue-evidence.sha256), [validation](native-glm-queue-validation.json),
[privacy scan](native-glm-queue-privacy.json), and
[verifier controls](native-glm-queue-verifier-controls.json) preserve failed grades
and absent remote publication. Verification checks recorded consistency, not private
behavior reexecution or autonomous reliability. Prior public archives are unchanged.

```sh
python3 verify_candidate_native_observed.py glm queued_announcements
python3 verify_glm_queue_negative_controls.py
```

Two coherent corruptions with recomputed outer hashes are rejected: a control
bound to the wrong source and a context audit bound to the wrong request. Existing
Devstral observed evidence remains accepted. Full raw requests, credentials,
profiles, private source, future tasks and graders remain private. A fresh Q4 Spam
comparison is still required; its prior recovered Spam result is conditional.
