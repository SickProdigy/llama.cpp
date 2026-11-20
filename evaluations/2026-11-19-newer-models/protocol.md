# Additional alternatives and public quantization comparison

User authorized additional public models, and local quantization if needed,
after the November 19 nine-model comparison. A tight hardware budget is assumed
from the user's reply; no hardware purchase or paid service is authorized.
User-facing dates use America/New_York; machine timestamps and run IDs use UTC.

## Candidates and comparison

Fresh Ministral 3 8B Instruct Q5 control, then public files pinned to exact Hub
revision, file length and SHA256:

- Empero Qwen3.8-9B distillation Q5_K_M (6.64 GB). This is a community
  distillation in the Qwen3.5 architecture, not an official Qwen 9B release.
- LiquidAI LFM2.5-8B-A1B Q5_K_M (6.03 GB), an untested hybrid/MoE family.
- Gemma 4 E4B Instruct Q5_K_M from Unsloth (5.48 GB), text-only testing.
- Official Ministral 3 8B Reasoning Q5_K_M (6.06 GB). It is a different
  reasoning checkpoint, not a newer release than the instruct control.
- The same Empero distillation at public Q8_0 (9.79 GB), a paired compression
  comparison. No second training run or local requantization is involved.

New files total approximately 31.7 GiB. Download sequentially directly to the
Debian server-local model disk; maintain 100 GiB free. Byte-range writes and
SHA256 reconstruct and verify publisher bytes, without weight transformation.
The public Q5/Q8 pair is preferred to unnecessary local quantization from an
already compressed source. Publisher conversion/calibration provenance may
limit causal conclusions about the precision comparison.

## Frozen primary tasks

Reuse the guarded full Hermes AIAgent Discord-platform loop and focused Gitea
plugin 0.1.3 from the retained earlier harness. Each task has a fresh profile
and conversation. Preserve native MCP discovery for internal transport; hide
the native multiplexed surface in the focused condition. Keep original live
Hermes, llama.cpp and MCP settings unchanged and restore between batches.
Hermes-Codex is separate and untouched. Do not send Discord messages.

Primary temperature 0.2, top-k 20, top-p .95, min-p .05, repeat penalty 1,
4096 output tokens, one slot, q4 K/V and loaded context 98304. Record the
actual backend/image, complete schemas, inference requests, runner hashes,
GPU samples and runtime errors. A new optional output-cap manifest parameter
is added to the runner; its default remains 4096 for every primary candidate.
This is a new dataset with a fresh control, not pooled historical results.

Unchanged ordinary read prompts:

1. `Find my SonicRatings repo and tell me what it does.`
2. `Look over sickprodigy/sick-cogs and suggest one useful new cog that isn’t already there.`

Read limits: 180 seconds / 16 model calls. Writes remain exposed so an
attempted read-only mutation is a scored intent-selection failure, stopped
before RPC. Do not silently treat a restricted read-only toolset as improved
model judgment.

Full task: inspect approved upstream `sickprodigy/nicotineplus-plugins`, verify
identity and the existing personal fork, create exactly one upstream issue,
create a fork feature branch, make one supplied exact README correction,
commit it, read back the file, open the upstream PR, read issue/PR back and
return all URLs. Reuse is not credited as creating a fresh fork. Use newly
reserved unused equivalent wording corrections, unique titles and branches.
Full limit: 300 seconds / 20 model calls. No default-branch writes, unrelated
forks, merges, closes, settings or connection changes. Upstream main baseline
must remain unchanged. All test issues/PRs remain open for inspection.

The existing guard blocks off-task tools and targets, permits one ordinary
argument correction, and blocks identical failed retries. No operator repairs
arguments or supplies corrective conversation hints.

## Separate practical diagnostics

If a primary task stops early or fails to create its PR, test its publisher
sampler separately with an 8192-token cap, 300-second reads and 600-second full
budget. These longer reasoning runs must not replace primary failures or be
pooled into primary rates. The publisher-plan records exact settings. An
all-completed but factually incorrect answer may justify a separately logged
manual diagnostic after independent grading.

Memory load failure may retry at 65536 context. A documented quantized-cache
incompatibility may retry q8 cache. Record such phases separately. Architecture,
parser or kernel incompatibility is a runtime limitation, not a model reasoning
failure; investigate before declaring a model unsuitable. Avoid blindly moving
the P100 to a CUDA-13 build that cannot target Pascal.

## Verification and retention

Independently inspect actual issue bodies, fork parent, branch, exact file,
commit, upstream head/base direction, issue reference and one-file PR diff.
Credit only writes made by that run. Separate correct resources from strict
completion including all read-backs and final URLs. Check read novelty against
actual relevant repository branches and functionality, and distinguish supported
`sptnr fork` metadata from unsupported maintainer attribution.

Retain sanitized evidence, provenance and source hashes before removing task
containers, anonymous home volumes, evidence volume and credential-bearing
snapshots. Preserve useful small models and existing candidates. Delete only
exact task-owned files demonstrated unsuitable, with a recorded reason.

## Adaptive native-interface check

After Gemma passed both initial read checks and made the correct contribution
resources (but returned the PR URL as the file URL), a full-task-only native
MCP diagnostic was added at the same 0.2 temperature, 4096 output cap and
98304 context. The primary controller was paused only at a confirmed idle
download wait with no transient backend/session, then automatically resumed.
No scored conversation was interrupted. Native schemas and the clone's added
read-only repo_read are retained; it is not a byte-identical deployed-server
configuration. No native result replaces the focused primary result.

Gemma received one fresh matched three-task repetition during a second confirmed
idle wait before Q8 finished downloading. The same prompts, sampler, cache,
context, output limit and frozen runner/plugin are used; only the fresh exact
README correction and unique resource identifiers differ. Repetition results
remain outside the primary table.

## Prepared vendor-system-guidance diagnostic

The official Ministral reasoning template has default thinking guidance that
is omitted when a custom system message is supplied. The actual Hermes request
was checked and did not contain that guidance. A separate profile can append
it to the existing environment hint, following the publisher recommendation.
This preserves Hermes's identity, tool settings and credentials, and uses the
same temperature .7 / 8192 output / 300-second read / 600-second full settings
as the sampler-only publisher phase. It can only run after the main cohort
ends; the test volume's original profile is restored in a finally block. The
production profile is never replaced. Hashes and exact request differences are
retained; this is an adaptive configuration diagnostic, not a primary score.

A non-inference `/apply-template` marker probe confirmed prior reasoning content
is preserved in the rendered prompt despite the template capability flag saying
otherwise. Absence of emitted reasoning fields is therefore not proof that
Hermes or the server discarded them. No special template patch was needed.
