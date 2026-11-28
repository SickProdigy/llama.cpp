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

The separate private [hermes-tool-training repository](/chatgpt-codex/hermes-tool-training) contains reviewed tool-trajectory validation, whole-family holdouts, resumable LoRA jobs, independent result comparison, exact-base merging and export preparation. Tiny synthetic CPU smokes establish machinery only. Real reviewed training data and actual training-PC GPU qualification remain required before a useful fine-tune.

Primary artifact references: [publisher](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B), [public Q6](https://huggingface.co/bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF), [official template reference](https://huggingface.co/ggml-org/MiMo-V2.6-Distill-Qwen-9B-GGUF).

Native launch admission subsequently stopped before inference because Docker's separate staging filesystem reached its reserve. The obsolete task-added IQ4 copy there was retired under the owner's cleanup authorization, restoring about112.76GiB free; main-folder20 and useful stagedQ3 are unchanged. See the cleanup report's staged-retirement receipt. This was a storage admission event, not a model-quality failure.
