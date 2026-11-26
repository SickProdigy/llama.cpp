# Fable Q4 reasoning with a cold coding gateway

November26: the matched cold-start Q4 trial fails the full workflow in22.24
coding minutes. The plugin is unloadable after all three turns: its patch puts
`from __future__ import annotations` at line152. Project collection stops with
that SyntaxError; original-preservation and independent checks also fail.
These are candidate source failures, not test-harness setup failures.

| Dependent turn | Coding seconds | Actual outcome |
|---|---:|---|
| Lifecycle repair |499.05|Plugin and new test module committed locally; plugin cannot import |
| Documentation |91.70|README added; syntax failure remains |
| Cancellation feature |743.83|Further code/docs changes; syntax failure remains; issue/push/PR left to user |

The8 original Beets test methods and their file bytes remain unchanged. A new
`beetsbridge/test_disable_imports.py` module cannot collect because its package
fails to import. Behavior and regression-test adequacy are therefore not
established. The final answer describes intended fixes/coverage but does not
complete the requested contribution.

Independent authenticated final reads verify all40 upstream baseline blobs
unchanged, zero issues, zero PRs and HTTP404 for the actor's fork. Nothing needs
closing. The exact Gitea remote, current branch and commit were already supplied
as initial workspace facts. A local commit does not prove publication.

There are92 completed backend requests and no output-length finishes. Maximum
completed input is77,940tokens. One native auxiliary request takes88.71s at29,932
uncached input tokens and107 output tokens; it emits literal tool-call markup
with no structured-summary headings. No tools execute in that auxiliary call.
The final main request retains all three literal user tasks. The syntax failure
is present before compaction, so the bad checkpoint does not explain it.

This is matched to the [cold Q6 trial](native-fable-q6-thinking-cold-beets.md):
new isolated profile/process/gateway, no preceding read control, main
T1.0/top_p0.95/top_k20/thinking enabled/seed20261124/output16,384/context98,304,
q4_0 K/V, current b12723-abca69200 llama.cpp and the same prior pinned experimental
Hermes image. All107 registered source hashes verify. The fresh Q4 profile
matches all1,006 original pre-test file hashes; only a drifted skill-usage counter
is sourced from a byte-identical unused profile copy, without copying conversation
state or changing originals. Preparation controls are excluded from model scores.

The experimental Hermes image differs from the owner's newer rebuilt runtime.
These two cold Fable cells are comparable to each other, not verdicts on that
updated stack. Q6 preserves valid imports and passes its project suite while
still failing the requested behavior/publication; Q4 breaks loading. Neither
completes this workflow, and one lineage per quant does not establish a causal
precision effect or unattended reliability.

Full model SHA256 and41/41 GPU layers are verified. Peak sampled GPU is8,964MiB;
GPU model7,790.09MiB, host model272.81MiB and GPU KV540MiB. Across136 samples
with10-second pauses, no measurement errors, guards or study swap are observed.
Charged cgroups peak at7,314,804,736bytes and process PSS at2,439,166,976bytes.
Sampling can miss transient peaks; whole-host swap is not attributed.
Original IDs/images/configurations/running state, alias/context,30 retained model
metadata entries, four owner profile hashes, pending edits and Codex all pass
postflight checks. Owned terminal supervisor, helpers/backend/network are removed;
disk reserve is106.58GiB. No model download/deletion or production policy change.

[Sanitized observations](native-fable-q4-thinking-cold-beets-summary.json),
[SHA256](native-fable-q4-thinking-cold-beets-summary.sha256), and
[validation](native-fable-q4-thinking-cold-beets-validation.json) bind the saved
results. Private source, model messages, grader output and credentials stay local;
the public receipt is not a behavioral replay.
