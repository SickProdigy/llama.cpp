# Completed current-runtime quant comparison

Eight completed Beets workflows are independently audited below. **None passes the complete requested coding, follow-up and Gitea publication workflow.** Retain the deployed VibeForged Q4 default; no tested higher precision upgrade is justified by these cases. This is a practical hold decision, not evidence that Vibe is autonomously reliable.

| Candidate | GPU peak MiB | Repair / docs / feature minutes | Coding / wall minutes | Actual forge result |
|---|---:|---|---|---|
| [adapted-q4-current](native-adapted-q4-current-cold-beets.md) | 15,456 | 46.22 / 7.97 / 29.92 | 84.12 / not normalized | issue/fork/PR |
| [adapted-iq4-current-r2](native-adapted-iq4-current-r2-cold-beets.md) | 15,926 | 51.92 / 5.03 / 53.63 | 110.58 / 114.69 | issue/fork/PR |
| [adapted-iq3-current](native-adapted-iq3-current-cold-beets.md) | 12,904 | 19.76 / 7.56 / 5.18 | 32.50 / 36.50 | issue/fork; no PR |
| [fable-q5-current-thinking](native-fable-q5-current-thinking-cold-beets.md) | 10,224 | 13.68 / 2.97 / 15.20 | 31.85 / 34.71 | no issue/fork/PR |
| [fable-q6-current-thinking](native-fable-q6-current-thinking-cold-beets.md) | 11,566 | 8.07 / 4.24 / 24.36 | 36.67 / 40.39 | no issue/fork/PR |
| [fable-q8-thinking](native-fable-q8-thinking-cold-beets.md) | 14,624 | 21.33 / 2.12 / 15.23 | 38.68 / 42.45 | no issue/fork/PR |
| [vibe-q4-thinking](native-vibe-q4-thinking-cold-beets.md) | 8,964 | 20.71 / 5.94 / 25.55 | 52.20 / not normalized | no issue/fork/PR |
| [vibe-q6-thinking](native-vibe-q6-thinking-cold-beets.md) | 11,566 | 16.48 / 42.63 / 4.92 | 64.03 / not normalized | no issue/fork/PR |

## What the comparisons support

Fable Q5/Q6/Q8 share the current evaluator/backend, context, main/auxiliary controls and initial tool schemas. Q5 uses4.30GiB less peak GPU than Q8. Q5 passes its project/original suites while Q6/Q8 have additional project defects, but every workflow still fails required behavior and publication. Their durations measure failed attempts, not time to a correct answer. Public tensor production/calibration, cache and filesystem placement differ; no precision-only causal or monotonic quality claim follows.

Adapted IQ3 gives more GPU headroom than Q4/IQ4, but its two-line field rename breaks ordinary dispatch and all turns hit edit safeguards. Q4/IQ4 actually publish but fail the requested behavior. At98k, Q4 uses56/66 GPU layers and about2.9GiB host model buffers; IQ4 uses63/66 and1,250.63MiB host model buffers. Their load/latency/quant differences are not isolated precision effects. IQ4 R2 failed full Hermes-Codex preservation on an unexplained start timestamp change; its qualified restoration remains an explicit failed invariant. Later runs use fresh full Codex baselines, with no waiver.

Vibe Q4/Q6 both fail earlier code/test requirements. Q6 final context400 was masked as502 by the older recorder; the final phase is confounded. The transparent recorder correction is synthetically checked, but actual native recovery from a model context400 remains untested.

The [earlier wide-memory comparison](../2026-11-23-wide-memory/comparison.md) retains the correct Spam workflow (115.60 coding minutes) and behavior/publication-positive Announcer workflow (116.53 minutes, with README/reporting/metadata qualifications). These remain useful measured overnight tradeoffs on different tasks/runtime/layouts. They do not turn the current failed Beets cases into successes.

## Remaining decision-relevant work

Run retained Fable Q4 on the same current evaluator/settings as Q5/Q6/Q8 before comparing its precision/quality directly. Existing Q4 reasoning trials use an older evaluator. This requires fresh current capacity admission, then the same three natural tasks on a new fixture without hints or score feedback. The8,465,553,920-byte file is already retained; no download is needed. No successful Q4 outcome is assumed.

Additional public adapted Q3_K_M is metadata-only, not downloaded/admitted; staging is close to the100GiB reserve and useful models are protected. Larger adapted Q5/Q6 files exceed device capacity before context if fully GPU-resident; partly CPU layouts are unmeasured and storage-constrained, not proven quality failures. IQ3 q8 cache remains an unlaunched control, with no evidence its early source defect is cache-caused. See [options](../../MODEL-OPTIONS.md).

## Reproducibility and limits

[Normalized observations](completed-current-quant-comparison.json) bind all eight delivered source-summary hashes. Rebuild with `python3 build_completed_current_quant_comparison.py` from this directory. Individual reports contain source audits, pins, preservation, privacy and verifier limits. Missing wall values are explicit nulls, not zeros; Q4 wall is separately88.46 minutes in its linked report.

Every cell is one workflow with three dependent turns, not three independent trials. Quant precision is not a substitute for source/behavior/tests/docs/claims/publication audits. Native CLI success, project tests, capacity markers or PR creation alone are insufficient. No GPT5 equivalence or autonomous reliability is established. No deployment/default change, custom quantization or GPU purchase occurred.
