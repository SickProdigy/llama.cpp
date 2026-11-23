# Matched non-mapped IQ3 resource baseline

The retained Hermes-adapted 27B IQ3_XXS completes the same three probes as
[Q4](resource-q4.md), using the current pinned b12627 runtime and explicit
`--load-mode none`. This resolves the initial mapped-loading PSS caveat for this
measured backend configuration. It is **not a fresh coding/Gitea result**.

| Probe | Input/output tokens | IQ3 seconds | Q4 seconds |
|---|---:|---:|---:|
| Defined tool call | 293 / 28 | 21.97 | 25.06 |
| Synthetic retrieval | 16,152 / 9 | 173.22 | 194.90 |
| Synthetic retrieval | 59,937 / 9 | 611.53 | 657.92 |

The tool arguments and both returned markers are independently verified. The
60k request reuses 16,020 cached tokens and processes 43,917 new tokens. These
are short outputs and partially cached prompts, not coding throughput scores.
Loading takes 61.69 seconds after a full on-disk hash read warms OS file cache.
Ambient services and separate CPU-only harness preflights are uncontrolled.
This is a matched layout observation, not a quantization-only causal experiment.

Across 170 samples, IQ3 peaks at **12,930 MiB GPU** and **1.87 GiB process PSS**;
minimum GPU free is 3,345 MiB. Sampled process/cgroup swap stays zero. The
8 GiB cgroup reports a 4 KiB peak overshoot, retained in the evidence. Charged
file memory includes shared buffers and cache; separate peak columns must not
be summed. Neither a cap nor samples prove exact whole-host allocation. Global
host swap counters change independently and cannot be attributed to this model.

The exact IQ3 SHA is
`390a54c26ed8fc42a558f073e5745b7c0c1922086bbcc07e2e6357a7b527c345`.
Both layouts use 98,304 context, q4 K/V, one slot, 512 MiB prompt cache,
fit-off, batch512/ubatch128 and eight CPU threads. IQ3 offloads all layers;
Q4 offloads 56. See the preregistered [v2 protocol](resource-protocol-v2.json).
The actual backend image remains
`sha256:7561b4761f849925a728c5ac2bd1f4a649b6a76f24544e7f992b047ad016cec3`.

Original services are restored and exact owned test containers/network removed.
Original configuration, four profile hashes, all 30 GGUF metadata entries,
owner pending work/instructions and the entire Hermes-Codex snapshot match.
The fresh audit finds **104.86 GiB free**; no model was added/deleted during
this pilot. Later native workflows reserve overhead with a 7 GiB backend cap
and measure the combined experimental runtime against 8 GiB, with an ongoing
100 GiB disk-reserve guard. That differs from these backend-only pilots.

See [summary](resource-baseline-v2-summary.json),
[preservation](resource-baseline-v2-preservation.json),
[owner audit](resource-baseline-v2-owner-preservation.json),
[cleanup](resource-baseline-v2-cleanup.json),
[validation](resource-baseline-v2-artifact-validation.json),
[privacy scan](resource-baseline-v2-privacy.json) and
[archive hash](resource-baseline-v2-evidence.sha256). After verifying the archive
hash and extracting into a new directory:

```bash
python3 verify_resource_baseline_v2.py --root /absolute/path/to/extracted
```

This checks all 35 manifested files, source/protocol registration, complete
responses, exact token counts and memory observations. Private native profiles,
credentials, keys, tasks, grading checks and reference fixes are excluded.
