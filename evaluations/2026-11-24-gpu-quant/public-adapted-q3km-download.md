# Public adapted27B Q3_K_M transfer and header audit

The public artifact is downloaded and its complete **13,752,764,064-byte** stream matches SHA256 **`a0c809f93de2bcd813e1b6fbd5c2d1f692821814a4261a316f7c8bca9cf23248`**. Transfer time **20.44 minutes**. The exact download helper and exclusive anonymous volume are removed. **GPU fit, context performance and coding/Gitea quality remain untested.** No production model/default change.

Public [netprojects artifact revision](https://huggingface.co/netprojects/Qwen3.8-27B-hermes-adapted-GGUF/tree/10fdf357f14825c61ad7eb42a932e1f1e4390e8f): `Qwen3.8-27B-hermes-Q3_K_M.gguf`; revision `10fdf357f14825c61ad7eb42a932e1f1e4390e8f`. Publisher file size/LFS SHA and Git blob ID `41dea4be62b59d1c3bdde40e5b8424609aabcc18` were checked before transfer. Worker/policy SHA bindings were checked inside the isolated no-GPU downloader. No conversion/custom quantization, overwrite, silent resume or parallel model transfer.

## Actual metadata and qualifications

The completed-file bounded header has866 tensors, general file type12, and a9,004-byte chat template with SHA256 `af16f654968d47d09a6c604e00370b12dbc21f76456f59c9e98b82e84d9f6375`. Tensor names/dimensions and template match the independently captured retained IQ3_XXS/Q4_K_M and staged IQ4_XS headers. Tensor type mixtures differ; raw counts are in the archive.

| Artifact | Recorded importance-matrix dataset | Entries / chunks |
|---|---|---:|
| New Q3_K_M | `imatrix-calib.txt` |496 /150|
| Retained IQ3_XXS | `imatrix-calib.txt` |496 /150|
| Staged IQ4_XS | `calib-train.txt` |496 /104|
| Retained Q4_K_M | No imatrix keys recorded |Unknown|

Matching names/counts do not prove identical calibration contents or unquantized source weights. Missing keys do not prove no importance matrix was used. This is a public tensor-family/production comparison, not an isolated precision ablation. No GPU residency is inferred from file size or the Q3 label.

## Reserve and preservation evidence

The [new prospective transfer policy](prospective-adapted-q3km-current.json) requires102GiB post-file staging admission and102GiB original admission; both stop at101GiB, above the user100GiB minimum. Earlier105/102 margins and historical results are unchanged. Final staging/original free observations are **102.02/103.31GiB**. Shared-root use can change these values; no future GPU admission is implied.

The separately documented [failed study-added Q5 retirement](study-owned-q5-retirement.md) funded this transfer. All30 original models and useful staged IQ4 remain unchanged; new Q3_K_M is the only added weight. Fresh independent postflight verifies all three original runtime records, including full recorded Hermes-Codex state, four owner setting hashes, original loaded alias/context and owner pending tracked files/ignored instructions unchanged. Original services remained running; no GPU/model/actor calls or Gitea fixture mutations occurred in this transfer stage.

Cleanup verifies exact terminal0/non-OOM helper `3c32f823…`, its name/image/label, exclusive anonymous `/opt/data` volume reference and absence afterward. The named model staging volume remains. No general Docker prune or owner-setting change.

## Next measurement

A prepared, unlaunched resource protocol tries98k/all66GPU first with ubatch64/q4 K/V. Only actual CUDA allocation OOM permits the declared98k65/66 or64/66 layer layouts;64k/allGPU is the final allocation fallback. CPU buffers/context changes must be recorded. Host/cache/helper cgroups/PSS, swap, actual layer placement, headroom and latency must pass fresh admission before any native coding trial. Request controls match the adapted-family reference, not the different Fable sampler. No resource source is frozen or launched by this transfer result.

## Reproducibility

[Summary](public-adapted-q3km-download-summary.json), [archive](public-adapted-q3km-download-evidence.tar.gz), [SHA256](public-adapted-q3km-download-evidence.sha256), [validation](public-adapted-q3km-download-validation.json), [known-value privacy](public-adapted-q3km-download-privacy.json).

```sh
python3 verify_public_adapted_q3km_download.py public-adapted-q3km-download-evidence.tar.gz
```

The verifier checks saved full-stream identity, policy/source bindings, actual headers, reserve/preservation flags and exact cleanup consistency. Four recomputed-manifest controls reject wrong SHA, false Codex preservation, a stale IQ3 header and a violated transfer floor. It does not re-hash an absent weight file, replay inference, or repeat live owner/remote inspection. Private profiles/credentials/graders and raw actor conversations are excluded. This is not a tenth coding result, a reliability finding or GPT5 equivalence.
