# MiMo 9B and local-workflow training — November 27

The pinned public MiMo V2.6 Distill Qwen 9B Q6_K loads **98,304 context / 33 of 33 GPU layers / 8,350 MiB observed peak GPU memory** on the existing P100 backend. The 7,793,710,624-byte download matches full SHA-256 `ef96d05a2ddf2cbb450d1af1ac3860ec769d3575bafa70692ee5609bda3fad7d`. This is capacity/serialization evidence, not a native coding/Gitea success or a new everyday-model recommendation.

Both the public Q6 built-in template and official ggml Q8 reference template complete the genuine tool call, its tool result and dependent history followup correctly. Built-in yields no nonempty reasoning in this short test; the reference configuration yields nonempty reasoning and retains it in the rendered next request. Templates differ in object-argument serialization and thinking prefill; they are explicitly separate configurations. The reference template is selected for the next reasoning trial.

Only the reference configuration receives the longer probes: exact markers at 16,164 / 59,934 / 79,929 actual input tokens all pass, taking 60.89 / 215.82 / 134.62 seconds. The later prompt can reuse a substantial prefix: these are not cold-cache benchmarks. Loading a 98k window and exercising about 80k input do not validate full-window coding. Aggregate observed study cgroup peaks are 6.56 GiB built-in / 4.40 GiB reference, including charged cache and supervisor; no study swap is observed. All 33 layers are reported on GPU; GPU allocation includes model, q4 KV, recurrent state and compute buffers.

The fresh strict postflight verifies all 20 model files, four owner profile hashes, selected owner source/pending work, original container IDs/images/configurations/running state, restored original Vibe alias/context and full unchanged Hermes-Codex state. The exact supervisor, backend containers and test network are removed. Model files remain in the usual `models/` directory. About 190 GiB free remains there.

[Machine-readable capacity/probe summary](capacity.json). Backend `b12723-abca69200` is unchanged; no CUDA/framework production upgrade, local model training or production model switch occurred.

## Native MiMo result

**Failed coding workflow, successful forge publication.** In one fresh development conversation, MiMo completes all three dependent tasks and publishes three commits through native local editing/tests and scoped Gitea MCP. The personal-fork branch targets the correct upstream PR. All local and independently cloned remote source digests match. Native exits are zero, and both the authored project suite and immutable original suite pass at every phase. Those facts do not establish correct plugin behavior.

The independent real Nicotine+ 3.3.11 checks fail every phase. The published plugin invents `core.buddies.is_buddy`; actual triggered requests raise `AttributeError`. Its tests invent the same method. The test named for repeated newly added users sends a second message without the trigger and therefore does not exercise duplicate-trigger suppression. The committed sibling `autospamignore` already shows the real `core.buddies.users` membership API. The final settings patch additionally compares a mixed-case configured phrase directly with `line.lower()`, failing the trimmed-preference check. The final answer's claims that case-insensitive matching and safeguards are preserved are unsupported by actual behavior.

| Dependent task | Coding time | Authored / immutable original suites | Real Nicotine checks | Publication |
| --- | --- | --- | --- | --- |
| New-buddy idempotency and regressions | 19.28 min | Pass / pass | Fail | Issue, fork, branch and upstream PR |
| Accurate Auto Buddy documentation | 2.63 min | Pass / pass | Fail; unchanged invented API | Same contribution updated |
| Live configurable room and trigger | 17.57 min | Pass / pass | Fail; invented API and mixed-case setting | Third commit and same PR updated |

Total coding time is **39.49 minutes** across 82 completed backend requests. The first request takes 65.80 seconds with 13,084 input tokens. The maximum actual request has 82,605 input tokens; native compression creates a retained child session during the final step. The GPU peak remains 8,350 MiB with 33/33 GPU layers. The aggregate observed study cgroup peak is 6.57 GiB, with zero study swap and no reserve breach. No grader feedback or operator correction is supplied to the model.

Fresh postflight confirms all 20 model records, four owner profile hashes, owner source/pending work, original container IDs/images/configuration/running state, original Vibe alias/98k context and the full unchanged Hermes-Codex state. Exact task containers, network and supervisor anonymous volume are removed; the useful named staging volume remains. Configured Gitea readback confirms test issue #1 is closed and PR #2 remains open and unmerged at `0185f3550e0d9571039d774576baf896865ebd41`. This failed trajectory is excluded from positive training data. [Machine-readable native summary](native-mimo-q6-summary.json).

A later read-only import probe in the Vibe actor confirms the shared development image lacks an importable `pynicotine` dependency. The independent grader uses the actual pinned Nicotine+ runtime; authored project tests can instead construct mocks. The published failures above remain real target-runtime defects, and sibling source already supplies the correct membership API, but this environment limits direct dependency verification during development. A separate prospective comparison will expose the same pinned real dependency read-only to both models and qualify native imports/offline handler construction before inference. Earlier results will remain separate; no private tests, reference fixes or grader feedback will be supplied to the actors.

This is one workflow with three dependent tasks, not three independent repetitions. The retained Vibe Q4 comparison uses the same predeclared tasks, native local-development tools, scoped publication and independent checker; its own declared sampler and builtin template differ. No new winner or production replacement is established.

## Retained Vibe control result — November 28

**Failed, with no published contribution.** The predeclared Vibe Q4 configuration receives the same task sequence and 32 actual CLI tool names. It takes **50.21 coding minutes / 156 completed backend requests**, versus MiMo's 39.49 minutes / 82 requests. Its first request takes 61.20 seconds with 12,391 input tokens; actual input later reaches 83,431 tokens. The final step has three retained lineage sessions, including two compression transitions. These are end-to-end observations, not cold throughput or precision-only comparisons.

| Dependent task | Coding time | Native exit | Authored / immutable original suites | Real runtime / publication |
| --- | --- | --- | --- | --- |
| New-buddy idempotency | 8.99 min | 1 | Pass / pass | Incorrect buddy API; unpublished |
| Documentation | 4.66 min | 0 | Pass / pass | Same runtime defect; unpublished |
| Live settings | 36.55 min | 1 | Fail / pass | Runtime and preference-contract defects; unpublished |

The plugin invents `core.buddies.buddies`. The final settings implementation uses a descriptor list and `core.settings` instead of the real plugin preference contract. The real-core ordinary case raises `AttributeError`; subsequent cases cannot re-enable the plugin. Those later outcomes are qualified as shared-handler failure/cascade observations, not eight independent defects. The authored suite ends with **2 failed, 100 passed and 2 subtests passed**. Its final response acknowledges two test-isolation problems but also claims core behavior works and leaves publication to the user.

Vibe claims the upstream is only on GitHub despite the correct selected Gitea origin being present in its initial user context. Public-mirror guidance also exists, but explicitly says pushes use configured Gitea. Readback through configured Gitea confirms the fixture's main remains `f9980ddc8aa6809e2f98f3ee95436bdb368e7a3d`, with zero issues and zero PRs. This is evidence of no published contribution; it is not a separate proof about whether any private fork exists.

The peak remains 8,944 MiB GPU / 41 of 41 layers, with a 7.25 GiB observed aggregate study cgroup peak, zero study swap and no reserve breach. Fresh strict preservation and exact cleanup pass, including full unchanged Hermes-Codex state. No grader feedback or operator correction is given. [Machine-readable Vibe summary](native-vibe-q4-summary.json). Both workflows remain excluded from positive training data; neither establishes a new everyday-model recommendation.

The completed runs report **95.93% MiMo / 95.68% Vibe token-weighted cached input**. Vibe's median backend request is 6.83 seconds versus MiMo's 14.74, yet Vibe uses 156 requests versus 82 and takes longer overall. These observations point toward iteration count and long requests, rather than a general prompt-cache failure, as important timing factors. Cumulative input counts repeatedly include shared history; they do not imply a multi-million-token context window. [Cache/timing audit](cache-observations.json).

## Dependency-qualified evaluator — November 28

A separate prospective comparison retains the task/checker/model settings while adding the actual pinned Nicotine+ 3.3.11 dependency to development. Its 507-file corpus is extracted from the same immutable target-runtime image and fully hash-checked. The isolated evaluator derives from the existing C9 image; production Hermes, llama.cpp, CUDA and driver configuration remain unchanged.

The first image's `PYTHONPATH` approach fails the actual native terminal import check: Hermes clears that variable. The corrected image uses a normal virtualenv site-packages path entry. A native terminal command now imports the pinned dependency and loads the original Auto Buddy through its actual offline plugin handler. All 83 original tests also pass. These zero-inference controls qualify dependency availability only. Both candidates then pass fresh wire serialization, two-identity/40-blob fixture admissions and native read-only MCP transport controls. MiMo's separate native trial is complete and audited; the matched thinking-enabled Vibe dependency-qualified trial is complete and audited. [Exact task prompts and cohort inputs](dependency-cohort-inputs.json). No private grader tests or reference fixes are exposed to actors. [Dependency environment receipt](dependency-environment.json).

## Dependency-available MiMo result — November 28

**Improved API use and publication, still a failed full workflow.** With the pinned real dependency importable in development, MiMo uses `core.buddies.users` correctly. All five registered runtime checks pass for its initial patch and documentation update. The initial request reaches its tool budget without the requested PR; the model admits that omission. It opens the upstream PR during the natural documentation follow-up, then publishes the settings commit to the same PR. No private grader feedback or operator fix is supplied.

| Dependent task | Coding time | Native exit | Authored / original suites | Registered real runtime |
| --- | --- | --- | --- | --- |
| New-buddy idempotency | 22.06 min | 1 | Pass / pass | 5/5 pass; requested PR delayed |
| Documentation | 4.58 min | 0 | Pass / pass | 5/5 pass; upstream PR opened |
| Live settings | 28.55 min | 0 | Pass / pass | 7/8 pass; mixed-case configured trigger fails |

Total coding time is **55.19 minutes / 119 completed requests**, with a maximum actual input of83,042 tokens and97.30% token-weighted cached input. The final authored suite has100 passing tests and2 passing subtests. The published patch compares the configured trigger directly with `line.lower()`, so a mixed-case preference fails despite its case-insensitive documentation claim. The model notices and fixes an intermediate room-selection error itself, but leaves this trigger defect in its submitted code.

A **separate posthoc source-review check** also confirms that its permanent acknowledgment cache blocks a legitimate add → remove → add cycle. The original plugin and working reference permit that cycle; both initial and final candidate source snapshots fail it. This supplemental result is labeled separately and does not rewrite the prospective primary grades. The corrected case-sensitive negative control isolates its intended failure. No supplemental feedback is sent to either actor.

Independent Gitea readback confirms issue1 closed and upstream PR2 open/unmerged from the personal fork, final commit `993fb2d1a2ddc8dcf3bde58c91eb26e31bb6382e`. Local and independently cloned published source digests match at every step. The GPU peak remains8,350MiB/33 of33 layers; aggregate observed cgroup peak is6.94GiB with zero study swap and both storage floors preserved. All20 models, owner profiles/source/pending work, original runtime configuration and full Hermes-Codex state pass preservation; exact task cleanup passes. This full trajectory remains excluded from approved positive training data. [Machine-readable result](native-mimo-q6-dependency-summary.json).

This is a development-environment comparison, not an isolated weight-only improvement or an untouched generalization task. The retained thinking-enabled Vibe comparison uses the same dependency-equipped evaluator after fresh two-identity baseline/fork-absence checks; its completed result is below. No new production default is selected.

## Dependency-available Vibe result — November 28

**Failed, unpublished local draft.** The thinking-enabled Vibe Q4 configuration takes **26.55 coding minutes /140 completed requests** over the same three dependent tasks. It uses the real `core.buddies.users` API, but checks dictionary membership case-sensitively. That misses an existing buddy with a different username case in every phase. Its project tests fail; the immutable83-test original suite passes.

| Dependent task | Coding time | Native exit | Project suite | Registered real runtime |
| --- | --- | --- | --- | --- |
| New-buddy idempotency | 10.43 min | 1 | Fail | 4/5 pass; existing-buddy case match fails |
| Documentation | 3.39 min | 0 | Fail | Same4/5 result; code unchanged |
| Live settings | 12.73 min | 1 | Collection error | 5/8 pass; case matching, preference descriptors and live updates fail |

The final plugin has no required preference descriptors and caches settings at startup. Its ad hoc settings callback does not make actual preference updates work. A leftover diagnostic `test_check.py` invokes test setup without class setup and breaks project collection. The blank-setting case passes because cached defaults still happen to satisfy that one path; it does not establish working live preferences. The separate remove/re-add supplemental check passes for both initial and final source, unlike MiMo's permanent-cache patch.

Configured Gitea readback finds the original fixture main unchanged with40 baseline blobs, zero issues and zero PRs. No remote-source grade exists. This proves no published contribution, not absence of every possible private fork. Its final text proposes GitHub CLI; no executed `gh` command is found in the final saved native history. No operator correction or private grader feedback is provided.

The peak remains8,944MiB GPU/41 of41 layers. Aggregate observed cgroup peak is7.22GiB, with zero study swap and both storage floors preserved. Actual input reaches83,390 tokens;97.71% of cumulative input is cached. Strict preservation verifies all20 models, owner profiles/source/pending work, original runtime and full unchanged Hermes-Codex state. Exact cleanup passes. The full trajectory is excluded from positive training data. [Machine-readable result](native-vibe-q4-dependency-summary.json).

Neither dependency-available configuration qualifies as a reliable unattended workflow. MiMo's published initial fix passes more registered behavior checks, but its delayed PR, configured-trigger defect and supplemental regression remain material. Vibe finishes sooner but has no correct published contribution; that duration is not a successful-task speedup.

A read-only profile audit finds the owner main output cap is4,096 and auxiliary compression explicitly disables thinking. The main thinking flag is unspecified in that file. The experiment explicitly enables thinking for both request types with8,192 caps, so it is not an exact everyday-profile replica. A separate [nonthinking configuration followup](vibe-nonthinking-prospective.json) is registered, retaining the current sampler, caps and task/evaluator controls. It will need fresh serialization/identity/fixture admission after the pending CPU software requalification. No production setting or default model has changed.

## Workflow and training parts

The new development case is Auto Buddy idempotency, accurate documentation and live configurable room/trigger settings on a clean copy of the same committed Nicotine+ plugin tree. Native local terminal/file tools perform edits and tests; the scoped workspace publisher uses actual configured Gitea MCP for publication, with issue/fork/PR operations. The redundant remote edit tool is omitted in this new profile. The task does not name a forge host; selected Git origin and persistent project context supply that preference.

The checker uses working-reference and deliberate-regression controls with the real offline Nicotine+3.3.11 plugin handler and buddy implementation. A later audit finds the old case-sensitive negative contains a syntax typo: its import failure does not qualify isolated case-sensitivity detection. The frozen file is preserved; a syntactically valid replacement now fails only the intended case-insensitive membership case, with the other four cases passing. This correction does not alter primary checker code or the directly observed candidate runtime results. [Control audit](checker-control-audit.json). GUI delivery and network user watching are stubbed; no Soulseek connection occurs. There is no private-helper-signature publication gate. Original tests, public behavior, authored regressions, final claims and actual remote bytes are still independently checked after each turn. This is a new workflow configuration and a development case, not an untouched generalization holdout.

A retained VibeForged Q4 comparison is prospectively planned under the same new workflow and tasks, with its declared baseline sampler. Improvements over older remote-edit Beets cases cannot be attributed solely to MiMo. Both original development-environment comparisons above are complete; MiMo's separate dependency-qualified trial is complete, and the thinking-enabled Vibe dependency trial is complete. Its fresh capacity check loads 98,304 context with 41/41 GPU layers, peaks at 8,944 MiB GPU memory, and passes the tool call/result/dependent-history sequence. Aggregate observed study cgroup peak is 6.55 GiB with no study swap. Fresh strict preservation and exact cleanup pass before its separate native trial. [Vibe control capacity receipt](vibe-control-capacity.json).

The separate private [hermes-tool-training repository](/chatgpt-codex/hermes-tool-training) contains reviewed tool-trajectory validation, whole-family holdouts, resumable LoRA jobs, independent result comparison, exact-base merging and export preparation. Tiny synthetic CPU smokes establish machinery only. Three reviewed component seeds are now available privately; a broader dataset and actual training-PC GPU qualification remain required before a useful fine-tune.

Primary artifact references: [publisher](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B), [public Q6](https://huggingface.co/bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF), [official template reference](https://huggingface.co/ggml-org/MiMo-V2.6-Distill-Qwen-9B-GGUF).

Native launch admission subsequently stopped before inference because Docker's separate staging filesystem reached its reserve. The obsolete task-added IQ4 copy there was retired under the owner's cleanup authorization, restoring about112.76GiB free; main-folder20 and useful stagedQ3 are unchanged. See the cleanup report's staged-retirement receipt. This was a storage admission event, not a model-quality failure.


## November 28 resumed nonthinking Vibe comparison

The registered nonthinking comparison is complete. It fails the workflow in14.94 coding minutes across80 requests: no repository changes, no authored tests, no issue and no PR. This uses the same C11 dependency image, Vibe Q4 weights,98,304 context,41/41 GPU layers, sampler and8,192 output caps; thinking is explicitly false for main and auxiliary. The actual first native wire has32 tools, the selected fixture context and no remote-edit tool. This is one development configuration comparison with three dependent tasks, not an exact everyday-profile replica or reliability estimate.

| Dependent task | Coding time | Native exit | Source changes | Registered real runtime |
| --- | --- | --- | --- | --- |
| New-buddy idempotency | 9.42 min | 0 | None | 3/5 pass; requested behavior remains absent |
| Documentation | 3.31 min | 0 | None | Same3/5 baseline result |
| Live settings | 2.21 min | 0 | None | 4/8 pass; requested settings remain absent |

All80 native tool calls are46 `skill_manage` and34 `skill_view`. The46 proposed skill operations are staged for approval, not applied; the actor repeatedly tries to read a nonexistent `autobuddy-integration` skill and rereads unchanged existing skills. The native no-progress guard ends each phase. Exit0 therefore means a stopped conversation, not successful work. Normal skill approval is retained; no operator approves these edits or feeds the actor corrections. This failure does not establish that thinking should universally remain enabled, but disabling it alone did not help this workflow.

The unchanged original83 tests pass at all three steps; that is not proof of new functionality. Real Nicotine+3.3.11 checks remain at3/5,3/5 and4/8. All source digests match the baseline. The separate remove/re-add supplement also passes on the untouched original source, with valid semantic controls; it does not satisfy the requested changes. Configured Gitea MCP independently confirms fixture main `f9980ddc8aa6809e2f98f3ee95436bdb368e7a3d`,40 baseline blobs, zero issues and zero PRs. No claim is made about absence of every possible private fork.

Peak GPU memory is8,944MiB, aggregate observed study cgroup peak6.93GiB, with zero study swap. Maximum actual prompt input is50,060 tokens. Strict preservation and exact cleanup pass for all20 models, owner profile/source/pending work, original service identity/image/config/running state and full Hermes-Codex state. The normal services are restored. The failed trajectory is excluded from positive training data. [Machine-readable result](native-vibe-q4-nonthinking-summary.json).

The first resumed startup attempt encountered a missing pinned test-backend image before any model request. It was independently restored and archived, and is not counted as a model failure or hidden model retry. The exact old backend image was recovered from an immutable official AMD64 manifest after a storage admission check, leaving more than100GiB free on Docker storage. The scored attempt uses that recovered original backend; production images were not downgraded.

Next diagnostic: prospectively compare a leaner native tool configuration while preserving local coding/testing and configured Gitea publication. The observed skill-management loop gives a specific reason to test tool selection before downloading another quantization. Keep this separate from model-only comparisons and retain normal owner approval settings.


A [skills-disabled configuration comparison](skills-disabled-prospective.json) is now registered before inference. It removes only `skills_list`, `skill_view` and `skill_manage` from the completed nonthinking setup, preserving memory and approval settings. Native oneshot schema selection verifies the expected29 tools; terminal and actual scoped Gitea identity/repository reads pass, with writes denied under the read-only preflight lease. Both authenticated identities verify the original40 fixture blobs, zero issues/PRs and absent actor fork. This untouched fixture can be reused without another duplicate repository. The first SDK schema check included GUI-style `clarify`; using the native oneshot selection removes it as the CLI does. That operator-only check performed no inference or forge writes and is not a model result.


## Skills-disabled comparison: complete, still fails

The registered29-tool nonthinking Vibe comparison finishes in8.07 coding minutes across178 requests. It leaves the source unchanged and publishes no contribution. All175 native tool calls use `execute_code` to attempt an invented `git search_repositories` command. The code prints only subprocess stdout, omitting stderr and return status; an empty output is repeatedly treated as another search to try. Removing skill tools changes the loop, not task success. No operator correction or private grader feedback is supplied.

| Dependent task | Coding time | Native exit | Source changes | Registered real runtime |
| --- | --- | --- | --- | --- |
| New-buddy idempotency | 3.32 min | 1, iteration limit | None | 3/5 baseline cases pass |
| Documentation | 2.12 min | 0, no-progress stop | None | Same3/5 baseline result |
| Live settings | 2.63 min | 1, tool limit | None | 4/8 baseline cases pass |

The actual initial wire confirms29 tools, thinking false,8,192 output cap and selected fixture context. Original83 tests pass and all source digests remain equal; there are no authored regressions. The separate remove/re-add supplemental check passes on the untouched baseline, not on a new fix. Actual configured Gitea MCP readback confirms original main/40 blobs, zero issues and zero PRs. Absence of every possible private fork is not claimed. The viewer process terminates before the run ends; complete native SQLite snapshots, recorder metrics, exact supervisor events and independent final grades remain available. The test is not restarted.

Observed peak GPU memory is8,944MiB with all41 layers offloaded; aggregate study cgroup peak7.09GiB, zero study swap, and actual maximum input43,401 tokens. All20 retained models, owner profiles/source/pending work, original runtime and full Hermes-Codex state pass preservation. Exact task cleanup passes and normal services are restored. Full failed trajectories remain ineligible for positive training. [Machine-readable result](native-vibe-q4-skills-disabled-summary.json).

This single dependent development workflow supports keeping the default unchanged and rejecting this configuration as an improvement. It does not establish a general benefit from removing skills or enabling/disabling thinking.

## Newly researched candidates, not model-quality results

The official [Mellum2.1 Instruct card](https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Instruct) describes a12B/2.5B-active MoE trained with repository shell/file workflows and131,072-token context. Its official GGUF repository was updated November26. The pinned public Q6 is10,879,833,184 bytes. A bounded16MiB header inspection identifies `mellum`,28 layers,128-dimensional attention heads and a built-in template; the pinned llama.cpp source includes the architecture. These facts justify a compatibility test, not a GPU-fit or agent-performance claim. Publisher claims have not been independently reproduced. [Pinned selection, exact checksum and gates](mellum21-candidate.json).

Download admission occurs only after the completed skills-disabled preservation and cleanup. The file goes directly into `llama.cpp/models`, with a separate partial filename, size/full-SHA checks, per-chunk storage checks and no duplicate Hugging Face cache copy. Preserve the existing20 models and100GiB reserves. A fresh before/after runtime/profile/source/model check must finish before GPU qualification. No production configuration change, MTP head or real training is part of this download. Next gate is measured98k GPU fit and genuine short tool/result/history calls before any coding workflow.

A same-publisher, same-revision [MiMo Q8 candidate](mimo-q8-candidate.json) is also pinned at9,545,979,424 bytes. It remains undownloaded as a possible later precision comparison with Q6. Higher precision is not assumed to repair the observed code and reasoning defects. Mellum tests a different candidate before another MiMo quantization.


Mellum now passes [operator-only profile/wire and native transport preflights](mellum21-preflight.json):32 native tools, configured Gitea identity/repository reads, normal memory/skills approvals, main/aux thinking false and8,192 caps. Both identities verify the original40 fixture blobs, zero issues/PRs and actor fork404. No inference is involved. Separate [resource qualification](mellum21-resource-prospective.json) and [three-task native workflow](mellum21-native-prospective.json) protocols are registered before model calls; successful download, measured resource/tool compatibility and preservation remain launch gates.

The training repository now provides reviewed-data bundling and receiving-side verification, committed as `ed2019e`. Its53 unit tests and a byte-identical local relocation of the private3-component seed bundle pass. The source approvals and exact train/evaluation split remain linked; no raw captures, weights or credentials are copied. No external transfer or actual training occurs. A broader dataset and actual training-PC qualification remain required.


Before Mellum inference, an [explicit-seed amendment](mellum21-explicit-seed-amendment.json) pins main and auxiliary requests to20261127 and short capacity probes to20261123. The unused seed-unspecified profile and receipts are archived; fresh wire/transport checks are repeated. No model result or GPU test preceded this amendment, and the live weight download is unchanged.


The [Mellum Q6 download](mellum21-download.json) is complete:10,879,833,184 bytes and full SHA match the pinned public artifact. It took16.14minutes. All original20 models remain unchanged; the main-folder count is now21. Independent before/after checks verify full unchanged service/Codex state, owner profiles/source/pending work and storage reserves. No GPU qualification, workflow or training has started at this point. The artifact is directly under `llama.cpp/models`, with no duplicate HF cache copy.


## Mellum short GPU/tool qualification: pass

The public Q6 loads98,304 context with29/29 layers onGPU and observed peak11,124MiB. Three actual responses pass: exactly one valid `lookup_record` call, completion using the supplied result with no extra tool call, and exact dependent-history value. No separate reasoning is returned. Aggregate observed study cgroup peak is6.57GiB with zero study swap. Normal services are restored; all21-model inventory, owner profiles/source/pending work and full unchanged Hermes-Codex state pass preservation, followed by exact task cleanup. [Capacity result and retained responses](mellum21-capacity.json).

This establishes loaded allocation and short tool-history compatibility only. No long synthetic retrieval probe, actual MCP mutation or coding workflow is included. The registered full native development comparison remains the next gate, after fresh two-identity fixture readmission.


## Mellum Instruct native workflow: complete, fails

Mellum2.1 Instruct Q6 finishes the three dependent tasks in3.90 coding minutes,33 requests and30 model-visible tool calls. Every native exit and project-suite run is zero, yet the actual handler fails the requested behavior. This is a fast failed draft, not a successful-task speedup.

| Dependent task | Coding time | Project suite | Registered real Nicotine runtime |
| --- | --- | --- | --- |
| New-buddy idempotency | 2.37 min | Pass | 2/5; invented `Buddies.list_buddies()` breaks all triggering cases |
| Documentation | 0.51 min | Pass | Same2/5; no API repair |
| Live settings | 1.02 min | Pass | 2/8; invented API persists, preference declaration also fails |

The first patch invents `core.buddies.list_buddies()` despite the installed3.3.11 dependency being available. Its new test files contain only empty `pass` test bodies: three initially and six finally. All original83 tests pass, but the new tests detect no behavior. The primary authored-regression collector only searches `tests/`, so it lists none for these root-level files. A separate posthoc source/AST review and actual baseline replay includes every root test and confirms they also pass without any fix. This omission in automatic discovery does not change the directly observed runtime failures; primary grades remain untouched.

The documentation step changes the plugin description, not a README. The final code defines `setup()` without preference metadata/class defaults. The actual preference check fails; other final cases are blocked by the invented buddy API, so those failures do not independently isolate every settings defect. Final success/ready-for-use claims are contradicted by the real handler.

Three local commits on local `main` are real, ending at `78e62b2a016de01acc273af6addd90249e3fc45c`. They are not a personal-fork/upstream contribution. There are no Gitea calls or transport records, and no forge dispatch inside `execute_code`. Actual configured MCP readback and both-identity full-blob checks confirm original40-blob upstream main, zero issues/PRs and actor fork404. Ordinary local code editing is not a wrong-host forge action; the failure is missing publication. No new test repository was needed.

Observed peak GPU memory remains11,124MiB/all29layers. Aggregate observed cgroup peak is7.13GiB with zero study swap; maximum actual prompt is28,688 tokens. All21 model files, owner profiles/source/pending work, original runtime and full unchanged Hermes-Codex state pass preservation; exact cleanup passes. No operator correction or grader feedback is provided. The full trajectory is excluded from positive training. [Machine-readable result, supplemental controls and root-test review](native-mellum21-instruct-summary.json).

The next candidate is the separate official [Mellum2.1 Thinking Q6](mellum21-thinking-candidate.json). Pinned metadata confirms matching tensor names/dimensions/types and a different thinking template; this does not prove fit or quality for its weights. Plan16k main/8k auxiliary output caps at98k context, reasoning enabled, before inference. This is a declared accuracy-first configuration comparison, not a pure thinking-flag toggle. A fresh verified download/preservation and measured thinking-compatible short tool/history qualification remain required. Same-publisher MiMo Q8 remains an undownloaded fallback candidate.


Thinking preflight now verifies actual HTTP serialization of both the main16k and compression8k request paths, reasoning enabled, seed20261127 and the declared sampler, with no inference. The actual native32-tool transport and both-identity40-blob/no-issue/no-PR/fork404 fixture admission pass. A new-controller-only regression-discovery amendment includes pytest-discovered root/module test files and fixtures. Executing that actual grader function on the preserved bad Instruct snapshot finds all three root test files, confirms they pass on baseline, and still rejects real runtime behavior. This is an operator coverage check, not a new model repetition; old scores are unchanged. [Preflight and grader evidence](mellum21-thinking-preflight.json), [resource protocol](mellum21-thinking-resource-prospective.json), [native protocol](mellum21-thinking-native-prospective.json). No Thinking GPU or coding-quality result is claimed yet.


The [Thinking Q6 download](mellum21-thinking-download.json) is complete:10,879,834,400 bytes and fullSHA match the pinned artifact. Before/after checks preserve the previous21 models, full runtime/Codex state and owner profiles/source/pending work. Main-folder inventory is now22, all100GiB reserves preserved. The file is directly under `llama.cpp/models` with no duplicateHFcache. Actual Thinking GPU/tool and coding qualification remain pending.


## Mellum Thinking short compatibility: pass

The Thinking Q6 independently loads98,304 context with29/29 GPU layers and observed peak11,124MiB. It returns exactly one correct lookup, completes using the supplied result without another call, and returns the exact dependent-history marker. Separate reasoning is present in all three responses and retained in the rendered tool-result continuation; raw reasoning is kept private and is not training data. The16k probe cap and actual main16k/compression8k serialization are verified. Aggregate observed study cgroup peak is6.57GiB with zero study swap. All22models, owner profiles/source/pending work and runtime/fullCodex state pass preservation and exact cleanup. [Measured result](mellum21-thinking-capacity.json).

This remains short compatibility, not coding correctness, actual MCP routing or long-context retrieval quality. The declared three-task native workflow is next after fresh fixture readmission, with no operator correction or private grader feedback.


## Mellum Thinking native workflow: better initial code, still fails

The three dependent tasks finish in **27.86 coding minutes**,96 requests and92 model-visible tool calls. Native exits are all0, with no external timeout. This is an accuracy-first16k-main/8k-auxiliary configuration with reasoning enabled, not a pure flag toggle against Instruct's8k main cap.

| Dependent task | Coding time | Real Nicotine checks | Forge result |
| --- | --- | --- | --- |
| New-buddy idempotency | 11.12 min | 5/5 | Upstream issue #1; no personal-fork branch or PR |
| Documentation | 5.78 min | 5/5 unchanged runtime | No publication |
| Live settings | 10.95 min | 7/8; preferences declaration fails | No publication |

The initial patch uses actual `core.buddies.users` with casefold comparisons. Two authored regression tests fail semantically on original code (duplicate acknowledgement and mixed-case duplicate insertion), then pass with the fix. All83 original tests remain green; final project suite is85 tests plus2subtests. Separate posthoc removal-and-re-add checks pass for both initial and final snapshots, unlike MiMo's cached acknowledgement implementation. No private checks or corrections are fed to the actor.

The final code reads current settings and trims/falls back, but declares neither native `settings` defaults nor `metasettings`. The preferences check fails before its configured-value assertions; live-change and blank-fallback cases pass. The authored tests remain the two initial cases and do not cover preferences. README/PLUGININFO edits retain inaccurate auto-add-on-join wording and advertise configurability without native preference declarations. Runtime checks alone do not establish documentation correctness.

The model uses Gitea and learns its login is `hermes-agent`, yet sends upstream owner `chatgpt-codex` as the working fork owner and sends `hermes-agent` as a repository fork name. Normal scope guards reject these arguments. Its final authentication/network explanation is unsupported by those errors. Upstream issue **#1** is created (database ID1622, mistakenly cited as the issue number in finals); no successful remote branch, commit or PR is recorded. Two local commits ending `ece760b` do not complete publication. All turns finish naturally; more iteration allowance is not an established remedy.

Observed peak GPU memory is11,124MiB with29/29 layers at98,304 context; maximum actual prompt is65,750tokens. Aggregate observed study cgroup peak is6.55GiB with zero study swap. Minimum free space stays108.23GiB on Docker root and168.90GiB on the model/staging filesystem. All22 model files, owner profiles/source/pending work, original runtime and full unchanged Hermes-Codex state pass preservation and exact cleanup. The owner default is unchanged. The complete failed trajectory is excluded from positive training. [Measured native result](native-mellum21-thinking-summary.json).

Thinking is substantially better than Instruct for this initial code task, but neither qualifies for unattended contributions. A useful next controlled comparison is automatically supplied, verified workspace roles (authenticated actor, Git-origin upstream and personal-fork destination), with no per-task implementation hint. It must use its own registered protocol; these results must not be relabeled after changing tools/context. A fresh Announcer family is separately reserved from training and still awaits checker-control qualification. Same-publisher MiMo Q8 remains undownloaded.


The reserved fresh Announcer family now passes operator checker qualification: initial/final references10/10 and12/12, a semantic negative is detected, and both reference changes preserve83 original tests/2subtests. Two harness setup errors are preserved and corrected before any model exposure. Exact checker/reference answers remain private, and the training repository rejects this family from both SFT and loss evaluation. This is test-bank qualification, not a new model success. [Qualification receipt](fresh-announcer-checker-qualification.json).


## Automatic workspace roles: native preflight passed

The optional [workspace-roles hook](../../hermes-profile/workspace-roles/README.md) now derives explicit upstream and personal-fork identities from selected Git and authenticated read-only Gitea metadata. It retains renamed selected personal forks and reports unavailable/conflicting metadata without raw transport exceptions. It neither rewrites model write arguments nor grants permissions.13 unit checks and the actual registered native hook pass; all32 full native tool schemas match the previous Thinking run, unrequested writes stay blocked, and main16k/aux8k serialization is unchanged. Both identities independently verify a fresh private40-blob fixture with no issues/PRs or actor fork. [Preflight evidence](workspace-roles-preflight.json).

The next separately registered development comparison repeats the same three AutoBuddy tasks with Thinking Q6 and this automatic context. It is a context/interface intervention, not a new independent benchmark or weight improvement. The separate reserved Announcer task remains unexposed. The owner profile/model is unchanged.


The first cold roles-context admission is an infrastructure failure, not a model score: its generated backend hostname was64 characters and Python IDNA lookup rejected it. No actor/LLM request was sent. A controlled exact-supervisor stop restored original services; all22model records, owner source/profile and fullCodex state match their baselines. Exact owned cleanup passed, and failed source/protocol/logs are preserved.

A separately registered short namespace admits58–59byte dialed labels before owner stop. Actual DNS lookup, refreshed native context/schema/cap checks and both-identity40-blob fixture readmission pass. The first actual native request now contains verified upstream/actor/fork roles,32unchanged tools, reasoningtrue,16384 main output cap and seed20261127. The coding/publication trial is live; no quality success is claimed. [Admission and correction evidence](workspace-roles-native-admission.json). Owner defaults remain unchanged; exact postflight preservation/restoration/cleanup runs independently after the supervisor terminates.


## Explicit public issue/PR numbers: optional response format

The live role-context development run creates its fork, branch, commits and issue, then repeatedly attempts a PR referring to databaseID1623 rather than public issue #1. Its original0.1.6 plugin/profile remain frozen; the trial is not corrected or relabeled. This observation motivates an optional0.1.7 focused-plugin result format for future trials.

With `explicit_reference_numbers: true`, issue/PR responses begin with `issue_number`/`pull_number` matching existing tool argument names. The native public `number`, prose/state and other fields remain; the top-level database `id` is omitted. Missing valid public numbers cause an error rather than a database-ID fallback. The option defaults to false. All focused tool schemas and native mutation arguments/permissions remain unchanged.35unit checks and pure replays of two actual captured responses pass, with zero model/transport calls. [Replay evidence](explicit-reference-numbers-preflight.json). No native deployment or model improvement is claimed; actual per-profile qualification and the fresh-family comparison remain required. The fresh Announcer prospective plan is amended before any actor exposure to use the same qualified presentation across all candidates.


## Workspace-role comparison complete: publication improves, workflow fails

With automatic verified roles, Thinking Q6 finishes the three dependent tasks in **23.71 coding minutes**, or **27.71 minutes from supervisor launch until original services are restored**. The actual runtime grades remain5/5,5/5 and7/8; project and original83-test suites pass throughout. The first native exit is1, later exits0, with no external timeout. Earlier status described the first exit as a60-turn-limit termination; the allowed60turns and exit1 are confirmed, but the available log does not independently establish its exact cause.

The model now creates its actual personal fork, a valid feature branch, three remote commits and upstream issue #1. Repeated PR attempts reference globaldatabaseID1623 rather than public issue #1 and are rejected by the existing guard. No PR is created. Configured Codex-MCP readback confirms issue1closed/noPR; its private-fork lookup returns notfound. A separate authorized actor-identity audit verifies the fork parent and every one of41branch blobs: they match the documentation snapshot, not the final local settings changes. All40original upstream blobs remain unchanged. Final local commit `b610170` is not the published branch head `d4c5e5c253bb51aebe43da8a0a6eca9506154687`.

Two new tests fail original code on meaningful existing-buddy/casefold assertions. The repeat-named test is unfinished after first-call checks and clearing users; do not infer repeated-trigger regression coverage from its name. Independent real repeated-trigger and posthoc removal/re-add checks pass. The final code still omits native settings/metasettings declarations; the preference case fails before configured-message checks. Source also leaves the configured phrase unlowercased when comparing with `line.lower()`. PLUGININFO is updated, but rootREADME remains unchanged and the final description advertises unavailable native preferences.

Across104completed backend requests, maximum actual input is59,306tokens. Observed GPU peak is11,124MiB/all29layers; aggregate study cgroup peak6.65GiB, zero study swap. Minimum free space is108.47GiB Docker root/168.74GiB model storage. All22model records, owner profile/source/pending work, original runtime and full unchanged Hermes-Codex state pass preservation and exact owned cleanup. No private feedback/operator repair is fed to the actor; the full failed trajectory is excluded from positive training. [Complete result and actor byte readback](native-mellum21-thinking-workspace-roles-summary.json).

## Public reference numbers: actual native qualification passed

The optional0.1.8 plugin exposes explicit `workspace_publication_only: true` to reproduce the32-tool local-edit/workspace-publish interface without a private source patch. Combined with `explicit_reference_numbers: true`,36unit checks and actual registered native MCP issue/PR/read/list/context checks pass. Public issue1/PR2 remain the reference numbers; top-level database IDs are omitted. Actual full schemas match the frozen32-tool trial and unrequested writes remain blocked. Two operator setup failures are preserved: copying the generic plugin restored remote-edit registration, and an unbound fresh actor proxy correctly hid existing references. Qualification uses a narrowly bound read-only operator proxy for the existing development case, zero model calls or forge mutations. [Native admission](explicit-reference-numbers-native-qualification.json).

The completed model result above keeps its original raw-response interface. Fresh-family model comparisons still need their own exact profile/cap/fixture admissions with the newly qualified optional settings. No production profile switch, adapter training or new model-quality success is claimed.


## Same-publisher MiMo Q8: download and resource plan

The next precision candidate is `MiMo-V2.6-Distill-Qwen-9B-Q8_0.gguf` from the same pinned bartowski revision as retainedQ6. The9,545,979,424-byte public artifact is downloading directly into the usual `llama.cpp/models` directory, with a guarded partial file, exact fullSHA admission, no duplicate HF cache and preservation of all22original model records/runtime/owner state and100GiB reserves. No service stop, inference or training runs during the download. [Pinned artifact, header and resource plan](mimo-q8-download-resource-prospective.json).

The local32MiB append-only prefix matches Q6's architecture,427tensor names/dimensions, tokenizer and builtin chat template. Q6 contains125Q6_K/77Q8_0/225F32 tensors; Q8 contains202Q8_0/225F32 tensors. These are tensor type counts, not proof of identical float values or model correctness. Full download/checksum remains required.

The separately gated resource plan selects the same pinned official reference template used by the leadingQ6 configuration,98,304context/all33GPU layers/q4KV and16k output cap. It requires exactly one correct lookup, actual tool-result completion without extra calls, an exact dependent-history answer and16k/60k/80k marker probes. Markers may reuse prefix cache; they are not cold throughput or real coding/Gitea success. Per-model fresh native profiles still need16kmain/8kaux serialization and actual role/number/schema/fixture admission. The owner default remains unchanged.


The [Q8 download is complete](mimo-q8-download.json):9,545,979,424bytes and fullSHA match the pinned public artifact, using one HTTP request with no retries. All22previous model records, owner profile/source/pending work and full runtime/Codex state are unchanged; main-folder inventory is now23. The file is in the normalmodels folder with no duplicateHFcache. Model storage has about159.70GiB free and Docker storage108.52GiB, above all100GiB floors. GPU fit/tool/history/large-input admission and fresh coding still remain unproven.


## MiMo Q8 reference-template compatibility: pass

The same-publisher publicQ8 independently loads **98,304context /33of33GPU layers /9,788MiB observed peak GPU memory** with automatic fitting disabled. Load/readiness takes63.24seconds. It emits exactly one correct lookup, completes using the real supplied result without further tools and answers the dependent-history question exactly. Separate reasoning is present and retained in the rendered continuation; raw reasoning remains private and is not training data.

Exact synthetic markers at15,984/59,934/79,929actual input tokens all pass, taking72.29/256.40/144.60seconds. These later prompts may reuse a substantial prefix, so this is not a cold throughput comparison. The16k probe cap differs from the olderQ6 resource test's8k cap; freshQ6/Q8 coding comparisons must use matching16kmain/8kaux budgets. A loaded98k window and these marker/tool-history passes do not establish full-window coding or real MCP publication correctness.

Aggregate observed study cgroup peak is6.56GiB, with zero study swap. Minimum free space remains108.38GiB Docker root/159.61GiB model storage. All23model records, owner profile/source/pending work, original runtime and full unchanged Hermes-Codex state pass preservation; exact owned supervisor/model/network/anonymous-volume cleanup passes and the named useful staging volume remains. OriginalVibe alias/context are restored. [Complete measured result](mimo-q8-capacity.json).

Q8 now meets the selectedGPU/context/resource/tool-history admission. No scored fresh native coding/Gitea trial has used it yet. The next step is the reserved Announcer comparison with the qualified automatic roles/public-number presentation, fresh fixtures/profiles and meaningful independent behavior/publication checks. No production default switch or training has occurred.

## Fresh Announcer native comparison started

The once-only MiMo Q8 supervisor has started for the reserved Announcer queued-send family. Actual native transport, all 32 tool schemas, automatic forge roles, both fixture identities and main16k/aux8k serialization admissions pass. The real grader wiring rejects the baseline and a semantic negative, accepts both reference repairs, and preserves the original83tests. These are harness admissions, not model wins.

The model must repair stale/canceled queued sends, document the behavior, then honor the live Sending enabled setting, publishing through an upstream issue, its own fork/branch and an unmerged upstream PR. It receives no private grader results or reference fixes. The entire family remains excluded from training and loss evaluation. Planned order is Q8, matched Q6, Vibe Q4 and Mellum Thinking; publisher samplers differ across model families. No fresh coding verdict is available yet. [Registered admission and comparison details](fresh-announcer-native-admission.json).
