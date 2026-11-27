# Current adapted 27B IQ4_XS: 98k capacity passes with limited CPU spillover

The first [native attempt](native-adapted-iq4-current-interrupted.md) was interrupted by the staging-disk reserve guard without a quality verdict. The separate [fresh retry](native-adapted-iq4-current-r2-cold-beets.md) now completes and fails the published workflow. Capacity remains measured independently of coding correctness.

November 27: the retained public IQ4_XS completes all six current-runtime probes
at **98,304 context / 63 of 66 reported layers on GPU / ubatch 64**. All-GPU
allocation fails; 65/66 loads but its first inference request hits CUDA allocation
failure. The registered next layout, 63/66, completes with correct tool arguments,
real tool-history followups and exact 16k/60k/80k markers. No coding/Gitea quality
qualification is claimed. The next stage is a fresh three-turn natural workflow.

| Probe | Input / output tokens | Cached input tokens | IQ4 seconds | Current Q4 seconds |
|---|---:|---:|---:|---:|
| Defined tool call | 293 / 28 | 0 | 23.68 | 35.96 |
| Actual tool result | 356 / 37 | 320 | 6.67 | 8.10 |
| Dependent followup | 419 / 6 | 392 | 2.19 | 2.91 |
| 16k retrieval | 16152 / 9 | 0 | 247.09 | 198.40 |
| 60k retrieval | 59937 / 9 | 16084 | 804.16 | 663.77 |
| 80k retrieval | 79932 / 9 | 59869 | 428.05 | 369.64 |

Long-prompt timings reuse previous input; they are not uncached throughput
benchmarks. Q4 caches 16,020 tokens for the 60k probe versus IQ4's 16,084. Actual
rendered inputs match. Q4 uses 56/66 layers and ubatch 128, whereas IQ4 uses 63/66
and ubatch 64. IQ4 is faster for the short tool exchange and slower for these large
prompts. Placement, batching and calibration differ, so no precision-only causal
or general performance claim follows. The host is shared with other workloads.

Selected buffers are **13,122.69 MiB GPU model**, **1,250.63 MiB host model**,
1,728 MiB GPU KV, 451.91 MiB GPU compute and 17.50 MiB host compute. This is
mostly GPU inference with explicit CPU spillover, not a fully GPU-resident model.
Q4's measured host model buffer is 2,982.90 MiB. Layer counts do not establish equal
shares of model arithmetic. The smaller file and lower host buffer do not prove
faster practical task completion.

Across **299 five-second selected-layout samples**, peak GPU is
**15,926 MiB**, aggregate study cgroups **7,028,965,376 bytes**,
and process PSS **3,209,647,104 bytes**. Cgroups include charged file cache and
helpers; PSS and cgroup maxima must not be summed. There are zero observed
measurement errors, budget guards and study swap. Whole-host swap counters do
change and cannot be attributed to the study. Sampling can miss transient peaks.
Minimum original/staging free space is 111,675,060,224 /
110,408,265,728 bytes, both above the 100 GiB reserve.

Every probe reserves its requested 8,192 output tokens inside the allocated
context; largest actual input is 79,932 tokens. Outputs are short. This does not
establish long-output coding reliability or useful answers across a full 98k
conversation. The separate older 64k all-GPU result remains historical evidence;
this run selects the first complete registered 98k layout and never reaches the
61-layer or 64k fallback candidates.

The failed layouts, actual CUDA error logs and selected placement are retained.
All-GPU fails before readiness; 65/66 reaches readiness then fails its first
request. Neither is a model-quality failure. Readiness alone therefore did not
prove inference fit. No hidden automatic context or placement fallback was used.

The exact file is `Qwen3.8-27B-hermes-IQ4_XS.gguf`, **15,321,491,104 bytes**,
SHA256 `d25b50a2bfdfba157c2baf959f298d706d70083255bab95232ffcd40fbafcaba`,
from [netprojects revision 10fdf357](https://huggingface.co/netprojects/Qwen3.8-27B-hermes-adapted-GGUF/tree/10fdf357f14825c61ad7eb42a932e1f1e4390e8f).
A fresh whole-file hash matches before model calls. Header comparison verifies
866 equal tensor names/shapes and an equal chat-template hash against Q4. Tensor
quantization types differ; IQ4 records `imatrix.gguf`, `calib-train.txt`, 496
entries and 104 chunks, while Q4 lacks recorded imatrix metadata. Equal names,
shapes and template do not prove identical pre-quantization weights or numerical
equivalence. Preserve this production/calibration distinction in quality claims.

Both current capacity cells use llama.cpp b12723/fee, non-mapped loading,
q4_0 K/V, one slot, two cache checkpoints, 512 MiB host prompt cache, fit off,
eight CPU threads, temperature .8/top-p 1/top-k 0, thinking disabled and 8,192
output caps. Backend cap is 6.5 GiB with aggregate study cap 8 GiB and no study
swap. The inactive selected file's kernel page residency is zero before the
first allocation attempt; subsequent failed-layout retries may reuse warmed
pages. Load timings are not a cold-fallback benchmark.

After completion, independent checks verify original runtime identities/images,
configuration and running state, original alias/context, four owner profile
hashes, all 30 retained model metadata entries, pending owner source/instructions
and the complete recorded Hermes-Codex state. Exact owned supervisor, backend
and network cleanup passes. No weights were downloaded or deleted in this stage.

Reproduce the saved-evidence validation with:

```sh
python3 verify_current_adapted_iq4_resource.py resource-adapted-iq4-current-evidence.tar.gz
```

The verifier checks the manifest, frozen controller/protocol/cache-helper hashes,
actual layout order/CUDA failures/placement, sampled memory/reserves, response
hashes/token headroom, marker observations and actual assistant/tool-history
lineage. It validates saved observations, not fresh inference, coding or Gitea
correctness. Its green result must not be read as model qualification.

[Summary](resource-adapted-iq4-current-summary.json),
[evidence archive](resource-adapted-iq4-current-evidence.tar.gz),
[SHA256](resource-adapted-iq4-current-evidence.sha256),
[validator](verify_current_adapted_iq4_resource.py),
[validation](resource-adapted-iq4-current-validation.json), and
[privacy scan](resource-adapted-iq4-current-privacy.json).

The archive contains synthetic requests/responses, numerical observations and
source for the bounded resource pilot. It contains no actor coding session,
private grader/reference answer, owner credentials or full owner profile.
