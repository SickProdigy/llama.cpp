# Adapted 27B public quant header comparison

November 23, 2026, before full Q3 download or inference. This is metadata
inspection, not a model quality or memory-fit result.

The pinned Q3_K_M and Q4_K_M files have identical tensor names/shapes and
byte-identical tokenizer metadata, including token arrays and chat template.
All non-quantization metadata matches. Quantization type and four importance
matrix metadata fields differ: Q3 reports `imatrix.gguf`, `imatrix-calib.txt`,
496 entries and 150 chunks; Q4 has no corresponding fields. Missing metadata
does not prove which quantization procedure was actually used. Quality
differences cannot be attributed solely to bit precision, and matching headers
do not prove identical source weights.

Both files are from
[`netprojects/Qwen3.8-27B-hermes-adapted-GGUF`, revision `10fdf357f14825c61ad7eb42a932e1f1e4390e8f`](https://huggingface.co/netprojects/Qwen3.8-27B-hermes-adapted-GGUF/tree/10fdf357f14825c61ad7eb42a932e1f1e4390e8f).
Full-file sizes and advertised SHA256 values are pinned in
[public-model-metadata.json](../public-model-metadata.json). Q4 was independently
fully hashed before its resource/native stages; this preflight does not hash
the complete Q3 file. Q3's prefix was fetched with HTTP206; Q4's prefix was read
from the retained, previously verified study model.

To reproduce, run `python3 verify.py --fetch` here. This fetches exactly two
16 MiB public prefixes with required HTTP206 range/size and SHA256 checks;
it does not download full weights. It then checks the complete metadata and
tensor descriptor fingerprints against `expected.json`. Alternatively pass
`--prefix-root DIR` containing `q3-header/prefix.bin` and
`q4-header/prefix.bin`; no network is used without `--fetch`.

The result verifies saved header observations only. GPU/host allocation,
latency, actual tool parsing and fresh coding/Gitea quality remain separate
measurements. No private prompts, graders, profiles or signing keys are included.
