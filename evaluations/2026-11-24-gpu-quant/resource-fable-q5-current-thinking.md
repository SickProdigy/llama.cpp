# Current public Fable Q5: 98k fits; the 60k answer is not exact

The public FableVibes Q5_K_M completes all six capacity requests at **98,304 context / 41 of 41 reported GPU layers / 10,224 MiB sampled peak GPU**. Minimum sampled free GPU memory is **6,051 MiB**. Host model buffers are **333.44 MiB**, so all layer offload does not mean zero host allocation. The 60k prompt returns `60000` instead of the requested `capacity-check-60000`; the 16k and 80k markers are exact. Actual short tool arguments, assistant/tool-result lineage and dependent answer are retained and verified. **This is capacity evidence, not a coding/Gitea workflow pass.**

| Probe | Input / output tokens | Cached input | Seconds | Observation |
|---|---:|---:|---:|---|
| `lookup_record` | 291 / 87 | 0 | 27.07 | Actual `name=memory-probe` tool call |
| Tool-result completion | 411 / 86 | 377 | 1.99 | Actual assistant and tool result retained |
| Dependent history | 521 / 36 | 496 | 0.97 | Exact `tool-history-capacity-ok` |
| 16k | 16,165 / 173 | 0 | 39.57 | Exact marker |
| 60k | 59,935 / 247 | 16,033 | 155.92 | Required prefix omitted |
| 80k | 79,930 / 104 | 59,803 | 101.64 | Exact marker |

The selected [public file](https://huggingface.co/tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF/blob/9cf910a7ad68dfedcbdfc46ef0fe5003dec07c23/Qwen3.6-14B-A3B-FableVibes-Q5_K_M.gguf) is **9,852,131,840 bytes**, full SHA256 `d8fe99004cefb2cf26a1750851acf3cabd53247958e144f88e08beeb36ffbcab`, publisher revision `9cf910a7ad68dfedcbdfc46ef0fe5003dec07c23`. The sequential download takes 1,083.99 seconds, verifies the stream length/full hash and fsyncs before rename. The resource controller independently rehashes the complete staged file before inference. Only this file receives cache advice; no global cache flush or cold-host proof is claimed. Original 30 models and useful staged IQ4 are preserved.

The bounded Q4/Q5/Q6/Q8 headers have the same **733 tensor names/dimensions and 8,057-byte chat template**, SHA256 `55d4931433fe502b794226ee7f4d206a6bdd436ac9f80eb7d8ebb4c639f9ea0c`. Tensor quantization mixes differ. Each records quantization version 2 without importance-matrix metadata; absence does not prove identical calibration or unquantized weights. No local quantization is performed.

Runtime uses current owner-derived evaluator `c9b40eb8dea441cba7ded2e6589e5c011545ffc1ec76a0dc736f8e399d8f947b` and llama.cpp `fee4289628e7ba09f6fbf62d6ce4325aebb2531ffde2154d41276fe4acc58da3`, build b12723-abca69200. Context 98,304, one slot, q4_0 K/V, two checkpoints, 512 MiB RAM cache, load mode `none`, fit off, requested ngl 99, eight CPU/batch threads, batch 512, ubatch 128 and poll 0 match the current Fable Q6/Q8 capacity settings. Each request uses temperature 1, top-p 0.95, top-k 20, min-p 0, repeat penalty 1, presence penalty 0, thinking enabled, seed 20261123 and output cap 16,384. Every rendered input plus reserved output fits below the loaded context. The 80k request reserves 16,384 output tokens with 1,990 further tokens of headroom; its actual output is much shorter. This is not coherent reasoning validation across the entire trained context.

The backend becomes ready in **75.44 seconds**. Logs measure **9,051.81 MiB GPU model / 333.44 MiB host model / 540 MiB GPU KV / 229.01 MiB GPU compute / 28.01 MiB host compute**. Across 76 five-second samples, aggregate charged study cgroups peak at **7,023,349,760 bytes**, process PSS at **1,721,315,328 bytes**, and study swap remains zero. No measurement error, budget guard or CUDA OOM occurs. These overlapping memory views are not added together. Whole-host swap moves by 14,918 input and 5,031 output pages without attribution to the study. Sampling can miss transient peaks.

Minimum measured original/staging free space is **111,278,829,568 / 112,956,198,912 bytes**, both above 100 GiB. Transfer admission requires space for the full file plus 105 GiB; the transfer and resource stage stop at 102 GiB on staging, while retaining the requested 100 GiB floor on the original filesystem. The alternate adapted 27B Q3_K_M remains unadmitted because its proposed staging margin is only about 2 GiB. The evaluator's implicit data volume is measured at 16 KiB, rather than explaining prior multi-GiB shared-disk fluctuations. No unowned Docker prune or useful-model deletion occurs.

| Current matched Fable capacity cell | Sampled GPU MiB | 16k seconds | 60k seconds | 80k seconds | Exact markers |
|---|---:|---:|---:|---:|---:|
| Q5_K_M | 10,224 | 39.57 | 155.92 | 101.64 | 2/3 |
| [Q6_K](resource-fable-q6-current-thinking.md) | 11,566 | 40.49 | 165.24 | 106.64 | 3/3 |
| [Q8_0](resource-fable-q8-thinking.md) | 14,624 | 47.29 | 156.51 | 102.79 | 2/3 |

These are single shared-host observations with reasoning-output and cache differences, not isolated throughput benchmarks or precision-only causality. Q5/Q8 load from the staging filesystem; retained Q6 loads from the original model mount. The [matched Q6/Q8 coding workflows](native-fable-q6-current-thinking-cold-beets.md) both fail. Q5's lower memory use or similar synthetic latency is not evidence it will complete the real contribution task.

Strict postflight verifies original container IDs/images/configuration/running state and restored alias/context, the full fresh Hermes-Codex snapshot, four owner settings hashes, all 30 original model metadata entries, both staged Q5/IQ4 metadata entries, owner pending/tracked files and ignored instructions. Exact terminal download/resource supervisors, their exclusively referenced anonymous volumes, backend and empty study network are removed. Both useful staged weights remain available. No issue or PR is opened by this resource-only test.

The [evidence archive](resource-fable-q5-current-thinking-evidence.tar.gz), [summary](resource-fable-q5-current-thinking-summary.json), [validation](resource-fable-q5-current-thinking-validation.json) and [privacy scan](resource-fable-q5-current-thinking-privacy.json) preserve synthetic request/response captures, numeric measurements, full hashes, header/calibration observations, controller/protocol and preservation/cleanup evidence. Owner credentials/settings contents, pending edits, private graders and model-agent conversations are excluded. The verifier derives actual tool arguments and assistant/tool-result history, requested/actual context headroom, resource limits and the failed 60k exact-match result. Four recomputed-manifest negative controls reject wrong tool arguments, fabricated assistant lineage, a 9 GiB host budget and a false exact-marker claim.

```sh
python3 evaluations/2026-11-24-gpu-quant/verify_current_fable_q5_resource.py evaluations/2026-11-24-gpu-quant/resource-fable-q5-current-thinking-evidence.tar.gz
(cd evaluations/2026-11-24-gpu-quant && sha256sum -c resource-fable-q5-current-thinking-evidence.sha256)
```

This verifies saved consistency, not fresh inference, actual configured MCP or code correctness. The next quality cell needs a new no-DB profile, actual SDK/code/configured-Gitea preflights, a fresh upstream fixture and the same natural coding/docs/cancellation requests, with independent published-source/test/docs/claim review and no corrective feedback. No autonomous-reliability or GPT-5-equivalence claim follows from these six capacity requests.
