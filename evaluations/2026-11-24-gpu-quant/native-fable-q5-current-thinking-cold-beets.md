# Current FableVibes Q5: native coding and Gitea audit

The fresh three-turn Beets workflow **fails** in **31.85 coding / 34.71 total wall minutes**. It fits the P100 at 98,304 context, 41/41 reported GPU layers and 10,224 MiB peak GPU. No deployment or default change.

| Turn | Time | Native exit | Project / immutable original checks | Independent behavior |
|---|---:|---:|---|---|
| Lifecycle repair | 13m 41s | 1, iteration limit | 86 / 83 passed, plus 2 subtests each | Waiting/dispatched imports still start after disable/shutdown |
| Documentation | 2m 58s | 0 | 86 / 83 passed | Added abandonment/manual-scheduler claims contradict code |
| Cancellation follow-up | 15m 12s | 0 | 97 / 83 passed | Pending-only cancellation misses waiting work; no publication |

## Selection and reproducibility

Public `tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF`, revision `9cf910a7ad68dfedcbdfc46ef0fe5003dec07c23`, `Qwen3.6-14B-A3B-FableVibes-Q5_K_M.gguf`, 9,852,131,840 bytes, SHA256 `d8fe99004cefb2cf26a1750851acf3cabd53247958e144f88e08beeb36ffbcab`. Existing public artifact; no conversion or custom quantization. See [capacity and header/calibration qualifications](resource-fable-q5-current-thinking.md).

The current evaluator/backend and initial main sampler/tool schemas match current Q6/Q8: main thinking, temperature1, top-p0.95, top-k20, seed20261124, 16,384 cap; auxiliary nonthinking temperature0.2, top-p0.95, top-k40, 8,192 cap. One slot, q4 K/V, ubatch128, 512 MiB RAM cache, two checkpoints, fit off/load none. Production4096 cap remains separate. Public tensor production/calibration and model filesystem/cache differ; these are not precision-only causal experiments.

139/139 backend requests complete, no backend errors or length finish. First backend call **55.11s**, largest completed input **84,135 tokens**. The sole auxiliary call takes **104.04s** and emits patch/tool markup instead of a conversation checkpoint. The run resumes; all three literal tasks survive. Failures already exist before summarization, so compression is not their sole cause.

192 ten-second samples: 10,224 MiB peak GPU; 333.44 MiB host model, 28.01 MiB host compute; aggregate study cgroup peak 7,347,576,832 bytes, process PSS2,514,857,984 bytes, zero study swap/guards/measurement errors. These include evaluator/helper/cache allocations and are sampled peaks. Both actual filesystems stay above100GiB. See numerical evidence for minima.

## Independent source and publication review

The worker and serial-lock boundary are unchanged. `_disabled` only gates timer dispatch; clearing timers cannot invalidate already-dispatched/waiting jobs. Cancellation removes/counts `_pending` entries only. Running jobs remain allowed, but unstarted jobs waiting behind them are not cancelled. Authored tests cover pending flags and validation rather than the required waiting-work race; the manual-disabled test only queues a timer and never fires it.

The README preserves existing guidance but incorrectly promises abandonment of all activation work and says manual imports bypass the scheduler. The final answer claims a pushed branch, safe callbacks and unavailable MCP. Configured MCP actually returns19 recorded calls; six attempts target repositories outside the evaluation lease. The allowed fixture and authenticated identity were supplied. Independent actor-authenticated remote read verifies all40 upstream baseline blobs unchanged, no issue/PR, and actor fork GET404. No issue was opened to close. Local shell DNS failure and wrong-target scope denials do not establish configured MCP failure. No remote source is claimed; all graded snapshots are local.

Supplementary pinned Nicotine+3.3.11 PluginHandler observations: baseline TFFF, correct reference TTTT, Q5 TFFF for fresh old timer / fresh old dispatched worker / waiting worker without reload / registered cancellation. Existing private bindings are unchanged, so the dispatched/waiting defects are valid ordinary behavior failures. Fake timers/deferred threads/import boundaries are used; no live GUI/media/beets process. Folder stress controls fail two cases at nonexistent-folder validation; that is qualified separately from waiting-worker evidence. Same-object reload is stress, not normal GUI reload proof.

Original runtime alias/context, container identity/config, four owner settings, original30 weights, staged IQ4+Q5 and owner pending source/instructions pass fresh preservation checks; the entire Hermes-Codex snapshot is unchanged. Exact owned supervisor, anonymous volume, backend/proxies/network are removed. Useful weights remain. No assessor hints, patches, resends or extra continuation were supplied.

## Evidence and limits

[Summary](native-fable-q5-current-thinking-cold-beets-summary.json), [archive](native-fable-q5-current-thinking-cold-beets-evidence.tar.gz), [SHA256](native-fable-q5-current-thinking-cold-beets-evidence.sha256), [validation](native-fable-q5-current-thinking-cold-beets-validation.json), [privacy](native-fable-q5-current-thinking-cold-beets-privacy.json).

```sh
python3 verify_current_fable_q5_native.py native-fable-q5-current-thinking-cold-beets-evidence.tar.gz
```

The standalone verifier checks saved measurements, local source hashes/static worker facts, claims, remote observations and restoration consistency. It does not rerun inference, authenticated remote lookup or private behavioral graders. All40 source files per snapshot are included; raw conversations/databases/profiles, private graders/reference implementation and signing keys are excluded. Three recomputed-manifest negative controls reject fabricated success, concealed host-memory excess and altered source. This is one dependent workflow, not three independent trials, reliability or GPT5 equivalence. Q5's shorter failed duration is not a correct-task speedup.
