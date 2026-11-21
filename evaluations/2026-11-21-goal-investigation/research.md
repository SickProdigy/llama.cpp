# Local repository-agent goal: research and experiment rationale

Goal started November 21, 2026. Work is active; this is not a completed ranking.

## What changed in the question

The desired result is an ordinary repository assistant resembling an editor
agent: infer the configured forge and owner, inspect a checkout, implement a
novel fix, run checks, and publish correctly. Previous strict MCP-only tests
remain valid transport diagnostics. Blocking every terminal attempt is not a
fair measure of coding capability when a real isolated checkout would allow
terminal execution. Earlier published fixes also contaminated repeated diagnosis.

## Primary-source findings

- [SWE-bench Verified](https://www.swebench.com/verified) distinguishes complete
  agent systems from a standardized minimal agent. It versions the scaffold
  and discloses sampling differences. Compare both model and environment, not
  leaderboard names alone.
- [mini-SWE-agent evaluation guidance](https://mini-swe-agent.com/latest/usage/swebench/)
  separates generation of candidate patches from independent execution-based
  grading, using isolated environments. A model-authored passing test alone
  is not a sufficient correctness check.
- [Anthropic agent-evaluation guidance](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)
  recommends repeated trials, inspecting outcomes and transcripts, and auditing
  grader assumptions. Unexpected valid approaches should not fail merely for
  differing from an operator's prescribed sequence.
- [Anthropic tool-design guidance](https://www.anthropic.com/research/writing-tools-for-agents)
  emphasizes meaningful tool context, clear boundaries, efficient results and
  representative held-out evaluations. Reader pagination is a measurable tool
  contract change, not a model-weight improvement.
- [Hermes tool-search evaluations](https://github.com/NousResearch/hermes-agent/tree/main/evals/tool_search)
  compare discovery enabled/disabled and record bridge calls separately from
  underlying calls. Discovery and task execution need separate diagnostics.
- [Hermes quality troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
  calls for checking the actual model/session, context pressure and available
  tools. Confirm runtime state rather than assuming persisted defaults apply
  to every open conversation.

## Preserved prior work

The existing uncommitted natural-workflow protocol, read-only HTTP probes and
focused-reader 0.1.4 patch were present at goal start. Preserve them. Their
transport/HTTP probes are not complete Hermes runs; one old-reader trial timed
out. The reader patch preserves MCP truncation/line metadata and adds a safe
continuation line; 23 focused-plugin unit checks passed here. Fresh full-Hermes
repetitions below evaluate the actual agent integration separately.

## Experiments now prepared/running

1. Full Hermes read ablations: VibeForged Q4 and FableVibes Q4, three fresh
   repetitions per cell. Source task: old versus new reader, owner policy held
   unchanged. Owner task: new reader held constant, original versus explicit
   persistent owner/automation identity. Alternate condition order by trial.
2. Qwopus owner-policy ablation: three fresh repetitions per condition, because
   that model previously selected the automation fork. Same short user request;
   owner knowledge belongs in persistent profile context, not repeated user text.
3. Credential-free local coding-capability track: clean stdlib-only checkout,
   normal Hermes terminal/file tools, no inherited issue/PR history or solution
   files, readonly container image and isolated per-trial writable workspace.
   Agent-visible smoke checks plus independent hidden behavior/regression checks.
   A real native-terminal smoke run executed the visible suite successfully.
4. After capability tests, integrate finalists with a dedicated Gitea evaluation
   repository and actual upstream issue/fork/PR publication. Keep publication
   and code behavior separately graded; clean test issues after evidence.

Use existing models first. Consider same-checkpoint precision/sampling and
context changes only as separately logged experiments. Preserve the 100 GiB
reserve, production credentials/endpoints, user-managed environment and the
separate Hermes-Codex instance. No paid service or hardware purchase is authorized.

## Community reports: useful leads, not our benchmark results

A [5080/Hermes Q4-versus-Q6 report](https://www.reddit.com/r/LocalLLM/comments/1vzgzhx/q4_k_m_vs_q6_k_as_a_toolusing_agent_engine_found/)
checks actual written files rather than trusting success claims. Its author
also discloses that sampling temperature changed with precision, so it cannot
isolate a quantization effect. We hold those conditions constant in our planned
same-checkpoint comparisons. A [separate 16 GB model report](https://www.reddit.com/r/LocalLLM/comments/1wbufw3/16gb_vram_model_test/)
uses a small coding sample and agent tasks on a different GPU/backend. Those
reported rates are leads, not transferable measurements on the P100.

The community's no-final-newline line-count defect was tested against our actual
Hermes image: both three-line inputs returned total_lines=3. Do not update or
patch the framework for a bug we cannot reproduce here. Its numbered source
format still warrants checking final file contents independently.

## Additional observations and planned controls

The live Hermes container starts at /opt/hermes with only /opt/data mounted;
there is no pre-mounted programming checkout. Prior local searches in the
agent install directory must not be interpreted as the same environment as an
editor opened in the project. The new coding arena sets both actual cwd and
terminal config to /workspace and mounts a clean per-trial project there.

A public FableVibes Q6_K file is pinned and downloading, preserving the reserve.
Compare Fable Q4/Q6 and existing VibeForged Q4/Q6 under the same coding profile;
these are precision experiments within checkpoints, not new training runs.
The publisher's generation defaults also differ from our .2 baseline; a later
sampling diagnostic must be separate from the matched primary results.

## Coding-harness preflight corrections

Initial coding attempts exposed two harness errors before any ranking was
accepted: the image's HERMES_WRITE_SAFE_ROOT pointed at /opt/data rather than
/workspace, and seeded files retained a different UID while capabilities were
dropped. Those attempts are explicitly excluded. The corrected harness runs as
UID/GID 1000, owns its isolated workspace/records volumes, and scopes file-tool
writes to /workspace. The final smoke test edits and restores an existing source
file, creates/patches/reads a new file, and runs the visible suite. Hermes's
read-before-whole-file-write protection stays enabled; the smoke respects it.
A per-trial permission assertion runs before any model API request.

## Fresh tasks and broader development behavior

[SWE-rebench's NeurIPS paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/21bec6ace947b1b58967b945c8ac0f10-Abstract-Datasets_and_Benchmarks_Track.html)
uses newly collected interactive repository tasks to reduce reliance on static,
potentially contaminated evaluations. This reinforces using a previously
unpublished booksearch response-shape defect rather than recycling an issue
whose solution our agent can read. It does not prove our checkpoint never saw
similar defensive JSON code during training.

[Scale's SWE-Bench Pro V2 announcement](https://labs.scale.com/blog/swe-bench-pro-v2)
describes a refreshed public split and network-locked evaluation protocol;
its [primary research paper](https://proceedings.mlr.press/v306/deng26f.html)
emphasizes deeper, multi-file development tasks. Our small utilities remain
development diagnostics. A real repository fix, retained conversation follow-up,
and bulk-reference coding stress test broaden coverage, but do not establish
ability to independently maintain a large application over many revisions.

## Context capacity versus useful coding context

[NVIDIA RULER](https://github.com/NVIDIA/RULER) evaluates several long-context
task types rather than treating simple recall as sufficient evidence.
[NoLiMa's primary paper](https://proceedings.mlr.press/v267/modarressi25a.html)
also tests retrieval without direct literal matching. These motivate testing an
actual code change amid substantial repository reference material, alongside
ordinary-input coding. A loaded 98,304-token window or a successful needle
lookup does not establish equally strong debugging at that length. We are not
reporting RULER/NoLiMa scores for our models; these sources inform test design.

## Checkpoint identity and training claims

The [VibeForged publisher card](https://huggingface.co/tvall43/Qwen3.6-14B-A3B-VibeForged-v2-GGUF)
describes a pruned MoE subsequently trained on coding/tool-oriented traces.
The [FableVibes card](https://huggingface.co/tvall43/Qwen3.6-14B-A3B-FableVibes)
also describes a pruned base, with reasoning and tool/coding data used for
recovery. These are publisher descriptions, not independent performance
verification. They explain why checkpoint specialization is a plausible lead,
but do not establish superior repository-agent reliability in our setup.

The misleading local filename `Qwen3.8-9B-Q5_K_M.gguf` belongs to
[Empero's community distillation](https://huggingface.co/empero-ai/Qwen3.8-9B-Distill-GGUF),
not an official stock Qwen release. The earlier comparison already documented
this; initial commentary in this goal mislabeled it and was corrected. Both its
live hash and the actual stock Qwen3.5 Q5 hash match their earlier verified
publisher downloads. The stock file is now a separate control, so derivative
results are not credited to unmodified Qwen.


## Existing different-family control

The [GPT-OSS publisher card](https://huggingface.co/openai/gpt-oss-20b/blob/main/README.md)
reports a 16 GB memory target for its native MXFP4 weights; the
[llama.cpp maintainer announcement](https://github.com/ggml-org/llama.cpp/discussions/15095)
confirms native MXFP4 support. Neither establishes P100 latency or 98K agent
reliability. The corresponding already-retained ggml-org GGUF has verified
provenance; revisit it under native repository coding instead of treating old
MCP review probes as a definitive novel-coding result. Measure the actual local
configuration. Its file exceeds the original approximate 8 GB preference, so
report that tradeoff even if it fits GPU memory. No additional download needed.


## Cache precision diagnostic

The [official llama.cpp server reference](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
exposes independent K/V cache types including f16 and q4_0; the installed
binary's help confirms both. That makes an existing-weight cache-only launch
comparison possible without quantizing or downloading another weight file.
Record actual memory and code outcomes. These unseeded, single-session-per-
condition comparisons are exploratory; different code outcomes do not by
themselves establish a causal cache-precision effect. Never treat a failure to
load within memory as a failed reasoning attempt.


## Observed GPT-OSS Harmony failures

The durable GPT-OSS trial loaded normally at native 131,072 context (~12,572 MiB
GPU memory), but llama.cpp b12464 rejected a generated header placing
`functions.terminal` in a channel position. It returned an HTTP/SSE 500 about
peg-native format, which Hermes retried as provider unavailability. This is
neither a measured CUDA OOM nor proof that the code patch itself is incorrect.
The [related upstream report](https://github.com/ggml-org/llama.cpp/issues/27720)
used the identical GGUF hash. Its maintainer traced that reporter's failures to
dropped reasoning history; our actual outgoing assistant messages preserve
nonempty reasoning_content, so that explanation does not automatically apply.
A [different parser fix](https://github.com/ggml-org/llama.cpp/pull/31556) handles
an extra constraint after a final channel. It does not establish that updating
will fix our malformed tool-recipient-as-channel output. Preserve the raw
failure and test serving/sampling changes separately before rejecting the file
or claiming a general backend fix. No parser repair or runtime update has been
applied to this cohort.

### Request overrides must be verified in the deployed revision

The tempting GPT-OSS `grammar_lazy: false` request override is ineffective here.
The [deployed server source](https://github.com/ggml-org/llama.cpp/blob/d3c3e242c/tools/server/server-common.cpp)
erases that request field before applying the chat session. The
[matching GPT-OSS parser](https://github.com/ggml-org/llama.cpp/blob/d3c3e242c/common/parsers/gpt-oss.cpp)
selects lazy grammar for automatic tool choice and recognizes valid recipient
headers as triggers. Our malformed recipient-as-channel header can bypass those
triggers. That is a plausible mechanism, not a completed causal experiment.
Forcing required tool choice would also change normal final-answer behavior, so
it is not silently substituted into the primary comparison.

### Preserve Pascal compatibility when changing the runtime

[NVIDIA CUDA 13 release notes](https://docs.nvidia.com/cuda/archive/13.0.0/cuda-toolkit-release-notes/index.html)
remove offline compilation and library support for Pascal. A newer llama.cpp
source revision therefore does not justify blindly replacing this P100 runtime
with an arbitrary newer CUDA image. Any experimental build must retain a
compatible toolkit/architecture target and be tested separately from production.
No runtime update has been applied as a presumed cure for the model's header
errors.

### Publisher guidance for the larger existing control

The [Qwen3.6 35B model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
separates precise-coding sampling from general thinking and instruct settings.
It also describes historical thinking preservation for agent use. The
prepared 35B offload configuration uses that coding sampler and explicitly
preserves thinking; the actual GGUF template supports the option. This is a
separate practical profile, so any benefit cannot be attributed solely to
model size or to offloading.

### Avoid judging every model under one universal sampler

[OpenAI's gpt-oss reference README](https://github.com/openai/gpt-oss/blob/main/README.md)
recommends temperature 1.0 and top-p 1.0. Our matched .2 baseline is intentionally
held constant, but cannot by itself answer which practical configuration is
best. A separate complete-workflow diagnostic uses the reference sampler with
low reasoning effort. It preserves reasoning messages and uses the unchanged
parser; no tool-argument repairs or task-specific patch hints are introduced.


## Additional external evaluation review (November 21, during new cohort)

[Local Agent Bench](https://github.com/localagentbench/Localagentbench) publishes
100 mock-MCP tasks, repeated trials, hardware tiers, and raw traces. Its protocol
fixes the engine version, reports context use, and separates incompatible runs.
Useful lessons: pin the complete stack, inspect outcome evidence and measure
variance. Its MCP-only mock battery does not measure a real repository patch,
published fork bytes, large-context coding, or our P100 serving stack; its
leaderboard is a candidate source rather than our model ranking.

[Hermes's own tool-performance harness](https://github.com/NousResearch/hermes-agent/blob/main/evals/toolperf_abeval/README.md)
uses environment traps and trace-derived measures for tool-layer changes. It
explicitly warns that tiny success-rate differences need run-by-run inspection.
This supports excluding confirmed startup/fixture defects, preserving negative
model runs, and distinguishing reduced tool waste from actual code correctness.

## New Hermes-trained model lead

[The Qwen3.8 27B adapter publisher](https://huggingface.co/harness-hub/Qwen3.8-27B-hermes-adapted)
reports an RL-trained Hermes adapter, with per-task evaluation trajectories.
Training/evaluation use thinking off, temperature .8/top-p1 and BF16/vLLM; the
publisher discloses losses as well as gains and different context behavior.
This is a better candidate rationale than model-name popularity, but neither
the measured gains nor statistical evidence transfers automatically to GGUF.

[NetProjects' merged public GGUF](https://huggingface.co/netprojects/Qwen3.8-27B-hermes-adapted-GGUF)
provides an IQ3_XXS file small enough for a measured P100 attempt and documents
its source revisions and limited conversion checks. Its lower-precision files
are made from a Q8 base with an importance matrix; they are not the publisher's
BF16 evaluation. We use the existing public file, without local quantization,
MTP, or a vision projector. Download pinned revision
`6a786a26437f9210d5da0954208c7335ee0a55e1`, 11,637,692,064 bytes, expected SHA-256
`390a54c26ed8fc42a558f073e5745b7c0c1922086bbcc07e2e6357a7b527c345`.
The downloader checks the 100 GiB reserve and verifies the entire file before
any model inference. Loading, speed, and task correctness remain unmeasured
until the separately labeled extension runs.


## Multi-turn state and intermediate effects

[BFCL's multi-turn methodology](https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html)
distinguishes tool-call syntax from state and response outcomes across turns.
This motivates verifying actual issue/branch/PR state and retained followups,
while accepting different valid solving sequences. We do not import its
leaderboard scores or report a partial local suite as a BFCL result.

[CAREFUL-Bench](https://arxiv.org/abs/2611.02978), a November 2026 preprint,
argues that final-state-only scoring can hide redundant or unwanted intermediate
effects. Our inference is to preserve the entire MCP trace, distinguish rejected
requests from applied mutations, and audit publication direction and scope.
The scoped gateway prevents specified writes; that protection is not evidence
that an unscoped model would never request an unwanted operation. No new user
approval requirement is inferred from this paper for already authorized tests.

[Terminal-Bench](https://www.tbench.ai/) presents agent/model combinations and
uncertainty, rather than treating a model name as the entire evaluated system.
Our ordinary and bulk booksearch sessions are different input conditions, not
two interchangeable IID repetitions. API sessions supply two fresh attempts
on a second task, but a handful of tasks still cannot establish an unattended
reliability percentage. The model, quant, backend, native template, sampler,
context, tools, policy, test environment and budgets all belong in the result.


## Compression replay: investigate the caller as well as the model

The local 35B bulk trace has a provider-confirmed 119,824-token request against
a 98,304-token window. It contains the original large user/reference packet and
a restated copy after a handoff. The installed compactor's deduplication checks
message UIDs; the original direct-SDK harness has no persistence store and its
user rows lack those UIDs. A no-inference native method control reproduces two
copies without a UID and one with it; a native SDK/store mock verifies that
normal persistence supplies the ID. This limits model-only conclusions from
the affected run, while preserving independently observed code failures.

[Upstream oversized-user reports](https://github.com/NousResearch/hermes-agent/issues/145195)
and [restatement reports](https://github.com/NousResearch/hermes-agent/issues/131104)
describe related compression hazards. They are not identical reproductions of
our SDK caller. The [linked display PR](https://github.com/NousResearch/hermes-agent/pull/132466)
explicitly leaves model-facing history unchanged; its existence does not prove
a runtime update fixes our wire request. We instead test normal persistence
and then short-active-request/history-reference packaging in separate controls,
with unchanged source/task/model settings and all original failures retained.


The exact carrier layout matters: the captured oversized request's summary sits
on an assistant tool-call row. Extending the native replay control to that shape
shows two copies even with a UID. The conservative leading-tool-flow fallback
restores the old protected head when moving the carrier would split tool flow.
Thus normal persistence aligns the caller and enables some deduplication; it
is not a demonstrated complete fix for this actual edge. Both fixed 35B
persistence/packaging controls remain necessary, with outcomes still pending.

## Context work should preserve task performance

[Anthropic's context-engineering account](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
recommends retrieving files on demand, preserving decisions and unresolved work
through compaction, and limiting redundant tool output. This supports the real
checkout and focused readers; it does not justify stuffing every repository
into a larger window. Our bulk packet is a stress condition, not the recommended
ordinary workflow. Its history-packaging control keeps the same reference and
current task while changing whether the large reference is the active request.

[Hermes's current developer documentation](https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching)
separately describes gateway hygiene and in-loop compaction, with usage anchors,
reactive overflow handling and bounded retries. The programmatic test exercises
the native in-loop SDK, not every gateway lifecycle path. Current online docs
can describe a newer revision than the pinned installed image: the recorded
runtime SHA and native replay controls establish what was actually exercised.
A current documentation feature is not evidence that our older binary has it.

## Remaining gap: natural context growth across dependent requests

Two recent preprints sharpen a limitation of our tests:

- [CompactionBench, primary manuscript](https://www.preprints.org/manuscript/202611.0780)
  constructs persistent repository sessions from predetermined successive
  requirements, with executable checks after evolving the code. Its authors
  distinguish front-loaded padding from continuing context growth and track
  task accuracy, token cost and completion time together. That is a better
  eventual long-session gate than merely loading a large window. We have not
  run their benchmark or implemented APEC; their cloud-model findings are not
  P100 performance measurements. The manuscript is explicitly a preprint.
- [CompAct-Bench v1](https://arxiv.org/abs/2611.25673v1), submitted November 19,
  evaluates compaction by continuing successful trajectories after a controlled
  compaction boundary. Its abstract reports task-state distortion as well as
  omitted information, motivating checks that unresolved work has not become
  a falsely claimed success. We reviewed its stated method, not independently
  reproduced its results.

Our bulk-reference and seeded-history controls diagnose input packaging and
native replay. They do not simulate a natural series of dependent code changes
across repeated compactions. The README followup is also too short to establish
that ability. Retain this limit in the recommendation. A candidate first needs
credible ordinary task results before allocating a much longer development
sequence; these sources do not justify endless additional cohorts when basic
fixes remain incomplete.

## Speed work should retain correctness evidence

The [speculative-decoding guide at the tested source revision](https://github.com/ggml-org/llama.cpp/blob/d3c3e242c16b8cbf51400fad410cd69b22d64f35/docs/speculative.md)
lists MTP and draftless methods and provides an end-to-end benchmark pointer.
It also distinguishes synthetic acceptance, whose output is not valid target
model output, from normal verification. Our trials use ordinary decoding;
loaded MTP tensors alone are not enabled speculation. A future acceleration
study needs measured memory, acceptance, tool behavior and correctness, not
only a displayed token rate. [Issue #25618](https://github.com/ggml-org/llama.cpp/issues/25618)
contains quantized-output divergence reports from other configurations; we
have not reproduced them on the P100 or concluded that this build is affected.
No additional speculative-inference cohort is included here.
