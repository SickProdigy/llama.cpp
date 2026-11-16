# FableVibes versus refreshed VibeForged control — November 13, 2026

Dates in the title use America/New_York; raw logs use UTC. Both use the downloaded
Q4_K_M weights at 98,304 context on the 16 GiB Tesla P100. No training, issue writes,
commits or pushes were performed. The original runtime is restored after testing.

## Results

| Model · 98,304 context | Gitea used | GitHub attempted | Routing pass | Content pass | Both | Timeout | Median turn |
|---|---:|---:|---:|---:|---:|---:|---:|
| VibeForged v2 Q4_K_M control | 3/9 | 7/9 | 2/9 | 1/9 | 1/9 | 1 | 139.2s |
| FableVibes Q4_K_M | 2/9 | 8/9 | 1/9 | 0/9 | 0/9 | 1 | 182.8s |

Each row is three fresh sessions for each fixed prompt. Routing requires a
successful configured Gitea repository operation and no explicit GitHub attempt;
content is graded independently. A completed turn alone is not a pass. Partial
answers have useful content with material grounding, count or novelty defects.
Manual notes, complete answers, tool/error counts, tokens and first tools are
in [runs.csv](runs.csv) and [the sanitized evidence archive](evidence.tar.gz).

## Recommendation

Keep the current VibeForged deployment for now. FableVibes did not improve these
repository tasks under the matched existing profile: no fresh content pass,
frequent GitHub routing, incorrect repository inventories and overlapping cog
proposals. VibeForged also remains unreliable; its one combined pass in nine
is not a production-readiness result. These small task-specific samples do not
rank general model intelligence or prove that a different tuning cannot help.
A newer-base fine-tune would need the same held-out routing and grounded-content
evaluation before replacing the current model.

## Why a new control

The deployed llama.cpp build changed from b12282-aa75ff323 in the previous sweep
to b12316-5d4c8eeb2, with a different backend image ID. Hermes and Gitea MCP image
IDs match the earlier evaluation. The old scores therefore remain historical;
this comparison reruns VibeForged on the current pinned backend image using the
same frozen live profile as FableVibes. No claims of statistical significance
are made from these small sequential stochastic samples.

## Method

- Full shipped AIAgent conversation/tool/compression loop, CLI platform selection,
  root in disposable exact-image containers. Native Discord/API conversation
  parity is not established by this harness. Automatic CLI coding guidance is
  retained uniformly. Session history and session DBs are absent in fresh runs;
  the frozen memory directory is empty. Normal SOUL/skills/plugins load, while
  automatic background review is disabled. Explicit model-driven skill edits
  can occur only inside that disposable profile.
- One slot, all GPU layers, q4_0 K/V, main output cap 4,096, 30 iterations,
  external 600-second turn limit with no model-visible wrap-up hint. The watchdog
  requires a running container and a fresh scored-turn marker before acting.
- Same temperature 1.0, top-k20, top-p0.95, min-p0.05, repeat penalty1 and random
  seed setting. Properties are asserted before every run. Each checkpoint keeps
  its native chat template (these were verified byte-identical); alias/template differences are recorded rather than
  pretending this is blinded. Model identity is visible in the system prompt.
- Same tool configuration: Gitea deferred behind discovery, connection management
  exposed, general web/terminal/code access retained. Known forge writes and
  connection mutations are recorded and blocked. No routing/corrective hints
  are appended to the user prompts during scored runs.
- Backend `--n-predict 512` remains the original default for both. The known
  uncapped auxiliary-summary path can therefore still truncate summaries. This
  measures the existing profile, not a claim that the runtime budget defect was
  repaired. Main requests explicitly specify 4,096.
- The backend cache may persist between sessions for a model. Token/cache counters
  and first-call latency are recorded; elapsed times include different workflows
  and are not isolated cold-start or raw throughput benchmarks. Auxiliary and
  interrupted-stream usage may be absent from main-loop counters.

The unchanged user prompts are:

1. `Find my SonicRatings repo and tell me what it does.`
2. `Look over sickprodigy/sick-cogs and suggest one useful new cog that isn’t already there.`
3. `Review sickprodigy/sick-cogs and suggest five useful new cogs that aren’t already there. Explain why each would fit.`

Separate fixture verification found the same Sick-Cogs main/develop tree SHAs and
SonicRatings README blob as the earlier evaluation. The 48-cog develop catalog
can therefore be reused. Repository renaming from sptnr was handled once in the
previous protocol; this run does not silently change fixtures. Grounding and
novelty checks use main, active develop and relevant Red core features, with
peripheral mistakes distinguished from defects in the primary proposal.

## Runtime measurements

- VibeForged v2 Q4_K_M control: sampled peak 9084 MiB; median first API-call latency 4.2s (9 recorded fresh runs). Five-second samples can miss transient peaks.
- FableVibes Q4_K_M: sampled peak 9084 MiB; median first API-call latency 3.6s (9 recorded fresh runs). Five-second samples can miss transient peaks.

## Separate history sequences

**VibeForged v2 Q4_K_M control:** Fail (sequence). Turn1 157.4s Pass content: source-consistent provider/rating/playlist overview and issue reads; double-fork history phrasing peripheral. Turn2 204.6s Partial: fiat conversion is a distinct useful gap, but falsely describes Red metadata as load_extensions and init as just imports, suggests requirements.txt instead of normal info.json dependency metadata. Turn3 97.9s failed context-too-long; no five proposals, repeated summary failure. No GitHub across sequence; accumulated-context failure rather than routing drift.

**FableVibes Q4_K_M:** Fail (sequence). Turn1 58.1s content Pass: correct external-provider to personal Subsonic/Navidrome star-sync overview and companion playlists, but GitHub routing. Turn2 117.1s Fail: generic music playback/queues/volume overlaps Red Audio without distinct custom scope; invents Movies announcement, Donate music and treats separate SonicRatings project as this repository integration. Turn3 205.6s Fail: context-too-long, no five ideas; repeated truncated auxiliary summaries and no completed compression. Sequence380.8s, three GitHub attempts, zero successful Gitea repository operations. CLI harness only.

History turn times/counters and exact answers are retained in
[history-turns.csv](history-turns.csv). Previous context is provided only by the
normal full-agent conversation history; no manual corrections are inserted.

## Evidence and limitations

The archive retains actual request bodies (including system prompts/tool schemas),
underlying calls/results, final answers, discovery/surface/properties, compression
telemetry, backend logs, GPU samples, manual grades and reproducer scripts.
[evidence-manifest.json](evidence-manifest.json) lists hashes. Raw Docker inspections,
private snapshots, auth stores and credential values are excluded/redacted.
The scripts require a fresh private profile and this workspace's Docker resources;
they are an operational record, not a portable one-command benchmark.

Current primary references for overlap checks include Red's
[Cleanup](https://docs.discord.red/en/latest/cog_guides/cleanup.html),
[CustomCommands](https://docs.discord.red/en/stable/cog_guides/customcommands.html)
and [Core](https://docs.discord.red/en/stable/cog_guides/core.html) guides.
OpenWeather's [current-weather documentation](https://openweathermap.org/api/current)
requires `appid`, contrary to an explicit no-key claim in a control answer.
Other fixture/cog source excerpts are retained in the
[earlier grading evidence](../2026-11-12/grading-evidence.json), at the unchanged refs.

Restoration is verified through original container/image/environment/command/port/
mount comparisons, source configuration and credential hashes, backend health and
properties, native gateway process presence, and authenticated Gitea reads as the
expected `hermes-agent` service account. Final fixture refs are checked for drift.
Temporary evaluation resources and private snapshots are removed after sanitized
export verification. No change was made to hermes-codex.

A [November 16 grading correction](grading-corrections.md) fixes one GameRoom
capability statement in the manual notes; aggregate scores are unchanged.
