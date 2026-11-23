# Adapted 27B Q4: completed conditional recovery

November 23, 2026. The recovered native Hermes session completed the initial
enforcement fix, README followup and cooldown feature, publishing three commits
through configured Gitea to a personal fork and an upstream PR. Independently
cloned published files match the local drafts and pass the original suite and
separate public-callback behavior checks. No hidden grading feedback was sent.

This is a **conditional recovery**, not a fresh primary trial. The first coding
attempt was interrupted by the backend cgroup OOM described in the
[checkpoint comparison](checkpoint-comparison.md). Recovery resumed that same
partially edited checkout and history with a neutral continuation. It used two
context checkpoints, without task-specific corrective instructions.

| Coding stage | Actor minutes in recovery | Project tests | Original suite | Independent behavior/source/docs |
|---|---:|---:|---:|---|
| Enforcement fix | 50.05 | 86 passed | 83 passed | Pass within audited scope |
| README followup | 17.06 | 86 passed | 83 passed | Pass; only README changed incrementally |
| Cooldown feature | 42.91 | 92 passed | 83 passed | Pass within audited scope |

Project/original runs also report two subtests. The earlier interrupted coding
segment adds 10.59 minutes: approximately 120.60 active coding minutes across
the interrupted segment and three recovery turns. This excludes the separate
read control, checkpoint experiments and restoration gaps. HTTP latency across
64 complete captures has median 71.50 seconds and maximum 402.24 seconds;
these include prefill and generation, not isolated decode throughput.

The initial regression rejects the original bug. Three of six new feature tests
reject the pre-feature implementation, including real cooldown assertions.
Existing tests are preserved except a compatible message-text fixture extension.
Test coverage still has gaps: the new independence test varies several factors
together, and authored tests omit some phrase/boundary/all-user-reset cases.
Independent behavior and source audits address the relevant requirements; green
authored tests alone are insufficient. Tests use fake peers, not a live
Nicotine+ GUI/network session.

Reporting is **not a clean pass**. All three final answers link to
`gitea.rcs.top` rather than configured `gitea.rcs1.top`; the former did not
resolve when checked. The actual issue, fork, branch, three commits and PR
exist at the configured instance. The PR description remains on the initial
fix and earlier 17/86 test counts after the cooldown feature was published.
These errors remain part of the result; the evaluator did not correct them.

## Resource observations and cleanup

The SHA-pinned public Q4 file uses runtime image
`sha256:7561b4761f849925a728c5ac2bd1f4a649b6a76f24544e7f992b047ad016cec3`,
56 GPU layers, 98,304 context, non-mapped loading, q4 K/V, 512 MiB prompt cache
and `--ctx-checkpoints 2`. Main/compression output caps are 8,192 tokens.
Each coding turn has a 10,800-second budget and 60 iterations; request/stale
timeouts are 5,400 seconds. Native sampling is not seed-pinned.

632 complete aggregate samples record peak charged cgroup memory 7.09 GiB,
peak process PSS 5.37 GiB, zero observed experiment cgroup swap and no resource
guard. A completed real native request reaches 77,968 prompt tokens. All 632 GPU observations show a peak of 15,456 MiB used and a minimum of
819 MiB free. The minimum sampled model-disk reserve is 103.27 GiB. Individual backend/supervisor/actor/proxy
limits and sampled aggregate guards do not prove a continuous whole-host peak;
short audit containers and driver allocations retain accounting limitations.
Whole-host swap counters increased independently, so this is not a swap-free
whole-machine claim. Disk reserve stayed above 100 GiB.

The test issue was independently verified closed and the PR remains open and
unmerged. Original service identities/images/configuration, four settings-file
hashes, all 30 model metadata entries, owner pending files/ignored instructions
and unchanged Hermes-Codex were audited after restoration. Exact experiment
containers and network were removed. A subsequent fresh Announcer stage may
stop the original services again under its separate restoration protocol.

## Evidence and limits

[Summary](native-q4-recovery-summary.json),
[bundle](native-q4-recovery-evidence.tar.gz),
[SHA256](native-q4-recovery-evidence.sha256), and
[verification result](native-q4-recovery-validation.json).
Run `python3 verify_native_q4_recovery.py` to check archive hashes, observations,
per-phase source consistency, test logs, publication records and audit flags.
That verifies saved evidence consistency, not the private behavioral tests.

Raw prompts/responses, consoles, profiles/databases, ignored owner instructions,
private graders/reference fixes, selected private-project source snapshots and
credentials/signing keys remain local. Full private-workflow reproduction needs
those retained inputs. The bundle contains sanitized numeric observations,
fingerprints, project/original test logs, operator controls and audit summaries.

This is one family with dependent followups, using focused scoped forge tools
and a publication execution gate. It establishes useful conditional coding and
Gitea capability, with reporting errors. It does not establish autonomous
reliability, a model winner, a precision-only effect or a reason to buy hardware.
