# Public adapted 27B Q3_K_M: measured current capacity

The pinned public Q3_K_M completes the registered capacity probes at **98,304 context**, with **66/66 layers reported offloaded to GPU** (`-ngl 99`) and ubatch **64**. Actual buffers are recorded below. Sampled GPU peak is **14,920 MiB**. This is capacity evidence; **a fresh native coding/Gitea workflow is still required** before assigning a workflow-quality verdict or choosing a model.

| Probe | Input tokens | Cached input | Output tokens | Seconds |
|---|---:|---:|---:|---:|
| tool | 293 | 0 | 28 | 23.98 |
| tool-result | 356 | 320 | 22 | 2.81 |
| tool-followup | 404 | 377 | 6 | 1.84 |
| prompt16000 | 16,152 | 0 | 9 | 238.70 |
| prompt60000 | 59,937 | 16,084 | 9 | 787.79 |
| prompt80000 | 79,932 | 59,869 | 9 | 425.28 |

Synthetic retrieval results: **16000: exact, 60000: exact, 80000: exact**. Short tool arguments and actual assistant/tool history are independently checked against saved request/response bytes. These calls use synthetic lookup_record data, not configured Gitea MCP. Small outputs do not establish correctness across the full context. Cached long prompts are not uncached prefill benchmarks.

```text
0.01.435.102 I load_tensors: offloaded 66/66 layers to GPU
0.01.435.112 I load_tensors:        CUDA0 model buffer size = 12153.77 MiB
0.01.435.113 I load_tensors:    CUDA_Host model buffer size =   521.00 MiB
0.33.372.229 I llama_kv_cache:      CUDA0 KV buffer size =  1728.00 MiB
0.33.410.659 I sched_reserve:      CUDA0 compute buffer size =   408.50 MiB
0.33.410.680 I sched_reserve:  CUDA_Host compute buffer size =    17.00 MiB
```

Readiness takes **75.83 seconds**. All registered layout attempts and allocation outcomes are retained in the summary; no HTTP or host guard failure is silently treated as CUDA OOM. Requested GPU-layer counts do not establish equal shares of model computation. CPU model/compute buffers remain relevant even with all layers reported offloaded.

Across **290 five-second samples**, aggregate charged cgroups peak at **7,049,977,856 bytes**, process PSS at **2,415,563,776 bytes**, and study swap at **0 bytes**. These include charged cache and relevant helpers; sampling can miss transient peaks. Whole-host swap counter movement is not attributed to the study. Both actual storage filesystems remain above the user 100 GiB reserve and the registered 101 GiB stage stop threshold. Fresh admission required 102 GiB on each; older stage policies were not rewritten.

Runtime uses backend fee4289628e7ba09f6fbf62d6ce4325aebb2531ffde2154d41276fe4acc58da3, C9 observer image, one slot, q4_0 K/V, load none, fit off, batch 512, eight threads, two context checkpoints and 512 MiB cache RAM. The adapted reference sampler is nonthinking temperature0.8/top_p1/top_k0/min_p0/repeat1/presence0, seed20261123 and 8192 output cap. These controls differ from Fable thinking runs. Selected-file pages were verified inactive before the first attempt; this is not a global cache flush or proof that all driver/host caches are cold.

Artifact: `netprojects/Qwen3.8-27B-hermes-adapted-GGUF` at revision `10fdf357f14825c61ad7eb42a932e1f1e4390e8f`, file `Qwen3.8-27B-hermes-Q3_K_M.gguf`, **13,752,764,064 bytes**, full SHA256 `a0c809f93de2bcd813e1b6fbd5c2d1f692821814a4261a316f7c8bca9cf23248`. The selected file was freshly fully hashed before GPU calls. No local weight quantization was performed. The [download report](public-adapted-q3km-download.md) records transfer, provenance and exact download-helper cleanup.

The actual header records 866 tensors, imatrix.gguf / imatrix-calib.txt / 496 entries / 150 chunks. IQ3_XXS lists the same calibration filename/counts; IQ4_XS lists calib-train.txt / 104 chunks. Q4_K_M has no recorded imatrix keys, which does not prove no matrix was used. Tensor names/dimensions and the 9004-byte template match across the four adapted variants; tensor-type mixes differ. These facts do not prove identical calibration contents or unquantized weights. The archive binds the fresh capacity-admission header, whose observation timestamp differs from the earlier download-stage header.

Strict postflight verifies original runtime alias/context, container identities/images/configurations/running states, four owner setting hashes, all 30 original model metadata records, both staged weights and owner pending edits. **Hermes-Codex's full recorded state matches the fresh baseline**, including start time. The earlier IQ4 timestamp exception is not waived. Exact owned supervisor/anonymous-volume/backend/network cleanup passes, preserving named model storage. Postflight free GiB: original **103.31**, staging **102.05**.

[Evidence archive](resource-adapted-q3km-current-evidence.tar.gz), [summary](resource-adapted-q3km-current-summary.json), [validation](resource-adapted-q3km-current-validation.json), [privacy scan](resource-adapted-q3km-current-privacy.json). Archive SHA256: `d56e77cb76f6d4d06279d5660e3c2d192debb1d04804db302fecd7b3c7793544`. The standalone verifier checks saved evidence. Qualification rejects six recomputed-manifest tamper controls; it does not replay inference or independently reproduce a full model download.

```sh
python3 evaluations/2026-11-24-gpu-quant/verify_current_adapted_q3km_resource.py evaluations/2026-11-24-gpu-quant/resource-adapted-q3km-current-evidence.tar.gz
(cd evaluations/2026-11-24-gpu-quant && sha256sum -c resource-adapted-q3km-current-evidence.sha256)
```

| Current practical layout | Reported GPU layers | Ubatch | Sampled GPU MiB | 16k seconds | 60k seconds | 80k seconds |
|---|---:|---:|---:|---:|---:|---:|
| adapted-q4-current | 56/66 | 128 | 15,456 | 198.40 | 663.77 | 369.64 |
| adapted-iq4-current | 63/66 | 64 | 15,926 | 247.09 | 804.16 | 428.05 |
| adapted-iq3-current | 66/66 | 64 | 12,904 | 271.56 | 870.56 | 463.15 |
| adapted-q3km-current | 66/66 | 64 | 14,920 | 238.70 | 787.79 | 425.28 |

These layouts use the current backend, but placement, tensor family, calibration, production and microbatch differ. Cached-input timing is measured practical behavior, not a precision-only or uncached-throughput comparison. The three previously completed adapted coding cells fail; Q3_K_M coding remains pending.

The [nine completed current workflows](completed-current-quant-comparison.md) still provide no full pass. This resource stage adds no coding-quality sample, no autonomous reliability estimate and no GPT-5 equivalence claim. Production remains unchanged.
