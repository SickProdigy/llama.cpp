# Current Fable Q4: native coding and configured Gitea

The fresh matched workflow **fails** in **34.37 coding /37.77 supervisor wall minutes**. Q4 fits98,304 context at41/41 GPU layers and8,964MiB peak, but leaves the requested lifecycle defect unfixed, implements pending-only cancellation and publishes no issue/fork/PR. All115 backend requests complete without errors. No deployment/default change.

| Turn | Time | CLI exit | Project / immutable originals | Behavior |
|---|---:|---:|---|---|
| Lifecycle repair |14m06s|0|89 /83 passed, plus2 subtests each|Only reporting guards changed; waiting workers still start|
| README |1m06s|0|89 /83 passed|Existing guidance retained, waiting-work contract still wrong|
| Cancellation |19m10s|1, iteration cap with generated final response|94 /83 passed|Pending timers cancelled; dispatched/waiting work and counts wrong|

## Source, tests and claims

The seven original lifecycle/scheduling/validation methods, including `_import_worker`, are AST-identical to baseline. The initial change removes two result/error-reporting guards; this does not stop imports waiting behind the serialized worker lock. Final cancellation registers `/beetscancel`, removes timer entries from `_pending`, and reports their count. Work already dispatched is no longer in that map and continues. Raw folder arguments are not canonicalized like import paths; that static limitation is separate from the measured waiting-work defect.

All83 immutable original project tests pass. The Beets subset grows from8 original tests to14 after the first turn and19 after the feature:6+5 additions, all8 original methods preserved. Authored tests check timer flags or execute workers before shutdown; they miss the waiting-worker race. The original project's green suite is not proof of the requested fix. Two extra local `beetsbridge_fix` documentation/commit-message artifacts are included in the42-file snapshots.

The README retains setup and file-safety guidance but explains pending timer cleanup rather than the still-broken waiting-work contract. Initial/follow-up answers claim the fix complete despite unchanged worker behavior. The closing answer reports publication blocked rather than claiming a real PR; its test totals14/19 match Beets subset totals, not14 newly added regressions.

Pinned Nicotine+3.3.11 real PluginHandler observations qualify baselineTFFF/referenceTTTT/candidateTFFT: fresh old timer and registered pending cancellation pass; fresh-instance old dispatched worker and waiting worker without reload fail. Relevant private bindings are unchanged, so these are public behavior defects. Supplementary folder controls also fail dispatched cancellation/counts; their same-object reactivation stress passes and is not normal GUI-reload proof. Fake timers/deferred threads/import boundaries are used; no GUI, media or real beets process is exercised. Observers were registered before all actor turns; no grader feedback or assessor patch/resend reached the actor.

## Actual Gitea state

Configured gateway records12 calls, including7 denials for targets outside the lease. The model selected `sickprodigy/nicotineplus` despite the supplied current Git root/origin and allowed upstream. Its local terminal DNS failure does not establish MCP unavailability: actual configured MCP calls and no-model native preflights succeeded.

Independent actor-authenticated read verifies all40 upstream baseline blobs unchanged, no issue/PR and personal fork GET404. All graded source is local; no remote code is claimed. No issue was created to close. Operator setup only seeded the committed baseline in a fresh private upstream; it did not write a model answer or pre-create the actor fork.

## Runtime, context and latency

Public artifact `tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF`, revision `9cf910a7ad68dfedcbdfc46ef0fe5003dec07c23`, `Qwen3.6-14B-A3B-FableVibes-Q4_K_M.gguf`,8,465,553,920 bytes, full fresh SHA256 `21aa4b0b28090469e8a319c889451df2f1ea6aad27ac3818c8c8a86f86d5bc9e`. Already retained; no download/custom quantization. See [current capacity and production qualifications](resource-fable-q4-current-thinking.md).

Actual first main controls and33 tool schemas match current Q5/Q6/Q8: thinkingT1/top-p0.95/top-k20, seed20261124, configured16,384 cap. Auxiliary nonthinkingT0.2/top-p0.95/top-k40/cap8192. Same C9 evaluator/fee backend,98k/q4 KV, ubatch128,512MiB RAM cache/two checkpoints, fit off/load none, one slot. Production4096 remains separate. Different public tensor/calibration production, filesystem/cache and generated trajectories prevent isolated precision causality.

First backend request67.35s; largest completed input83,321 tokens, leaving14,983 raw window tokens. A configured16k cap does not guarantee that headroom at every later request; no length finish or context error occurs. Auxiliary71 takes116.05s and emits literal test-file write markup plus a line-numbered read result instead of a conversation checkpoint. First resumed main request takes120.31s (3.94min combined). All three literal tasks remain in the final main request, and the lifecycle defect predates compression.

The final request115 takes221.31s with58,933 uncached input tokens. Its actual last user-role message is Hermes' native instruction that the maximum tool-calling iterations have been reached and a final summary is required. This is ordinary runtime budget feedback, not an assessor hint or fourth requested task. The model generates a closing response; native CLI exits1. Backend success and CLI completion remain distinct from code correctness.

Across200 ten-second samples:8,964MiB GPU peak, aggregate study cgroup6,651,801,600 bytes, process PSS2,303,496,192 bytes, zero study swap/guards/measurement errors. Reported CUDA model7,790.09MiB, host model272.81MiB, GPU KV540MiB, GPU compute229.01MiB/host compute28.01MiB. Both filesystem reserves remain above100GiB. Sampled peaks can miss transients; charged cache/helpers are included.

Fresh strict preservation verifies original container identity/config/running state and alias/context, all30 original and both staged models, four owner profiles, owner pending source/instructions, and the full unchanged Hermes-Codex snapshot. Exact owned supervisor/anonymous volume/backend/proxies/network are removed. No older Codex timestamp waiver is used.

## Reproducibility and limits

[Summary](native-fable-q4-current-thinking-cold-beets-summary.json), [archive](native-fable-q4-current-thinking-cold-beets-evidence.tar.gz), [hash](native-fable-q4-current-thinking-cold-beets-evidence.sha256), [validation](native-fable-q4-current-thinking-cold-beets-validation.json), [privacy](native-fable-q4-current-thinking-cold-beets-privacy.json), [literal natural tasks](beets-natural-task-queries.json).

```sh
python3 verify_current_fable_q4_native.py native-fable-q4-current-thinking-cold-beets-evidence.tar.gz
```

Saved source/measurement consistency is reproducible; inference, private grading and authenticated remote reads are not replayed by this verifier. Raw actor conversations/profiles, private graders/reference code and credentials are excluded. Four recomputed-manifest controls reject fabricated success, consistently over-budget memory, altered source and another candidate's control receipt. This is one dependent workflow, not three independent trials or autonomous reliability. Its failed duration is not a correct-task speedup. No GPT5 equivalence claim.
