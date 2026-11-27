# Adapted Q5/Q6: current transfer exclusion, not measured GPU fit

At **2026-11-27T09:45:50.899857+00:00**, the active Q3_K_M study's observer records **103.25 GiB** free on original-model storage and **102.00 GiB** on staging. Both filesystems have a **100 GiB minimum reserve**. Original 30 models and useful staged IQ4 remain protected.

The same pinned public checkpoint's Q5/Q6 artifacts cannot be downloaded onto either current filesystem while preserving that reserve. Even hypothetically reclaiming only the new Q3_K_M artifact before the download is insufficient:

| Artifact | Public bytes | Projected staging GiB after hypothetical Q3-only reclaim and download |
|---|---:|---:|
| Qwen3.8-27B-hermes-Q5_K_M.gguf | 19,535,701,664 | 96.62 |
| Qwen3.8-27B-hermes-Q6_K.gguf | 22,431,000,000 | 93.92 |

This arithmetic uses the actual storage observation and the pinned full public file lengths. It is **not** an actual retirement, download, CUDA allocation attempt, CPU-offload measurement or model quality failure. The Q3 file was active at the observation; no deletion decision is authorized by this audit. Free space can change afterward.

The [saved observation and pins](adapted-q5-q6-storage-exclusion-20261127.json) include the source API/revision, full advertised hashes and exact byte arithmetic. Original-model storage is also too close to the floor to admit either file. Adequate additional storage would remove this transfer exclusion; GPU/context/host-memory placement would still require a measured capacity stage. A large model file alone does not establish actual GPU allocation or exclude every partly CPU layout.

The [remaining public-quant horizon](additional-public-quant-horizon-20261127.json) pins untested Fable Q3, Vibe Q3 and Vibe Q8 text artifacts. The [full GGUF sibling metadata](additional-public-quant-metadata-20261127.json) distinguishes model weights from vision projectors and confirms that Vibe Q5 is absent at the selected revision only. Those alternatives are not admitted downloads, proved GPU fits or quality improvements. Already tested Fable Q8 is not counted as an untested alternative.
