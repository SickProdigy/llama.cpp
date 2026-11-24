# GLM-4.7-Flash public Q4_K resource stage

Completed November 24, 2026. The pinned model completes five resource, template
and tool-history probes at 98,304 context on the P100 using CPU expert spill.
This is a capacity result, not a coding/Gitea quality result. Fresh native trials
are separate and remain under evaluation.

| Probe | Actual input tokens | Output tokens | Seconds | Recorded result |
|---|---:|---:|---:|---|
| Defined lookup tool | 181 | 120 | 21.57 | Valid tool call |
| Assistant completion after tool result | 323 | 117 | 3.98 | Completes tool turn |
| Fresh dependent user followup | 455 | 59 | 2.87 | Exact returned marker |
| Synthetic 16k | 16,091 | 397 | 184.50 | Exact final marker |
| Synthetic 60k | 59,856 | 612 | 1,410.74 | Exact final marker |

The largest request reuses 16,081 cached tokens and processes 43,775 new tokens.
Recorded prefill is 1,341.81 seconds, averaging 32.62 new tokens/second; decoding
averages 8.87 tokens/second. These are complete responses with measured rendered
inputs, not cold-prefill benchmarks. The 16k request reuses two tokens. Actual
assistant reasoning survives the subsequent rendered tool history. Synthetic
markers and a defined tool do not prove coding, configured MCP routing, or
long-conversation reliability. Output reserve is 16,384 tokens.

The successful requested layout uses 99 GPU layers and 12 CPU expert layers,
non-mapped loading, matching q4_0 K/V declarations, one slot, batch512/ubatch128,
eight CPU threads, fit disabled, 512 MiB prompt cache and two context checkpoints.
No fallback expert layout is used. Requested placement is retained; verbosity-3
logs do not expose a complete per-tensor allocation inventory. Loading takes
83.03 seconds after independent full-file hashing and DONTNEED advice for only
this study-owned file. Cache and ambient host activity are uncontrolled.

Across 320 complete samples, peak charged experimental cgroups are **6.564 GiB**,
all-process PSS **4.865 GiB**, and GPU **15,336 MiB**. These independent peaks
must not be summed. Experiment swap, guard violations and measurement errors
are zero. Backend cap is 6.5 GiB, supervisor cap 512 MiB and aggregate guard
8 GiB, with no experiment swap allowance. Charged cache/shared buffers are
included. These samples do not prove a continuous additional whole-host bound.
Minimum observed host available memory is 32.268 GiB and disk free111.734 GiB.
Whole-host swap counters rise **643,370 pages in and 2,030,760 out** across this
stage, despite zero observed experiment-cgroup swap. They show substantial host
swap activity and cannot identify the responsible process or establish model
swap use. They also limit latency comparisons with runs under other host loads.

Backend image is `sha256:7561b4761f849925a728c5ac2bd1f4a649b6a76f24544e7f992b047ad016cec3`,
build `b12627-225a5345b`. Sampler is temperature0.7, top-p1, top-k0, min-p0,
repetition1 and presence0, with `enable_thinking=true`, `clear_thinking=false`.
Different architectures, cache paths, samplers, output lengths and host loads
prevent interpreting these timings as a precision-only comparison. Q3 also
uses the earlier four-probe sequence; Devstral uses five probes.

## Preserved operator configuration failure

The first GLM attempt exits before context readiness: q4_0 K with f16 V is
rejected because MLA initialization requires equal declared cache types. It is
not a GPU OOM or a model quality failure. The earlier operator rationale focused
on the absence of a separate MLA V tensor and missed the earlier type-equality
check. The corrected attempt sets both declarations to q4_0 before any GLM
coding actor. Context, sampler, memory limits, probes, tasks and graders remain
unchanged. The failed logs, old protocol/registration, superseded rationale,
correction, source pins and restoration audits are preserved in the archive.

Pinned [context initialization](https://raw.githubusercontent.com/ggml-org/llama.cpp/225a5345bbb0e0c70859af5441ba922beb666fcf/src/llama-context.cpp)
requires the equality and enables Flash Attention for quantized V declarations.
The [CUDA implementation](https://raw.githubusercontent.com/ggml-org/llama.cpp/225a5345bbb0e0c70859af5441ba922beb666fcf/ggml/src/ggml-cuda/fattn.cu)
and [tile implementation](https://raw.githubusercontent.com/ggml-org/llama.cpp/225a5345bbb0e0c70859af5441ba922beb666fcf/ggml/src/ggml-cuda/fattn-tile.cuh)
provide a generic 576/512 path. Source inspection guided the correction;
the completed requests provide the actual measured compatibility evidence.
No runtime rebuild or production setting change was needed.

## Pin, restoration and evidence

- Repository: `ggml-org/GLM-4.7-Flash-GGUF`
- Revision: `7559e96b7e324ab405897dc2b91492b0f376ad4a`
- File: `GLM-4.7-Flash-Q4_K.gguf`, 18,244,193,920 bytes
- SHA256: `b6019edc5fbe37d3660d2e994d16c839a7855a6f03362c5dcf8142ba479cd0d2`

Anonymous download and independent resource-stage hashes agree. At the end of
each resource attempt, original service IDs/images/configuration, four profile
hashes, owner pending files/instructions, original Vibe alias/98k context, all29
original model entries and unchanged Hermes-Codex are independently verified.
Owned resource containers/network are removed;111.734 GiB is free. Later native
stages have their own restoration obligations and may temporarily stop the
original Hermes/backend while using the GPU.

[Summary](resource-glm-summary.json), [archive](resource-glm-evidence.tar.gz),
[SHA256](resource-glm-evidence.sha256), [privacy scan](resource-glm-privacy.json)
and [validation](resource-glm-validation.json) retain synthetic requests, complete
responses, samples, frozen controls and restoration audits. Pinned public runtime
sources are included; native profiles, private coding tasks/graders, owner
repository source and credentials are not exported.

```sh
python3 evaluations/2026-11-23-wide-memory/verify_candidate_resource.py glm
```

The verifier checks retained bytes, pins, token/measurement consistency,
restoration and the exact cache-configuration correction. A separate
[negative format control](resource-glm-negative-control.json) changes a pinned source and correctly recomputes archive/manifest
hashes; verification still rejects the source mismatch. These checks do not
rerun inference or certify agent quality.
