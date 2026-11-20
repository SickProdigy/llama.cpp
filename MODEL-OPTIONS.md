# Model follow-up options

Recorded November 19, 2026. This is a reminder of possible next steps, not a
record of tests on the spare PCs or a change to the deployed model.

## First direction: test existing files on spare hardware

Keep the P100 16 GiB server as the reference. Test the public GGUFs already
available before spending time making custom quants or buying hardware.

| Machine | First candidates | Purpose and limits |
|---|---|---|
| RTX 2070, 8 GB | Gemma 4 E4B Instruct Q5_K_M first; consider Q4 only if needed | Backup for smaller jobs. Gemma peaked at 4,804 MiB on the P100; fit, context and speed on the 2070 remain untested. Reserve memory for desktop use. |
| RTX 5080, 16 GB, if available | Gemma first, then VibeForged/FableVibes | Measure faster task execution and preserve useful backup models. The desktop 5080 has the same nominal VRAM capacity as the P100, not a larger model budget. No speed multiplier has been measured. |
| Current P100, 16 GiB | Existing VibeForged default; Gemma with focused Gitea tools as next trial | Stable reference for matched comparisons. Gemma is a promising trial, not established unattended coding reliability. |

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

- [Current recommendation and limitations](evaluations/2026-11-19-newer-models/investigation.md)
- [Current testing matrix](evaluations/2026-11-19-newer-models/matrix.md)
- [Exact evaluation protocol](evaluations/2026-11-19-newer-models/protocol.md)
- [Hardware research](evaluations/2026-11-19-newer-models/hardware.md)
- [llama.cpp quantization documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md)
- [llama.cpp importance-matrix documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/imatrix/README.md)
- [NVIDIA desktop RTX 5080 specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/)
