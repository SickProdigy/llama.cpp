# Wider-memory Hermes model evaluation

Started November 23, 2026. Goal active; no new model fit or agent-quality result
is claimed. The owner prioritizes correct agent work over speed and permits the
full P100 plus up to 8 GiB additional host RAM for model spillover.

## Stages

1. Pin public model files and inspect current hardware, disk and previous tests.
   Download one additional large file at a time, keeping at least 100 GiB free
   and preserving all original useful weights. Begin with adapted 27B Q4_K_M,
   then its Q3_K_M, Devstral Small 2 24B and GLM-4.7-Flash as compatibility permits.
2. In isolated pinned-runtime trials, find measured layouts at realistic context
   sizes, starting at 98,304 and considering 65,536 where needed. Record active
   inference, GPU peaks, backend cgroup anon/file/current/peak/swap, process
   RSS/PSS and host swap-activity deltas. Enforce the 8 GiB host budget rather
   than assume 16+8 GiB is available for weights. Distinguish supported hardware
   layouts from useful model behavior. Do not change production images/settings.
3. Freeze new symptom-led tasks, reference/preservation checks, profile versions,
   sampler and measured generous budgets before scored calls. Use a normal
   selected checkout, native persistence and configured Gitea for real upstream
   issues, personal forks and upstream PRs, followed by dependent changes.
   Do not repeat old published problems as fresh accuracy evidence. Score code,
   public behavior, preserved behavior, meaningful tests, docs, claims, state
   retention and actual remote publication separately. No grader hints to models.
4. Audit promising candidates on matched tasks/repetitions as justified by the
   observed failure patterns. Report small-sample limitations and hardware-only
   blockers. Update the model matrix and options with actual evidence, restore
   the original runtime after GPU stages, close test issues, and deliver sanitized
   reproducible artifacts and staged commits.

Slow, correct work is acceptable. Do not reject a model merely for exceeding
old speed targets; measure throughput and choose budgets with room for actual
prompt processing, output and tool execution. Budgets remain bounded and fixed
before scored runs. A successful load, green authored test suite or opened PR
is insufficient to call a model correct.

The prior compact-review evaluation is complete and remains unchanged. Its
failed reviewer results do not substitute for testing these models as actors.
The new study should not automatically put that unqualified gate in front of
all publication. Genuine execution and independent outcome auditing still apply.
Tool-interface differences must be explicit; experimental focused wrappers
making real MCP calls are not an unmodified native-MCP comparison.

## Initial pinned download

[Publisher](https://huggingface.co/netprojects/Qwen3.8-27B-hermes-adapted-GGUF),
revision `10fdf357f14825c61ad7eb42a932e1f1e4390e8f`:
`Qwen3.8-27B-hermes-Q4_K_M.gguf`, 16,810,714,560 bytes, SHA256
`6512bb1c2595575fc0aed39b7d72a6aaf71084b1164b5d3749f87a6c2a3d3bf3`.
Download checks exact length/hash before atomic rename and checks disk reserve
throughout. It does not stop the deployed backend or use GPU inference.

[Public file metadata](public-model-metadata.json) also pins the Q3 alternative,
[Devstral GGUFs](https://huggingface.co/unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF)
and [GLM GGUF](https://huggingface.co/ggml-org/GLM-4.7-Flash-GGUF).
These metadata are download identities, not tested fit/quality results.

Original runtime/profile/model inventory is privately snapshotted before work:
VibeForged Q4, 98,304 context, 29 retained models, approximately 123.96 GiB free.
Hermes-Codex is excluded from all changes/restarts. Owner-managed settings,
credentials, pending source edits and model files must be preserved. Only new
study-owned downloads may be removed as required by the sequential disk budget,
with exact identity checks and recorded disposition; do not delete useful owner
models to make several new files fit simultaneously.

## Pre-inference preparation

Two fresh initial defects reproduce through actual public plugin callbacks;
reference corrections pass independent checks and all 83 original tests plus
two subtests. [Validation summary](fixture-validation.json) is not model output;
private checks and references stay outside model profiles.

[Resource pilot bounds](resource-protocol.json) register the 8 GiB host cap,
no backend swap, limited host prompt cache, measured 16k/60k context probes and
bounded layout fallback before any new inference. A same-checkpoint IQ3 baseline
will use the same resource settings. The protocol does not claim loaded or
active fit yet.

## First resource stage delivered

[Initial baseline and its loading-memory caveat](resource-baseline.md) are complete
and restored. The Q4 file download is complete. [Protocol v2](resource-protocol-v2.json)
registers non-mapped loading before any Q4 inference. Full native actor workflows
and the remaining candidate trials are still required.
