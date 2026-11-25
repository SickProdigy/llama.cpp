# GPU-resident quantization comparison

November 24, 2026. In progress. The first thinking-disabled Fable Q6 workflow
fails independently audited correctness and publication checks; Q4 also fails without any edits. Vibe Q4 is policy-confounded; fresh trusted-profile runs also fail the full workflow; reasoning-mode controls remain pending.

| Checkpoint / public quant | Measured capacity (98,304 unless stated) | Fresh Beets coding/Gitea workflow |
|---|---|---|
| FableVibes Q6_K, retained | Probes complete; capacity layout complete; native confirms 41/41 layers offloaded; 11,566 MiB peak sampled GPU | Repair not performed; README inaccurate; feature breaks manual imports, tests fail collection, no publication ([audit](native-fable-q6-beets.md)); 21.05 coding minutes |
| Same FableVibes Q4_K_M, retained | Capacity probes complete; 8,964 MiB sampled GPU | All three coding turns make no edits/tests/publication; skill-request stops; 1.70 coding minutes ([audit](native-fable-q4-beets.md)) |
| VibeForged v2 Q4_K_M, retained | Capacity complete; 8,964 MiB sampled GPU; selected-file cache verified 0 after originals stop | Unchanged source; all18 code-tool calls blocked by unattended policy ([audit](native-vibe-q4-beets.md)); fresh trusted run also fails path recovery ([audit](native-vibe-q4-trusted-beets.md)) |
| VibeForged v2 Q4_K_M, explicitly trusted profile | Same measured GPU layout; native41/41;8,964MiB peak |17 Python executions succeed but repeat wrong `~/beetsbridge`; no edits/tests/forge writes;2.217 coding minutes plus15.327-minute inefficient read ([audit](native-vibe-q4-trusted-beets.md)) |
| Same VibeForged v2 Q6_K, explicitly trusted | Capacity complete; native41/41;11,566MiB sampled GPU | Grounded read and partial cancellation/docs; lifecycle unfixed,19 authored tests fail collection, no publication;9.564 coding minutes ([audit](native-vibe-q6-trusted-beets.md)) |
| Adapted27B IQ4_XS, public |98k CUDA OOM at ub128/64;64k passes all probes,15,788MiB peak GPU/no study swap;51,942-input request598.86s ([evidence](resource-adapted-iq4.md)); native confirms66/66 GPU layers | Local repair passes; docs reporting and cancellation counts/callback identity fail; no publication;85.75 coding minutes including2 failed summaries/native fallback ([audit](native-adapted-iq4-beets.md)) |
| FableVibes Q5_K_M, public | Possible intermediate; not downloaded or measured in this study | Not started |
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
