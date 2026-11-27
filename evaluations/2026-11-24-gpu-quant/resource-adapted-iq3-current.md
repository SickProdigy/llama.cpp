# Current retained IQ3_XXS: 98k capacity admitted, coding quality pending

November 27: the retained Hermes-adapted 27B IQ3_XXS completes all six current
resource probes at **98,304 context**, without a fallback. The backend reports
**66/66 layers offloaded**, **12,904 MiB sampled GPU peak** and **521 MiB host
model buffers**. This is a measured mostly-GPU layout, not zero host allocation.
The short tool/history exchange and exact 16k/60k/80k markers pass. These are
synthetic capacity checks, not a Hermes coding or actual Gitea MCP result.

| Probe | Input tokens | Cached input | Output tokens | Seconds |
|---|---:|---:|---:|---:|
| Actual named tool call | 293 | 0 | 28 | 24.20 |
| Actual tool result completion | 356 | 320 | 30 | 3.98 |
| Dependent history followup | 412 | 385 | 6 | 1.92 |
| Exact 16k marker | 16,152 | 0 | 9 | 271.56 |
| Exact 60k marker | 59,937 | 16,084 | 9 | 870.56 |
| Exact 80k marker | 79,932 | 59,869 | 9 | 463.15 |

The tool result is attached to the model's actual assistant/tool-call record;
the subsequent assistant answer is retained rather than fabricated. The final
followup returns exactly `tool-history-capacity-ok`. There is no configured
forge lookup or actor profile in these probes. Their small outputs do not
establish long-output reasoning or complete-context correctness.

The selected layout requests all GPU layers (`-ngl 99`), ubatch 64, batch 512,
eight CPU threads, one slot, q4_0 K/V, two cache checkpoints, 512 MiB cache RAM,
load mode `none` and automatic fit off. The registered 64k fallback is permitted
only after an actual CUDA allocation failure; it was not used. Backend readiness
takes 65.57 seconds. Full file length/SHA verification precedes inference.
Selected-file cache pages are measured inactive after original services stop;
that does not prove a universally cold host or driver cache.

Actual buffers are **10,136.68 MiB CUDA model / 521 MiB host model**,
**1,728 MiB GPU KV**, **408.50 MiB GPU compute / 17 MiB host compute**.
Recorded free GPU memory is about 3,371 MiB. Across 319 five-second samples,
aggregate charged cgroups peak at **7,024,836,608 bytes**, process PSS at
**2,267,031,552 bytes**, with zero study swap, guards or measurement errors.
Charged file cache and relevant helpers are included; transient peaks can be
missed. Whole-host swap counters move and are not attributed to the study.
Both actual filesystems remain above the 100 GiB reserve.

The live engine records a Tesla P100-PCIE-16GB, NVIDIA driver 535.261.03,
an i7-8700 host and Docker 29.10.1. Timing shares an active host. The backend is
the pinned current image
`fee4289628e7ba09f6fbf62d6ce4325aebb2531ffde2154d41276fe4acc58da3`;
the C9 supervisor/observer image is pinned separately in the evidence. Resource
requests use temperature 0.8, top-p 1, top-k/min-p 0, repeat penalty 1,
presence penalty 0, thinking off, seed 20261123 and an 8,192 output cap.

The exact retained artifact is `Qwen3.8-27B-hermes-IQ3_XXS.gguf`,
**11,637,692,064 bytes**, SHA256
`390a54c26ed8fc42a558f073e5745b7c0c1922086bbcc07e2e6357a7b527c345`.
Its original download revision is `6a786a26437f9210d5da0954208c7335ee0a55e1`;
the same advertised file hash is recorded at the comparison's
[netprojects revision 10fdf357](https://huggingface.co/netprojects/Qwen3.8-27B-hermes-adapted-GGUF/tree/10fdf357f14825c61ad7eb42a932e1f1e4390e8f).
No new weight was downloaded or quantized for this stage.

A bounded read of this actual retained file confirms 866 tensors and
importance-matrix metadata `imatrix.gguf`, `imatrix-calib.txt`, 496 entries and
150 chunks. Current Q4/IQ4/IQ3 headers match tensor names/shapes and chat-template
hashes, but tensor type mixes differ. IQ4 records 104 chunks of `calib-train.txt`;
Q4 has no recorded imatrix metadata. Missing metadata is not proof no matrix
was used, and equal shapes/templates do not establish identical unquantized
weights. An older generically labeled `q3` header is not substituted for this
actual IQ3_XXS header.

| Current layout | 16k seconds | 60k seconds | 80k seconds | Sampled GPU MiB |
|---|---:|---:|---:|---:|
| Q4_K_M, 56/66 GPU, ub128 | 198.40 | 663.77 | 369.64 | 15,456 |
| IQ4_XS, 63/66 GPU, ub64 | 247.09 | 804.16 | 428.05 | 15,926 |
| IQ3_XXS, 66/66 reported GPU, ub64 | 271.56 | 870.56 | 463.15 | 12,904 |

These are observed practical layouts, not a precision-only causal experiment:
calibration, tensor mixes, placement, microbatch and cache reuse differ. The
smaller IQ3 has more GPU headroom but was not faster on these prompts. Cached
60k/80k requests are not uncached prompt benchmarks. Q4 and IQ4's completed
coding workflows fail; this resource-only IQ3 result supplies no quality winner.

Original alias/context, container identities/images/configurations, four profile
hashes, all 30 retained model metadata records and pending owner edits pass
independent post-run checks. **Hermes-Codex's entire recorded state matches this
stage's fresh baseline**, including start time. This does not erase the
[earlier IQ4 timestamp exception](native-adapted-iq4-current-r2-cold-beets.md).
Staged IQ4 metadata is unchanged. Exact study containers/network and the
supervisor's exclusively attached anonymous volume are removed; model storage
is retained. Post-stage free space is about 103.75 GiB on original-model storage
and 115.15 GiB on staging.

The [60-file archive](resource-adapted-iq3-current-evidence.tar.gz),
[summary](resource-adapted-iq3-current-summary.json),
[validation](resource-adapted-iq3-current-validation.json) and
[privacy scan scope/result](resource-adapted-iq3-current-privacy.json) retain
actual requests/responses, numeric samples, source pins and bounded header
metadata. Inputs are synthetic; no actor conversation, credential, profile or
private behavioral grader is included. The standalone verifier rederives tool
arguments, actual history lineage, markers, response hashes, context headroom,
placement, memory/reserve limits and restoration from saved observations.

From the repository root:

```sh
python3 evaluations/2026-11-24-gpu-quant/verify_current_adapted_iq3_resource.py evaluations/2026-11-24-gpu-quant/resource-adapted-iq3-current-evidence.tar.gz
(cd evaluations/2026-11-24-gpu-quant && sha256sum -c resource-adapted-iq3-current-evidence.sha256)
```

This validates saved evidence, not new inference or code correctness. The next
step is a fresh native coding/documentation/cancellation conversation with actual
configured Gitea issue, fork and PR actions, isolated from prior graders and
results. No autonomous-reliability or GPT-5-equivalence claim follows from these
six probes.
