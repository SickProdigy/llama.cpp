# Interactive Q4 memory failure and checkpoint comparison

The first native Q4 coding attempt stops before completing its initial task.
Kernel logs independently confirm a host cgroup OOM, with a 6.5 GiB backend cap;
this is a resource interruption, **not a completed model-quality failure**.
Only an unfinished local patch exists. No changed regression tests or forge
writes are recorded before the interruption.
The preceding read control reaches the correct configured Gitea repository,
but its explanation is not wholly accurate. No fresh whole-workflow pass exists.

Passing the earlier tool/16k/60k probes did not establish interactive fit. During
normal repeated requests, the backend retains context checkpoints separately
from the 512 MiB prompt-cache limit. The pinned upstream
[source](https://github.com/ggml-org/llama.cpp/blob/225a5345b/tools/server/server-context.cpp)
creates checkpoints near prompt ends and bounds their list by count. Actual
trace entries show each checkpoint occupies **149.626 MiB**.

A preregistered comparison replays the same 12 captured request prefixes,
including one duplicate: **11 unique prompt histories, not independent tasks**.
Only one token is generated per request. No actor tools or Gitea actions run.

| Context checkpoints | Completed requests | OOMKilled | Peak sampled main + supervisor PSS | Maximum saved checkpoints |
|---|---:|---|---:|---:|
| Default 32 | 10/12 | Yes | 6.61 GiB | 17 |
| Explicit 2 | 12/12 | No | 4.42 GiB | 2 |

Both use the same public Q4 SHA, pinned b12627 image, 98,304 context, 56 GPU
layers, q4 K/V, non-mapped loading, 512 MiB prompt cache, 6.5 GiB backend cap,
512 MiB supervisor cap and zero swap allowance. Sampled backend swap stays zero.
Model-file hashing is followed by advisory DONTNEED for that specific study-owned
file; no global cache/swap flush occurs. Neither advisory cache control nor
cgroup/PSS observations prove exact whole-host attribution.

This isolates a useful memory-management change under these replay conditions.
It does **not** establish full native fit: outputs are shortened and the replay
has no actor overhead. Some reuse is slower with fewer checkpoints. Actual
coding, dependent followups, preservation, meaningful tests, documentation and
remote publication still require independent audits. The interrupted conversation
will be treated as a recovery diagnostic, separately from the fresh second family.
A scratch-copy native admission control preserves all 28 message rows through
ordinary `sessions discard`; no task replay or force-unlock is used.

The original services/settings, all 30 model metadata entries, pending owner
work/instructions and entire Hermes-Codex snapshot are verified preserved after
both arms. Exact owned supervisors/backends/networks are removed. The last audit
has **103.60 GiB free**. No original model is deleted or production image updated.

See [summary](checkpoint-comparison-summary.json),
[offline validation](checkpoint-comparison-validation.json),
[privacy scan](checkpoint-comparison-privacy.json) and
[archive SHA](checkpoint-comparison-evidence.sha256). Verify the archive hash,
extract into a new directory, then run:

```bash
python3 verify_checkpoint_comparison.py --root /absolute/path/to/extracted
```

The archive includes raw memory observations, complete one-token responses,
input fingerprints/counts and strictly numeric checkpoint trace fragments.
Private prompt bodies, verbose logs, profiles, databases, ignored project
instructions, credentials, keys, future tasks and grading/reference code remain
local. The verifier checks 111 manifested files and both measured outcomes;
it does not reconstruct private policy inputs or certify coding correctness.
