# Vibe Q6 reasoning on the current Hermes runtime

November26: the matched Q6 workflow fails after64.03 coding minutes. It shares
[Q4's current-owner-derived evaluator](native-vibe-q4-thinking-cold-beets.md),
current llama.cpp, task family, sampler, output cap,98,304 context and q4_0 KV.
This is one lineage per quant, not a causal precision experiment or reliability estimate.

| Dependent turn | Seconds | CLI exit | Outcome |
|---|---:|---:|---|
| Lifecycle repair |988.68|1|Partial stop-event patch; authored test and independent lifecycle checks fail |
| Documentation |2558.06|1|README claims safety the code does not provide; output length exhausted |
| Cancellation feature |295.31|1|No feature inference succeeds: prompt exceeds context |

All snapshots compile. Project tests report84 passes, two passing subtests and
one failure in each phase. The frozen original suite reports82 passes, two
passing subtests and one failure: a new required worker argument breaks its
existing call. The actor changes one of eight original Beets test methods to
accept the new signature; seven remain unchanged. It adds two tests. Its new
worker test exits the Thread-mock scope before firing the timer, so it fails to
observe its expected fake thread. Green or broken authored tests alone do not
establish the requested behavior.

The shared stop Event is cleared on reload, allowing old waiting work to resume.
Independent lifecycle checks record three failures in the first two phases;
the final six-test feature suite records six failures. The cancellation command
is absent. Its absence after a context-rejected turn is not a clean measurement
of the model's ability to implement the feature. The README removes the existing
Commands section and falsely says stopped waiting work cannot resume.

The backend completes107 requests;23 further requests fail HTTP400 because the
rendered prompt is98,346 tokens against98,304 available. The gateway exposes
these as502 to Hermes, whose retries cannot fix the oversized request. This is
context handling, not GPU allocation or an OOM. Largest successful input is
98,069 tokens. Three auxiliary requests each consume the full8,192 output cap
(336.90s/331.66s/240.73s), producing repetitive histories rather than faithful
bounded checkpoints. Later ones repeat hundreds of alleged completed actions;
one asserts all tests pass despite recorded failure. All user tasks remain
literal in the final main request. The lifecycle defects already precede this
context failure, so repairing context alone cannot establish workflow success.

Independent authenticated Gitea reads verify40 unchanged upstream blobs, zero
issues, zero PRs and HTTP404 for the actor fork. Nothing needs closing.

All118 frozen source bindings and full model SHA verify. All41 layers are on
GPU, peak11,566MiB, with10,392.38MiB GPU model,397.85MiB host model and540MiB
GPU KV buffers. Across375 samples there are no measurement errors, guards or
study swap; charged cgroups peak7,032,295,424 bytes and process PSS2,670,272,512.
Sampling can miss transient peaks. Host buffers and charged cache are not proof
of transformer-layer CPU spillover.

Original service IDs/images/config/running state, alias/context, four profile
hashes,30 retained models, owner pending work and Codex pass postflight. Owned
stage containers/network are gone and104.48GiB remains free. Q6 consumes more
GPU memory than Q4 and neither succeeds; this sample establishes no practical
Q6 quality advantage. Prior slower adapted27B Q4 successes remain valid measured
tradeoffs on their own tasks/runtime, not directly matched scores.

[Sanitized observations](native-vibe-q6-thinking-cold-beets-summary.json),
[SHA256](native-vibe-q6-thinking-cold-beets-summary.sha256),
[validation](native-vibe-q6-thinking-cold-beets-validation.json).
Private source/messages/graders and credentials stay local.
