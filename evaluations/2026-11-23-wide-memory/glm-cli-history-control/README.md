# GLM client history control

November 23, 2026. Passed a CPU-only, scripted-response integration control
through two real Hermes CLI processes, a real harmless terminal tool call,
normal session discard, persisted resume, and a dependent user followup.
Three captured outgoing requests retain the scripted reasoning before and
after the followup, and serialize `enable_thinking: true`,
`clear_thinking: false`, and the 16,384-token output cap.

This does **not** run GLM weights, its embedded llama.cpp template, GPU kernels,
the normal complete tool profile, or Gitea. It establishes client history
retention only; runtime compatibility, memory fit and coding quality remain
pending. An earlier operator attempt stopped on a SQL typo after the first CLI
process; it is not a model failure.

The tested image is
`sha256:97b08c5ce375113809299fc8c5dd86ae60600f618158d15fe4ad5fc9d7f4b7ae`.
To repeat, mount an empty writable directory at `/results` and `run_control.py`
read-only at `/control.py` in that image; run `python /control.py` as UID 1000
with network disabled, runc, no GPU, read-only root, writable `/tmp`, and
512 MiB memory with the same memory-swap limit. The HTTP server is loopback
inside the container. The script creates its own minimal dummy-key profile.

`wire-projection.json` omits system/user messages and contains only scripted
assistant sentinels, terminal results and selected request settings. Raw CLI
logs, full requests, profiles and databases remain private. This projection
allows checking the retention claim without publishing unrelated system text.
Run `python3 verify.py` in this directory to verify hashes and retained fields;
that verifies the saved evidence, not a new CLI execution or model quality.
