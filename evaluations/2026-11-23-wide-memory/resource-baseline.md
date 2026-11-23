# Initial resource baseline and loading-memory caveat

The retained adapted 27B IQ3_XXS completed three resource probes at 98,304 loaded
context on the P100. **This is not a new agent-correctness result or proof of a
strict 8 GiB loading-memory fit.** A process-residency observation requires an
explicit loading-mode comparison before that claim.

| Probe | Actual input tokens | Output tokens | Seconds | Observed response |
|---|---:|---:|---:|---|
| Defined local test tool | 293 | 28 | 17.65 | Correct lookup_record call and arguments |
| Synthetic 16k capacity | 16,152 | 9 | 172.83 | Exact requested final marker |
| Synthetic 60k capacity | 59,937 | 9 | 608.85 | Exact requested final marker |

The tool is a parser/transport probe, not an actual Gitea operation. Simple final
marker retrieval is not a coding benchmark. All responses are complete and the
actual usage equals the template/tokenizer measurement. The last request reuses
16,020 cached tokens and processes 43,917 new tokens; its time is not cold 60k
prefill. Load readiness takes 85.46 seconds after a full model SHA read, which
warms file cache. A concurrent model download and ambient host activity are
uncontrolled. Do not attribute speed differences from older reports to model
precision alone.

## Effective configuration and memory observations

The current deployed backend was already image
`sha256:7561b4761f849925a728c5ac2bd1f4a649b6a76f24544e7f992b047ad016cec3`,
build `b12627-225a5345b`, when this study began. Earlier study reports used
b12464. This study did not update the production image. New comparisons pin the
current image and preserve that actual original runtime.

The baseline uses all GPU layers, q4 K/V cache, one slot, 512 MiB host prompt
cache, explicit fit-off, eight CPU threads and disabled CPU polling. Docker
memory and memory+swap limits both equal 8 GiB, leaving zero backend swap
allowance. There are 172 samples at approximately five-second intervals.

- Sampled peak total GPU use: **12,930 MiB**, minimum free **3,345 MiB**.
- Sampled active-inference process PSS peak: **1.27 GiB**.
- Process PSS peak across loading and inference: **8.93 GiB**, dominated by
  mapped file pages during loading.
- Charged cgroup memory peak: **8 GiB plus 256 KiB**, a small observed accounting
  overshoot retained in the evidence. Reclaimable file cache dominates much of
  this charge; it is distinct from process anonymous residency.
- Backend cgroup swap and process swap: **zero** in the collected samples.
  Global host swap counters change and include unrelated services; those deltas
  do not prove that the model swapped.

A cgroup limit alone does not prove an equal process-residency limit when shared
mapped pages were charged elsewhere. PSS is also not the same as additional
whole-host physical allocation. Neither interpretation is hidden by calling the
probe a fit. [Protocol v2](resource-protocol-v2.json) registers explicit
`--load-mode none`, supported by this pinned backend, a sampled PSS budget guard,
and a matched baseline retest. It keeps the other primary resource parameters
and bounded Q4 layout search. This amendment precedes all Q4 inference and all
scored actor calls. It is an accounting diagnostic, not a quality-score rerun.

## New model and preservation

The public Q4_K_M download completes with 16,810,714,560 bytes and transfer SHA256
`6512bb1c2595575fc0aed39b7d72a6aaf71084b1164b5d3749f87a6c2a3d3bf3` from pinned
revision `10fdf357f14825c61ad7eb42a932e1f1e4390e8f`. The controller rehashes actual
on-disk weights before GPU use. Download alone proves neither runtime fit nor
agent correctness. Approximately **108.3 GiB** remains free after the download.

Original Hermes/VibeForged runtime is restored. IDs/images/configuration,
four profile hashes, all 29 pre-existing model inventory entries, owner pending
files and ignored instructions match the starting snapshot. Hermes-Codex's
entire snapshot is unchanged. Only the new study-owned Q4 file is added. The
exact exited baseline supervisor, backend and internal network are removed;
the completed download container is also removed. No global prune/cache flush
or swap reset occurs.

[Summary](resource-baseline-summary.json), [preservation](resource-baseline-preservation.json),
[owner preservation](resource-baseline-owner-preservation.json),
[artifact validation](resource-baseline-artifact-validation.json),
[archive hash](resource-baseline-evidence.sha256) and
[privacy scan](resource-baseline-privacy.json) accompany the evidence.
The preservation snapshot was captured while the new download was still partial;
the completed file is recorded separately in [download status](download-status.json).
No original weight is removed.

Verify the archive hash, extract it to a new directory, then run:

```bash
python3 verify_resource_baseline.py --root /absolute/path/to/extracted
```

This validates all manifested bytes, source registration, three complete
responses, actual input counts and memory observations, including the loading
overshoot. It performs no new inference and certifies no agent behavior. Source
launch code expects this study's runtime names and restoration contract; do not
rerun completed queues or run that controller unchanged against another setup.
Private native profiles, coding tasks, graders, references and issuer keys are
excluded. The goal remains active for v2 resource pilots and full native
coding/Gitea workflows.
