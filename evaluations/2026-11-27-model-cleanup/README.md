# User-authorized model cleanup — November 27, 2026

The owner authorized a broader cleanup of failed and unnecessary candidates after the initial 35B retirement. The expanded batch removed **10 files / 73.58 GiB**; both batches total **94.41 GiB**. Observed free space on the usual `models/` filesystem after the expanded batch: **197.56 GiB**. There are **19 remaining GGUFs** in that folder. The two separate staged adapted weights were not part of this deletion.

## Removed in the expanded batch

| File | Decision | Recorded reason |
|---|---|---|
| `DeepHermes-3-Llama-3-8B-q8.gguf` | historical tool failure | No exposed tool-call path in recorded Hermes run. |
| `Hermes-3-Llama-3.1-8B.Q8_0.gguf` | historical tool failure | Recorded unreliable forge/tool routing; no current advantage or planned comparison. |
| `Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf` | historical tool failure | Recorded text-only response instead of tool use. |
| `meta-llama-3.1-8b-instruct-q4_k_m.gguf` | historical tool failure | Recorded no tool-call path; retain newer compact helpers instead. |
| `qwen2.5-coder-14b-instruct-q4_k_m.gguf` | historical tool failure | Did not call tools for the explicit issue-create task. |
| `qwen2.5-coder-7b-instruct-q8_0.gguf` | historical tool failure | No confirmed MCP completion after three long model calls. |
| `LFM2.5-8B-A1B-Q5_K_M.gguf` | unsuitable main agent | Failed primary grounded reads and contribution; narrow publisher-profile metadata success does not justify retaining another helper. Not an all-tests-fail claim. |
| `Qwen3.8-9B-Q8_0.gguf` | redundant precision | Retain same-checkpoint Q5; Q8 showed no demonstrated primary workflow advantage. Successful contribution evidence remains valid. |
| `Qwen3.5-9B-Q8_0.gguf` | redundant precision | Retain stock Q5 as baseline; historical Q8 tool successes and later 3/9 combined results do not justify a second large stock precision reference. |
| `Qwen3.5-14B-A3B-Claude-Opus-Reasoning-Distilled-4.6-MXFP4_MOE.gguf` | superseded mixed candidate | Weak issue-write reliability and repeated tool errors; older eventual success is preserved in reports. Retain the working Vibes family instead. |

Historical template/tool failures are not proof that a model can never work with a different runtime. Retiring redundant precision or mixed candidates is a storage/priority decision; it does not erase successful narrow tests. In particular LFM passed a narrow metadata task, Qwen3.8 Q8 completed contributions, stock Qwen3.5 Q8 had tool successes, and the Opus-distilled file had an older eventual success. Those records remain intact. No new model-quality test was performed during cleanup.

## Retained in the main folder

- `FlashModel-Qwen3.5-9B-Q5_K_M.gguf`
- `Ministral-3-14B-Instruct-2512-Q4_K_M.gguf`
- `Ministral-3-8B-Instruct-2512-Q5_K_M.gguf`
- `Ministral-3-8B-Reasoning-2512-Q5_K_M.gguf`
- `Ornith-1.5-9B-uncensored.Q5_K_M.gguf`
- `Qwen3.5-9B-9b-v5s1-imat-Q4_K_M.gguf`
- `Qwen3.5-9B-Agent.q5_k_m.gguf`
- `Qwen3.5-9B-Q5_K_M.gguf`
- `Qwen3.6-14B-A3B-FableVibes-Q4_K_M.gguf`
- `Qwen3.6-14B-A3B-FableVibes-Q6_K.gguf`
- `Qwen3.6-14B-A3B-VibeForged-v2-Q4_K_M.gguf`
- `Qwen3.6-14B-A3B-VibeForged-v2-Q6_K.gguf`
- `Qwen3.8-27B-hermes-IQ3_XXS.gguf`
- `Qwen3.8-27B-hermes-Q4_K_M.gguf`
- `Qwen3.8-9B-Q5_K_M.gguf`
- `Qwopus3.5-4B-Coder-Fable5-v1-Q5_K_M.gguf`
- `gemma-4-12b-it-Q6_K.gguf`
- `gemma-4-E4B-it-Q5_K_M.gguf`
- `gpt-oss-20b-MXFP4.gguf`

All four VibeForged/FableVibes files remain, including the active VibeForged Q4. The adapted 27B IQ3/Q4 have useful older results and remain comparison/overnight options. Stock Qwen Q5 stays as a baseline; Qwen3.8 Q5 keeps the smaller same-checkpoint alternative. Gemma E4B and Qwopus 4B retain small-helper options. Other retained candidates have meaningful narrow successes or remain distinct comparisons; retention is not a claim of unattended reliability.

## Verification and scope

Each removed file was regular, non-symlink, single-link, matched its captured identity before deletion, and received a complete SHA-256 read. Available public pins were checked as an additional guard. Running container commands, entrypoints and environment were checked for candidate references before each removal. Every retained model has unchanged device/inode/size/mtime/mode/ownership/link metadata. The original llama.cpp, Hermes and Hermes-Codex container IDs, start times, restart counts and configuration hashes are unchanged. No service restart, profile change, training or quantization occurred.

Exact expanded decisions, per-file checksums, identities, services and space observations: [expanded-retirement.json](expanded-retirement.json). Initial 35B deletion: [retirement.json](retirement.json). The initial batch removed 22,360,456,160 bytes after checking its full hash and inactive status; all 29 other files were unchanged at that point.

The unnecessary HDD copy job was stopped and its sole incomplete copy removed; the old staged source weights were never deleted. Additional downloads can use the usual `llama.cpp/models` directory, subject to fresh admission and the 100 GiB free-space floor.

This explicit authorization supersedes earlier preserve-original30 guidance for these 11 named files only. Historical preservation attestations stay true for their recorded epochs; future studies must capture a fresh current inventory rather than reuse the old baseline. Original benchmark evidence and download pins remain available.
