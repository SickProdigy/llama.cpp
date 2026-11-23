# Adapted 27B Q4: measured resource pass, agent correctness still untested

The 16.81 GB public Q4_K_M file completes the registered resource probes with
98,304 context, 56 GPU layers and explicit `--load-mode none` on the P100.
**It is now eligible for the full native agent tests. This is not a coding or
Gitea-workflow pass.**

| Probe | Actual input | Output | Seconds | Result |
|---|---:|---:|---:|---|
| Defined test tool | 293 | 28 | 25.06 | Correct lookup_record function/arguments |
| Synthetic 16k | 16,152 | 9 | 194.90 | Exact final marker |
| Synthetic 60k | 59,937 | 9 | 657.92 | Exact final marker |

All three responses are complete. The final request retains 16,020 cached tokens
and processes 43,917 new tokens, so this is not cold 60k prefill. There are
185 approximately five-second memory samples. No layout fallback, caller replay,
controller error or memory guard occurs. The first registered layout succeeds.

Observed peak GPU use is **15,456 MiB (15.09 GiB)**, with **819 MiB minimum free**.
Process PSS peaks at **4.50 GiB**, and reported RSS high-water stays below 8 GiB.
Cgroup and process swap remain zero in the samples. The backend has an 8 GiB
memory cap and zero swap allowance; its reported charged-memory peak includes a
small 244 KiB accounting overshoot, retained in the evidence. Charged `file`
contains shared-memory model buffers as well as reclaimable cache: these are
reported separately, and independent peak columns must not be summed.

This addresses the mapped-loading PSS caveat in the [initial baseline](resource-baseline.md)
for this tested configuration. It does not prove an exact additional whole-host
allocation bound: driver/shared accounting and unrelated services remain outside
that simple interpretation. Global host swap counters change while backend swap
stays zero; the global delta cannot be attributed to this model alone.

Loading takes 75.45 seconds after the controller independently reads and verifies
the on-disk file SHA. That read warms file cache. The download had already
finished, but ambient host activity is uncontrolled. The [matched IQ3 test](resource-baseline-v2.md) with this explicit loading
mode is now complete. Its resource timings are observations with ambient-host
and cache limitations. Do not rank model quality from these short synthetic outputs.

## Identity and configuration

- Repository: `netprojects/Qwen3.8-27B-hermes-adapted-GGUF`, revision
  `10fdf357f14825c61ad7eb42a932e1f1e4390e8f`.
- File: `Qwen3.8-27B-hermes-Q4_K_M.gguf`, 16,810,714,560 bytes, SHA256
  `6512bb1c2595575fc0aed39b7d72a6aaf71084b1164b5d3749f87a6c2a3d3bf3`.
- Current pinned backend: image `sha256:7561b4761f849925a728c5ac2bd1f4a649b6a76f24544e7f992b047ad016cec3`,
  build `b12627-225a5345b`; no production image update was performed.
- q4 K/V, one slot, 512 MiB host prompt cache, batch512/ubatch128, eight CPU
  threads, polling disabled, fit-off, 512 output cap for these probes.
- Same direct sampler as the initial baseline; [protocol v2](resource-protocol-v2.json)
  was registered before Q4 inference. Native actor output/budgets are separate.

## Preservation and replay

The original VibeForged runtime is restored. Original container
IDs/images/configuration, four profile hashes, all 30 model inventory entries
(the 29 originals plus this new Q4), owner pending edits/instructions, and the
entire Hermes-Codex snapshot match the before-pilot state. Approximately
**108.29 GiB** remains free. The exact owned supervisor, backend and empty internal
network are removed. No original model was deleted, and no global prune or cache
or swap flush was performed.

See [summary](resource-q4-summary.json), [preservation](resource-q4-preservation.json),
[owner preservation](resource-q4-owner-preservation.json),
[validation](resource-q4-artifact-validation.json), [privacy](resource-q4-privacy.json)
and [archive hash](resource-q4-evidence.sha256). After checking the archive hash
and extracting to a new directory, run:

```bash
python3 verify_resource_q4.py --root /absolute/path/to/extracted
```

The verifier checks all manifested files, source/protocol registration,
complete responses, actual token counts, measured residency and launch settings.
It performs no new inference or semantic coding certification. As in the first
stage, private coding tasks/graders/references, native profiles and keys are
excluded. The next outcome to establish is correct multi-turn coding, tests,
documentation and actual upstream/personal-fork publication by the agent.
