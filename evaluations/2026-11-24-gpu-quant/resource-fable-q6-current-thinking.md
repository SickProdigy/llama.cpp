# Current Fable Q6 capacity reference

November 26: the retained public Fable Q6_K completes all six capacity requests
on the same current llama.cpp image/settings used for Q8. All 41 layers are
explicitly on GPU at 98,304 context with q4_0 KV and automatic fit disabled.
Peak sampled GPU memory is 11,566 MiB, leaving 4,709 MiB free. The model uses
10,392.38 MiB of GPU model buffers and 397.85 MiB of host model buffers;
GPU KV is 540 MiB and GPU compute 229.01 MiB. No transformer layers are
assigned to CPU. Host model and compute buffers remain reported separately.

The retained 11,325,370,880-byte file passes its pinned full SHA256 before loading.
Publisher `tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF`, revision
`9cf910a7ad68dfedcbdfc46ef0fe5003dec07c23`, file
`Qwen3.6-14B-A3B-FableVibes-Q6_K.gguf`, SHA256
`7ae56e5003365c568635c14158381df134577877c90ae15f34dbc6de2ca7ffb1`.
The previously inspected Fable Q4/Q6/Q8 headers have matching tensor names,
dimensions and chat template, with no imatrix metadata; missing metadata does
not establish identical calibration. Q8 tensor production differs from K quants.
No new model download, deletion or quantization occurs in this stage.

| Request | Input tokens | Cached input | Seconds |
|---|---:|---:|---:|
| Tool call | 291 | 0 | 20.73 |
| Actual tool result | 389 | 355 | 2.53 |
| Dependent tool followup | 519 | 494 | 1.87 |
| 16k marker | 16,165 | 0 | 40.49 |
| 60k marker | 59,935 | 16,033 | 165.24 |
| 80k marker | 79,930 | 59,803 | 106.64 |

The initial tool call has correct name/arguments; the real assistant/tool history
is retained, and the dependent followup returns the exact tool code. All three
marker answers are exact, including the prefix omitted by Q8 at 60k. These are
single synthetic observations, not evidence that Q6 generally reasons better.
The 80k request benefits from 59,803 cached input tokens; its latency is not
an uncached 80k benchmark. Every request reserves 16,384 output tokens within
the measured window. Advertised larger contexts remain untested here.

Across 77 samples with five-second pauses: zero measurement errors, guard
violations or study swap. Aggregate charged cgroups peak 7,020,474,368 bytes;
process PSS peaks 1,796,613,120 bytes. Charged file cache is included and does
not indicate CPU transformer-layer spillover. Global host swap counters move
1,140 input/4,081 output pages without attribution to the study. Sampling can
miss transient peaks. Both disk reserves remain above 100 GiB throughout.
The specific inactive model file has zero cached pages immediately before load;
this is not proof about storage-device caches or global cold-cache state.

The original runtime is restored and independently checked: container identities,
images/configuration, original alias and 98k context, four profile file hashes,
all 30 original model metadata entries, 40 owner files/pending edits and the
full recorded Hermes-Codex state are preserved. Postflight free space is
104.30 GiB on the original model drive and 104.41 GiB in staging. Exact owned
backend/network and terminal supervisor are removed; no study job remains.

Q6 uses 3,058 MiB less sampled GPU memory than Q8 under this layout. This is
capacity evidence, not a current Hermes coding/Gitea pass: the older Q6 workflow
used a different Hermes image and recorder. A fresh matched current-runtime Q6
coding/issue/fork/PR run is the next comparison. The completed current Q8 run
fails that workflow; increasing precision alone has not established a winner.

[Observations](resource-fable-q6-current-thinking-summary.json),
[evidence archive](resource-fable-q6-current-thinking-evidence.tar.gz),
[SHA256](resource-fable-q6-current-thinking-evidence.sha256),
[validation](resource-fable-q6-current-thinking-validation.json).
The saved-observation verifier checks hashes, registered sources, actual buffers,
request headroom, memory, responses and restoration; it does not rerun inference.

```sh
python3 verify_current_fable_q6_resource.py resource-fable-q6-current-thinking-evidence.tar.gz
sha256sum -c resource-fable-q6-current-thinking-evidence.sha256
```
