# Fable Q8: GPU fit succeeds, coding/Gitea workflow fails

November26: public Fable Q8 fails the three-turn workflow in38.68 coding
minutes (42.45 supervisor wall minutes including setup/load/grading/restoration).
It fits98,304 context with all41 layers on GPU, but leaves incorrect behavior,
broken authored tests, incomplete documentation and no real contribution.

| Dependent turn | CLI seconds | CLI exit | Project / original / independent exits |
|---|---:|---:|---|
| Lifecycle repair |1279.98|1|1 / 0 / 1|
| Documentation |127.45|0|1 / 0 / 1|
| Cancellation feature |913.52|1|2 / 0 / 1|

The [exact task queries](beets-natural-task-queries.json) explicitly require
manual imports with automation off, abandoning not-started work across disable
and reload, meaningful tests and a real upstream issue/personal fork/PR. Later
queries require accurate docs and cancellation that permits newly queued work.
Native context already supplies the selected Git/Gitea origin and authenticated
identity is available through the configured tools. No operator correction or
private grader result was fed back to the actor.

The repair replaces the stopping check with the automatic-import setting,
blocking manual dispatch when automation is off. It adds13 root tests; one
checks `.called` on an ordinary callback function and fails. Project results
are95 passes/one failure/two passing subtests in the first two turns. All83
original tests/two subtests still pass, and all8 original Beets test methods
remain unchanged. That green baseline suite does not establish preserved
behavior: it misses the new manual-dispatch regression.

The final feature retains that regression. Its new conftest calls
`types.ModuleType(..., __path__=None)`, which raises TypeError before tests can
collect. The final explanation blames missing `pynicotine`; this observed error
is in the authored mock constructor. The old failing root test remains unchanged.
A new cancellation test even expects a later queued import to remain skipped,
contrary to the requested behavior. README bytes are unchanged after the docs
turn and contain no `/beetscancel` documentation.

The registered independent suite reports6 failure records across3 tests in
turns0/1 and9 across6 tests in turn2. Many fail at the same initial worker-dispatch
precondition; these are not nine distinct demonstrated bugs. Separate post-run
corroboration on the frozen final source, with automation enabled where needed,
confirms the downstream problems without changing the actor or registered score:

- No-argument cancel reports zero for two pending timers and leaves both pending;
  it marks folders cancelled without cancelling those timer objects.
- Later newly queued work for the cancelled folder does not dispatch.
- A previously dispatched, not-started worker still invokes the import method
  after disable/reload and after cancellation.

These observations use mocked import boundaries, not real media imports. The
final answer repeatedly says it needs to push/open a PR, but makes zero Gitea
calls. Independent authenticated reads verify40 unchanged upstream baseline
blobs, zero issues, zero PRs and HTTP404 for the personal fork. Nothing needs closing.
The documentation answer also refused to commit/push for lack of an explicit
instruction despite the publish request; this was not an operator approval block.

There are130 usage-complete backend captures, no unmatched requests, no HTTP or
transport errors and no output-length finishes. Largest completed input is83,484
tokens. Three requested16,384-token output reservations exceed remaining window
space, by up to1,564 tokens, but every actual input/output fits. No real overflow
recovery is exercised; the corrected recorder's synthetic controls remain separate.
Two auxiliary calls (38.72s/94.87s,32/337 output tokens) emit literal skill-view
and patch markup rather than checkpoints; no auxiliary tools execute. The bad
manual gate is already present in tool output at request32, before the first
auxiliary request52. Compaction does not explain that earlier source regression.
All three literal user tasks remain in the final main request. Native ancestry,
CLI handles and exact query hashes independently verify on byte-identical saved
SQLite copies; the two accepted compactions do not prove faithful summaries.

All122 frozen source bindings and the full pinned model SHA verify. The current
owner-derived Hermes evaluator, current llama.cpp and corrected recorder are
bound prospectively. Older Fable Q4/Q6 cells use an older Hermes image/recorder;
this is not a precision-only comparison or an autonomous-reliability estimate.
A current Q6 reference remains relevant before judging the precision difference.

Peak sampled GPU is14,624MiB; GPU model13,450.91MiB/host model515.31MiB/KV540MiB.
Across231 samples with10-second pauses, no measurement errors, guards or study
swap are observed. Charged cgroups peak7,228,424,192 bytes; process PSS peaks
2,777,708,544 bytes. Charged cache is included, not CPU transformer-layer offload.
Sampling can miss transient peaks. Both disk reserves remain above100GiB.
Original runtime IDs/images/config/running state, alias/context, four profile
hashes,30 original models,40 owner source files/pending edits and Codex pass
postflight. Owned terminal supervisor, backend/helpers and network are removed.
Original-drive free space is104.31GiB. No original model is deleted.

[Sanitized observations](native-fable-q8-thinking-cold-beets-summary.json),
[SHA256](native-fable-q8-thinking-cold-beets-summary.sha256),
[validation](native-fable-q8-thinking-cold-beets-validation.json).
Private actor messages/source snapshots/graders stay local. Validation verifies
saved observations and actual audit results; it does not mean the model passed.
