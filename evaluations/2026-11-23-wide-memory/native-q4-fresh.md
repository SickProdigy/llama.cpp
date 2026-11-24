# Fresh adapted27B Q4 native Hermes workflow

Completed and restored November 23, 2026. This fresh Announcer workflow completes
its initial fix and two dependent followups with independently checked source,
behavior preservation and actual Gitea publication. Documentation and final-answer
accuracy have qualifications, so this is not an unqualified workflow pass.

The pinned model/runtime/layout are the same as the [Q4 resource pilot](resource-q4.md),
with `--ctx-checkpoints 2`, non-mapped loading, 56 GPU layers, 98,304 context,
512 MiB prompt cache and one slot. The normal-policy native CLI profile uses
focused Gitea tools and a visible project-test publication gate. No private
behavioral grader or corrective audit finding was sent to the actor. A separate
read-only control precedes an independent fresh coding conversation; all coding
followups resume that coding conversation.

| Stage | Actor time | Project tests | Independent source/behavior and remote audit |
|---|---:|---:|---|
| Send-time disabled check | 32.93 min | 86 | Pass; all three new tests reject original bug |
| README followup | 7.41 min | 86 | Only README changes; wording qualification below |
| Room cancellation followup | 76.19 min | 91 | Pass; four of five new tests reject pre-feature code |

The immutable original 83 tests plus two subtests pass at every stage. Existing
test AST is unchanged. Independent checks cover selective/case-insensitive
cancellation, multiple pending jobs, no-argument cancellation, already-sent rooms,
bookkeeping and preserved disabled-send behavior. These unit/fake-peer checks and
source inspection do not replace live Nicotine+ GUI/network testing.

The actor opens upstream issue 3, uses its personal fork and branch
`wide-queue-q4-announcer-disable-gate`, and publishes upstream PR 4 with nine
commits. Final head is `ec238323fed7acee5ad356007483473f1a34a858`;
local and independently fetched remote source digests match at every stage.
The PR title/body are updated for the feature. The issue is independently verified
closed afterward; the PR remains open and unmerged. Upstream main is unchanged.

The remaining qualifications are substantive:

- The README describes switching sending off as stopping the remaining queue.
  Actual behavior checks the setting at each callback: re-enabling before a
  pending callback allows that room to send. An independent control demonstrates
  this; skipped callbacks are not retried. This wording persists in the final PR.
- Final answers describe 11/16 plugin-file tests as the full suite; actual project
  totals are 86/91. The final PR body correctly scopes 16 to the plugin test file.
- Fully-cancelled single-room bookkeeping passes even before the new feature.
  The other four new feature tests reject pre-feature code; green tests alone
  are not the correctness verdict.

The visible publication gate rejects incompatible tuple/int cancellation edits
before the actor combines the dependent changes. This is original-suite feedback,
not private-grader intervention. The final combined implementation passes the
independent checks, but the gate is part of the tested setup.

Measured over 703 aggregate samples: peak charged experiment cgroups **6.934 GiB**,
all-process PSS **5.034 GiB**, GPU **15,456 MiB**, and zero observed experiment
swap or resource-guard events. All 60 HTTP bodies complete without transport
errors; largest completed prompt is **67,720 tokens**. HTTP median is **73.22 s**,
maximum **662.80 s**; this includes prompt processing and generation, not isolated
decode speed. The coding stages total **116.53 minutes**; the separate read-only
control is excluded. Global swap counters increase (29,189 pages in, 239,216 out),
which cannot be attributed to this no-swap experiment. Samples do not prove
continuous whole-host peaks. Disk reserve stays above 100 GiB.

The three original services, original model alias/context, four profile files,
owner pending files/instructions and Hermes-Codex are independently verified
preserved/restored. All 30 model entries were unchanged during this stage.
After both Q4 stages completed, only the newly downloaded Q4 study weight was
hash-verified and retired temporarily to admit Q3 while preserving the original
29 and the disk reserve. The public pin permits restoring a selected winner.

[Summary](native-q4-fresh-summary.json), [sanitized archive](native-q4-fresh-evidence.tar.gz),
[SHA256](native-q4-fresh-evidence.sha256), [privacy scan](native-q4-fresh-privacy.json),
and [validation](native-q4-fresh-validation.json) retain numeric observations,
source fingerprints, project-test logs and scoped audit records. Raw prompts,
responses, profiles, private project source, graders and credentials stay local.

```sh
python3 evaluations/2026-11-23-wide-memory/verify_native_q4_fresh.py
```

The verifier checks saved evidence consistency; it does not recreate private
behavioral grading or certify reliability. One fresh family and its dependent
followups, alongside a separate conditional recovery, do not establish a model
winner. Q3, Devstral and GLM remain pending actual evaluation.
