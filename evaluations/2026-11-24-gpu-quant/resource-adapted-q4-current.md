# Current adapted 27B Q4: measured 98k fit with CPU spillover

November 26: the retained public Hermes-adapted 27B Q4_K_M completes all six
capacity requests on current llama.cpp b12723/fee at **98,304 context with 56/66
reported layers on GPU**. Peak sampled GPU is **15,456 MiB**, with 819 MiB free.
An all-GPU attempt at the same context first fails actual CUDA allocation before
any inference; backend exit 1, no host cgroup OOM kill. Both layouts and logs
are preserved. The untried 52/48-layer fallback layouts are not results.

The registered protocol tries all GPU first and allows only explicit fallback
after observed CUDA allocation OOM. Automatic fit is off, q4_0 KV, one slot,
checkpoints 2, cache RAM 512, non-mapped loading, eight CPU threads/CPU quota,
backend cap 6.5 GiB and aggregate study guard 8 GiB; swap is disabled. The
sampler matches the prior useful Q4 configuration: temperature .8/top-p 1/
top-k 0, thinking off, 8,192 output headroom. This differs from the Fable reasoning
profile; it is not a precision-only comparison across checkpoints.

GPU model buffers are **12,787.45 MiB**, host model **2,982.90 MiB**;
GPU KV **1,512 MiB**, CPU KV **216 MiB**; GPU compute **544.75 MiB**, host
compute **34.12 MiB**. About 81.1% of reported model-buffer bytes are on GPU;
layer counts do not imply the same share of compute. The CPU portion executes
inference, not merely weight storage. This layout satisfies the mostly-GPU plus
bounded-host target, but it is not fully GPU-resident.

## Actual probes

| Request | Input tokens | Cached input | Seconds |
|---|---:|---:|---:|
| Tool call | 293 | 0 | 35.96 |
| Actual tool result | 356 | 320 | 8.10 |
| Dependent followup | 417 | 390 | 2.91 |
| 16k marker | 16,152 | 0 | 198.40 |
| 60k marker | 59,937 | 16,020 | 663.77 |
| 80k marker | 79,932 | 59,805 | 369.64 |

The actual tool call has correct name/arguments, its real response/history is
retained, and the dependent followup returns the exact code. All three marker
answers are exact. These are short synthetic checks, not code or MCP publication
quality. Each requested input plus 8,192 output fits the measured window; actual
usage also fits. The 80k timing benefits from 59,805 cached tokens and is not an
uncached 80k benchmark. The 60k request takes 11.06 minutes despite cached input;
this cost matters for practical use. The earlier runtime's same 60k probe took
657.92 seconds versus 663.77 here, not evidence of a meaningful speed improvement.

Across **251 selected-layout samples** with five-second pauses: no measurement
errors, guard violations or study swap. Charged cgroups peak **7,020,060,672 bytes**;
process PSS peaks **5,322,948,608 bytes**. Charged file cache is included. Global
host swap counters move 2,435 input/69,286 output pages without study attribution;
the study's observed swap remains zero. Sampling may miss transient peaks.
The failed all-GPU layout has seven samples, no measurement errors or guard
violations; its CUDA allocation failure is not a quality score.

Selected-layout load time is 63.59 seconds. File-page residency is zero before
the first all-GPU attempt, but that failed load can warm pages before fallback;
the selected load is not a cold-storage benchmark. Hardware: Tesla P100 PCIe 16GB,
driver 535.261.03, Intel i7-8700 host, 12 logical CPUs/64 GB class host memory,
eight-CPU experiment quota. The host runs other services, so these are operational
timings rather than isolated hardware benchmark rankings.

## Pins, preservation and next comparison

The 16,810,714,560-byte retained file passes its full SHA256 before loading:
`netprojects/Qwen3.8-27B-hermes-adapted-GGUF`, revision
`10fdf357f14825c61ad7eb42a932e1f1e4390e8f`, file
`Qwen3.8-27B-hermes-Q4_K_M.gguf`, SHA256
`6512bb1c2595575fc0aed39b7d72a6aaf71084b1164b5d3749f87a6c2a3d3bf3`.
The bounded header records 866 tensors, qwen35 architecture, quantization
version 2 and chat-template hash. No imatrix metadata is present; that does not
establish calibration equivalence with another public quant. Advertised 262k
context is not measured here. No download, deletion or local quantization occurs.

Both disk reserves remain above 100 GiB. Actual postflight verifies restored
original IDs/images/configuration/alias/context, four owner profile hashes,
all 30 original model metadata entries, 40 owner files/pending edits and unchanged
Codex state. Free space is 104.14 GiB on the original model drive and 104.29 GiB
in staging. Exact owned backend/network and terminal supervisor are removed;
no study job remains. Owner settings and original weights are unchanged.

The prior [fresh Spam quality result](../2026-11-23-wide-memory/native-q4fresh-spam.md)
passes independent source/behavior/publication audits in 115.60 coding minutes,
on an older runtime. It remains a useful patient-work lead, not a current-runtime
or autonomous-reliability claim. Next is a fresh current C9/fee/transparent-recorder
coding/Gitea test on the same natural Beets lifecycle/docs/cancel requests used
for the smaller candidates, before attributing future Q5 differences to precision.

[Observations](resource-adapted-q4-current-summary.json),
[evidence archive](resource-adapted-q4-current-evidence.tar.gz),
[SHA256](resource-adapted-q4-current-evidence.sha256),
[validation](resource-adapted-q4-current-validation.json).
Saved-observation checks verify registered source bindings, both actual layouts,
CUDA OOM evidence, placement, hashes, headroom, memory and responses; they do not
rerun inference or private coding graders.

```sh
python3 verify_current_adapted_q4_resource.py resource-adapted-q4-current-evidence.tar.gz
sha256sum -c resource-adapted-q4-current-evidence.sha256
```
