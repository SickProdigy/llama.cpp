# GPU-resident quantization comparison

November 24, 2026. In progress; no new coding-quality verdict yet.

| Checkpoint / public quant | Capacity at 98,304 context | Fresh Beets coding/Gitea workflow |
|---|---|---|
| FableVibes Q6_K, retained | Probes complete; requested all-GPU layout, automatic fit off; 11,566 MiB peak sampled GPU | Launched; unscored |
| Same FableVibes Q4_K_M, retained | New matched stage pending | Pending |
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

Explicit tensor-placement logging is added before the native actor runs because
the capacity-stage log verbosity does not enumerate tensor buffers. All-layer
offload was requested, and auto-fit disabled; no CPU-fallback inference is made
from file size alone. The resource controller verifies full file SHA256 before
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
