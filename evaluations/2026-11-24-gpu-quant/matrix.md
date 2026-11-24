# GPU-resident quantization comparison

November 24, 2026. In progress. The first thinking-disabled Fable Q6 workflow
fails independently audited correctness and publication checks; other cells remain pending.

| Checkpoint / public quant | Capacity at 98,304 context | Fresh Beets coding/Gitea workflow |
|---|---|---|
| FableVibes Q6_K, retained | Probes complete; capacity layout complete; native confirms 41/41 layers offloaded; 11,566 MiB peak sampled GPU | Repair not performed; README inaccurate; feature breaks manual imports, tests fail collection, no publication ([audit](native-fable-q6-beets.md)); 21.05 coding minutes |
| Same FableVibes Q4_K_M, retained | Capacity probes complete; 8,964 MiB sampled GPU | Fresh native coding launched; unscored |
| VibeForged v2 Q4_K_M, retained | New matched stage pending | Pending |
| Same VibeForged v2 Q6_K, retained | New matched stage pending | Pending |
| FableVibes Q5_K_M, public | Possible intermediate; not downloaded or measured in this study | Not started |
| Adapted 27B Q5/Q6 | Weight files alone exceed 16 GiB; excluded from GPU-resident shortlist | Not run; no quality-failure claim |

Fable Q6's five completed resource requests include a real tool-call/result/
dependent-history exchange, a 16,152-token input and a 59,937-token input. The
latter takes 152.76 seconds and returns the expected marker. These synthetic
capacity checks do not establish real coding or MCP reliability. Peak relevant
aggregate charged cgroups: 7,045,599,232 bytes (6.562 GiB); process PSS:
1,736,166,400 bytes (1.617 GiB). Charged cache is included. No experiment swap,
measurement errors or resource guard triggers are observed in 57 samples.
Whole-host swap moves by 92,503 input and 11,148 output pages without attribution.
Sampling is not a continuous whole-host memory guarantee.

The capacity-stage log verbosity does not enumerate tensor buffers. The completed
native load independently confirms 41/41 layers offloaded, 10,392.38 MiB CUDA model
buffers, 397.85 MiB host model buffers and 540 MiB GPU KV. Automatic fit is disabled;
fit is not inferred from file size. The resource controller verifies full file SHA256 before
inference and restores original service identity/configuration/running state,
original alias/context, and unchanged Hermes-Codex state afterward.

The new task family exercises a real Beets import lifecycle defect, retained
documentation followup and a cancellation feature, with actual upstream issue,
personal fork and PR actions. Private baseline/reference behavioral and original
suite controls are validated before actor calls. SDK serialization and actual
read-only configured Gitea transport pass. An initial operator transport setup
failure caused by generated fixture bytecode is preserved privately, corrected
before actor calls, and excluded from model scores.

The older [development controls](../2026-11-21-goal-investigation/development-notes.md)
already show mixed Q4/Q6 outcomes within checkpoints. They are historical evidence,
not new scores or proof that precision alone explains a difference. The earlier
[wider-memory comparison](../2026-11-23-wide-memory/comparison.md) retains the slower
adapted 27B Q4's useful correctness result and latency tradeoff.

Reproduce saved capacity consistency checks:

```sh
python3 verify_resource.py resource-fable-q6-evidence.tar.gz
sha256sum -c resource-fable-q6-evidence.sha256
```

[Pinned public files](public-candidates.json), [registered plan](plan.md),
[resource observations](resource-fable-q6-summary.json),
[validator result](resource-fable-q6-validation.json) and
[credential-scan scope/result](resource-fable-q6-privacy.json) are retained.
Public consistency validation does not rerun inference or private behavior checks.

The completed Fable Q6 native baseline has 141 samples, peak charged study cgroups
6.698 GiB, PSS 2.019 GiB, no study swap/guards/errors, and 93 complete HTTP captures.
The largest prompt is 74,903 tokens, substantially filled by failed-clone history;
this is not useful full-window reasoning proof. All issued tasks remain literal,
no compression occurs, and the native generic iteration-limit finish message
persists in later history. Original runtime/profile/owner/Codex/model preservation,
exact cleanup and independent empty upstream issue/PR lists are verified. This
one unsuccessful nonthinking lineage does not establish a general Fable or
quantization ranking. The prospective publisher reasoning-enabled Q4/Q6 pair
remains a separate control before any practical recommendation.

Fable Q4's separate capacity stage also completes/restores: 62 samples, 8,964 MiB
GPU, 6.516 GiB charged cgroups, 1.445 GiB PSS, no study swap/guards/errors. Its
59,937-token probe takes 151.49 seconds. Whole-host swap moves 3,407 input/1,276
output pages without attribution. These operational pilot timings include
brief CPU-only evidence helpers when sampled; they do not isolate a quantization
speed effect. [Q4 resource evidence](resource-fable-q4-summary.json) is validated
with the same positive/coherent-negative checks. The fresh native coding stage
is launched with an untouched profile and the same declared task/sampler/seed.
