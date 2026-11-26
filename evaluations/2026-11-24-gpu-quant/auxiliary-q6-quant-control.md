# Fable Q6 auxiliary quantization control, November 26

Retained public FableVibes Q6_K also fails all three saved-history checkpoint
replays. This is a matched followup to the native-history q4_0-cache rows in the
[Q4 control](auxiliary-precision-controls.md), not a main coding/Gitea score.

The actual Q6 file is pinned and fully SHA256-verified before inference. Context
98,304, output cap8,192, seed20261124, current b12723-abca69200 backend, original
history, q4_0 K/V and each generation sampler match the new Q4 control. Every
request verifies zero cached tokens. The model alias string deliberately remains
the same to preserve request input; the file/full hash identify the actual weights.

| Auxiliary mode | Seconds | Output tokens | Semantic result |
|---|---:|---:|---|
| Original nonthinking |116.26|58|Literal `read_file` markup; no checkpoint |
| Same sampler, reasoning enabled |106.90|191|Historical coding continuation plus `read_file` markup; no checkpoint |
| Publisher reasoning sampler |146.65|1,473|Answers historical feature task instead of creating required checkpoint |

All41 layers are offloaded to GPU. Peak sampled GPU use is11,566MiB, GPU model
buffer10,392.38MiB, host model buffer397.85MiB and GPU KV540MiB. Across85
five-second samples there are no measurement errors, resource guards or study
swap. Aggregate charged cgroups peak at7,041,839,104bytes and process PSS at
1,546,645,504bytes; sampling can miss transient peaks and cannot attribute global
swap. The original runtime/alias/context, all30 retained model metadata entries,
settings, pending owner work and separate Codex instance pass postflight checks.
Owned terminal supervisor, backend and network are removed. Disk reserve remains
106.79GiB; no download, quantization or deletion occurred.

The [sanitized numeric summary](auxiliary-q6-quant-control-summary.json) contains
captures, placement, source fingerprints, manual judgments and the exact Q4
reference archive hash; its [SHA256](auxiliary-q6-quant-control-summary.sha256)
binds these saved observations. Raw history, generated text and credentials
remain private. Semantic judgments were audited locally, not replayed publicly.
Public quant-production/calibration differences and one history/seed prevent a
precision-only causal claim or an unattended-reliability conclusion.

Q6 alone does not solve this auxiliary failure. A fresh Q6 reasoning coding
trial with a cold profile/process/gateway is the next independent check. Its
initial coding session will omit the earlier preliminary read control, whose
native MCP cooldown state was coupled to coding. Exact configured-MCP identity,
repository lookup and tree reads pass a separate read-only admission check;
this is service compatibility evidence, not a model capability score.
