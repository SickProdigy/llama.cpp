# Repaired Hermes profile and Qwen9B Q5 comparison — November 16, 2026

## Protocol and results

The user requested an approximately 8-GB model file, leaving room for a large
context on the 16-GiB P100. The new Qwen3.5-9B Q5_K_M weights are 6,577,841,376
bytes; the file SHA-256 was checked against its publisher's Hugging Face LFS OID.
Both models run at 98,304 context on the same pinned llama.cpp b12407-e574a17b0
image and original Hermes image. The backend had already updated before this
task; this evaluation did not upgrade it.

| Model / repaired Discord agent profile | Routing | Content | Both | GitHub attempted | Timeouts | Median turn |
|---|---:|---:|---:|---:|---:|---:|
| VibeForged v2 Q4_K_M | 6/9 | 3/9 | 3/9 | 3/9 | 0 | 63.2s |
| Qwen3.5-9B Q5_K_M | 6/9 | 4/9 | 3/9 | 3/9 | 0 | 100.7s |

Each model receives three fresh repetitions of each unchanged user prompt:

1. `Find my SonicRatings repo and tell me what it does.`
2. `Look over sickprodigy/sick-cogs and suggest one useful new cog that isn’t already there.`
3. `Review sickprodigy/sick-cogs and suggest five useful new cogs that aren’t already there. Explain why each would fit.`

A separate sequence sends the same three prompts with normal accumulated
conversation history. Read-only forge guards block known write methods and
connection mutations; local scratch/code/terminal and external web tools remain
available. No corrective user hints are added during scored turns. Complete
model-facing requests, tool calls/results, answers and manual grade notes are
retained in the sanitized archive. Passing requires both a successful configured
Gitea repository operation with no GitHub attempt, and a complete grounded
answer meeting the requested count and novelty. Useful but materially defective
answers are Partial. Completion flags alone are insufficient.

These use the full shipped AIAgent loop with **Discord platform selection**,
normal SOUL/skills/plugins, and its platform-specific prompt posture, inside
disposable exact-image containers. No Discord messages are sent. Native gateway
transport/delivery and an existing live session are not tested. Previous CLI
scores used automatic coding guidance; do not pool them with this experiment or
attribute any difference to a single repair. This comparison changes the profile
and platform as a bundle; targeted preflights validate individual mechanisms.

## Interpretation and decision

Keep VibeForged Q4 as the live model for now. Both models pass routing and
content together in 3/9 fresh turns. Qwen has one more content-only pass (4/9
versus 3/9), but more outright content failures (four versus two); VibeForged has
four Partial answers versus Qwen's one. Neither is established as reliable for
open-ended repository novelty reviews. VibeForged's median turn is 63.2s versus
Qwen's 100.7s. These workflows differ, so this is not a pure decode benchmark.

Qwen Q5 meets the memory objective: its 6.58-GB model file loaded 98,304 context
at 7,348 MiB and peaked at 7,472 MiB in five-second samples, versus VibeForged's
9,028 MiB loaded / 9,082 MiB sampled peak. Keep the verified download available
for lower-memory trials; there is no demonstrated workflow-quality reason to
replace the current model. No larger context is claimed or configured.

Both models now finish all three history turns without a context-too-long
failure, but neither history sequence is fully source-correct. No natural
history compression was triggered, so this is not proof that all long-session
summary quality is solved. The separate real compressor preflight demonstrates
that the local output-budget override works beyond 512 tokens.

This is not a controlled before/after fine-tuning experiment: the models have
different architectures, weights, quantization and native templates. The result
does not establish that community fine-tuning is better or worse than vendor
post-training. Earlier CLI scores also differ in platform, backend and profile.
The strongest mechanism result is concrete: models emitted with_lines themselves
on only 5/25 (VibeForged) and 3/23 (Qwen) file calls, while all 48 effective dispatches
had readable, finite line arguments after the native hook. These counts include
failed path/cooldown calls; they do not mean 48 successful file reads. Wrong paths,
wrong forge choices, repeated retries, and incorrect novelty/fit claims remain.

Further work should target verified branch/catalog reasoning and a wider held-out
set of actual user tasks before downloading or training many more checkpoints.
The fixed three-prompt benchmark is intentionally small and should not become
training data for claims of generalization on these same prompts.

## Deployed profile repairs

- The compression task alone supplies `extra_body.max_tokens: 8192` and
  `chat_template_kwargs.enable_thinking: false` through the existing auxiliary
  configuration path. Ordinary agent requests retain max_tokens 4,096; the
  backend default remains 512. This targets this local Qwen-compatible backend,
  not arbitrary external-provider semantics.
- Gitea schemas are direct (`tools.tool_search.enabled: off`). Connection
  administration is disabled in the normal agent. Public and private owner
  repositories default to the configured Gitea source; external research still
  has web access.
- Environment/skill examples use the actual registered
  `mcp__mcp_gitea_hermes__` namespace. The repository-management skill no longer
  teaches speculative multi-encoding/gzip decoding, and its fabricated tool
  inventory is replaced with the verified current surface.
- The local `gitea-readable-defaults` plugin uses the supported `pre_tool_call`
  modify hook to default omitted text-read arguments to `with_lines: true` and
  a 160-line excerpt. Explicit raw reads/ranges and binary paths are preserved.
  Model-emitted and effective dispatch arguments are retained separately; the
  model still has to choose valid paths and refs.

## Preliminary diagnostics and protocol correction

Before final scoring, three fresh VibeForged lookup turns used the repaired
configuration with readable-file guidance only. One failed without an explanation,
two produced partially correct explanations. The third omitted the readable flag
and returned to base64 decoding. The host batch scheduler was paused while that
turn finished; no diagnostic turn was interrupted. The remaining preliminary
batch was canceled with restoration verified. All three turns, requests and
logs are retained under `diagnostics/` in the archive and are excluded from the
paired scores. This prompted the native default-argument plugin and its tests;
no diagnostic outcome was silently replaced or counted as a final repetition.

## Targeted preflight

A real `ContextCompressor._call_summary_llm` call received 60 synthetic numbered
project/port facts. The captured request used the compression-only 8,192 cap
and disabled thinking. It finished in 56.9 seconds, retained all 60 project IDs
and ports, and the backend recorded **1,731 generated tokens**, exceeding the old
512-token default. This proves the override reaches the actual summary path;
it does not guarantee arbitrary long-history summary quality.

Four plugin behavior tests cover omitted flags, preserved raw/binary/other tools,
explicit ranges and invalid start lines. The native plugin loader and hook
dispatch were then exercised: a call omitting flags became UTF-8 lines 1–160,
while an explicit raw call was unchanged. A real configured Gitea file read
also returned readable lines 1–24. The actual
Discord AIAgent surface contained 25 direct Gitea schemas and no
manage_connections tool. The matching repository fixtures and authenticated
service principal were reverified before scoring. Preflight request/schema/
source-output evidence and backend timings are in the archive.

## Resource and history measurements

- VibeForged v2 Q4_K_M: sampled peak 9,082 MiB; median first API-call latency 3.3s.
- Qwen3.5-9B Q5_K_M: sampled peak 7,472 MiB; median first API-call latency 5.2s.

**VibeForged v2 Q4_K_M history:** Fail (sequence). Turn1 80.7s Partial: correct SonicRatings core but unsupported rating-range processing claim. Turn2 147.2s Fail: localhost webpage server presented as user/Discord-accessible and Python built-in ahttp.Server invented; central implementation/access assumptions invalid. Turn3 159.8s Partial: webhook receiver, embed authoring, local calculator, wiki and bot telemetry have useful cores, but existing-webhook/Last.fm-import and bot-monitoring fit claims are fabricated, Wolfram math capability not distinguished. All3 completedTrue,28 successful Gitea repository operations,zero GitHub,one tool error. Total387.7s; no compression triggered and no summary-truncation/context-too-long failure, so completion is not proof of natural-history compaction quality.

**Qwen3.5-9B Q5_K_M history:** Partial (sequence). Turn1 37.7s Pass: correct SonicRatings purpose/providers/modes and companion playlists; fork wording peripheral. Turn2 135.3s Partial: generic arbitrary-AppID Steam feeds can add scope beyond per-game cogs, but claims no Steam announcement integration despite Ark/DayZ/Icarus/etc and assumes private-beta news via API auth without validation. Turn3 72.2s Partial: generic Steam, anime/manga, weather, donation/bounty economy and lyrics/theory have potential new scopes, but repeats Steam absence and incorrectly says Navidrome handles music-library ratings, mixing prior SonicRatings context. All3 completedTrue,seven successful Gitea repo operations,zero GitHub,one tool error. Total245.2s; no compression triggered and no truncation/context-too-long failure.


Five-second GPU samples can miss transients. First API-call latency includes
generation and may use prompt cache; it is not first-token latency or a pure
throughput comparison. Native checkpoint chat templates are preserved, and
model identity remains visible. Both use matched temperature 1, top-k 20,
top-p 0.95, min-p 0.05, repeat penalty 1, q4 K/V, one slot, 30 iterations and a
600-second external limit per turn. Fresh profiles have no session databases or
conversation history and an empty memory directory. Background review is off.

## Evidence and operational outcome

- [Fresh run metrics and manual grades](runs.csv)
- [Separate history turns](history-turns.csv)
- [Aggregate metrics](aggregate.json)
- [Sanitized evidence archive](evidence.tar.gz) and [member checksums](evidence-manifest.json)

Private Docker inspections, raw profile snapshots, auth stores and credential
values are excluded or redacted. Harness scripts are an operational record
requiring this workspace's Docker resources and a fresh private profile.
Original containers/images/configuration were restored and verified before the
live repair. The tested profile changes and native plugin were then applied to
`hermes-agent`, retaining its VibeForged alias, 98,304 context, 4,096 main cap,
credentials, endpoints, SOUL and Sick-Cogs skill. Post-restart native-hook and
authenticated Gitea checks passed as `hermes-agent`, with unchanged fixture refs.
Container identities/images/environment/ports/mounts remain unchanged.

A private original-config/Gitea-skill rollback backup is retained at
`hermes-agent/data/backups/2026-11-16-profile-repair/` (directories 0700,
files 0600, owner matches the existing configuration). It is not exported.
Temporary test containers/volume and host private snapshots are removed after
sanitized export verification. No change was made to hermes-codex. The plugin's
[maintainable source and installation notes](../../hermes-profile/README.md) and
[final verification](verification.json) accompany this report. Live gateway
process presence is checked; actual Discord delivery remains untested.

The earlier comparison has a [grading erratum](../2026-11-13-fablevibes/grading-corrections.md)
correcting one GameRoom capability note without changing aggregate scores.
