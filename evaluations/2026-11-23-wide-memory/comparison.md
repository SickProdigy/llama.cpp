# Wider-memory comparison and retained model

Completed November 24, 2026. **The public Hermes-adapted 27B Q4_K_M is the strongest
observed supervised actor lead in this tested configuration.** Its new fresh Spam
lineage completes the repair, documentation, feature and real issue/fork/PR work;
its separate fresh Announcer lineage passes source/behavior checks with recorded
qualifications. This study does not establish unattended or general coding-agent
reliability from two task families with dependent followups.

The original Vibe runtime is restored. The Q4 file is retained alongside all 29
original models, with [over111 GiB free](retained-models.json). This is a retained
experimental option; owner-managed runtime settings are preserved.

## Quality comes before speed

| Public candidate | Fresh Spam workflow | Fresh Announcer workflow | Coding minutes, Spam / Announcer |
|---|---|---|---:|
| Adapted 27B Q4_K_M | Repair, originals, docs, feature, meaningful coverage and actual publication pass | Behavior/publication pass; README, count/reporting and frozen-metadata qualifications remain | 115.60 /116.53 |
| Adapted 27B Q3_K_M | Actual repair fails despite green project tests and correct issue/fork/PR; feature alone passes | Behavior/publication pass with documentation/reporting qualifications | 35.41 /20.65 |
| Devstral Small 2 24B Q4_K_M | Original notification preservation fails; existing test weakened; no required publication | Feature retains orphaned empty-job reply state; no required publication | 48.93 /104.65 |
| GLM-4.7-Flash Q4_K | Preservation/cooldown/test adequacy fail; correct issue/fork, no commit/PR | Lost completion replies, retained room state, incorrect docs, no publication; repetition stops all turns | 85.00 /215.29 |

The [matrix](matrix.md) and individual reports preserve raw failed checks. For
Announcer's optional room argument, a frozen metadata assertion is separately
qualified against actual pinned supported dispatchers: missing command metadata
does not reject the argument. Source and additional callback controls distinguish
the genuine Devstral/GLM state defects from that assertion. Passing authored tests,
a created PR, or a zero CLI exit is never substituted for correct behavior.

The earlier [Q4 Spam recovery](native-q4-recovery.md) remains conditional and is
excluded from this fresh comparison. [The new fresh result](native-q4fresh-spam.md)
resolves that specific fairness gap. Historical IQ3/Vibe/other-model cohorts use
different tasks and settings; they are not new matched quality scores here.

## What the larger budget enables

All four named candidates complete resource probes in the pinned runtime at
98,304 context, then undergo the native workflow trials. These are the maximum
sampled native observations across each candidate's two families:

| Candidate / tested layout | Peak GPU MiB | Aggregate study cgroups GiB | Process PSS GiB | Largest completed native prompt |
|---|---:|---:|---:|---:|
| Adapted Q4,56GPU layers | 15,456 | 7.044 | 5.034 | 77,347 |
| Adapted Q3,all layers GPU | 14,946 | 6.919 | 2.382 | 62,241 |
| Devstral Q4_K_M,32GPU layers | 14,880 | 6.974 | 5.725 | 73,156 |
| GLM Q4_K,12CPU expert layers | 15,336 | 6.833 | 5.909 | 84,237 |

These layouts use non-mapped loading, limited host prompt cache, q4 K/V and two
context checkpoints. Charged cache/helpers are included; no experiment swap is
observed and aggregate guards remain at 8 GiB. Whole-host swap counters sometimes
move substantially and are reported without attribution. Sampling does not prove
continuous whole-host allocation bounds. Context capacity and file size alone
are not correctness evidence.

Q4's first longer native attempt had a host cgroup OOM despite a short resource
pass. The [checkpoint comparison](checkpoint-comparison.md) preserves the default 32
failure and measured two-checkpoint control. The successful native Q4 backend cap
is 6656m/6.5 GiB. GLM's initial unequal K/V configuration rejection and correction
are also preserved, rather than counted as a model-quality failure.

## Findings that affect the interpretation

- The adapted checkpoint aligns best with these tool/contribution tasks. The data
  do not isolate fine-tuning as a cause: architecture, weights, templates, output
  settings and sampling also differ. Even Q3/Q4 public files have different
  importance-matrix metadata, so this is not a precision-only causal experiment.
- The slower Q4 completed the requested work more accurately in this cohort.
  Native timings include policy, tools, output and CPU offload. Q4's fresh Spam
  first coding request has zero cached tokens; several other runs reuse a warm
  first prefix. These are operational timings, not controlled throughput rankings.
- GLM's separate native 300-second compression no-output guard interrupts auxiliary
  prefill despite extended main/provider timeouts. Hermes ultimately uses a
  deterministic checkpoint, not a successful model-generated summary. The next
  primary retains all three literal tasks. Earlier initial/README defects and
  repetition precede compaction, so that confound cannot explain all failures.
  The source-verified 5400-second compression proposal remains untested/unapplied.
- Full native persistence, natural fresh tasks and dependent followups expose
  behavior that earlier guided/stateless or read-only tasks miss. Original tests,
  independent cases, real published source, docs, claims and remote resources need
  separate review. Model-authored green tests can encode a bad expectation or
  fail to exercise the real callback.
- Q4's own intermediate new-test failure is corrected without operator hints or
  implementation-priority changes. Independent controls verify the same-user,
  same-room rule distinction, actual setting bounds and long-cooldown cleanup
  beyond the coverage provided by the authored tests alone.

Use Q4 as a supervised, patient batch-work lead for this configuration, with
independent review of each real change. The observed50-minute initial fix and
51-minute feature turn are material operational limits. The evidence does not
support treating any small local model as a replacement for a correctness gate.

## Scope, preservation and evidence

The scoped/friendly Gitea wrappers, normal full profile, explicit execution
publication gate and pinned native runtime are part of these outcomes. This is
not an unmodified raw-MCP model-only comparison. No private graders, corrective
hints, neutral continuations or task restatements are supplied to the actors.

Private source/requests/profiles/tasks/checks remain retained locally. Sanitized
archives expose numeric observations, source fingerprints, project/original test
logs and scoped audits. Validators prove saved-evidence consistency, not complete
private behavior reexecution or autonomous reliability. Public files/revisions/
full hashes are recorded in [comparison data](comparison.json) and resource reports.

[Temporary owned-weight rotations](study-weight-rotations.json),
[final retention](retained-models.json) and [six closed test issues](test-issue-cleanup.json)
are independently checked. Original service identity/image/configuration, four
profile files, owner pending files/instructions and Hermes-Codex state are preserved;
owned runtime containers/networks are removed. PRs remain unmerged audit artifacts.

The retained 35B's four earlier trials were reviewed rather than repeated solely
because its file looked affordable. They use different tasks, include a context/
runtime-affected bulk run, and do not establish the new 8 GiB aggregate host fit or
complete task correctness. The original 35B weight is preserved; no new35B quality
score or spare-GPU result is claimed.
