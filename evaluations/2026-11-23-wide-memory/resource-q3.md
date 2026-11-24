# Adapted27B public Q3_K_M resource stage

Completed November 24, 2026. The pinned public Q3 file completes all four
resource/template/history probes at 98,304 context on the P100. **This is not a
coding or Gitea task-quality pass.** A separate fresh native coding workflow
starts only after this stage restores and independently verifies the originals.

| Probe | Actual input tokens | Output tokens | Seconds | Recorded answer |
|---|---:|---:|---:|---|
| Defined lookup tool | 293 | 28 | 18.17 | Correct function and arguments |
| Dependent tool-history followup | 374 | 6 | 2.40 | Exact returned code |
| Synthetic 16k | 16,152 | 9 | 157.62 | Exact final marker |
| Synthetic 60k | 59,937 | 9 | 572.80 | Exact final marker |

The 60k request retains 16,020 cached tokens and processes 43,917 new tokens.
These are complete recorded bodies with measured rendered/tokenized input,
not cold-prefill benchmarks. Main output reserve is 8,192; actual outputs are
short. Synthetic markers and one artificial tool do not establish coding,
MCP routing or long-conversation reliability.

The first declared layout succeeds: non-mapped loading, requested `-ngl 99`,
q4 K/V, one slot, batch512/ubatch128, eight CPU threads, fit disabled,
512 MiB prompt cache and two context checkpoints. No fallback is used.
Backend image is `sha256:7561b4761f849925a728c5ac2bd1f4a649b6a76f24544e7f992b047ad016cec3`
(build `b12627-225a5345b`). The backend has a 6.5 GiB cgroup cap with zero
swap allowance; the aggregate guard is 8 GiB including the supervisor and
labelled experimental helpers. Requested placement is recorded; detailed
per-tensor allocation is not exposed in the retained verbosity-3 logs.

Across 155 complete aggregate samples, peak charged cgroups are **6.554 GiB**,
all-process PSS **2.189 GiB**, and GPU **14,946 MiB**, leaving at least
**1,329 MiB GPU free** in these samples. These independent peaks must not be
summed. Experiment swap, measurement-error samples and resource-guard samples
are all zero. Minimum observed host available memory is 30.65 GiB.
Global swap counters increase by 1,098 pages in and 16,259 out; those whole-host
changes cannot be attributed to this no-swap experiment. Cgroup accounting
includes charged cache/shared buffers; sampled cgroups/PSS do not prove a
continuous additional whole-host allocation bound.

Loading takes **59.22 s** after an independent full-file SHA read, followed by
DONTNEED advice for this specific study file. Download/cache state and ambient
host activity are uncontrolled; this is not a cold-cache proof. The direct
sampler is temperature0.8, top-p1, top-k0, min-p0, repetition1, presence0,
with thinking disabled. The [Q3/Q4 calibration metadata differs](quant-header-preflight/README.md),
and earlier Q4 resource probes use different output caps/history sequence and
backend cap. Timing differences are observations, not a precision-only causal
or model-quality ranking.

## Public file pin

- Repository: `netprojects/Qwen3.8-27B-hermes-adapted-GGUF`
- Revision: `10fdf357f14825c61ad7eb42a932e1f1e4390e8f`
- File: `Qwen3.8-27B-hermes-Q3_K_M.gguf`, 13,752,764,064 bytes
- SHA256: `a0c809f93de2bcd813e1b6fbd5c2d1f692821814a4261a316f7c8bca9cf23248`

The anonymous pinned download and independent on-disk resource hash both match.
Only one additional large study weight is present. The 29 original model entries
are unchanged; the study-owned Q4 was temporarily retired before this download
and remains reproducible from its public pin. No original model was deleted.

## Restoration and evidence

At the end of this resource stage, all three original service IDs, images and
configurations, four profile hashes, owner pending files/instructions and the
entire Hermes-Codex snapshot are independently verified preserved. The original
VibeForged alias and 98k context are restored; 110.56 GiB is free. The owned
backend, supervisor and empty resource network are removed. The next native
stage has its own restoration obligation; this historical resource restoration
is not a statement that no later GPU experiment is running.

[Summary](resource-q3-summary.json), [archive](resource-q3-evidence.tar.gz),
[SHA256](resource-q3-evidence.sha256), [privacy scan](resource-q3-privacy.json)
and [validation](resource-q3-validation.json) retain the synthetic requests,
complete responses, raw numerical memory samples, frozen source/protocol and
restoration audits. No native actor profiles, private tasks, graders, repository
source or credentials are exported.

```sh
python3 evaluations/2026-11-23-wide-memory/verify_candidate_resource.py q3
```

The verifier checks retained bytes, pins, observations and audit consistency.
It does not rerun inference or certify coding correctness. See the
[native matrix](matrix.md) for the separate quality outcome.
