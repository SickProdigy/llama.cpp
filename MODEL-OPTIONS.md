# Model follow-up options

Recorded November 19, 2026. This is a reminder of possible next steps, not a
record of tests on the spare PCs or a change to the deployed model.

## November 23: wider-memory testing started

The [new evaluation](evaluations/2026-11-23-wide-memory/plan.md) is active.
The retained IQ3 baseline completes 16k/60k resource probes, but mapped loading
shows why the Docker memory cap alone is insufficient proof of an 8 GiB resident
budget. See [measurements and loading-mode amendment](evaluations/2026-11-23-wide-memory/resource-baseline.md).
The [matched non-mapped IQ3 baseline](evaluations/2026-11-23-wide-memory/resource-baseline-v2.md)
now completes the same probes at 1.87 GiB peak process PSS and zero observed
backend swap. That resolves the loading caveat for the measured layout, without
establishing whole-host fit or agent correctness.
The adapted Q4 public file now [completes resource probes](evaluations/2026-11-23-wide-memory/resource-q4.md)
at 98,304 context with 56 GPU layers and non-mapped loading: 15.09 GiB GPU and
4.50 GiB peak process PSS. The first native attempt hits a host cgroup
OOM despite the short resource pass. A [checkpoint comparison](evaluations/2026-11-23-wide-memory/checkpoint-comparison.md)
completes with `--ctx-checkpoints 2` while default32 reproduces the OOM.
The [conditional native recovery](evaluations/2026-11-23-wide-memory/native-q4-recovery.md)
completes independently checked code/docs/forge stages, with wrong final URLs
and stale PR metadata. The [fresh Announcer sample](evaluations/2026-11-23-wide-memory/native-q4-fresh.md)
also completes independent code/behavior and publication checks, with README
re-enable wording and plugin/full-suite count qualifications. The [other candidates](evaluations/2026-11-23-wide-memory/matrix.md)
remain pending. No winner or autonomous reliability is established.
The original runtime is restored and audited after each completed GPU stage.
[Study-owned weight rotation records](evaluations/2026-11-23-wide-memory/study-weight-rotations.json)
track temporary Q4/Q3/Devstral removal to admit the next public file while preserving
the original29 and disk reserve. The selected model can be retained from its pin
at the end; rotation is not a quality-failure verdict.

Public [format metadata](evaluations/2026-11-23-wide-memory/candidate-format-preflight.json)
was initially inspected from16MiB prefixes for Devstral and GLM. Devstral's full
pinned file now completes the resource stage below; GLM's full public weight
[passes its pinned hash check](evaluations/2026-11-23-wide-memory/glm-download-verification.json),
and [completes the five-probe resource stage](evaluations/2026-11-23-wide-memory/resource-glm.md)
at 98k with CPU expert spill. Native coding quality remains unproven. GLM's embedded template
uses `clear_thinking: false` with `enable_thinking: true` to preserve reasoning
across user turns. A [scripted native CLI control](evaluations/2026-11-23-wide-memory/glm-cli-history-control/README.md)
now verifies client reasoning retention through a real terminal call and
persisted followup, with the intended settings serialized. Resource probes now
exercise the actual GLM template/history and P100 inference. Full-profile
coding/Gitea behavior and quality remain unverified.
Do not copy Qwen's thinking-off settings. Devstral declares `mistral3`,40layers,
8KVheads; GLM declares `deepseek2` with MLA and47layers. These guide bounded
layout trials; file size and metadata are not quality/fit proof.

The [pinned adapted Q3/Q4 header comparison](evaluations/2026-11-23-wide-memory/quant-header-preflight/README.md)
finds matching tensor names/shapes and tokenizer metadata, but differing
importance-matrix metadata. Compare these public files as provided; a quality
difference cannot be attributed solely to bit precision. The [full pinned Q3](evaluations/2026-11-23-wide-memory/resource-q3.md)
now completes tool/history/16k/60k resource probes at 98k context, 14,946 MiB
GPU and 2.19 GiB peak process PSS, with zero observed experiment swap. Fresh
Spam coding [fails the requested repair](evaluations/2026-11-23-wide-memory/native-q3-spam.md)
despite green project tests and correct Gitea publication; the cooldown feature
passes separately. [Fresh Q3 Announcer](evaluations/2026-11-23-wide-memory/native-q3-queue.md)
passes scoped source/behavior checks with documentation/reporting qualifications.
Devstral's [full pinned Q4_K_M resource stage](evaluations/2026-11-23-wide-memory/resource-devstral.md)
completes tool/history/16k/61k probes at 98k context with 32 GPU layers and CPU
spill: 14,880 MiB GPU, 6.56 GiB peak charged host memory and zero observed
experiment swap. Its 61,640-token request takes 856.60 seconds with 16,039 cached
tokens. The [fresh Spam workflow](evaluations/2026-11-23-wide-memory/native-devstral-spam.md)
passes scoped next-message/cooldown checks locally, but fails original notification
preservation, weakens a test and performs no requested Gitea issue/fork/PR actions.
[Fresh Announcer](evaluations/2026-11-23-wide-memory/native-devstral-queue.md)
preserves the original suite and initial fix, but its room-cancellation feature
retains reply state for emptied jobs and no contribution is published. The raw
metadata-check failure is qualified by actual pinned dispatcher behavior;
[matched posthoc controls](evaluations/2026-11-23-wide-memory/announcer-dispatch-cleanup-comparison.json)
show Q3/Q4 clear that state. The owned Devstral weight is temporarily rotated
after both completed audits; the full pinned GLM download is verified and its
five-probe resource stage completes at98k with 12 CPU expert layers,15336MiB
GPU and6.564GiB peak charged host memory, zero experiment swap. Whole-host
swap counters rise substantially; no attribution to the model is made. The60k
request takes1410.74s. The initial unequal K/V configuration failure and
correction are preserved. GLM's [fresh Spam workflow](evaluations/2026-11-23-wide-memory/native-glm-spam.md)
fails preservation and cooldown correctness, has unusable undiscovered authored
tests and creates no commit/PR despite a correct issue/fork. Coding takes 85 minutes
within budget, with no experiment swap. Fresh Announcer remains underway.
A matched fresh Q4 Spam trial is registered after both GLM audits; the recovered
Q4 Spam outcome remains conditional. Resource fit is not quality proof.

## November 22: full P100 plus up to 8 GiB host spillover

The owner widened the candidate budget to the P100's 16 GiB VRAM plus up to
8 GiB additional system RAM for model spillover. This is a proposed next
comparison, not a completed load or quality result. Keep the current fresh
review cohort unchanged, finish its audits/restoration, then test wider layouts
in a separate stage. The separate Hermes-Codex stack stays unchanged.

| Candidate | Why consider it | What still needs measurement |
|---|---|---|
| Same Hermes-adapted 27B Q3_K_M, 13.75 GB published file | Intermediate precision; may fit mostly or entirely on GPU | Actual 98k context memory, speed and task correctness |
| Same Hermes-adapted 27B Q4_K_M, 16.81 GB published file | Compare higher precision within the same adapted checkpoint using limited CPU offload | CPU-resident weights/runtime overhead within 8 GiB, GPU buffers/KV, latency and independent quality |
| Devstral Small 2 24B public GGUF | Its historical local failure was GPU OOM at 64k, not a demonstrated coding-quality failure; the new budget changes that blocker | Current pinned backend/template support, 64k+ actual fit and useful task performance |
| GLM-4.7-Flash 30B MoE, public Q4 file about 18.2 GB | Different coding/tool-use checkpoint newly plausible with a small CPU share | Pinned-runtime architecture/template, expert offload, 98k cache and actual quality; no P100 fit claim yet |

The [same-checkpoint publisher](https://huggingface.co/netprojects/Qwen3.8-27B-hermes-adapted-GGUF)
provides these larger quants. Its short-prompt precision measurements do not
establish agent reliability. The [original adapter author](https://huggingface.co/harness-hub/Qwen3.8-27B-hermes-adapted-GGUF)
also distinguishes BF16 training/evaluation from quantized llama.cpp behavior.
[Devstral's author](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)
describes coding/tool-use training; [public GGUFs](https://huggingface.co/unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF)
still need a pinned revision, byte length and hash before use.

[GLM model author](https://huggingface.co/zai-org/GLM-4.7-Flash) and
[llama.cpp-maintainer GGUF files](https://huggingface.co/ggml-org/GLM-4.7-Flash-GGUF/tree/main)
provide a separate family to consider; third-party RAM estimates are not load evidence.

Also inspect the retained 35B MoE's previous CPU-expert results before another
trial; its existing offload layout is not proof of staying within the new 8 GiB
host budget. Do not repeat a previously fitting but unsuccessful model solely
because its file now looks affordable.

Sixteen plus eight is not 24 GiB of usable model weights: context/KV, execution
buffers and host overhead also count. CPU offload can slow generation, and
better quantization is a hypothesis, not a fix for tool coordination or review
reasoning. Measure model RSS/PSS, anonymous/file memory, active swap deltas,
GPU peak and actual prompt latency. Existing host swap use is not evidence that
a new model caused swapping; do not flush system swap or disturb other services.
Preserve original useful models and at least 100 GiB model-disk reserve, using
one additional large download at a time when necessary.

## November 21 investigation: best tested supervised lead

Earlier guided-edit passes are insufficient for selecting an editor-like coding
agent. The [new investigation](evaluations/2026-11-21-goal-investigation/investigation.md)
checks a fresh real-source defect, independent behavior checks, original tests,
actual published code and a retained followup. No candidate has yet qualified
on that complete workflow. Keep the older hardware shortlist provisional.

Completed ordinary/bulk real-source trials include the existing full Qwen3.6
35B A3B with CPU expert offloading, public Qwen3.5 27B UD-IQ3_XXS, the
Hermes-adapted 27B IQ3_XXS, and Qwen3-Coder 30B A3B IQ3_XXS. They fit tested
configurations, but none repairs all six booksearch defects. The adapted 27B
ordinary run is the strongest supervised lead: four defects, meaningful executed
tests and a verified issue/PR/followup. Its 11.638 GB file peaked at 13,094 MiB
with 98,304 context loaded. The larger file limit is a measured practical fit,
not an assumption that an 8 GB file is required. The final API diagnostic published a correct fix with genuine coverage and
passes preservation checks, but its README overgeneralizes terminal states.
Context controls are complete; none establishes unattended reliability.
[Exact candidate configuration](evaluations/2026-11-21-goal-investigation/supervised-candidate.json)
records the effective sampler, full backend launch, memory and limits.

After all model jobs finished, the newly downloaded stock dense 27B and
Qwen3-Coder 30B files were removed only after their exact sizes/hashes matched.
All other GGUF files were unchanged, including the adapted 27B and existing
useful models. About 125.3 GiB was free at cleanup, above the 100 GiB reserve.

The ordinary/bulk native coding precision comparisons did not show a consistent
benefit from higher weight precision or F16 cache across checkpoints. Those
small unseeded samples do not prove that precision never matters. No model has
been quantized locally during this investigation; the new download is a public
publisher-provided quant. Preserve the 100 GiB reserve.

## Spare-PC options (not yet validated on those GPUs)

Keep the P100 16 GiB server as the reference. Test the public GGUFs already
available before spending time making custom quants or buying hardware.

| Machine | First candidates | Purpose and limits |
|---|---|---|
| RTX 2070, 8 GB | Gemma 4 E4B Instruct Q5_K_M first; consider Q4 only if needed | Backup for smaller jobs. Gemma peaked at 4,804 MiB on the P100; fit, context and speed on the 2070 remain untested. Reserve memory for desktop use. |
| RTX 5080, 16 GB, if available | Adapted27B IQ3XXS after native runtime compatibility checks; existing small files for lighter tasks | Reuse the measured P100 candidate as a starting point. The same nominal 16 GB capacity does not establish fit or speed on the 5080; those measurements remain pending. |
| Current P100, 16 GiB | Existing VibeForged production default; adapted 27B IQ3XXS is the current supervised evaluation lead | Production default is preserved. No tested model has qualified for unattended repository work; see November 21 matrices. |

Use a llama.cpp build and driver appropriate for each GPU. Do not copy the
P100 CUDA image onto the 5080 and assume compatibility. A GGUF can move between
machines when their runtimes support its architecture and quantization format.

Each PC could run its own llama.cpp HTTP server. Hermes could select the
appropriate endpoint for a whole task, letting an idle PC handle work. That
requires explicit endpoint/profile selection or a dispatcher; automatic task
routing is not implemented. Separate PCs do not automatically pool GPU memory.
Use trusted-network access and authentication for any exposed endpoint.

## Local quantization, when a promising checkpoint needs it

Quantization reduces weight precision and file size, potentially sacrificing
quality. It does not train better reasoning/tool use or increase the model's
trained context limit. Prefer existing verified public GGUFs when suitable.

1. Choose a checkpoint based on workflow potential, supported architecture and
   expected memory fit. Pin its revision and verify the downloaded files.
2. Obtain original high-precision weights or an F16/BF16 GGUF. Convert original
   Hugging Face weights to GGUF if necessary.
3. Produce Q5_K_M and, if useful for the 2070, Q4_K_M directly from that
   high-precision source. Avoid repeated quantization of an existing low-bit file.
4. Optionally generate an importance matrix using representative code and tool
   conversations, separate from evaluation prompts, then use it during quantization.
5. Save the source revision, converter/quantizer commit, commands, calibration
   provenance and output SHA256 hashes. Transfer the finished GGUF and verify
   its hash on the destination.
6. Compare the outputs using the same Hermes/MCP workflow, sampling and tool
   interface. Keep quantization effects separate from hardware speed changes.

Example commands after installing llama.cpp and model conversion dependencies:

```bash
# Skip conversion when a suitable high-precision GGUF already exists.
python convert_hf_to_gguf.py /path/to/original-model \
  --outfile model-f16.gguf --outtype f16

./build/bin/llama-quantize model-f16.gguf model-Q5_K_M.gguf Q5_K_M
./build/bin/llama-quantize model-f16.gguf model-Q4_K_M.gguf Q4_K_M

# Optional calibration; choose GPU offload layers to fit the source model.
./build/bin/llama-imatrix -m model-f16.gguf -f calibration.txt \
  -o imatrix.gguf -ngl 0
./build/bin/llama-quantize --imatrix imatrix.gguf \
  model-f16.gguf model-imatrix-Q4_K_M.gguf Q4_K_M

sha256sum model-*.gguf
```

The example calibration uses CPU execution. Increasing GPU offload can speed
that inference pass, but the high-precision source plus buffers may exceed an
8 GB or 16 GB GPU; partial offload is an option. Ordinary conversion and
quantization primarily depend on CPU, system RAM and storage, so a 5080 alone
does not guarantee faster quantization.

Budget temporary disk for the original weights, intermediate GGUF and outputs
at the same time. A dense 9B F16 weight set is roughly 18 GB before format
and architecture differences. Inspect actual sizes first; preserve the existing
100 GiB free-space reserve and useful small/task models. Remove task-owned
intermediates only after successful output verification and evidence retention.

## Test and retention checklist

- Real-code follow-up completed: Gemma failed; FableVibes produced a correct
  patch with the focused tools, but its write-up still had factual mistakes.
  See [comparison](evaluations/2026-11-20-real-code-comparison/investigation.md);
  prefer Fable for the next supervised trial rather than repeating Gemma first.
- On each spare PC, verify backend properties, actual available VRAM, loaded
  context, idle/active memory and the first completed tool-call time.
- Run repository explanation/review and an authorized issue → fork branch →
  exact edit → upstream PR workflow. Independently verify resources, diffs,
  read-backs and returned URLs. Use the established test protocol/guard.
- Keep the focused interface identical for hardware comparisons. Native-tool
  diagnostics are separate: Gemma's previous native contribution failed.
- Start below memory limits, then test the desired context under actual input.
  Loading 98k is not proof of useful full-window coding; the recorded Gemma
  context success was a 63,098-token retrieval plus MCP-read task.
- Retain the strongest agent candidate and useful lightweight helpers per PC;
  do not keep every quant by default. Record failures before deleting clearly
  unsuitable large files. Restore the normal server/profile after comparisons.

## Evidence and references

- [Historical November 19 recommendation and limitations](evaluations/2026-11-19-newer-models/investigation.md)
- [Historical November 19 testing matrix](evaluations/2026-11-19-newer-models/matrix.md)
- [Exact evaluation protocol](evaluations/2026-11-19-newer-models/protocol.md)
- [Hardware research](evaluations/2026-11-19-newer-models/hardware.md)
- [llama.cpp quantization documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md)
- [llama.cpp importance-matrix documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/imatrix/README.md)
- [NVIDIA desktop RTX 5080 specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/)

## November 20 Fable-trace follow-up

[Comparison](evaluations/2026-11-20-fable-trace-models/investigation.md): Qwable
and Qwopus failed the MCP code task on local search; Parable could not load
98k context. Fable remains the strongest supervised workflow trial, with
assistance/prose caveats. Only the 3.16 GB Qwopus Q5 file is retained from this
new cohort, as a small helper candidate. Its 4,742 MiB P100 result is not yet a
2070 measurement. Verify owner namespace selection and remote source navigation
before another everyday-agent profile switch.


### Qwen3-Coder coding-specialist control (completed; new file removed)

[Qwen3-Coder 30B A3B Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
is a non-thinking agentic-coding checkpoint, distinct from the older Qwen2.5
Coder files already tested and the general Qwen3.5/3.6 controls. Its publisher
specifies .7 temperature, .8 top-p, top-k20 and repetition penalty 1.05.
Native context is 262,144; the advertised 1M extension is not measured P100 capacity.

A public [Unsloth IQ3_XXS](https://huggingface.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF)
is 12,848,766,112 bytes, revision `b17cb02dd882d5b6ab62fc777ad2995f19668350`,
SHA256 `d6b85d2b6633c55be3751848acc74fab40d28d93b27dabacd96ceabe10962057`.
The current goal downloaded and verified this file, preserving about 102.8 GiB
free. It loaded 98,304 entirely on the P100 (no CPU fallback), with 15,348 MiB
observed in the ordinary run. That run finished in 488 seconds but repaired
0/6 public defects, used a test copying its own algorithm, and published no
contribution. The paired bulk run also repaired 0/6, used a self-contained test simulation
and published nothing (1,288 seconds including both turns and independent
grading, 15,350 MiB observed). Both edited/original suites pass despite wrong
behavior. Fit and faster decoding did not establish useful repository-agent
correctness. Keep the earlier Qwen2.5 results separate and preserve the 100 GiB
reserve. The new file was removed after exact-hash verification at final cleanup;
its pinned public revision and results remain available for reproducibility.

### Later software-speed option: speculative decoding (not measured here)

The [speculative-decoding documentation at our pinned llama.cpp source](https://github.com/ggml-org/llama.cpp/blob/d3c3e242c16b8cbf51400fad410cd69b22d64f35/docs/speculative.md)
lists `draft-mtp` and n-gram methods. The adapted file retains MTP tensors, but
all scored runs here use ordinary decoding: retained tensors do not mean the
feature was enabled. A later speed experiment could reuse existing weights,
measure acceptance and memory, and repeat actual tool/coding checks before
changing the recommended profile. No P100 speedup is established.

[Upstream #25618](https://github.com/ggml-org/llama.cpp/issues/25618) reports
nonidentical greedy outputs in quantized speculative configurations on other
setups. That report is not a reproduced P100 defect; it is a reason to verify
the actual configuration instead of promising unchanged output. The pinned
documentation also says synthetic-acceptance benchmark output is not valid
model output. Do not use synthetic acceptance to score repository-agent quality.
This is a recorded future lead, not another cohort in the current investigation.
