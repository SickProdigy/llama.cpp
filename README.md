# Llama.cpp and Hermes-Agent Model Notes

GGUF testing notes for Hermes Agent running through llama.cpp.

This file tracks which local GGUF models can actually complete the Hermes Agent plus Gitea MCP workflow, not just whether they answer a prompt or make a promising first tool call. Use the matrix for quick comparison and the detailed sections below for why a model passed, failed, or landed in the middle.

## November 18, 2026 focused Gitea tools: current recommendation

**Keep VibeForged v2 Q4_K_M as the main model, with FableVibes Q4 as the close
alternative.** Clearer required-field tools improved actual issue → fork edit →
upstream PR behavior substantially. No model weights were trained.

| Model · focused tools · 98,304 context | Correct workflow resources | All requested read-backs / URLs too | Peak VRAM |
|---|---:|---:|---:|
| VibeForged v2 Q4_K_M | 3/3 | 2/3 | 9,082 MiB |
| FableVibes Q4_K_M | 3/3 | 1/3 | 9,082 MiB |
| Qwen3.5-9B Q5_K_M | 2/3 | 2/3 | 7,472 MiB |
| Qwen3.5-9B toolcall-preview Q4_K_M · new download | 0/2 | 0/2 | 6,690 MiB |

These small samples use one strict-body pilot and separate reference-only-body
repetitions; they are not reliability percentages. One harness-affected Fable
pilot is excluded. VibeForged also completed a separate fresh-fork workflow on
SonicRatings. A separate approximately 64k-input retrieval + MCP read passed
without compression at 9,082 MiB; the loaded window remains 98,304. The downloaded preview model succeeded on a narrower PR-only
follow-up and remains a research candidate, rather than the default.

The benefit is demonstrated with an actual same-Qwen PR-only comparison: native
multiplexed tools failed, while the focused tools opened and read back PR #11.
The earlier native comparison below is historical evidence for that interface.
Read/review quality remains uneven, so these results support bounded contribution
tasks, not unattended arbitrary repository work.

Removed 33.01 GiB of unsuitable/orphan model files, downloaded one verified
5.24 GiB candidate, and preserved small task models, embeddings and close agent
candidates. Approximately 250 GiB remained free after the download.

See the [full comparison and exact limitations](evaluations/2026-11-18-required-tools/investigation.md),
[focused tool implementation/configuration](hermes-profile/gitea-focused/README.md)
and retained sanitized requests, prompts and independent verification.

## November 18, 2026 upstream contribution workflow comparison

**With the original native tool interface, no model completed the full upstream
issue → fork fix → upstream PR workflow.**
The final three runs used the same frozen Discord agent profile, 42 tool
schemas, validated guard, sampling and llama.cpp b12464 at 98,304 context.
Earlier harness-affected probes were excluded and preserved separately.

| Model | Read/review sample | Final contribution result | Peak VRAM |
|---|---|---|---:|
| VibeForged v2 Q4_K_M | Useful explanation with unsupported fork claim; review drifted to web | Created issue #9 and fork branch; file update tried creating that branch again | 9,082 MiB |
| Qwen3.5-9B Q5_K_M | Useful explanation with unsupported claims; review drifted to local files | Created issue #10, branch and exact file commit; repeatedly omitted PR head/base | 7,472 MiB |
| FableVibes Q4_K_M | Passed both single read/review prompts | Tried opening the issue under the wrong upstream owner; blocked | 9,082 MiB |

Qwen got furthest on writes and uses the least memory, but a separate PR-only
follow-up also failed. Fable's MCP-only/temperature-0.2 implementation probe
failed after changing the supplied fork identifier. Neither diagnostic counts
as a full pass. A **non-model** control through the same Hermes MCP connection
opened [PR #7](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/pulls/7),
confirming the required connection permissions and cross-fork PR capability.

These are small capability probes, not reliability estimates; do not pool them
with earlier nine-session scores. The original runtime/model/configuration was
restored. See the [full results, exact task setup and retained artifacts](evaluations/2026-11-18-contribution/investigation.md),
[final write results](evaluations/2026-11-18-contribution/model-results.csv) and
[contribution test protocol](evaluations/write-workflow-protocol.md).

## November 17, 2026 real Gitea fork/issue probe

The earlier third-test probe exercised actual writes against the approved small
`nicotineplus-plugins` fixture. Both VibeForged model attempts failed: they
supplied a personal account as an organization and were stopped before unrelated
tool use. No model-created fork or issue resulted.

A separate direct control using the same Hermes MCP account created the test
fork and obtained an accepted issue #1 response. Read-back initially returned
404 with Issues disabled. After the owner enabled Issues, the same Hermes MCP
account successfully read issue #1 on November 18. This direct control is
**not an agent pass**; the two model failures remain unchanged.

See the [write probe and actual resource state](evaluations/2026-11-17-fork-issue/investigation.md)
and [bounded write-test protocol](evaluations/write-workflow-protocol.md).

## November 16, 2026 repaired profile and Qwen9B Q5 comparison

Both models were tested at 98,304 context on llama.cpp b12407 with the same
repaired profile and full AIAgent Discord platform selection in disposable
containers. No Discord messages or forge writes were sent. Each row has nine
fresh runs; history sequences are separate. This is a new protocol, not pooled
with the earlier CLI measurements.

| Model / repaired Discord agent profile | Routing | Content | Both | GitHub attempted | Timeouts | Median turn |
|---|---:|---:|---:|---:|---:|---:|
| VibeForged v2 Q4_K_M | 6/9 | 3/9 | 3/9 | 3/9 | 0 | 63.2s |
| Qwen3.5-9B Q5_K_M | 6/9 | 4/9 | 3/9 | 3/9 | 0 | 100.7s |

See the [full repair/Q5 comparison](evaluations/2026-11-16-q5-repaired/investigation.md)
and [per-run evidence](evaluations/2026-11-16-q5-repaired/runs.csv).

## November 13, 2026 FableVibes comparison

Both Q4_K_M models were rerun on llama.cpp b12316-5d4c8eeb2 at 98,304 context,
with matched sampling, q4 K/V, one slot, 4,096 main output and the current frozen
Hermes profile. Each row uses nine fresh full-agent CLI runs; history sequences
are separate. These are current control measurements, not pooled with November 12.
No issue-write test was performed.

| Model · 98,304 context | Gitea used | GitHub attempted | Routing pass | Content pass | Both | Timeout | Median turn |
|---|---:|---:|---:|---:|---:|---:|---:|
| VibeForged v2 Q4_K_M control | 3/9 | 7/9 | 2/9 | 1/9 | 1/9 | 1 | 139.2s |
| FableVibes Q4_K_M | 2/9 | 8/9 | 1/9 | 0/9 | 0/9 | 1 | 182.8s |

See the [full FableVibes comparison](evaluations/2026-11-13-fablevibes/investigation.md)
and [per-run grades/evidence](evaluations/2026-11-13-fablevibes/runs.csv).
The original runtime/configuration was restored; credentials/endpoints were
preserved. The evaluation performed no training or remote issue writes.

## November 12, 2026 ordinary repository prompt evaluation

These new measurements use the complete Hermes conversation loop, ordinary
repository prompts, three fresh repetitions per prompt, and separate history
sequences. They supersede any inference that the older guided issue-write
passes prove reliable ordinary repository work. All runs are read-only against
the forge; **no issue-write test was performed in this evaluation**.

| Candidate | Gitea used | GitHub attempted | Routing pass | Content pass | Both pass | Median turn |
|---|---:|---:|---:|---:|---:|---:|
| VibeForged v2 Q4_K_M · 98,304 | 2/9 | 8/9 | 1/9 | 1/9 | 0/9 | 194.7s |
| VibeForged v2 Q6_K · 98,304 | 6/9 | 4/9 | 5/9 | 1/9 | 0/9 | 326.6s |
| Qwen3.5-9B Q8 · 65,536 | 7/9 | 3/9 | 6/9 | 4/9 | 3/9 | 91.5s |
| Qwen3.5-9B Q8 · 98,304 | 5/9 | 4/9 | 5/9 | 3/9 | 3/9 | 127.9s |
| Qwen 9B · 65,536 · connections removed | 5/9 | 4/9 | 5/9 | 1/9 | 0/9 | 116.3s |
| Previous + direct tool schemas | 9/9 | 1/9 | 8/9 | 0/9 | 0/9 | 150.3s |
| Previous + readable bounded file guidance | 9/9 | 0/9 | 9/9 | 1/9 | 1/9 | 75.8s |

“Both pass” requires Gitea repository use, no GitHub attempt, and a grounded,
complete answer with distinct ideas. Task completion alone is insufficient.
Fixtures are public on Gitea (`private: false`), so this measures default-forge
choice rather than private authorization. `sptnr` was verified as renamed to
SonicRatings and the lookup prompt was fixed once before the scored matrix.

Q4/Q6 used identical 98,304 context, q4 K/V, one slot, native sampler settings,
4,096 output cap and tool configuration. Qwen used its native 0.8/top-k40
sampler, versus VibeForged's 1.0/top-k20; it is a separate model/configuration
comparison. The Q4/Q6 system prompt differs in its visible model-identity
line; this is not blinded. All models fit the P100: sampled peaks were Q4 9,084 MiB, Q6 11,684 MiB,
Qwen 65k 9,474 MiB and Qwen 98k 9,922 MiB. Median first API-call
latencies were respectively 3.8s, 5.5s, 3.3s and 3.7s (warm-cache
measurements, not first-token latency). Neither higher precision nor more context
established reliable task quality.

The investigation confirmed stale Gitea tool names, deferred Gitea discovery
beside eager connection administration, and a separate compression defect:
auxiliary requests omit an output cap and inherit server `--n-predict 512`.
Historical OAuth-token removal does **not** establish broken authentication.

No configuration tested here qualifies for reliable ordinary repository work.
The original Q4 configuration was restored. Prefer Qwen 65k for further
validation; direct schemas improve observed forge routing, while content and
novelty failures remain. Compression-budget, namespace and method-surface
repairs need separate validation before training. Credentials and endpoints
were preserved; the evaluation made no new issue writes.

See the [full investigation](evaluations/2026-11-12/investigation.md),
[per-run metrics and grades](evaluations/2026-11-12/runs.csv), and
[evidence layout](evaluations/2026-11-12/EVIDENCE.md) for configuration factors,
history outcomes, limits and restoration verification. These are uniform core
CLI evaluations; native Discord/API gateway parity is not claimed.

## Current Test Setup

Hardware baseline for all results in this file: NVIDIA Tesla P100 with `16 GiB` VRAM. Unless a section explicitly says otherwise, every model result and VRAM observation below came from this card.

Current llama.cpp compose is currently set to the active Qwen3.6 14B A3B VibeForged v2 Q4_K_M working target:

```yaml
-m /models/Qwen3.6-14B-A3B-VibeForged-v2-Q4_K_M.gguf
--alias qwen3.6-14b-a3b-vibeforged-v2-q4_k_m
--jinja
--host 0.0.0.0
--port 11430
--ctx-size 98304
--parallel 1
--cache-type-k q4_0
--cache-type-v q4_0
--n-predict 512
-ngl 999
```

Hermes Agent is currently set to:

- `model.default: qwen3.6-14b-a3b-vibeforged-v2-q4_k_m`
- `model.context_length: 98304`
- `model.max_tokens: 4096`

The Q4 model is now running at `98304`. `/props` confirmed the full context and
`nvidia-smi` showed about `9072MiB`, so it fits this 16 GiB P100 without CUDA
OOM. The first natural-prompt repo review still failed from tool-routing drift,
however, so 98k memory fit is confirmed while workflow quality remains mixed.

`model.max_tokens` matters here: leaving it unset let Hermes request huge post-tool generations, and llama.cpp treated the per-request OpenAI body as the real limit instead of the compose-level `--n-predict 512`.

## Ordinary Repository Task Criteria

The November evaluations require a successful configured Gitea repository read,
no GitHub attempt, and a grounded answer that satisfies the requested count and
novelty. Routing and content are scored independently; both must pass for a
combined pass. Separate history sequences measure context carryover. These
read-only tests do not establish issue-write reliability or native Discord/API
gateway parity.

### Historical Guided Workflow Criteria

| Check | Required result |
|---|---|
| Backend context | `/props` shows `n_ctx >= 64000`; in practice we target `65536` or higher because Hermes can still complete small prompts below that, but larger repo inspection and compression-heavy turns start breaking once usable context falls under the 64k floor |
| Minimal workflow | Creates one concept-only Gitea issue with valid MCP write args |
| Harder workflow | Only tested after minimal pass; completes one light repo-review-plus-issue flow |
| Tool behavior | Uses Gitea MCP instead of drifting into text-only replies or malformed write loops |
| Easy request latency | Ideally under `120-180s` in Hermes Agent |
| Output discipline | Avoids duplicate tool retries and runaway decode length |

## Test Matrix

### Nine-session Ordinary Repository Results (November 12–16)

Each row uses nine fresh full-agent sessions. November 16 uses the repaired
Discord agent profile on b12407; older rows use CLI selection on b12316 (Nov 13)
or b12282 (Nov 12). Compare the two November 16 rows as the matched pair; do not
pool or rank across profiles. Both means routing and content passed in one turn.
The dated sections retain all configurations and earlier scores.

| Model / quant | Evaluated | Context | Routing | Content | Both | Sampled peak VRAM | Median first API call | Median turn | Issue writes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| VibeForged v2 Q4_K_M | [Nov 16 · Discord](evaluations/2026-11-16-q5-repaired/investigation.md) | 98,304 | 6/9 | 3/9 | 3/9 | 9,082 MiB | 3.3s | 63.2s | Not retested |
| Qwen3.5-9B Q5_K_M | [Nov 16 · Discord](evaluations/2026-11-16-q5-repaired/investigation.md) | 98,304 | 6/9 | 4/9 | 3/9 | 7,472 MiB | 5.2s | 100.7s | Not tested |
| FableVibes Q4_K_M | [Nov 13](evaluations/2026-11-13-fablevibes/investigation.md) | 98,304 | 1/9 | 0/9 | 0/9 | 9,084 MiB | 3.6s | 182.8s | Not tested |
| VibeForged v2 Q6_K | [Nov 12](evaluations/2026-11-12/investigation.md) | 98,304 | 5/9 | 1/9 | 0/9 | 11,684 MiB | 5.5s | 326.6s | Not retested |
| Qwen3.5-9B Q8_0 | [Nov 12](evaluations/2026-11-12/investigation.md) | 65,536 | 6/9 | 4/9 | 3/9 | 9,474 MiB | 3.3s | 91.5s | Not retested |
| Qwen3.5-9B Q8_0 | [Nov 12](evaluations/2026-11-12/investigation.md) | 98,304 | 5/9 | 3/9 | 3/9 | 9,922 MiB | 3.7s | 127.9s | Not retested |

No candidate established reliable ordinary repository reviews in that comparison.
The November 16 decision was to keep VibeForged Q4: Qwen Q5 used less VRAM but
tied its 3/9 combined score and had a slower median turn. The November 18 write
comparison above is separate and does not establish an unattended-workflow winner.
Both finish the November 16 history sequence, with content defects remaining.
The tested local summary budget/read-default/routing profile fixes are deployed;
the existing model/credentials/endpoints remain. See the dated report and
[plugin source/config notes](hermes-profile/README.md). These tests do not prove
native Discord delivery, issue-write reliability or a million-token context.
First API-call latency includes generation/cache; sampled VRAM may miss peaks.

### Historical Guided Workflow Results

The matrix below preserves historical guided workflow probes (primarily June/July
2026, with later dated retests). Its “pass” labels apply only to those guided
issue-creation probes, not the ordinary repository acceptance test above.

Timings in the matrix are centered on the minimal issue-write workflow. Use `Minimal workflow total time` for the best apples-to-apples speed comparison; detailed call timing and retry behavior stay in the per-model write-ups.

Status rule: this matrix is about whether a model works for the real Gitea issue-creation workflow. Mark a model `🔴 Fail` if it cannot complete that workflow in a usable way, even if early tool calls looked promising. Use `🟡 Mixed` only when the model can complete at least one issue-creation path but remains unreliable, incomplete, or inefficient on a follow-up workflow.

| Model | Status | Size | VRAM observed | Reported / working context | Prompt size observed | Hermes Agent behavior | Minimal issue-write test | Minimal workflow total time | Harder workflow test | Harder workflow total time | Retest after Hermes/tool updates? |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---|
| `Hermes-2-Pro-Mistral-7B.Q8_0.gguf` | 🔴 Fail | n/a | n/a | `32768` despite `--ctx-size 98304` | ~2.2k | Template exposed no tool support; did not call any tool | Failed | Failed | Failed: no tool-call path | n/a | No: 32k context ceiling remains below the Hermes target |
| `DeepHermes-3-Llama-3-8B-q8.gguf` | 🔴 Fail | n/a | ~12.6 GiB | `65536` loaded | ~1.9k | Template exposed no tool support; did not call any tool | Failed | Failed | Failed: no tool-call path | n/a | Yes: old failure was tool exposure/template related |
| `DeepSeek-V4-Flash-MTP-Q4K-Q8_0-F32.gguf` | 🔴 Fail | n/a | n/a | n/a | n/a | Current llama.cpp build cannot load this architecture | Failed: model load blocked by unsupported architecture | Failed | n/a | n/a | No: backend architecture support is the blocker |
| `DeepHermes-3-Mistral-24B-Preview-q4.gguf` | 🔴 Fail | n/a | ~12.3 GiB | `32768` despite `--ctx-size 98304` | ~2.0k | Loaded with `-ngl 30`, q4 KV; template exposed no tool support and made no MCP call | Failed | Failed | Failed: no tool-call path | n/a | No: 32k context ceiling remains |
| `Devstral-Small-2-24B-Instruct-2512-Q4_0.gguf` | 🔴 Fail | n/a | ~12.8-14.5 GiB | `65536` loaded but OOM on first task; `32768` loads but Hermes rejects it | n/a | Backend loads, but no usable Hermes Agent path on this hardware | Failed: CUDA OOM at 65k before first prompt completes | Failed | Failed: blocked by main-model 64k minimum when reduced to 32k | n/a | No: P100 VRAM is the blocker |
| `gemma-4-12B-it-QAT-Q4_0.gguf` | 🟢 Pass | ~6.5 GB | ~7.6 GiB | `65536` loaded | ~14.1k minimal; ~26.1k advanced | Tool support exposed; `skill_view` detour, recovered from bad `get_file_contents` args, then valid issue-write path | Passed: concept issue created cleanly | ~97.6s | Passed with caveats: 1 concept issue created after repo-review recovery | ~190.9s | Baseline: useful low-VRAM comparison retest |
| `gemma-4-12b-it-Q6_K.gguf` | 🟢 Pass | ~9.2 GB | ~10.4 GiB | `65536` loaded | ~14.1k minimal; ~38.2k advanced | Tool support exposed; cleaner repo-review path than Q4, completed valid issue-write flow | Passed: concept issue created cleanly | ~117.9s | Passed: 1 concept issue created after repo review | ~289.4s | Baseline: useful clean-routing comparison retest |
| `Hermes-3-Llama-3.1-8B.Q8_0.gguf` | 🔴 Fail | ~8.5 GB | n/a | n/a | ~29k | Unreliable Gitea/tool routing | Failed | Failed | Failed: bad repo routing | n/a | Yes: routing is exactly what changed in Hermes |
| `Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf` | 🔴 Fail | n/a | ~8.0 GiB | `65536` requested | ~1.9k | No tool use; text-only reply on first call | Failed | Failed | Failed: no tool-call path | n/a | Yes: retest current generic tool handling |
| `NousResearch_DeepHermes-3-Mistral-24B-Preview-Q4_K_M.gguf` | 🔴 Fail | n/a | ~12.6 GiB | `32768` despite `--ctx-size 65536` | n/a | No usable tool calls | Failed | Failed | Failed: no usable tools | n/a | No: 32k context ceiling remains |
| `NousResearch_Hermes-4-14B-Q4_K_M.gguf` | 🔴 Fail | ~9.0 GB | ~11.9 GiB | `40960`; `65536` requested, plus repeated loading/overflow instability | ~14.4k minimal; ~21k prior repo explain | Repo search worked; minimal write looped on malformed issue-write args | Failed: body missing, then issue_number missing | Failed | Failed: 40.9k context ceiling | n/a | No: usable context remains below the target |
| `NousResearch_Hermes-4-14B-Q5_K_M.gguf` | 🔴 Fail | ~10.5 GB | ~15.8 GiB | `40960`; `65536` requested triggers training-context overflow warning | ~14.3k minimal; ~21k prior repo explain | Repo search worked; minimal write looped on bad tool strategy | Failed: create_or_update_file permission error, then body missing | Failed | Failed: 40.9k context ceiling | n/a | No: context and VRAM both remain blockers |
| `NousResearch_NousCoder-14B-Q4_K_M.gguf` | 🔴 Fail | ~9.0 GB | ~14.4 GiB | `65536` worked; `81920` train max; `98304` OOM with q8 KV | ~21k | Repo search and reads worked | Failed later: bad issue args | Failed | Read worked, write failed | n/a | Maybe: schemas changed, but stop Ollama first due VRAM |
| `NousResearch_NousCoder-14B-Q5_K_M.gguf` | 🔴 Fail | ~10.5 GB | ~14.8 GiB | n/a | ~14.3k search; ~15.5k minimal | Repo search worked | Failed later: body missing | Failed | Not tested after minimal failed | n/a | Maybe: write schema could improve, but VRAM is tight |
| `NousResearch_NousCoder-14B-Q6_K.gguf` | 🔴 Fail | ~12.1 GB | ~14.1 GiB | `65536` requested; repeated loading instability before settling | ~14.5k minimal | Minimal write looped on bad issue-write args after warmup 503s | Failed: body missing | Failed | Failed: warmup 503s, then repeated body-missing loop | n/a | Low priority: schema may improve, loading remains unstable |
| `meta-llama-3.1-8b-instruct-q4_k_m.gguf` | 🔴 Fail | n/a | n/a | `65536` loaded | ~1.9k | Template exposed no tool support; did not call any tool | Failed | Failed | Failed: no tool-call path | n/a | Yes: retest current generic tool handling |
| `Qwen3-14B-Q4_K_M.gguf` | 🔴 Fail | n/a | ~14.4 GiB | `40960` despite `--ctx-size 65536` | ~14.5k | Tool support exposed; called issue_write but malformed args | Failed: malformed args | Failed | n/a | n/a | No: 40.9k context and high VRAM remain blockers |
| `Qwen3-14B.Q5_K_M.gguf` | 🔴 Fail | n/a | ~13.0 GiB | `40960`; `65536` requested triggers training-context overflow warning | ~14.5k minimal | Tool support exposed; minimal write looped on malformed issue-write args | Failed: body missing | Failed | n/a | n/a | No: 40.9k context ceiling remains |
| `Qwen3.5-9B-Q8_0.gguf` | 🟢 Pass | n/a | ~9.5 GiB | `65536` requested; minimal and harder workflows completed cleanly | ~14.7k minimal; ~34.7k advanced | Tool support exposed; valid issue-write path on minimal and harder workflows | Passed: concept issue created cleanly | ~52.3s | Passed with caveat: recovered after one `get_dir_contents` error | ~110.5s | Retested Nov 12: 3/9 combined at both contexts; see latest matrix |
| `Qwen3.6-14B-A3B-VibeForged-v2-Q4_K_M.gguf` | 🟢 Pass | n/a | ~8.8 GiB | `65536` loaded | ~14.7k minimal; ~35.5k advanced | Tool support exposed; valid issue-write path on both minimal and harder repo-review turns | Passed: concept issue created cleanly | ~69.1s | Passed: 1 concept issue created after targeted repo review | ~160.1s | Retested Nov 13 at 98k: 1/9 combined; see latest matrix |
| `Qwen3.6-14B-A3B-VibeForged-v2-Q4_K_M.gguf` (98k natural-prompt retest) | 🟡 Mixed | n/a | ~8.9 GiB (`9072MiB`) | `98304` loaded and confirmed | ~25.4k shown during failed turn | Context was not exhausted, but the model disobeyed the explicit `use Gitea MCP` route: directory-as-file errors triggered MCP cooldown, then it drifted into web, browser, `execute_code`, curl, and GitHub attempts | Not retested | n/a | Failed: 30 tool turns exhausted without returning the requested five ideas | ~3m shown before interruption | Retested Nov 12/13: ordinary-task failures remain; see latest matrix |
| `Qwen3.5-14B-A3B-Claude-Opus-Reasoning-Distilled-4.6-MXFP4_MOE.gguf` | 🟡 Mixed | n/a | ~8.9-9.2 GiB | `65536` loaded in current test; Hermes metadata guessed higher | ~14.6k minimal; ~20.3k sequential harder; ~98k older resumed path | Tool support exposed, but write reliability is weak and it drifts after repeated tool failures | Failed: repeated `body is required` on clean minimal test | Failed | Mixed: older harder path eventually passed, but same-session retest failed | ~1059.4s older pass; ~53.3s failed retest | Yes: current schemas and routing may change this result |
| `Qwen3.6-14B-A3B-VibeForged-v2-Q6_K.gguf` | 🟢 Pass | n/a | ~11.6 GiB | `98304` loaded | ~14.7k minimal; ~48k advanced | Tool support exposed; valid `mcp_gitea_issue_write`; advanced flow still over-reads but now fits | Passed: issue #10 created | ~64.9s | Passed with caveats: 1 concept issue created after 18 API calls | ~346.8s | Retested Nov 12: 0/9 combined; see latest matrix |
| `qwen2.5-coder-14b-instruct-q4_k_m.gguf` | 🔴 Fail | ~9.0 GB | n/a | `65536` loaded | ~14.5k | Did not call any tool for explicit issue-create prompt | Failed | Failed | Failed: no usable tool-call path | n/a | Yes: native/current tool handling deserves one retest |
| `qwen2.5-coder-14b-instruct-q6_k.gguf` | 🔴 Fail | ~12.1 GB | ~15.2 GiB | `65536` requested; repeated loading instability | ~14.5k | No tool use; text-only reply after repeated 503 loading failures | Failed | Failed | Failed: no usable tool-call path | n/a | No: loading instability and VRAM leave no Ollama reserve |
| `qwen2.5-coder-7b-instruct-q8_0.gguf` | 🔴 Fail | ~8.1 GB | ~8.8 GiB | `65536` requested | n/a | No confirmed MCP completion; three long model calls, then Hermes shut down | Failed | Failed | Failed: simple prompt never completed | n/a | Yes: cheap retest under the cleaned Hermes setup |

## Detailed Outcomes

### DeepHermes 3 Mistral 24B q4

This model is interesting only in the sense that it nearly fits the card while staying under about `12.3 GiB` VRAM with `-ngl 30` and q4 KV, but the backend capability report is still a hard blocker. `/props` reports `n_ctx: 32768` and `supports_tool_calls: false`, even though Hermes requested `--ctx-size 65536`.

The first attempted Hermes issue-write probe had one false start while llama.cpp was still loading: Hermes retried three times and got `HTTP 503: Loading model`. After the model settled, a fresh run completed one API call with `in=1971 out=378 total=2349 latency=153.8s`, then ended with `tool_turns=0`. So it did not reach MCP at all; it simply wrote a normal text answer.

Outcome: lighter VRAM footprint than the Q4_K_M file, but still unusable for this workflow because it advertises only 32k context and no tool-call support.

### DeepSeek V4 Flash MTP Q4K Q8_0 F32

This file is a load-time failure with the current llama.cpp image, so it never reached the Hermes workflow at all. On July 2, 2026, llama.cpp started loading `/models/DeepSeek-V4-Flash-MTP-Q4K-Q8_0-F32.gguf`, then immediately aborted with an unknown model architecture error for `deepseek4_mtp_support`. The server exited before any prompt could run, so there is no meaningful VRAM, timing, or tool-behavior result to compare against the workflow matrix.

Outcome: closed fail for the current stack because this llama.cpp build does not support the model architecture.

### Devstral Small 2 24B Q4_0

This model is now a closed fail for Hermes Agent on this machine. At the normal `65536` target, llama.cpp loaded the model and reported `n_ctx_slot = 65536`, but the first real task immediately died with CUDA OOM during inference. The relevant run showed the model loading cleanly, then failing at task start with `CUDA error: out of memory`, while `nvidia-smi` was already around `12756MiB` VRAM. That means the weights fit well enough to start, but the combination of runtime KV cache plus compute buffers did not.

To document the fallback path, the test was then repeated with both llama.cpp and Hermes Agent reduced to `32768`. That let the backend load again, and `nvidia-smi` showed about `14476MiB` VRAM in use, but Hermes Agent refused to run the model because its main-model path enforces a minimum `64000` token context. Hermes surfaced the error directly: `Model devstral-small-2-24b-q4_0 has a context window of 32,768 tokens, which is below the minimum 64,000 required by Hermes Agent.`

Outcome: there is no usable Hermes Agent path here with the current setup. At `65536`, Devstral fails at runtime with GPU memory exhaustion; at `32768`, it no longer satisfies Hermes Agent's minimum context requirement.

### Gemma 4 12B it QAT Q4_0

This run now has enough evidence to classify the Gemma 4 Q4_0 variant as a pass for both the minimal and harder target workflows. On July 2, 2026, llama.cpp loaded the model with `n_slots = 1` and `n_ctx_slot = 65536`, while `nvidia-smi` showed about `7586MiB` VRAM in use. llama.cpp also warned that `<|tool_response>` needed token-type overrides and adjusted the EOG list, but those warnings did not block the actual tool path.

The verified minimal issue-write session was `20260702_141945_e2c589`. API call `#1` used `in=14051 out=271 total=14322 latency=72.0s`, then the model took a small detour through `skill_view`, which completed in `0.05s` with `6866` characters. API call `#2` used `in=16178 out=178 total=16356 latency=16.0s cache=14302/16178 (88%)`, then `mcp_gitea_issue_write` completed successfully in `0.16s` with a `422`-character tool result. API call `#3` used `in=16615 out=171 total=16786 latency=9.4s cache=16283/16615 (98%)`, and the turn ended cleanly with `tool_turns=2` and `finish_reason=stop`.

Outcome: the minimal issue-write flow is a real pass, not a fluke. The same session also completed the harder repo-review-plus-issue workflow, but with more wobble than the Qwen winners. In the follow-up turn, API calls `#4`-`#11` consumed about `190.6s` of model time while Gemma bounced through another `skill_view` call, `mcp_gitea_get_repository_tree`, `mcp_gitea_list_issues`, two failed `mcp_gitea_get_file_contents` calls with `repo is required`, then recovered and completed `mcp_gitea_issue_write` successfully. The harder turn ended cleanly with `tool_turns=9` and `finish_reason=stop`, for about `190.9s` total including tool time. That makes Gemma 4 Q4_0 a confirmed two-step pass, though it is still slower and noisier than the best Qwen passes.

### Gemma 4 12B it Q6_K

This run now has enough evidence to classify the Gemma 4 Q6_K variant as a pass for both the minimal and harder target workflows. On July 2, 2026, llama.cpp loaded the model with `n_slots = 1` and `n_ctx_slot = 65536`, while `nvidia-smi` showed about `10406MiB` VRAM in use. llama.cpp warned that `</s>`, `<|tool_response>`, and `<eos>` needed token-type overrides, and it adjusted the EOG list, but those warnings did not block the actual tool path.

The verified minimal issue-write session was `20260702_144559_469793`. API call `#1` used `in=14070 out=230 total=14300 latency=73.6s`. API call `#2` used `in=14445 out=123 total=14568 latency=8.8s cache=14282/14445 (99%)`, API call `#3` used `in=15381 out=41 total=15422 latency=6.3s cache=14558/15381 (95%)`, and API call `#4` used `in=17277 out=171 total=17448 latency=19.0s`, after which `mcp_gitea_issue_write` completed successfully in `0.06s` with a `422`-character tool result. API call `#5` used `in=17706 out=132 total=17838 latency=10.1s cache=17374/17706 (98%)`, and the turn ended cleanly with `tool_turns=4` and `finish_reason=stop`.

Outcome: the minimal issue-write flow is a real pass, though it is slower than the Gemma Q4_0 and Qwen winners because it took a few extra reasoning hops before issuing the valid write call. The same session also completed the harder repo-review-plus-issue workflow. In the follow-up turn, API call `#6` listed issues, API call `#7` read the repository tree, API call `#8` read `sptnr.py` successfully, and API call `#9` completed `mcp_gitea_issue_write` after a much longer `167.3s` reasoning pass. API call `#10` then wrapped up the turn cleanly, for about `289.4s` total including tool time. That makes Gemma 4 Q6_K a confirmed two-step pass with better repo-read discipline than the Q4_0 variant, but at a noticeably higher total latency.

### Hermes 3 Llama 3.1 8B Q8

This model was light enough to run faster, but Gitea behavior was unreliable. It sometimes treated `search Gitea` as a web-search request, sometimes explained what Gitea is, and sometimes failed to choose the Gitea MCP tool without extra steering.

Outcome: not reliable enough for the desired MCP-first Hermes Agent workflow.

### Hermes 4 14B Q4

This model has now been directly tested on the minimal issue-write workflow, and it fails there too. On July 1, 2026, `nvidia-smi` showed about `11884MiB` VRAM in use for this Q4 run. A previous simple repo-explain run showed decent early Gitea routing, but the backend still behaves like a `40960`-context model even when Hermes requests `65536`. On July 1, 2026, Hermes also logged `Could not detect context length for model 'hermes-4-14b-q4_k_m' ... defaulting to 256,000 tokens`, which is misleading noise on top of the real backend limit.

The first attempt at the minimal issue-write prompt hit startup instability: session `20260701_151351_e642d7` got three consecutive `HTTP 503: Loading model` failures before the turn retried. On the successful retry, API call `#1` used `in=14378 out=156 total=14534 latency=84.5s`. Hermes removed one duplicate `mcp_gitea_issue_write`, then the tool failed first with `body is required` and immediately after with `issue_number is required`.

From there the run degraded into the same family of bad retries we saw elsewhere. API call `#2` used `in=14677 out=52 total=14729 latency=5.2s`, then `mcp_gitea_issue_write` failed with `body is required` again. API call `#3` used `in=14880 out=131 total=15011 latency=11.0s`, after which Hermes started reporting the MCP server as unreachable after repeated identical failures. So the minimal result is now directly proven as a failure, not just missing data.

The separate blocker is still context. `65536` did not actually work here: the backend effectively lowered or capped behavior to about `40960`, so the requested context was not honored. The earlier repo-explain behavior already suggested the same 40.9k ceiling that limits the Q5 variant.

Outcome: slightly smaller than Q5, but still unusable for this setup because the minimal issue-write workflow emits malformed issue arguments and the backend remains capped at about 40.9k context.

### Hermes 4 14B Q5

This has had the best tool behavior so far. It correctly used `mcp_gitea_search_repos` for simple Gitea prompts and produced better answers than Hermes 3 or NousCoder.

Direct llama.cpp tool-call test:

```json
{
  "name": "mcp_gitea_search_repos",
  "arguments": "{\"query\": \"sptnr\"}"
}
```

Direct llama.cpp follow-up with a fake tool result also summarized correctly when instructed not to infer extra facts. The direct endpoint was fast on small prompts, about 20-21 generated tokens/sec.

The blocker is context. `65536` did not actually work on this model: even when requested, the backend stayed at `40960`, so the higher context was not honored. Hermes Agent then errors on larger repo/debug prompts:

```text
Auxiliary compression model hermes-4-14b-q5_k_m has a context window of 40,960 tokens, which is below the minimum 64,000 required by Hermes Agent.
```

Outcome: best behavior, but not usable for larger Hermes Agent workflows unless the context problem is solved.

### Meta Llama 3.1 8B Instruct Q5_K_M

This run now has enough evidence to classify the Q5_K_M variant as a failure for the target workflow. On July 1, 2026, it loaded with about `8192MiB` VRAM in `nvidia-smi` and handled the simple `search Gitea for sptnr and explain it` prompt in a single model call. Logs show API call `#1` used `in=1850 out=155 total=2005 latency=10.8s`, and the turn ended immediately with `tool_turns=0` and a plain text response.

There was no confirmed `mcp_gitea_search_repos` completion and no other MCP activity in session `20260701_145605_379e49`. So while it was fast and light, it did not follow the required Gitea MCP workflow at all.

Outcome: quick first response and low VRAM usage, but unusable for this setup because it stayed text-only instead of calling tools.

### NousCoder 14B Q4

Recent `search Gitea for sptnr and explain it` test completed with one Gitea MCP search call. `/props` reports `n_ctx: 65536`, so this is the first 14B test in this round that satisfies Hermes Agent's 64k context requirement at the backend level. Observed VRAM was about `14444MiB` (`~14.4 GiB`).

Logs show API call #1 used `in=20855 out=334` with `latency=142.2s`; API call #2 after the tool result used `in=21724 out=494` with `latency=42.7s`. Full model time for the turn was about `184.9s`, plus the `0.1s` MCP search.

Tool routing was good: it used `mcp_gitea_search_repos` immediately and did not use Web Search. Answer quality was mixed: it over-inferred original/fork relationship, open issues/PR details, and likely Spotify API behavior from limited search metadata. It also exposed a visible thinking section in the pasted run, which may be useful for debugging but is noisy for normal use.

Repo-inspection test 1: for `let's focus on sickprodigy/sptnr, can you check over codebase for errors in syntax`, NousCoder Q4 attempted a terminal clone with `git clone http://gitea:3000/sickprodigy/sptnr.git /workspace/repos/sptnr`. That is a better plan than reading `.gitignore` or `requirements.txt`, but it triggered a HIGH security approval because the clone URL used plain HTTP. After approval, the terminal command failed with `fatal: could not create work tree dir '/workspace/repos/sptnr': Read-only file system`. Logs show that repo-inspection first model call used `in=21693 out=1297` with `latency=101.9s` before the terminal attempt.

Repo-inspection test 2: after a fresh chat/run, NousCoder Q4 used the Gitea MCP tools more directly: `mcp_gitea_get_repository_tree`, then `mcp_gitea_get_file_contents` for `sptnr.py`. This is the best repo-inspection tool selection so far. Logs show the first repo-inspection model call used `in=21718 out=1039` with `latency=86.2s`; the next model call used `in=23677 out=296` with `latency=32.1s`. The pasted UI showed the model still contemplating for many minutes after the second call, so this run may have stalled after reading the right files.

Outcome: context is the best result so far because `/props` reports the needed 65k. Speed is slower than ideal. For simple search, answer quality still over-infers. For repo inspection, planning looked better than Hermes Q4 because it tried to clone and inspect the repo instead of reading unrelated files, but the test was blocked by terminal filesystem permissions.

Issue-write test: with the tightened Gitea issue skills, NousCoder Q4 still failed to create issues because the model emitted malformed `mcp_gitea_issue_write` arguments. Hermes logged `Unrepairable tool_call arguments for mcp_gitea_issue_write` and then the MCP server returned `body is required`. The malformed call happened around `18k` total tokens, and the run ended around `27k` total tokens, so this specific failure was not caused by reaching the configured context window. This points to weak structured tool-call reliability rather than context cutoff.

### NousCoder 14B Q5

This run now has enough data to classify the Q5 variant as a failure for the target workflow. On July 1, 2026, the simple `search Gitea for sptnr and explain it` prompt succeeded in two API calls: API call `#1` used `in=14268 out=159 total=14427 latency=82.5s`, then `mcp_gitea_search_repos` completed successfully, and API call `#2` used `in=15177 out=719 total=15896 latency=54.8s`.

The minimal issue-write prompt then failed in a repeat loop. API call `#3` used `in=15534 out=462 total=15996 latency=39.7s`, after which `mcp_gitea_issue_write` failed with `body is required`. The same failure repeated on API calls `#4` and `#5`, triggering Hermes repeated-exact-failure warnings, and by API call `#6` Hermes was reporting the Gitea MCP server as temporarily unreachable after the consecutive identical failures.

Outcome: repo search works, but issue creation fails because the model keeps emitting invalid `mcp_gitea_issue_write` arguments with no usable `body`.

### NousCoder 14B Q6

This model now has enough direct evidence to classify it as a failure for the target workflow. On July 1, 2026, `nvidia-smi` showed about `14470MiB` VRAM in use during the Q6 run. The minimal issue-write test first hit repeated warmup failures: session `20260701_155149_dec0b9` logged multiple `HTTP 503: Loading model` retries before the model finally settled enough to answer.

Once it did run, API call `#1` used `in=14459 out=1055 total=15514 latency=166.4s`. Hermes removed three duplicate `mcp_gitea_issue_write` calls, then the remaining issue-write call failed with `body is required`. API call `#2` used `in=15461 out=339 total=15800 latency=31.4s`, and `mcp_gitea_issue_write` failed with `body is required` again. API call `#3` used `in=15901 out=270 total=16171 latency=25.6s`, and the same `body is required` failure repeated, triggering the repeated-exact-failure warning.

API call `#4` used `in=16322 out=264 total=16586 latency=25.4s`, after which Hermes started reporting the Gitea MCP server as unreachable after three consecutive identical failures. API call `#5` used `in=16771 out=516 total=17287 latency=49.1s`, and the turn ended as a text response with `tool_turns=4`, not a created issue. So this is no longer just a vague stall; it is a direct minimal-workflow failure with a clear invalid-arguments loop after a slow warmup.

Outcome: not a usable win. Compared with the Q4 variant, this Q6 run used similar VRAM, took longer to settle, and still failed on repeated `body is required` issue-write arguments.

### qwen2.5 Coder 14B Q6

This model now has enough evidence to classify it as a failure for the target workflow. On July 1, 2026, multiple attempts to run the simple `search Gitea for sptnr and explain it` prompt failed during model warmup with repeated `HTTP 503: Loading model` and connection errors. After another restart, one clean turn finally completed, but it ended as a plain text response with `tool_turns=0`: API call `#1` used `in=14466 out=37 total=14503 latency=78.2s`, and the model still did not call the Gitea MCP search tool.

Outcome: even after lowering context to `65536` so the model could load, it remained unusable for the Gitea issue workflow because startup was unstable and the first prompt still ended without tool use.

### qwen2.5 Coder 7B Q8_0

This run now has enough evidence to classify the model as a failure for the target workflow. On July 1, 2026, it loaded with about `8836MiB` VRAM in `nvidia-smi` and began the simple `search Gitea for sptnr and explain it` prompt. Hermes then made three long model calls: the first ran about `182s` from `14:29:10` to `14:32:12`, the second ran about `361s` from `14:32:12` to `14:38:13`, and the third ran about `626s` from `14:38:13` to `14:48:39`.

There was still no `Turn ended:` line, no confirmed `mcp_gitea_search_repos` completion, and no text response recorded for session `20260701_142907_4eef9b`. Hermes was then shut down at `14:51:36`, so the run ended after roughly `1169s` of model time without finishing even the simple prompt.

Outcome: very low VRAM use for a 7B model, but too slow and too incomplete to count as usable for the Gitea MCP workflow.

### Qwen3 14B Q5_K_M

This run now has enough evidence to classify the Q5 variant as a failure for the target workflow. On July 1, 2026, llama.cpp warned `n_ctx_seq (65536) > n_ctx_train (40960) -- possible training context overflow`, which confirms the backend is really a 40.9k-context model even though Hermes requested `65536`. `nvidia-smi` showed about `13034MiB` VRAM in use during the run.

The verified minimal issue-write session was `20260701_174243_e867f5`. API call `#1` used `in=14498 out=478 total=14976 latency=109.8s`, then `mcp_gitea_issue_write` failed with `body is required`. Hermes retried the same bad write path three more times: API call `#2` used `in=15077 out=365 total=15442 latency=27.2s`, API call `#3` used `in=15543 out=322 total=15865 latency=25.3s`, and API call `#4` used `in=16016 out=551 total=16567 latency=44.0s`. Every tool failure was still `body is required`, and after the repeated identical failures Hermes escalated to the temporary MCP backoff message that the Gitea server was unreachable after three consecutive failures.

Outcome: tool support is present, but this model is not usable for the target workflow. It carries the same 40.9k context ceiling problem seen in other borderline 14B candidates, and its minimal issue-write path degraded into a repeated `body is required` loop instead of producing a valid issue body.

### Qwen3.5 14B A3B Claude Opus Reasoning Distilled 4.6 MXFP4 MOE

This variant used noticeably less VRAM than the Qwen3.6 baseline, ranging from about `8908MiB` in the current llama.cpp run to about `9186MiB` in earlier testing. On paper that looked promising. In practice, it remains inconsistent for the Hermes + Gitea workflow.

The older evidence is still real: after a messy, overlong resumed path, this model eventually created Gitea issue `#12` and therefore proved it can complete a harder one-issue workflow at all. That older success, however, came with heavy drift, compression pressure, and very poor efficiency.

The new minimal issue-write test on July 2, 2026 was a direct failure. In session `20260702_012307_3f8b67`, API call `#1` used `in=14598 out=184 total=14782 latency=55.8s`, then `mcp_gitea_issue_write` failed with `body is required`. The model retried the same bad write path on API calls `#2`, `#3`, and `#4`, each time hitting the same `body is required` error until Hermes marked the Gitea MCP server as temporarily unreachable after three consecutive identical failures. The run then drifted into a terminal attempt that exited with code `3`, and the turn ended without creating the issue. Total model time for the failed minimal workflow was about `77.8s`.

The same-session harder retry also failed, which is important because that two-prompt sequence matches your normal test pattern. Still inside session `20260702_012307_3f8b67`, the follow-up prompt first did some sensible reads: `mcp_gitea_get_repository_tree` and `mcp_gitea_list_issues`. But once it reached `mcp_gitea_issue_write` again on API call `#9`, it fell back into the exact same `body is required` loop on API calls `#9`, `#10`, `#11`, and `#12`, then drifted into another terminal error before ending as text. That failed harder retry used about `53.1s` of model time plus about `0.1s` of tool time, or about `53.3s` total.

Outcome: this model stays `Mixed`, but the current evidence is less flattering than before. It did eventually complete an older harder path, which keeps it out of the full-fail bucket, yet it now has a confirmed clean minimal failure and a confirmed same-session harder failure in the exact sequential pattern you usually test. Compared with the 9B and VibeForged winners, its write-tool reliability is clearly weaker.

### Qwen3.5 9B Q8_0

This run now has enough evidence to classify the 9B Q8_0 variant as a pass for the minimal target workflow. On July 2, 2026, `nvidia-smi` showed about `9452MiB` VRAM in use during the run, which is a strong result for a successful issue-write path. Hermes Agent used the configured `qwen3.5-9b-q8_0` model and stayed on the Gitea MCP route end to end.

The verified minimal issue-write session was `20260702_011407_e8376c`. API call `#1` used `in=14702 out=165 total=14867 latency=46.0s`, then `mcp_gitea_issue_write` completed successfully in `0.11s` with a `422`-character tool result. API call `#2` used `in=15104 out=139 total=15243 latency=6.2s cache=14646/15104 (97%)`, and the turn ended cleanly with `tool_turns=1` and `finish_reason=stop`. There was no malformed-arguments loop, no MCP backoff spiral, and no sign of the text-only failure mode seen in weaker models.

Outcome: this is a clean minimal-workflow pass and currently the lightest successful issue-write model in the matrix. It is now a strong candidate when you want lower VRAM use and faster turnaround than the heavier 14B passes.

The same session also proved the harder repo-review-plus-issue path. In the follow-up turn, session `20260702_011407_e8376c` made API calls `#3`-`#7`: it listed issues, hit one recoverable `mcp_gitea_get_dir_contents` error, recovered with `mcp_gitea_get_repository_tree`, read a large file (`40026` chars), then completed `mcp_gitea_issue_write` successfully. The added advanced turn consumed about `110.2s` of model time plus about `0.27s` of tool time, or about `110.5s` total, and ended cleanly with `tool_turns=5`. That makes it one of the strongest overall values in the sweep, not just the lightest successful model.

### Qwen3.6 14B A3B VibeForged v2 Q4_K_M

This Q4 variant now has a confirmed clean pass on the minimal Gitea issue-write workflow. On July 1, 2026, `nvidia-smi` showed about `8796MiB` VRAM in use during the run, which is notably lighter than the Q6 sibling while still keeping proper tool behavior. `/props` reports `n_ctx: 65536`, `supports_tool_calls: true`, and `supports_object_arguments: true`, so this model clears Hermes Agent's 64k context requirement for the basic workflow.

The confirmed minimal issue-write run was session `20260701_171816_e8cc09`. API call `#1` used `in=14713 out=241 total=14954 latency=64.3s`, then `mcp_gitea_issue_write` completed successfully in `0.14s`. API call `#2` used `in=15191 out=87 total=15278 latency=4.8s cache=14657/15191 (96%)`, and the turn ended cleanly with `tool_turns=1` and `finish_reason=stop`. Unlike several earlier 14B tests, there was no duplicate-tool pruning, no `body is required`, and no MCP unreachable spiral.

Outcome: this is now a fully proven local pass. The harder repo-review-plus-issue workflow also completed in the same session. After the minimal issue-create turn, Hermes handled a follow-up high-level repo review with API calls `#3`-`#7`: `mcp_gitea_get_file_contents` for `README.md` (`23236 chars`), `mcp_gitea_get_dir_contents`, `mcp_gitea_list_issues`, then a successful `mcp_gitea_issue_write`. The added advanced turn consumed about `140.5s` of model time plus about `19.6s` of tool time, or about `160.1s` total, and ended cleanly with `tool_turns=5`. That makes this Q4 variant the current best balance of VRAM, speed, and workflow completeness in the local sweep.

The October 22, 2026 natural-prompt retest at `98304` exposed a separate regression that additional context did not solve. For `use gitea mcp, checkover sickprodigy/sick-cogs and come up with 5 new cog ideas`, the model made 30 tool calls and reached only about `25.4k/98.3k`, so neither context exhaustion nor compression caused the failure. It requested the `cogs` directory through a file-content tool repeatedly, triggered an MCP-wide cooldown, and then ignored the requested tool boundary by trying web extraction, browser automation, `execute_code`, curl, and GitHub. The turn exhausted Hermes's 30-turn ceiling without producing the five ideas. Treat prompt/tool-routing obedience as a separate model-quality gate from context size and basic structured-tool support.

### Qwen3.6 14B A3B VibeForged v2 Q6_K

This is the first model in the sweep that checks the main Hermes Agent boxes at the same time: `n_ctx: 98304`, `supports_tool_calls: true`, and a confirmed successful Gitea write. The latest reload showed `11620MiB` in `nvidia-smi`, so the observed VRAM line can now be pinned at about `11.6 GiB` for this setup. The backend `/props` report also shows `supports_tools: true` and `supports_object_arguments: true`, which lines up with the successful MCP call.

The confirmed minimal issue-write run was session `20260629_164314_624c52`. Hermes logged API call #1 as `in=14712 out=232 total=14944 latency=60.1s`, then `tool mcp_gitea_issue_write completed (0.10s, 422 chars)`, followed by API call #2 as `in=15181 out=94 total=15275 latency=4.8s cache=14656/15181 (97%)`. The turn ended cleanly with `tool_turns=1`.

This run created Gitea issue `#10` on `sickprodigy/sptnr`, so it is the first real pass for the minimal write probe rather than a near miss. After raising context to `98304`, the harder one-issue repo-review workflow also completed in session `20260629_173204_ddcf90`, but only after a lot of extra probing. Hermes first hit `HTTP 503: Loading model` three times while llama.cpp was still warming up, then on the retried turn the model made `18` API calls, repeatedly retried `mcp_gitea_get_dir_contents`, read `README.md` (`23236 chars`), fetched several smaller files, read commits, issues, and pull requests, and finally completed `mcp_gitea_issue_write` on API call `#17`. The advanced run stayed under the new `98304` ceiling and ended cleanly with `tool_turns=17`, but total model time was about `346.8s`, so context headroom solved the overflow while workflow discipline is still loose.

Outcome: current best local baseline. Minimal write test passes cleanly; advanced one-issue repo review now passes at `98304`, but inefficiently.

## Lessons Learned

- Only run the harder repo-review workflow after a model has already passed the minimal issue-write test.
- Hermes `model.context_length` and `model.max_tokens` are different knobs: `context_length` is the full input-plus-output window, while `max_tokens` caps a single response. Leaving `max_tokens` unset caused runaway decode requests; `4096` is the current workable cap.
- llama.cpp `--n-predict 512` does not reliably protect Hermes turns by itself, because Hermes can override it in the OpenAI request body.
- Direct llama.cpp tests are much faster than full Hermes Agent turns because Hermes sends larger prompts, tool schemas, history, and retry context.
- Tool behavior and context capacity are separate gates. A model with long context but weak structured tool calls is still a failure for this setup.
- A model with good tool calling but less than `64k` usable context will still break once Hermes compression or larger repo inspection enters the picture.
- `--parallel 1` matters because extra slots multiply KV-cache memory pressure.
- Lower quantization does not inherently change max context, but it can free enough VRAM for a larger KV cache.
- The strongest local balance so far is still the Qwen3.6 VibeForged pair: Q4_K_M for efficiency, Q6_K for higher-context headroom.
- Repeated `body is required` or similar write-tool loops are usually structured-argument failures, not proof that the MCP server itself is broken.
