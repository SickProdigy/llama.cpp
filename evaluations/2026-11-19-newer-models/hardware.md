# Hardware decision notes

The live host reports an ASRock B365 Pro4, Intel i7-8700, approximately 62.5 GiB
RAM, and Tesla P100 PCIe 16 GiB. The GPU driver observed before this cohort is
535.261.03. During an active test, the P100 negotiated PCIe Gen3 x16
(current/max generation 3/3, current/max width 16/16). No driver, production image, motherboard, or GPU change is made.
The user's one-word budget reply was interpreted as a tight budget; country
and an exact spending ceiling are unknown. No purchase is authorized.

## Recommendation before results

Keep the existing P100 until the additional comparisons show whether accuracy,
memory or speed is the limiting factor. Quantization can reduce storage and
VRAM, but cannot be assumed to improve tool judgment. A larger/faster GPU
allows different weights, less compression or less CPU offload; it does not
repair missing issue bodies or mistaken upstream/fork identifiers by itself.

| Option | What changes | Practical limit for this setup |
|---|---|---|
| Keep P100 16 GiB | No cost; already runs the tested compact candidates at 98k | Pascal requires a compatible CUDA-12 build; performance and future software support differ from newer RTX hardware |
| Used RTX A4000 16 GB | Ampere, 140 W board power; same nominal VRAM | A software/platform and possible speed upgrade, not a capacity upgrade; no measured speedup is claimed |
| Used RTX 3090 24 GB | More single-card memory, Ampere; 350 W reference board power | A meaningful capacity target if a good price exists, but budget, PSU, clearance and cooling remain unverified; 24 GB does not guarantee every model at 98k |
| Used Tesla P40 24 GB | More memory, still Pascal; 250 W maximum | A capacity experiment, not a clear speed or software-longevity upgrade; passive cooling needs appropriate airflow |
| RTX 3060 12 GB | Newer architecture, less memory than the current card | Not a direct capacity upgrade for the user's larger-model/context objective |

The board's second full-length PCIe slot is electrically Gen3 x4; the first is
x16. Thus adding a second GPU is physically plausible from board specifications,
but available slots, case space, power connectors and PSU capacity are not
verified. Combined VRAM is not a transparent single pool: llama.cpp must split
the model and keep its per-device caches/buffers within each card's limits.
A mixed-card arrangement over the lower-bandwidth slot may help capacity without
providing a speedup. These are deployment inferences, not measured dual-GPU results.

Prefer evaluating a single-card memory target before spending money on a mixed
setup. No current asking price or purchase recommendation is asserted: region
is unknown and available listings/auction bids are not completed sale prices.

## Primary sources checked

- [ASRock B365 Pro4 specifications](https://www.asrock.com/MB/Intel/B365%20Pro4/index.asp): x16/x4 dual-slot configuration.
- [llama.cpp multi-GPU documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md): splitting, device selection and memory considerations.
- [NVIDIA CUDA architecture support](https://developer.nvidia.com/blog/navigating-gpu-architecture-support-a-guide-for-nvidia-cuda-developers): CUDA 13 removes offline compilation for pre-7.5 architectures; older compatible builds continue to work.
- [NVIDIA architecture/toolkit/driver matrix](https://docs.nvidia.com/datacenter/tesla/drivers/latest/cuda-toolkit-driver-and-architecture-matrix.html): Pascal's last toolkit family is CUDA 12.x and last driver branch R580.
- [NVIDIA RTX A4000 datasheet](https://www.nvidia.com/content/dam/en-zz/Solutions/gtcs21/rtx-a4000/nvidia-rtx-a4000-datasheet.pdf): 16 GB and 140 W.
- [NVIDIA RTX 3090 specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/): 24 GB and reference-card power.
- [NVIDIA Tesla P40 product brief](https://images.nvidia.com/content/tesla/pdf/Tesla-P40-Product-Brief.pdf): 24 GB and 250 W.
- [NVIDIA P40 board specification](https://images.nvidia.com/content/grid/pdf/DA-09018-001_v10.pdf).
