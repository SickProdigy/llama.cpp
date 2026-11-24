# GPU-resident quantization comparison — November 24, 2026

Status: first Fable Q6 capacity stage complete and original runtime restored.
The first fresh Fable Q6 nonthinking workflow is complete and independently
audited: repair/docs/feature/publication fail. Original runtime and all retained
models/owner settings are restored/verified; the Q4 capacity stage also completes/restores, and its fresh native coding
stage also completes with no edits or publication. Both baseline Fable quants
are audited/restored/cleaned; Vibe Q4 resource testing is active.
See [current matrix](matrix.md) and [resource evidence](resource-fable-q6-summary.json).

Compare retained FableVibes Q4/Q6 and VibeForged v2 Q4/Q6 first. Earlier native
coding controls show mixed quantization outcomes: Fable Q6 improved one queue
case; Vibe Q6 failed where Q4 passed. Later real-source tasks also failed at
these precisions. Those limited historical samples are not new passes or proof
that precision caused the differences.

Public file pins are in public-candidates.json. Retained filenames must still
match full SHA256 before use. Start at 98,304 context, all GPU layers, q4 K/V,
non-mapped loading, one slot, two context checkpoints, 512 MiB prompt cache.
Measure short/tool-history, 16k and 60k active prompts, actual allocation,
charged host cache/helpers, swap and latency before scoring real coding.
Resource completion is not a task-quality pass. Preserve comparable settings
within a checkpoint and record sampler/template/calibration differences.

Fable Q5 is available publicly and may provide an intermediate comparison after
existing files. The author's pinned Vibe v2 repository lists Q4 and Q6 but no
Q5_K_M. Do not invent an available version. Download one new artifact at a time
only when at least 100 GiB reserve remains, preserving all retained models.

Adapted 27B Q5/Q6 are excluded from this GPU-resident shortlist: their weight
files alone exceed the 16 GiB device, before KV/runtime allocations. This is a
capacity-screen exclusion, not an observed loading or quality failure. Its
prior Q4 slow successful workflow remains documented in the wider-memory study.

After resource checks, use fresh natural coding tasks with dependent docs and
feature turns and real upstream issue/personal fork/PR actions. Independently
check code, original behavior, tests, docs, claims and actual published snapshots.
Keep graders/private controls out of actor prompts. Report turn/total latency,
intervention and correctness together; no autonomous reliability claims.

Experiments must restore original runtime/settings, preserve owner pending edits,
credentials and Hermes-Codex, close owned test issues, and retain sanitized
reproducible evidence. Commit/push completed stages with README/options/matrix.

## Prospective reasoning-mode control

Before assigning a practical Fable recommendation, compare a separately registered
fresh Q4/Q6 pair with reasoning enabled and the author's generation sampling.
The current quartet remains an unchanged thinking-disabled, temperature .2
baseline; no actor receives a corrective hint or restart. The author's pinned
[source generation configuration](https://huggingface.co/tvall43/Qwen3.6-14B-A3B-FableVibes/blob/758757ae225247b95c28ad2897d89aafe3bd3d52/generation_config.json)
sets temperature 1.0, top-p .95 and top-k20. The pinned GGUF card describes a
reasoning-trained model and expects reasoning output. These are publisher
settings, not independent evidence of better local results. Register output,
compression, time and memory budgets before the new pair; report it separately
as a configuration comparison, never as a precision-only effect or rescued
baseline pass. No new reasoning-enabled actor run has started yet.

[Retained-file header comparison](quant-header-comparison.json) finds identical
names/shapes and tokenizer/template metadata within each Q4/Q6 pair; only the
general file-type field differs. No importance-matrix metadata is recorded.
That absence does not prove none was used or establish identical source weights
and conversion/calibration history. Full file SHA256 verification is separate
and occurs before each model's inference.

## Prospective adapted27B IQ4_XS fit check

The [pinned public IQ4_XS option](prospective-adapted-iq4-xs.json) is smaller
than the earlier adapted27B Q4_K_M while retaining the same trained checkpoint
family. It is not downloaded or measured here yet. Its weight file alone is
14.27 GiB, so room for context/runtime must be measured; no full-GPU claim follows
from that size. Inspect prior 27B controls before registering layouts. Preserve
all 30 retained models and the 100 GiB reserve. An owned staging volume on another
filesystem may avoid consuming the model drive's narrow reserve, but its actual
free space and ownership must be verified before download. No GPU purchase or
local quantization is implied.


The [VibeForged Q4 unattended baseline](native-vibe-q4-beets.md) completed without code changes: all 18 selected `execute_code` attempts were blocked by copied-profile one-shot approval policy. Repository read control succeeded; code-tool ability remains unmeasured. A separate isolated deny/approve pure-code control confirms this mechanism without model calls. Original deployed settings remain unchanged. The prospective comparison now uses a fresh explicitly trusted Vibe Q4/Q6 pair; Q6 deny-profile coding is deferred, with its capacity check proceeding independently. Fable Q4/Q6 baseline outcomes remain preserved. Higher precision has not yet demonstrated a quality gain.


Vibe Q6 [capacity evidence](resource-vibe-q6-summary.json) now completes: 98,304-token allocation, requested full GPU offload, 11,566 MiB peak GPU, 6.561 GiB charged study cgroups, no study swap or guards, and a 59,937-token probe in 153.634 seconds. Original services/settings/models were independently verified restored afterwards. Capacity is not coding quality. Fresh trusted Vibe Q4 coding is launched; the trusted Q6 profile is frozen and pending, with identical task/source/sampler/seed/caps. Both copied profiles actually execute the no-model pure-code approval check successfully.
