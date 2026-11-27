# Adapted 27B Q3_K_M: Gitea actions work, complete coding workflow fails

The public Q3_K_M completes all three dependent Beets requests in **48.01 coding minutes / 52.16 wall minutes**, but fails the requested repair, documentation accuracy, cancellation, regression tests and PR. All **54 backend calls complete**, without a context error, output-length finish, study swap or resource guard event. All three CLI exits are zero because the native repeated-edit safeguards end the turns; these are not successful-task completions.

This is one workflow with three dependent turns, not three independent trials. It supplies no autonomous reliability estimate or GPT-5 equivalence claim. Production configuration is unchanged. The [same artifact previously had qualified Announcer behavior/publication success](same-artifact-q3km-history-and-retention.json) in 20.65 minutes on an older runtime, while its Spam repair failed. That scoped positive result remains a reason to retain the file; it does not make the current Beets workflow pass.

| Turn | Coding minutes | Actual published result |
|---|---:|---|
| Repair and issue/fork/PR | 18.20 | Issue and personal fork; unused activation field, no functional repair or authored tests; no PR |
| Dependent documentation | 9.18 | Adds a disable/shutdown section which promises behavior the worker does not implement |
| Dependent cancellation feature | 20.63 | Same final source tree as the documentation turn, despite further accepted edit calls; no cancellation command/tests/PR |

The operator creates and seeds a disposable upstream with the unchanged 40-file baseline. Those operator actions are not model contributions or a teacher answer. The model itself opens upstream issue 1, creates its personal fork and submits eight accepted gateway file-edit calls on its contribution branch. Independent authenticated reads verify the actual fork parent, final head, all 40 final blobs and unchanged upstream baseline. No PR exists. The upstream issue is closed, confirmed by an explicit single-issue GET through both actor and connected operator reads.

The connected operator's private-fork branch listing reports `not found`; that tool does not expose an HTTP status. This is not evidence that the fork is absent. The separate authenticated actor read proves the fork and actual source bytes.

## Source and behavior

The published module adds `_activation_generation = 0` in initialization and assigns the current generation to it during load. **The new field is never read.** Thirteen original methods remain AST-identical, including worker dispatch, the import worker, disable/shutdown, timer stopping, folder validation, commands and reporting. Ordinary behavior is largely preserved, but the waiting/dispatched import defect is not fixed. There is no `beetscancel` registration or implementation.

The project and immutable original suites each report **83 passed, 2 subtests passed** after every turn. All eight original Beets test methods, and the entire Beets test file, remain unchanged. No regression or cancellation test is published. Green original tests therefore do not establish the requested behavior.

The unchanged supplementary controls run against a pinned real Nicotine+ 3.3.11 plugin handler after all actor turns, restoration and cleanup. Baseline and correct-reference controls qualify the observer before interpreting candidate results:

| Real-handler observation | Baseline | Correct reference | Published Q3_K_M |
|---|---|---|---|
| Old pending timer after fresh-instance reload; new work still runs | Pass | Pass | Pass |
| Old dispatched worker after fresh-instance reload; new work still runs | Fail | Pass | Fail |
| Worker already waiting at the import lock when disabled | Fail | Pass | Fail |
| Registered pending-work cancellation command | Fail | Pass | Fail |

The published source retains the observer's `_schedule`, threading and `_import_lock` bindings. These failures are not inferred from renamed private APIs. The separate folder-boundary controls also find the cancellation command absent; their same-object reactivation stress case passes and is explicitly not direct GUI-reload proof. All controls use fake timers/deferred workers and an import boundary, with no live GUI, network, music import or beets process. No private grader, reference answer or corrective feedback reaches the actor.

## Test-gate qualification and rejected proposals

All three turns stop at the native `gitea_edit_file` repeated-failure safeguard, with **8 / 8 / 8 reported consecutive failures**. The final DB assistant records are runtime guard messages, not generated closing success claims. No operator `continue`, resend, patch or policy change rescues the run. The gateway records **38 edit attempts: 8 accepted, 23 rejected by ordinary project/preservation test results, and 7 rejected as ambiguous edits**. Test paths are permitted. There are no outside-repository gateway denials.

An existing project test directly invokes `_import_worker(folder)`. Requiring new helper parameters breaks that private-helper ABI test, which alone does not prove public behavior is wrong. Two exact rejected proposals are independently observed through the same qualified real-handler controls, without changing source or asking the model to try again:

- The variant updating both timer arguments and worker signature abandons waiting work, but also blocks fresh active imports. Source inspection explains the mismatch between a job generation and the activation value; the observer reports **zero new imports** on a fresh enabled instance.
- The variant changing only the worker signature leaves the timer supplying one argument. Actual timer-dispatched work raises a missing-arguments `TypeError`, independently of the direct private-helper test.

Thus the private-ABI gate limitation is real, but it does not conceal a correct preserved-behavior repair in these proposals. The published fork remains unchanged in the relevant worker logic. The two curated proposal modules in the artifact are clearly labeled **unpublished**; they are not upgraded into completed repairs or model workflow success.

## Documentation and claims

The added README section says the worker checks generation and `_stopping` at the serialized import point, and that new activations permanently discard earlier waiting work. The actual worker is unchanged and does neither. It also promises normal exit-status reporting for already-running imports after disable, while the unchanged reporting functions return when stopping. Existing setup, command and file-safety text is retained, but cancellation documentation is absent.

The issue identifies the waiting-worker problem. Its reproduction steps mix pending-timer and already-dispatched states: step 4 leaves the second timer pending, which the baseline can cancel. Reproducing the worker race requires that work already be dispatched/waiting. The issue makes no authored-test or completed-PR claim. There is no generated final success statement to score as a false completion claim; the native guard messages end all three turns.

## Runtime, context and cost

The selected layout is **98,304 context / 66 of 66 reported GPU layers / ubatch 64**, with a **14,920 MiB sampled GPU peak** and about **1,355 MiB free**. Actual buffers are **12,153.77 MiB CUDA model / 521 MiB host model**, **1,728 MiB GPU KV**, and **408.50 MiB GPU compute / 17 MiB host compute**. All-layer offload is not zero host allocation.

Across **287 ten-second samples**, aggregate charged cgroups peak at **7,051,419,648 bytes**, process PSS at **2,522,446,848 bytes**, with zero study swap, guard events or measurement errors. Charged cache and relevant helpers are included; sampling can miss transient peaks. Both storage filesystems remain above the registered 101 GiB stop threshold and the user's 100 GiB floor.

The first real call takes **203.78 seconds** for **12,622 uncached input / 66 output tokens**. The largest completed prompt is **59,788 tokens**. No auxiliary/compression call occurs, and all three literal user requests remain in the final main request. Summary quality is untested; the failure is not attributed to lost compaction history. These timings measure a failed attempt, not time to a correct answer.

Actual first requests match the current IQ3_XXS/IQ4_XS references: the same 33 tool schemas, nonthinking temperature 0.8/top-p 1/top-k 0/min-p 0/repeat 1/presence 0, seed 20261124, 8,192 main/auxiliary caps, stream progress and qualified current evaluator/backend. Runtime uses one slot, q4_0 K/V, two context checkpoints, 512 MiB cache RAM, batch 512, eight threads, load `none` and automatic fit off. Quantized tensor mix/calibration, placement, microbatch and later trajectories prevent precision-only attribution.

Exact artifact: `netprojects/Qwen3.8-27B-hermes-adapted-GGUF`, revision `10fdf357f14825c61ad7eb42a932e1f1e4390e8f`, file `Qwen3.8-27B-hermes-Q3_K_M.gguf`, **13,752,764,064 bytes**, SHA256 `a0c809f93de2bcd813e1b6fbd5c2d1f692821814a4261a316f7c8bca9cf23248`. The file is fully rehashed before inference. [Download](public-adapted-q3km-download.md) and [capacity](resource-adapted-q3km-current.md) reports retain provenance, actual header/calibration differences and fit controls. Backend image is `fee4289628e7ba09f6fbf62d6ce4325aebb2531ffde2154d41276fe4acc58da3`; evaluator image is `c9b40eb8dea441cba7ded2e6589e5c011545ffc1ec76a0dc736f8e399d8f947b`.

## Preservation and reproducibility

Strict fresh-baseline checks pass for original container identities/images/configurations/running states, alias/context, four owner profile hashes, all 30 original model metadata records, both staged weights and owner pending edits. **Hermes-Codex's entire recorded state matches**, including its start time. This does not waive the historical IQ4 timestamp exception. Original services are restored; exact study backend, proxies, agent, network, supervisor and its exclusively attached anonymous volume are removed. Named model storage is retained. No new model default, custom quantization or GPU purchase occurs.

The [evidence archive](native-adapted-q3km-current-cold-beets-evidence.tar.gz) contains 186 manifest entries plus the manifest: full baseline/three captured source inventories, two curated unpublished modules, the three literal user requests, numeric observations, source findings and independent remote proofs. [Summary](native-adapted-q3km-current-cold-beets-summary.json), [validation](native-adapted-q3km-current-cold-beets-validation.json) and [privacy scan](native-adapted-q3km-current-cold-beets-privacy.json) state their limits. Raw actor requests/responses/consoles/DBs, credentials/profiles, private graders/reference code, signing keys, owner pending edits and other unpublished proposals are excluded.

```sh
python3 evaluations/2026-11-24-gpu-quant/verify_current_q3km_native.py evaluations/2026-11-24-gpu-quant/native-adapted-q3km-current-cold-beets-evidence.tar.gz
(cd evaluations/2026-11-24-gpu-quant && sha256sum -c native-adapted-q3km-current-cold-beets-evidence.sha256)
```

The standalone verifier checks saved source/measurement consistency. Eight recomputed-manifest tamper controls reject fabricated success, over-budget host memory, changed published worker, false closure, false Codex preservation, fabricated proposal success generated closing claims and altered user-task text. This is not new inference, live authentication, independent private-signature verification or full behavior-grader replay. See the [completed comparison](completed-current-quant-comparison.md) for the decision across candidates.
