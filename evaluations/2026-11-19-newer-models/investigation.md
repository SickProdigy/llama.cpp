# Additional models, precision and GPU decision

November 19, 2026 (America/New_York). UTC records and run IDs cross into
November 20. This is a new cohort with a fresh control, separate from the
[previous public-model comparison](../2026-11-19-public-models/investigation.md).

## Recommendation

**Gemma 4 E4B Instruct Q5_K_M is the strongest new trial candidate for the
focused Gitea profile. Keep the existing P100 for now.** Its 5.48 GB public file
passed all four read answers across two matched batches and created the correct
upstream issue, fork branch, exact commit and upstream PR in both contributions.
Both runs read all three resources back. Strict all-URL completion was 1/2:
the first answer returned the PR URL instead of the changed-file URL; the repeat
returned all three correctly. Contribution conversation times were 101.5 and
92.2 seconds. These are small capability samples, not reliability percentages.

The separate large-input check passed with 63,098 tokens in the last request,
all three distributed markers correct, a real MCP README read and the exact
heading. It took 126.0 seconds and peaked at 4,804 MiB (about 4.7 GiB), with
98,304 context loaded. The entire inert archive was checked as an exact
substring in every request. There was no compressed substitute. The sum across
two requests is 125,589 input tokens, not a 126k-token context window. This is
synthetic retrieval plus one tool read, not full-window coding validation.

Gemma's native-interface contribution created an issue and a branch, then
attempted local `patch`; the guard stopped it before execution. No commit or
PR resulted in that diagnostic. The tested recommendation therefore includes
the focused tools. Changing only the deployed model is not established as a
solution to the native multiplexed interface.

The original VibeForged backend, Hermes profile and MCP settings are restored;
the focused plugin remains optional source, not deployed. Tested settings for
a future Gemma trial are the downloaded `gemma-4-E4B-it-Q5_K_M.gguf`, alias
`gemma4-e4b-q5`, context 98304, one slot, q4 K/V, output 4096, temperature .2,
top-k 20, top-p .95, min-p .05 and repeat penalty 1. Use the existing
[focused-plugin configuration guide](../../hermes-profile/gitea-focused/README.md),
preserving native MCP discovery for its internal transport. The isolated MCP
clone includes canonical read-only `repo_read`; original write permissions are
unchanged. No normal gateway messages were sent during evaluation.

## Comparison and what was actually tested

See the [primary matrix](matrix.md), [per-run data](runs.csv),
[separate phase summaries](summary.json) and [manual read grades](manual-grades.json).
The 35 recorded tasks comprise 18 primary tasks across six files, plus 17
separately labeled publisher, repetition, native, guidance and context tasks.
Five new public files cover four untested checkpoints; Q5 and Q8 are two files
of the same Empero checkpoint. The sixth file is the fresh existing Ministral
8B Instruct control.

These are full Hermes AIAgent conversations with Discord-platform tool
selection and actual configured Gitea MCP transport, in disposable profiles.
The focused plugin is frozen at version 0.1.3. The source/schema audit verifies
identical focused Gitea schemas and runner, guard, profile-preparation and
plugin hashes. A manifest option for a larger output cap was added before any
new-cohort run; the default remains 4096 for every primary sample.

Primary conditions are temperature .2, 4096 output, q4 K/V, one slot and loaded
context 98304. All selected files loaded on the existing backend without a
fallback, driver update or image change. Reads have 180-second/16-call limits;
contributions have 300-second/20-call limits. The guard stops off-task tools,
read-only mutation attempts, wrong targets and extra writes before dispatch.
One ordinary argument correction is permitted; identical rejected retries stop.
No operator repairs arguments or supplies corrective conversation hints.

Read requests ask for SonicRatings' purpose and one new Sick-Cogs idea. The
contribution supplies one exact unused README correction and asks for upstream
issue, verified existing personal fork, feature branch, exact commit, upstream
PR, read-backs and URLs. Reuse is not fresh-fork creation credit. This measures
prescribed-edit execution, not autonomous diagnosis, implementation or testing
of a new code fix. Actual prompts, schemas, requests and responses are retained.
See the [protocol](protocol.md) for differences and adaptive decisions.

## Findings beyond the recommended candidate

- **Empero Qwen3.8 distill 9B Q5:** Grounded detailed explanation and a strictly
  complete contribution in 84.4 seconds, at 7,368 MiB. Its completed review
  claimed no moderation cog while overlooking `incidents` on develop. The
  proposed message-level automod is not itself the same as incidents; the
  whole-answer failure is the unsupported broad claim and an inconsistent file
  count. This is a community distillation in the Qwen3.5 architecture, not an
  official Qwen 9B release.
- **The same checkpoint Q8:** The 9.79 GB file also fits at 98304, peaking at
  9,922 MiB. Explanation and contribution passed; the primary review reached
  16 dispatched calls without a proposal. A 17th attempt was stopped. The
  publisher sampler completed a trivia suggestion, but Red already bundles
  trivia with categories, custom lists and leaderboards. We conservatively did
  not credit that as a useful new cog. The directory is absent from Sick-Cogs
  itself, and API/team/MCQ features could be extensions: this is an interpretive
  framework-aware novelty judgment, not an invented-directory claim.
- **LiquidAI LFM2.5 8B-A1B Q5:** Fast, but unsuitable as the main Gitea agent in
  this comparison. The primary full task put an owner-qualified path into the
  basename-only `fork_name` field and was blocked before RPC. Its publisher
  profile used the correct name but tried creating the already-existing fork,
  then reported it could not continue instead of reusing it. Neither run made
  an issue/branch/commit/PR. Reviews repeated an invalid read or switched to
  local `read_file`. A narrow metadata summary passed under publisher settings.
- **Ministral 3 8B Reasoning Q5:** Both the primary and sampler-only publisher
  contributions passed strictly (96.6/150.9 seconds). Read quality remained
  uneven: the primary explanation invented SonicPi as a source; the publisher
  explanation corrected the provider summary but inferred module purposes and
  fork-history conclusions without inspecting/comparing the relevant files.
- **Fresh Ministral 8B Instruct control:** Correct contribution resources in
  73.1 seconds, but skipped issue read-back. Its explanation again asserted
  unchanged fork contents without comparison; the review duplicated event
  scheduling/reminders already on develop. Its earlier successful batches
  remain a separate dataset, not rewritten or pooled into these results.

Publisher probes change sampler/output budgets separately: 8192 output,
300-second reads and 600-second contributions. They reuse warm backend caches;
their latency is not an isolated sampler-speed comparison. Main conversation
times exclude model loading and initial agent/MCP setup. Other home-server
services and sequential downloads remain running; these are observed workflow
timings, not isolated hardware-throughput benchmarks. GPU peaks are sampled
whole-card usage every three seconds.

## Precision and reasoning guidance

The Q5/Q8 public pair provides no demonstrated primary-workflow advantage from
the larger file in these samples. Both explain and contribute, while reviews
fail differently. This does not establish that Q8 is generally worse: there
is one primary sample per task per file, stochastic generation, and limited
publisher conversion/calibration provenance. Precision is not a new generation
of model or a guarantee of better repository judgment.

Local quantization is now authorized if needed, but none was necessary. Every
new file matches its publisher's pinned length and SHA256; no weights were
trained, converted or requantized. The formerly deferred AgentTuned checkpoint
still has only an 18.4 GB F16 public GGUF. It was rechecked, not downloaded or
scored. A recent Artemis Gemma variant was also researched; the publisher
describes compression of Google's QAT checkpoint. It was not selected or scored.
Full third-party model cards are not republished.

The Ministral reasoning template omits its default thinking guidance when a
custom system message is supplied. The original request lacked that guidance.
A separate fixed variant appended the official embedded guidance to the
existing disposable environment hint, following the publisher recommendation,
while preserving identity, tool settings and credentials. Source/variant
configuration hashes and request differences are retained. It elicited explicit
reasoning but did not fix invented module details; the full task ended after
two read calls with a statement about the next step, no writes and
`finish_reason=stop`. It was not an output-budget cutoff. The recommendation is
to leave that variant unused. Its results do not replace either earlier phase.

A non-inference template-render marker check confirmed prior reasoning content
was preserved despite a capability flag reporting otherwise. Therefore no
reasoning-template patch was made, and zero reported reasoning-token usage is
not treated as proof that the model did not reason. The original test profile
was restored byte-for-byte before Gemma's context run.

## Hardware, storage and practical limits

**Do not buy another GPU to address the failures measured here.** All five new
files fit the P100 with 98k loaded; failed fork arguments, incomplete tool
sequences and unsupported factual claims were not VRAM-allocation failures.
An upgrade could improve speed or enable different/larger weights, but an
accuracy benefit has not been demonstrated for a particular purchase.

The host is an i7-8700 with about 62.5 GiB RAM and an ASRock B365 Pro4. The P100
was observed at PCIe Gen3 x16; the second full-length board slot is x4. A mixed
second-card setup could increase usable capacity through model splitting,
without a guaranteed speedup. PSU, clearance and cooling remain unverified.
See the [hardware notes and official sources](hardware.md) for the P100/CUDA
compatibility, A4000/3090/P40 tradeoffs and why a 12 GB card is not a capacity
upgrade. No exact price recommendation is asserted without a purchasing region.

Five new files total 31.7 GiB, with approximately 150 GiB free and the 100 GiB
reserve maintained. Existing small models and useful earlier candidates are
preserved. No new file is deleted as an all-tests-fail dud: each has a correct
narrow read or a verified contribution in at least one profile. LFM remains a
narrow-helper candidate, not a recommended workflow driver. See the
[retention record](model-retention.json).

## Evidence and delivery

[Independent resource verification](verification.json),
[restoration checks](final-restoration.json), [cleanup record](cleanup.json),
[source/schema audit](comparison-controls.json) and the
[evidence archive](evidence.tar.gz) retain the basis for the conclusions.
The [manifest](evidence-manifest.json) hashes every member, and the
[archive checksum](evidence.tar.gz.sha256) covers the bundle. JSON and recorded
source hashes are validated. Credentials, private profile archives, Docker
inspections/environment dumps, unrelated repository metadata and email
addresses are excluded or redacted.

Controllers were interrupted only at confirmed idle download waits to use GPU
idle time for Gemma's native check and matched repeat; no scored task was
interrupted by an operator. All failures remain in the records. The runs
created nine upstream test issues and eight upstream PRs, left open for review;
no merges/closes/default-branch writes were performed. Upstream main remains
`84afaf401b29753b6810e4f92f253e0d28637dbf`.

Small samples of two read prompts and equivalent prescribed edits support a
trial recommendation, not general autonomous-coding reliability. The meaningful
next validation is a real small code fix under normal use, rather than assuming
more bits, longer thinking or another GPU will fix the observed behavior.
