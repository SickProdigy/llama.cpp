# GPU-resident quantization comparison — November 24, 2026

Status: first Fable Q6 capacity stage complete and original runtime restored.
Fresh native coding workflow launched; no new coding-quality verdict yet.
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
