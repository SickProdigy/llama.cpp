# Real-code model comparison — November 20, 2026

User authorized testing VibeForged and FableVibes on Gemma's real-code task and
emphasized inferring Gitea routing without repeated user reminders.

## Matched real-code tasks

Use the retained Gemma symptom-led prompt, guard and focused plugin 0.1.3.
Change only model, run identifier and unique feature branch. Existing public
Q4_K_M VibeForged v2 and FableVibes weights; no downloads or quantization.
98,304 context, one slot, q4 K/V, temperature .2, 4,096 output cap, 600 seconds,
28 calls, fresh copied Hermes profile per conversation. Same original images.
Read/write MCP account is cloned into an isolated MCP service. Production
Hermes and llama.cpp are stopped during the GPU trial and restored afterward.
Hermes-Codex is separate and untouched. No Discord messages are sent.

Only autospamignore/__init__.py may change, on the designated personal-fork
branch. The model must read source, investigate the reported infinite-setting
exception, open an upstream issue and PR, and return verified resource URLs.
Issue/PR text and patch are model-authored. Off-task tools/targets, default
branch writes, merges and settings changes are blocked before RPC. Permit one
ordinary invalid-argument correction; stop repeated invalid or identical calls.
No operator hints or repairs. One code commit maximum. Leave test resources
open for review, including failed runs; do not count an existing issue as a new
issue-write success. Repeated issue creation here is an authorized benchmark.

## Implicit routing probes

Separate fresh sessions ask exactly: `Find my SonicRatings repo and tell me
what it does.` No hosting service or tool instructions appear in that request.
Same focused interface and persistent owner-repository Gitea preference,
180 seconds / 12 calls, read-only task intent; attempted writes are blocked
rather than silently removing write tools. Measure routing separately from
whole-answer factual grounding. Focused routing does not establish native
multiplexed-tool reliability or prove a permanent change to live configuration.

## Verification

Retain complete prompts, schemas, calls, requests, source hashes, time/VRAM and
sanitized evidence. Independently inspect issues, fork branch/code and upstream
PR/diff where created. Before executing a model-authored helper, inspect its
patch. Test both infinity signs, NaN, invalid values and ordinary clamping.
These isolated helper checks do not establish live Nicotine+ integration.
Confirm upstream main unchanged and original runtime/profile restored. Remove
only exact task-owned containers/volumes and private snapshots after exporting
sanitized, hash-verified evidence.
