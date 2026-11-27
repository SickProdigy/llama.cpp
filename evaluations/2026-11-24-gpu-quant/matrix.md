# GPU-resident quantization comparison

[Current retained IQ3 coding/Gitea](native-adapted-iq3-current-cold-beets.md) fails in **32.50 coding / 36.50 wall minutes** at **98k / 66 of 66 GPU layers / 12,904 MiB peak**, with **521 MiB host model buffers**. A two-assignment rename breaks ordinary timer dispatch; cancellation, new tests, README changes and a PR are absent. All 36 backend calls succeed; the first takes **229.62 seconds**. All three turns end at native repeated-edit safeguards. Existing tests pass while independent source and real Nicotine controls expose the regression. Strict fresh-baseline restoration, owner settings/models and Hermes-Codex preservation pass; the issue is closed. This is a failed workflow duration, not a correct-task speedup.

[Current retained IQ3 capacity](resource-adapted-iq3-current.md) completes all six probes at **98k / 66 of 66 reported GPU layers / 12,904 MiB peak**, with **521 MiB host model buffers** and no study swap. Exact 16k/60k/80k markers pass; 60k takes **14.51 minutes** with cached input. Original services and this stage's full Codex baseline are restored and verified. The separately completed fresh coding/Gitea workflow fails; capacity is not a quality verdict.

[Fresh current IQ4 retry](native-adapted-iq4-current-r2-cold-beets.md) fits 98k with explicit host spillover but fails the published workflow in **110.58 coding / 114.69 wall minutes**. All 67 backend requests complete; actual issue/fork/PR succeed, but ordinary import dispatch breaks, cancel is absent and no new tests are published. Compression plus the first resumed request costs **30.83 minutes**. Original model settings and owner edits are verified. Hermes-Codex's start timestamp changed for an unknown reason, so its full-state preservation check failed. Retained IQ3 capacity passes, but its fresh coding workflow also fails.

[Owned Q8 retirement](study-owned-q8-retirement.md) recovered staging headroom to **117.45 GiB free**. Only the failed task-added Q8 file was removed after a fresh full-hash/ownership check; original30 models and useful IQ4 are preserved. That historical retirement funded the fresh retry; see its report for the later reserve.

[First current IQ4 native attempt](native-adapted-iq4-current-interrupted.md) was interrupted by the 100 GiB staging-disk safeguard after 14 successful requests. Memory remained within budget; no coding turn finished and **no quality verdict is assigned**. Actual upstream issue/personal fork/three commits are verified, but no PR. Original runtime/models/settings are restored, the issue is closed, and exact owned cleanup passes. That first attempt remains unscored; the separately admitted fresh retry is now complete.


[Current adapted 27B IQ4_XS capacity](resource-adapted-iq4-current.md) passes all six probes at 98k with 63/66 GPU layers and explicit CPU spillover: **15,926 MiB GPU / 1,250.63 MiB host model buffers**, no observed study swap. All-GPU and 65-layer layouts hit CUDA allocation errors. Exact 60k/80k markers return in 13.40/7.13 minutes with cached input. Original runtime/models/settings are restored and exact owned cleanup verified. The first coding attempt was interrupted without a quality score; the separately admitted fresh retry fails the published workflow.


[Current adapted 27B Q4 coding/Gitea](native-adapted-q4-current-cold-beets.md) completes actual issue/fork/PR publication but fails lifecycle, command registration, cancellation and documentation correctness in **84.12 coding minutes / 88.46 wall minutes**. All 37 requests complete without backend errors; 15,456 MiB GPU plus explicit CPU spillover. Original runtime/models/settings are restored. Current-runtime IQ4_XS capacity passes, but its fresh coding retry also fails; the earlier disk interruption remains unscored.


[Current adapted 27B Q4 capacity](resource-adapted-q4-current.md) completes all six probes at 98k with 56/66 GPU layers and explicit CPU spillover: 15,456 MiB GPU, about 2.9 GiB host model buffers, no study swap. All-GPU allocation fails; 60k input takes 11.06 minutes. The completed current-runtime coding/Gitea run publishes but fails behavior; see the result above.

[Current Fable Q6 coding/Gitea](native-fable-q6-current-thinking-cold-beets.md) fails in 36.67 coding minutes: initial repair absent, cancellation incomplete, project collection blocked, docs inaccurate, no remote issue/fork/PR. It fits 98k/all 41 GPU layers at 11,566 MiB. Matched current Q8 also fails (38.68 minutes/14,624 MiB); no precision winner is established.


[Current-runtime Fable Q8](native-fable-q8-thinking-cold-beets.md) fails the coding/Gitea workflow in38.68 coding minutes despite fitting all41 layers at98k/14,624MiB GPU. Manual imports regress, cancellation and authored tests fail, command docs are missing, and no issue/fork/PR exists. The original runtime/models/settings are restored and verified.

The [recorder correction](transparent-recorder.md) now preserves backend errors in synthetic native-SDK controls. Vibe Q6’s final turn was confounded by the old recorder masking context400 as502; earlier code failures remain. Real model recovery is untested.

The [current-runtime Vibe Q4 reasoning cell](native-vibe-q4-thinking-cold-beets.md) fails in52.20 coding minutes: project collection fails, final original suite regresses, independent behavior fails, no issue/fork/PR. All41 GPU layers fit at8,964MiB peak. [Matched Q6](native-vibe-q6-thinking-cold-beets.md) fails in64.03 coding minutes, with code/test defects followed by context overflow;11,566MiB peak GPU. The older Fable cells are not runtime-matched to these cells.


Updated November27. In progress. Nonthinking and trusted baselines remain
below; the matched cold Fable reasoning pair also fails. Those two cells share
an older experimental Hermes runtime. The [current-runtime preflight](current-runtime-preflight.md)
passes without model calls or forge writes; Vibe reasoning cells bind
that newer owner-source evaluator. Capacity alone is not coding/publication quality.

| Checkpoint / public quant | Measured capacity (98,304 unless stated) | Fresh Beets coding/Gitea workflow |
|---|---|---|
| Adapted27B IQ4_XS, current C9/fee, fresh R2 | 98k / 63 of66 GPU / ub64,15,926MiB peak; host model1,250.63MiB; actual81,911-token input | Published workflowFAIL: dispatch TypeError, no cancel/no added tests;110.58coding/114.69wallmin,67/67 backend requests; qualified Codex timestamp exception ([audit](native-adapted-iq4-current-r2-cold-beets.md)). Earlier [disk interruption](native-adapted-iq4-current-interrupted.md) remains unscored |
| Adapted27B IQ3_XXS, retained / current reference | Full hash verified;98k/66 of66 reported GPU/ub64;12,904MiB GPU,521MiB host model;all6probes and exact16k/60k/80k markers pass ([capacity](resource-adapted-iq3-current.md)) | Fresh native coding/Gitea not started;60k870.56s with16,084 cached tokens. Capacity is not a quality result |
| FableVibes Q6_K, retained | Probes complete; capacity layout complete; native confirms 41/41 layers offloaded; 11,566 MiB peak sampled GPU | Repair not performed; README inaccurate; feature breaks manual imports, tests fail collection, no publication ([audit](native-fable-q6-beets.md)); 21.05 coding minutes |
| Same FableVibes Q4_K_M, retained | Capacity probes complete; 8,964 MiB sampled GPU | All three coding turns make no edits/tests/publication; skill-request stops; 1.70 coding minutes ([audit](native-fable-q4-beets.md)) |
| VibeForged v2 Q4_K_M, retained | Capacity complete; 8,964 MiB sampled GPU; selected-file cache verified 0 after originals stop | Unchanged source; all18 code-tool calls blocked by unattended policy ([audit](native-vibe-q4-beets.md)); fresh trusted run also fails path recovery ([audit](native-vibe-q4-trusted-beets.md)) |
| VibeForged v2 Q4_K_M, explicitly trusted profile | Same measured GPU layout; native41/41;8,964MiB peak |17 Python executions succeed but repeat wrong `~/beetsbridge`; no edits/tests/forge writes;2.217 coding minutes plus15.327-minute inefficient read ([audit](native-vibe-q4-trusted-beets.md)) |
| Same VibeForged v2 Q6_K, explicitly trusted | Capacity complete; native41/41;11,566MiB sampled GPU | Grounded read and partial cancellation/docs; lifecycle unfixed,19 authored tests fail collection, no publication;9.564 coding minutes ([audit](native-vibe-q6-trusted-beets.md)) |
| Adapted27B IQ4_XS, public |98k CUDA OOM at ub128/64;64k passes all probes,15,788MiB peak GPU/no study swap;51,942-input request598.86s ([evidence](resource-adapted-iq4.md)); native confirms66/66 GPU layers | Local repair passes; docs reporting and cancellation counts/callback identity fail; no publication;85.75 coding minutes including2 failed summaries/native fallback ([audit](native-adapted-iq4-beets.md)) |
| FableVibes Q4_K_M, cold reasoning / older evaluator |41/41 GPU;8,964MiB sampled peak;98k q4 KV |Plugin unloadable after all3 turns; collection/preservation fail; no publication;22.24 coding minutes ([audit](native-fable-q4-thinking-cold-beets.md)) |
| FableVibes Q6_K, cold reasoning / same older evaluator |41/41 GPU;11,566MiB sampled peak;98k q4 KV |Final91 tests/2 subtests pass but lifecycle/cancellation/docs fail; no publication;13.16 coding minutes ([audit](native-fable-q6-thinking-cold-beets.md)) |
| VibeForged v2 Q4_K_M, cold reasoning / current evaluator |41/41 GPU;8,964MiB peak;98k |Collection and lifecycle/cancel fail; final preservation regression; no publication;52.20 min ([audit](native-vibe-q4-thinking-cold-beets.md)) |
| Same VibeForged v2 Q6_K, cold reasoning / same current evaluator |41/41 GPU;11,566MiB peak;98k |Partial repair fails; final context overflow; no publication;64.03 min ([audit](native-vibe-q6-thinking-cold-beets.md)) |
| FableVibes Q6_K, cold reasoning / current evaluator and transparent recorder | 41/41 GPU at98k;11,566MiB; all six current capacity probes complete | No initial repair; incomplete cancel; project collection fails; docs inaccurate, no remote issue/fork/PR;36.67 coding min ([audit](native-fable-q6-current-thinking-cold-beets.md)) |
| FableVibes Q8_0, public |Full file/hash verified;41/41 GPU at98k,14,624MiB peak;80k-input probe completes with59.8k cached ([capacity](resource-fable-q8-thinking.md)) | Manual-import/cancellation regressions, test collection failure, incomplete docs, zero Gitea actions;38.68 coding minutes ([audit](native-fable-q8-thinking-cold-beets.md)) |
| FableVibes Q5_K_M, public | Possible intermediate; not downloaded or measured in this study | Not started |
| Adapted 27B Q4_K_M, retained / current capacity | All-GPU98k CUDA OOM;56/66GPU passes all six probes;15,456MiB GPU;CPU model2,982.90MiB/CPU KV216MiB;60k663.77s ([capacity](resource-adapted-q4-current.md)) | Current Beets completes actual issue/fork/PR but fails lifecycle/cancellation/command registration/docs in84.12codingminutes ([audit](native-adapted-q4-current-cold-beets.md)); older correct Spam result remains qualified separately |
| Adapted 27B IQ3_XXS, retained / current evaluator | 66/66 GPU at98k;12,904MiB peak;521MiB host model; no study swap | Actual issue/fork/three commit writes, no PR. Published missing-field dispatch regression; no cancel/tests/docs;32.50coding/36.50wallmin; all3 turns stop at native edit safeguards ([audit](native-adapted-iq3-current-cold-beets.md)) |
| Adapted 27B Q5/Q6 | Weight files exceed16GiB, ruling out entirely GPU-resident layouts; limited CPU-offload fit unmeasured | Not run; no quality-failure claim |

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
with the same positive/coherent-negative checks. The fresh native coding stage used an untouched profile and the same declared task/sampler/seed; its completed no-edit result follows.

Fable Q4's completed native baseline has no edits in any phase, 37 complete
samples, 8,964 MiB GPU, 6.511 GiB charged cgroups, 1.826 GiB PSS and no study
swap/guards/errors. Its 38 complete HTTP captures reach only 17,979 prompt tokens;
this is failure before useful large-context code work, not a long-context success.
Original runtime/profile/model/owner/Codex preservation and exact cleanup are
verified; connected issue/PR lists are empty and upstream main unchanged.
The [Q4 report](native-fable-q4-beets.md) and artifacts retain that outcome.

Before either Vibe stage, repeat selected-file cache advice after the original
backend stops and record kernel page residency. Vibe Q4 is also the production
mapped model; advising it only before stop could leave shared mapped pages charged
outside the experiment. This accounting amendment changes no task, prompt, weights,
sampler or model settings. The same Vibe pair uses it; no global cache flush occurs.

Vibe Q4's [capacity observations](resource-vibe-q4-summary.json) complete and the
original runtime is restored before native launch. The selected production-model
file has 285,806,592 cached bytes after original stop, reduced to 0 by advice of
that inactive file only. The controller/helper registration is bound by the
saved-evidence validator; no global cache flush occurs. This is an accounting
control, not an accuracy improvement. The completed native stage is policy-confounded; see the appended finding below.

The [adapted27B IQ4_XS option](prospective-adapted-iq4-xs.json) is additionally
pinned as a smaller4-bit format, not a newer trained checkpoint. Its download and
full hash and measured64k capacity now complete. The fresh native trial passes
the local repair but fails docs, cancellation and publication; see its audit.


The [VibeForged Q4 unattended baseline](native-vibe-q4-beets.md) completed without code changes: all 18 selected `execute_code` attempts were blocked by copied-profile one-shot approval policy. Repository read control succeeded; code-tool ability remains unmeasured. A separate isolated deny/approve pure-code control confirms this mechanism without model calls. Original deployed settings remain unchanged. The prospective comparison now uses a fresh explicitly trusted Vibe Q4/Q6 pair; Q6 deny-profile coding is deferred, with its capacity check now completed independently. Fable Q4/Q6 baseline outcomes remain preserved. Higher precision has not yet demonstrated a quality gain.


Vibe Q6 [capacity evidence](resource-vibe-q6-summary.json) now completes: 98,304-token allocation, requested full GPU offload, 11,566 MiB peak GPU, 6.561 GiB charged study cgroups, no study swap or guards, and a 59,937-token probe in 153.634 seconds. Original services/settings/models were independently verified restored afterwards. Capacity is not coding quality. The fresh trusted [Q4](native-vibe-q4-trusted-beets.md) and [Q6](native-vibe-q6-trusted-beets.md) workflows now complete and fail the full task, with identical task/source/sampler/seed/caps. Both copied profiles actually execute the no-model pure-code approval check successfully.


A bounded HTTP range [inspection](adapted-iq4-header-inspection.json) of the pinned adapted27B IQ4_XS header now confirms 866 tensors and importance-matrix metadata (496 entries, 104 chunks, `calib-train.txt`). This differs from the Fable/Vibe files with no recorded imatrix fields; no isolated precision-only claim follows. The prefix inspection itself does not verify the full file, GPU fit or coding quality; the separate full download receipt now verifies integrity. A separately owned Docker staging volume has been measured to retain over 100 GiB after this artifact; bulk download is deferred during timed GPU stages.


The separate [publisher-profile preflights](publisher-profile-preflights.json) pass for both fresh Fable profiles: actual SDK serialization checks reasoning-enabled main16k, auxiliary nonthinking8k and author sampling; actual pure-code checks execute in copied profiles already set to explicit experimental trust. No reasoning-model calls have started. These controls establish configuration/execution capability, not model quality.


The [native compression-handle control](native-compression-handle-control.json) actually resumes a scratch copy of the completed compressed read session for two followups, preserving literal followup history. Native CLI uses a stable receipt-owner handle, while compressed transcript storage uses a child segment. Source-pinned observer V3 records both separately; Q6 is launched with that prospective observer fix. Q4 coding did not compact and remains a valid observed path-recovery failure. Earlier unsuccessful control setups remain retained and are not model trials. No live trial was corrected, continued or replayed.


The [trusted Q6 audit](native-vibe-q6-trusted-beets.md) confirms a partial feature attempt, preserved manual-command parsing and a grounded read, but no correct full workflow. Original source lifecycle functions remain unchanged; new tests fail collection on candidate and prior source. Invalid `git diff --no-header` calls hide child stderr/exit status. The scored Q4/Q6 tool schemas are identical33-tool JSON; trajectory differences are not an isolated precision benchmark.

Both model families' publisher descriptions motivate fresh reasoning-enabled controls. The newly pinned [Vibe generation configuration](vibe-publisher-mode-followup-proposal.json) matches Fable sampling1.0/.95/top-k20. Its [fresh profiles](vibe-thinking-profile-preflights.json) pass actual SDK16k-main/8k-aux and isolated code-approval checks. Enabling thinking is our experiment based on the reasoning-training description; the vendor JSON does not itself set that template flag. No reasoning inference is claimed yet.

The pinned adapted27B IQ4_XS artifact completed its full-file SHA256 check in the separately owned volume; both actual filesystem reserves stayed above100GiB. Capacity completes at64k after98k CUDA failures; the native workflow also completes with an initial repair pass but docs/feature/publication failures. Original30 retained files remain preserved.


[Download receipt](adapted-iq4-download-receipt.json):15,321,491,104 bytes match the pinned full hash. Transfer took1,491.731 seconds; minimum observed staging free space126,470,311,936 bytes, final134,768,402,432 bytes, original model drive118,607,450,112 bytes. Original30 files are not written. This is download/integrity evidence, not model inference latency or fit.

The [IQ4 native trial](native-adapted-iq4-beets.md) confirms66/66 GPU layers
with644MiB host model buffer. All83 originals remain green;92 project tests do
not catch the independent feature failure or2 additional posthoc callback/count
counterexamples. Its300s auxiliary inactivity guard is distinct from main5400s
settings. Native fallback and logical/physical handles are audited, without
operator rescue. [Production metadata](adapted-quant-production.md) preserves
Q3/Q4/IQ4 calibration/tensor differences.

## Native compression runtime control — November25

[The saved-history control](compression-runtime-control.md) succeeds with explicit
auxiliary5,400s/host5,400s+5,400s budgets and actual prompt-progress streaming.
The real guarded Hermes facade produces a2,650-token model summary from26,148
input tokens in633.84s,100→30 messages, no fallback. Peak sampled GPU15,788MiB,
study cgroups6.550GiB/PSS2.013GiB, zero study swap/guards; original runtime,
models/settings/owner edits/Codex are independently verified and owned helpers removed.
This combined runtime control uses saved history, not a full CLI/session or coding
quality test; it leaves all prior scores unchanged. New request messages differ
slightly from the old failed request. Future unused reasoning profiles need the
prospective amendment and actual main/auxiliary/host preflights before freezing.

## Fable Q4 reasoning capacity — November25

[Five probes pass](resource-fable-q4-thinking.md) at98,304 context, T1/p0.95/k20,
reasoning enabled and16,384 output cap. Sampled GPU8,964MiB, charged study
cgroups6.545GiB/PSS1.462GiB, zero study swap/guards/errors;54 complete samples.
The16,165-input probe takes41.77s;59,935-input takes153.38s including16,033 cached
tokens. Original runtime/models/settings/owner edits/Codex are preserved and owned
resource containers/network removed. Native coding, followups and publication
remain pending; no reasoning-mode quality win follows from capacity.

## Fable Q4 reasoning workflow — observed November25, audited November26

[Repair/docs/feature/publication fail](native-fable-q4-thinking-beets.md) in37.13
coding minutes,42.02minutes launch→restore. Initial86pass/2fail, final90pass/4fail;
all83originals+2subtests pass. Final claimed fork/PR do not exist in independent
completion-time readbacks.41/41GPU layers; peak8,964MiB/CG6.769GiB/PSS2.277GiB,
zero study swap/guards;134complete HTTP records and81,965maximum input tokens.

This run shares read-control gateway rejection state with the fresh logical coding
conversation, and its nonthinking auxiliary commits an85-token tool-call fragment
as reference context. All3user requests remain literal; checkpoint semantics fail.
These findings require prospective read-control isolation and auxiliary-mode tests;
the run cannot stand for an independent cold-health quantization comparison.
Original runtime/models/settings/owner edits/Codex were verified and owned resources
removed before the pause. Current production was rebuilt afterward; preserve its
new state for future tests. No everyday winner or autonomous-reliability claim.


The [November 26 auxiliary/cache controls](auxiliary-precision-controls.md)
replay one saved native checkpoint request at three sampler modes, with quoted
history and FP16 KV controls. None of eight outputs qualifies as a trustworthy
checkpoint. FP16 fits at98,304 context with41/41 GPU layers and10,162MiB sampled
GPU, versus8,964MiB withq4_0 KV. One reasoning output gains section coverage
but loses failing-test status and repeats its final log. These are auxiliary
controls, not new coding/Gitea passes; production settings remain unchanged.


The [matched Fable Q6 auxiliary replays](auxiliary-q6-quant-control.md)
also fail all three checkpoint requests: nonthinking and low-temperature
reasoning emit tool markup; publisher reasoning answers the old task. Q6 peaks
at11,566MiB GPU with41/41 layers and zero study swap. Higher weight precision
alone does not resolve this saved-history failure; fresh coding remains separate.


The [cold-gateway Fable Q6 reasoning workflow](native-fable-q6-thinking-cold-beets.md)
finishes in13.16 coding minutes: first repair/docs turns make no edits; the final
feature patch passes91 tests/2 subtests but fails independent cancellation checks.
No upstream issue, actor fork or PR exists on final authenticated readback.
All81 requests stay below64,067 input tokens with no compression or length finish;
the exact Gitea remote was supplied. This clean-start failure is independent of
the older read-control cooldown coupling. Same-method cold Q4 remains pending.
