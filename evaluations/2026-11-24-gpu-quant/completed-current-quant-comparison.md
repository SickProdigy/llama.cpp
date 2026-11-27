# Completed current-runtime quant comparison

Ten completed Beets workflows are independently audited below. **None passes the complete requested coding, followup and Gitea publication workflow.** Keep the deployed VibeForged Q4 configuration; these cases justify no precision upgrade or autonomous replacement. This is a practical hold decision, not evidence that the default is autonomously reliable or a proof about every task/public quantization.

| Candidate | GPU peak MiB | Repair / docs / feature minutes | Coding / wall minutes | Actual forge result |
|---|---:|---|---|---|
| [adapted-q4-current](native-adapted-q4-current-cold-beets.md) | 15,456 | 46.22 / 7.97 / 29.92 | 84.12 / 88.46 | issue/fork/PR |
| [adapted-iq4-current-r2](native-adapted-iq4-current-r2-cold-beets.md) | 15,926 | 51.92 / 5.03 / 53.63 | 110.58 / 114.69 | issue/fork/PR |
| [adapted-iq3-current](native-adapted-iq3-current-cold-beets.md) | 12,904 | 19.76 / 7.56 / 5.18 | 32.50 / 36.50 | issue/fork; no PR |
| [adapted-q3km-current](native-adapted-q3km-current-cold-beets.md) | 14,920 | 18.20 / 9.18 / 20.63 | 48.01 / 52.16 | issue/fork; no PR |
| [fable-q4-current-thinking](native-fable-q4-current-thinking-cold-beets.md) | 8,964 | 14.10 / 1.11 / 19.16 | 34.37 / 37.77 | no issue/fork/PR |
| [fable-q5-current-thinking](native-fable-q5-current-thinking-cold-beets.md) | 10,224 | 13.68 / 2.97 / 15.20 | 31.85 / 34.71 | no issue/fork/PR |
| [fable-q6-current-thinking](native-fable-q6-current-thinking-cold-beets.md) | 11,566 | 8.07 / 4.24 / 24.36 | 36.67 / 40.39 | no issue/fork/PR |
| [fable-q8-thinking](native-fable-q8-thinking-cold-beets.md) | 14,624 | 21.33 / 2.12 / 15.23 | 38.68 / 42.45 | no issue/fork/PR |
| [vibe-q4-thinking](native-vibe-q4-thinking-cold-beets.md) | 8,964 | 20.71 / 5.94 / 25.55 | 52.20 / 55.02 | no issue/fork/PR |
| [vibe-q6-thinking](native-vibe-q6-thinking-cold-beets.md) | 11,566 | 16.48 / 42.63 / 4.92 | 64.03 / 67.35 | no issue/fork/PR |

## What the comparisons support

Fable Q4/Q5/Q6/Q8 share the current evaluator/backend, 98k context, main/auxiliary controls and initial tool schemas. Q4 uses 5.53 GiB less peak GPU than Q8; Q5 uses 4.30 GiB less. Q4/Q5 pass project/original suites while Q6/Q8 have additional project defects, but every complete workflow fails required behavior and publication. Their durations are failed attempts, not time to a correct answer. Public tensor production/calibration, cache reuse and storage placement differ; higher precision does not establish a monotonic quality improvement here.

Adapted IQ3_XXS and Q3_K_M both report 66/66 layers on GPU at 98k, plus 521 MiB host model buffers. IQ3 has more GPU headroom (12,904 versus 14,920 MiB peak), but its published field rename breaks ordinary dispatch. Q3_K_M preserves the original worker behavior yet leaves the requested bug and cancellation unfixed, publishes inaccurate documentation and no tests/PR, and ends all three turns at native edit safeguards. Its actual initial 33 schemas/sampler/caps/seed match IQ3/IQ4. A direct private-helper ABI test limits refactors; separately audited rejected Q3_K_M proposals also regress actual normal imports, so that limitation does not hide a correct repair in this case.

Q4/IQ4 actually publish PRs but fail requested behavior. At 98k, Q4 uses 56/66 GPU layers and about 2.9 GiB host model buffers; IQ4 uses 63/66 and 1,250.63 MiB host model buffers. Their load/latency/quant differences are not isolated precision effects. IQ4 R2 failed full Hermes-Codex preservation on an unexplained start timestamp change; its qualified restoration remains an explicit failed invariant. Later stages, including Q3_K_M, use fresh full Codex baselines with no waiver.

All four adapted variants produce an issue and personal fork, while the six Fable/Vibe cells do not complete those actions. That is an observed checkpoint-family/tool-use pattern in this small case set, not proof of a training cause or general agent reliability. Correct forge selection does not establish correct code.

Vibe Q4/Q6 both fail earlier code/test requirements. Q6 final context400 was masked as502 by the older recorder; the final phase is confounded. The transparent recorder correction is synthetically checked, but actual native recovery from a model context400 remains untested.

The [earlier wide-memory comparison](../2026-11-23-wide-memory/comparison.md) retains the correct Spam workflow (115.60 coding minutes) and behavior/publication-positive Announcer workflow (116.53 minutes, with README/reporting/metadata qualifications). The exact same Q3_K_M artifact also has older Announcer behavior/publication-positive evidence in 20.65 minutes, with documentation/reporting qualifications, while its older Spam repair fails. [Full-hash identity and retention review](same-artifact-q3km-history-and-retention.json) preserves these facts. These remain valid measured tradeoffs on different tasks/runtime/layouts. They do not turn current failed Beets cases into successes, and they are not discarded merely because they are slow.

## Selection, exclusions and untested alternatives

The additional public adapted Q3_K_M is now downloaded, fully hashed, capacity-admitted and [fully audited](native-adapted-q3km-current-cold-beets.md). It supplies no successful workflow upgrade. Fable's public Q5 intermediate is also fully tested; task-added Q5/Q8 files were retired with their provenance/evidence retained, while original model files remain protected.

[Measured storage exclusions](adapted-q5-q6-storage-exclusion-20261127.md) prevent adapted Q5/Q6 downloads on the current filesystems while preserving the user's 100 GiB reserve and retained-model constraints. Even hypothetically reclaiming only the new Q3_K_M file would leave 96.62/93.92 GiB after those transfers at the recorded observation. Their GPU/context/host-memory placement and partly CPU layouts remain unmeasured. File size alone is not substituted for actual allocation evidence.

[Public pinned alternatives](additional-public-quant-horizon-20261127.json) retain Fable Q3, Vibe Q3 and Vibe Q8 as untested options. They are not assumed to fit or improve quality; Vibe Q5 is absent at the selected publisher revision only. Fable/Vibe lower Q3 alternatives are not needed to fit their retained Q4 models on this GPU; no lower/higher-precision quality ranking is inferred. IQ3 q8 cache remains an unlaunched configuration control, with no evidence that its source defect is cache-caused. No claim to exhaust every public artifact or runtime configuration is made. See [options](../../MODEL-OPTIONS.md).

## Reproducibility and limits

[Normalized observations](completed-current-quant-comparison.json) bind all ten audited source-summary hashes. Rebuild with `python3 build_completed_current_quant_comparison.py` from this directory. Individual reports retain actual source, pins, preservation, privacy and verifier limits. All ten wall totals are recorded and tied to [captured terminal timestamps and launch IDs](completed-current-quant-terminal-timings.json). This validates saved observations, not live reinspection of removed containers.

Every cell is one workflow with three dependent turns, not three independent trials. Quant precision is not a substitute for source/behavior/tests/docs/claims/publication audits. Native CLI success, project tests, capacity markers or PR creation alone are insufficient. No GPT-5 equivalence or autonomous reliability is established. No deployment/default change, custom quantization or GPU purchase occurred.
