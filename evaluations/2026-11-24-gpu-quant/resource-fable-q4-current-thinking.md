# Current Fable Q4 reasoning-mode capacity

Subsequent update: the [matched current native workflow](native-fable-q4-current-thinking-cold-beets.md) is complete and fails. Statements below describe the capacity checkpoint.

All six requests complete at **98,304 context /41 of41 GPU layers /8,964 MiB peak GPU**. Actual short tool arguments and dependent tool-history answer are correct. The16k exact-marker check fails (`16000`, missing its prefix);60k/80k markers are exact. **This is capacity evidence, not coding or configured Gitea quality.** Fresh current-evaluator native coding remains pending.

## Artifact and matched setup

Existing retained public `tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF`, revision `9cf910a7ad68dfedcbdfc46ef0fe5003dec07c23`, file `Qwen3.6-14B-A3B-FableVibes-Q4_K_M.gguf`,8,465,553,920 bytes, full fresh SHA256 `21aa4b0b28090469e8a319c889451df2f1ea6aad27ac3818c8c8a86f86d5bc9e`. No download, conversion or custom quantization. The original public pin is included verbatim and hash-bound to the prospective protocol.

Current llama.cpp image `fee4289628e7ba09f6fbf62d6ce4325aebb2531ffde2154d41276fe4acc58da3`, current qualified evaluator `c9b40eb8dea441cba7ded2e6589e5c011545ffc1ec76a0dc736f8e399d8f947b`. Same six synthetic requests and actual tool-history construction as current Q5/Q6/Q8; thinking enabled, temperature1/top-p0.95/top-k20/min-p0/repeat1/presence0, seed20261123,16,384 output cap. Planned native seed20261124 differs deliberately, as in the other cells.

One slot,98304 allocated context, q4_0 K/V, ubatch128/batch512, requested ngl99 with actual41/41 verified before probes, cache RAM512MiB/two checkpoints, fit off/load none, CPU threads8. Experimental output headroom differs from production4096.

| Probe | Actual input | Output | Cached input | Seconds |
|---|---:|---:|---:|---:|
| tool | 291 | 102 | 0 | 27.34 |
| tool-result | 426 | 123 | 392 | 2.69 |
| tool-followup | 573 | 95 | 548 | 2.16 |
| prompt16000 | 16,165 | 454 | 0 | 48.04 |
| prompt60000 | 59,935 | 79 | 16,033 | 155.34 |
| prompt80000 | 79,930 | 296 | 59,803 | 110.02 |

Load/readiness75.56 seconds.16k input is uncached;60k/80k reuse16,033/59,803 input tokens. Timings include variable reasoning output and shared-host/storage/cache effects; these are not cold whole-context throughput or isolated quantization effects.

## Memory and restoration

79 five-second samples:8,964MiB peak GPU /7,311MiB minimum free GPU; aggregate study cgroup6,973,968,384 bytes, process PSS1,658,934,272 bytes, zero study swap/guards/measurement errors. CUDA model7,790.09MiB, host model272.81MiB, GPU KV540MiB, GPU compute229.01MiB and host compute28.01MiB. All transformer layers are GPU-offloaded; host allocations still exist. Cgroups include charged cache/helpers, not just the server process. Whole-host swap counters are separately recorded and not attributed to the study.

Minimum original/staging reserves: 103.47/104.96GiB. Stage admission105GiB/abort102GiB, original minimum100GiB. No original or staged model was removed. Only selected-file DONTNEED/mincore is used; zero cached pages is not proof of globally cold hardware/storage caches. Five-second samples can miss transients.

Independent strict postflight verifies original container identities/configs/running state, original alias/context, four owner profile hashes, all30 original model metadata, both staged IQ4/Q5 metadata, owner tracked/pending files/instructions and the full fresh Hermes-Codex snapshot unchanged. No Codex timestamp waiver. Exact owned supervisor68e963…, exclusive anonymous volume, backend/network are removed after archiving. No actor, forge credentials or private grading inputs entered the capacity stage.

## Interpretation and evidence

Q4 has more GPU headroom than current Q5/Q6/Q8, but already misses one exact answer. Public artifacts share shape/template metadata without imatrix keys; that does not prove equal calibration or that no importance matrix was used. The header comparison is included as previously captured metadata; current full-file hash proves this retained file identity. Earlier Q4 native results use an older evaluator and remain separate. No quality upgrade or autonomous reliability is inferred.

[Summary](resource-fable-q4-current-thinking-summary.json), [archive](resource-fable-q4-current-thinking-evidence.tar.gz), [hash](resource-fable-q4-current-thinking-evidence.sha256), [validation](resource-fable-q4-current-thinking-validation.json), [privacy](resource-fable-q4-current-thinking-privacy.json).

```sh
python3 verify_current_fable_q4_resource.py resource-fable-q4-current-thinking-evidence.tar.gz
```

The verifier checks saved complete responses, actual tool arguments and retained assistant lineage, token/headroom/sampler consistency, placement, memory, source/protocol bindings and restoration. Four recomputed-manifest tamper controls are rejected. It does not replay inference, configured MCP, coding, private graders or live remote authentication. No GPT5 equivalence claim.
