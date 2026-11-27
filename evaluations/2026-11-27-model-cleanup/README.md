# User-authorized model cleanup

Removed the existing Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf after the owner authorized cleanup of slower models. This 22,360,456,160-byte model needs CPU expert offloading and showed no clear advantage over compact candidates in the November 19 comparison; later complete coding controls did not qualify it for unattended work. This is a hardware/workflow retention decision, not a universal model-quality claim.

All 29 other GGUF files, including every VibeForged/FableVibes variant and small helper model, have unchanged file identities. No production service was restarted. Exact identity, full pre-removal SHA-256 and observed disk space are in retirement.json. This explicit inventory change supersedes prior preserve-original30 requirements for this one file; historical preservation results remain scoped to their original runs.
