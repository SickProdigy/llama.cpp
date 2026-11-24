# FableVibes Q4: GPU fit, no completed coding work

November 24, 2026. **The matched Q4 baseline makes no code, test or documentation
changes in any of its three coding turns and publishes nothing.** It stops on
repeated skill requests. Its shorter duration is not a correctness improvement
over [Q6](native-fable-q6-beets.md); neither passes this configuration.

Public model `tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF`, revision
`9cf910a7ad68dfedcbdfc46ef0fe5003dec07c23`, file
`Qwen3.6-14B-A3B-FableVibes-Q4_K_M.gguf`, 8,465,553,920 bytes,
SHA256 `21aa4b0b28090469e8a319c889451df2f1ea6aad27ac3818c8c8a86f86d5bc9e`.
Full SHA256 is verified before resource and native inference. The runtime,
task family, sampler, seed, budgets and tool/profile configuration match the
Q6 baseline apart from model/alias/disposable upstream identifiers.

Native loading confirms 41/41 layers offloaded, 7,790.09 MiB CUDA model buffers,
272.81 MiB CUDA-host model buffers and 540 MiB GPU KV. Context is 98,304, q4 K/V,
one slot, two context checkpoints, non-mapped loading and 512 MiB host prompt
cache. Automatic fit is disabled. Temperature .2, top-p .95, top-k 40,
seed 20261124, thinking disabled and 8192 output cap are checked in every actual
native request. The internal network provides a selected checkout and scoped
Gitea MCP; external terminal Git/DNS and unrestricted web access are not the
measured workflow.

| Turn | Seconds | Actual outcome |
|---|---:|---|
| Separate repository discovery | 143.39 | Correct Gitea metadata lookups, then unnecessary terminal/web attempts; native web-search no-progress stop; no requested explanation |
| Initial lifecycle repair/contribution | 61.26 | Ten skill requests, no edit or contribution; no-progress stop |
| Retained documentation followup | 20.50 | Five skill requests, no edit or publication; no-progress stop |
| Retained cancellation feature | 20.48 | Five skill requests, no edit or publication; no-progress stop |

Coding totals **102.24 seconds / 1.70 minutes**, while the whole supervised GPU
stage takes 7.84 minutes including hash/load/read control/grading/restoration.
All CLI exits are 0; those exits do not establish task completion. Every coding
answer is a native no-progress message asking for `continue`. No continuation,
task restatement or corrective hint is supplied by the operator.

All 40 source fingerprints in every completed snapshot match the immutable
baseline. Existing 83 project/original tests pass in operator grading; the real
defect remains and the required command is absent. No new tests or regression
coverage exist. Counterfactual test runs and extra dispatcher runs are therefore
not repeated for identical source. The selected checkout, upstream/base, full
task and Beets policy are present in the first actual coding request. A source
observation after read control also confirms no persistent project changes.

All 38 captured HTTP responses complete without transport errors. The last
complete coding prompts contain 15,306 / 16,620 / 17,979 tokens and retain all
issued tasks; one native lineage persists without compaction or extra user-role
budget messages. This is not a large-context quality success: the workflow
already fails at short context. Separate [capacity probes](resource-fable-q4-summary.json)
exercise 59,937 tokens at the 98,304 loaded window.

37 native samples record 8,964 MiB GPU peak, 6.511 GiB aggregate charged cgroups
including cache/helpers, 1.826 GiB process PSS, zero experiment swap, zero
measurement errors/guards and at least 110.82 GiB model-disk reserve. Whole-host
swap moves 4,153 input / 688 output pages without attribution. Sampling is not a
continuous whole-host allocation guarantee. Proxy backend intervals range
0.82–67.75 seconds, median 1.56, sum 160.06; these include read/coding prefill,
generation and queueing rather than isolated decode throughput.

Independent connected-forge readbacks find no upstream issues or PRs and only
unchanged main `9ca0d61869324b4643b9f8b31b7c20153618f541` in
`chatgpt-codex/hermes-gpuquant-fable-q4-20261124`. Exact fork lookup authenticated
as `hermes-agent` returns 404. There are no owned issues to close. Original
runtime identity/configuration/alias/context, four profile files, all 30 retained
model metadata entries, owner pending files/instructions and Hermes-Codex
container state are independently verified. Exact owned containers/network are
removed; no everyday model/profile change occurs.

The [summary](native-fable-q4-beets-summary.json),
[positive validation](native-fable-q4-beets-validation.json) and
[coherent negative controls](native-fable-q4-beets-verifier-controls.json) retain
the unsuccessful outcome. The negative controls reject changed manual-source
and context-request bindings after coherent manifest/audit updates; there is no
authored-test mutation case because no authored tests exist. These are artifact
checks, not model trials or reexecution of private behavior.

```sh
python3 verify_native.py native-fable-q4-beets-evidence.tar.gz
python3 verify_native_controls.py native-fable-q4-beets-evidence.tar.gz
sha256sum -c native-fable-q4-beets-evidence.sha256
```

The [header comparison](quant-header-comparison.json) has matching tensor shapes
and tokenizer/template metadata within the Q4/Q6 pair, but does not prove equal
calibration/conversion history. One unsuccessful nonthinking lineage per quant
does not establish a causal precision ranking or general checkpoint inability.
Publisher-sampling, reasoning-enabled Q4/Q6 comparisons remain prospective.
