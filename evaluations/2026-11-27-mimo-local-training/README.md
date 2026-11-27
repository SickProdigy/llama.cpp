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

This is one workflow with three dependent tasks, not three independent repetitions. The retained Vibe Q4 comparison uses the same predeclared tasks, native local-development tools, scoped publication and independent checker; its own declared sampler and builtin template differ. No new winner or production replacement is established.

## Workflow and training parts

The new development case is Auto Buddy idempotency, accurate documentation and live configurable room/trigger settings on a clean copy of the same committed Nicotine+ plugin tree. Native local terminal/file tools perform edits and tests; the scoped workspace publisher uses actual configured Gitea MCP for publication, with issue/fork/PR operations. The redundant remote edit tool is omitted in this new profile. The task does not name a forge host; selected Git origin and persistent project context supply that preference.

The checker is qualified against a working reference and deliberate regressions using the real offline Nicotine+3.3.11 plugin handler and buddy implementation. GUI delivery and network user watching are stubbed; no Soulseek connection occurs. There is no private-helper-signature publication gate. Original tests, public behavior, authored regressions, final claims and actual remote bytes are still independently checked after each turn. This is a new workflow configuration and a development case, not an untouched generalization holdout.

A retained VibeForged Q4 comparison is prospectively planned under the same new workflow and tasks, with its declared baseline sampler. Improvements over older remote-edit Beets cases cannot be attributed solely to MiMo. The MiMo result above is complete; the retained Vibe comparison is in progress.

The separate private [hermes-tool-training repository](/chatgpt-codex/hermes-tool-training) contains reviewed tool-trajectory validation, whole-family holdouts, resumable LoRA jobs, independent result comparison, exact-base merging and export preparation. Tiny synthetic CPU smokes establish machinery only. Real reviewed training data and actual training-PC GPU qualification remain required before a useful fine-tune.

Primary artifact references: [publisher](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B), [public Q6](https://huggingface.co/bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF), [official template reference](https://huggingface.co/ggml-org/MiMo-V2.6-Distill-Qwen-9B-GGUF).

Native launch admission subsequently stopped before inference because Docker's separate staging filesystem reached its reserve. The obsolete task-added IQ4 copy there was retired under the owner's cleanup authorization, restoring about112.76GiB free; main-folder20 and useful stagedQ3 are unchanged. See the cleanup report's staged-retirement receipt. This was a storage admission event, not a model-quality failure.
