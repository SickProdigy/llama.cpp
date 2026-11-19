# Public GGUF comparison, November 19, 2026

This comparison downloads existing public model files, pins the publisher's
revision and verifies file length and SHA256. It performs no weight training,
conversion or quantization. One candidate is downloaded at a time, with a
100 GiB free-space reserve. Existing small task models and close agent
candidates are preserved.

## Cohort

- VibeForged v2 Q4 and FableVibes Q4: fresh controls from the existing files.
- Ornith 1.5 9B uncensored Q5: the variant identified in the community Hermes report.
- Ministral 3 8B Instruct Q5: official public GGUF.
- Armand0e Qwen3.5 9B Agent Q5: public coding-agent fine-tune.
- FlashModel Qwen3.5 9B Q5: additional public tool/reasoning candidate.
- GPT-OSS 20B MXFP4: official ggml-org GGUF; the larger file is a deliberate
  hardware-fit experiment informed by a same-P100 report.
- Full Qwen3.6 35B-A3B Q4: public Unsloth file, with CPU expert offload. It is
  not claimed to fit entirely in 16 GiB VRAM.

Willhar AgentTuned is deferred: the publisher and the Hub name search currently
provide only an 18.4 GB dense F16 GGUF, with no prepared small quant. It is not
scored as a failed model. No local quantization is authorized or performed.

The official Ministral 3 14B Instruct Q4_K_M was added as one justified follow-up
after the 8B family completed repeated contributions but showed read-quality
weaknesses. Its public 8,239,593,024-byte file is smaller than the existing
VibeForged file. This was an adaptive candidate addition, not part of the
original eight-model primary shortlist. It uses the same matched conditions.

## Primary conditions

Use the current frozen Hermes image and llama.cpp b12464 image, the same
configured MCP account, focused Gitea plugin 0.1.3 and full Discord-platform
AIAgent loop in disposable profiles. Do not send Discord messages or alter the
normal gateway, credentials, MCP allowlist or Portainer stack definitions.
Restore the original services between model batches and while waiting on files.

Primary sampling is temperature 0.2, top-k 20, top-p .95, min-p .05, repeat
penalty 1 and presence/frequency penalties 0. One slot, q4 K/V and 98,304
context are the initial configuration; main output cap is 4,096. Record actual
loaded context, cache type and CPU offload flags. A memory-related load failure
may be retried at 65,536; such exceptions remain visible in the results.
The full 35B initially offloads the first 24 layers' experts to CPU. Its
contribution budget is 600 seconds because this is a separate hybrid profile.

Run fresh, unchanged ordinary read prompts first:

1. `Find my SonicRatings repo and tell me what it does.`
2. `Look over sickprodigy/sick-cogs and suggest one useful new cog that isn’t already there.`

Read limits are 180 seconds / 16 model tool calls. All models see the same 32
schemas, including contribution tools. The guard stops any attempted mutation
on a read-only request before dispatch. This tests intent selection, not merely
operation in a toolset where writes are unavailable.

The third task is the authorized upstream issue → verified personal fork →
feature branch → exact README edit/commit → upstream PR workflow. Equivalent,
unused documentation corrections and unique identifiers are allocated in a
manifest before each run. Exact prompts and differences are retained. Limits
are 300 seconds / 20 model tool calls for the fully offloaded profiles.

No operator repairs model arguments or sends corrective conversation hints.
The guard blocks off-task tools, wrong targets, unexpected edits, extra writes,
settings changes, merges and closes. It permits one argument correction and
blocks identical failed retries until a confirmed mutation changes remote state.
An attempted forbidden action fails the routing check even when no RPC executes.

## Independent grading

Check actual resources through Gitea, including the fork parent, exact file
content and one-file PR diff, head/base direction, issue reference and open state.
Credit only writes made by that run. Report correct resources separately from
the stricter result requiring model read-backs and all requested final URLs.
Read answers are checked against captured tool results and reference snapshots;
completion alone does not establish a grounded answer.

Publisher-specific sampler or output-budget diagnostics, repetitions and useful
long-context probes are separate phases. Do not combine them with the primary
rows or silently replace failed attempts with a successful retry. Runtime or
harness incompatibilities must be distinguished from model reasoning failures.

Retain sanitized evidence and verified download provenance before removing the
temporary containers, volume and private credential-bearing snapshots. Test
issues and PRs remain open; the upstream default branch must stay unchanged.

The finalist 8B temperature-zero diagnostic was added after its repeated factual
errors, despite an earlier automatic diagnostic skip after clean primary
completion. Neither event is hidden. The native interface and long-input probes
are separate from matched primary results.

A final 14B native-interface diagnostic repeats only the full contribution task,
with the same native interface and clone permissions used for the 8B diagnostic.
It does not replace the 14B matched result or add another candidate.
