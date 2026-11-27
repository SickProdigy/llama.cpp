# MiMo 9B and local-workflow training — November 27

The pinned public MiMo V2.6 Distill Qwen 9B Q6_K loads **98,304 context / 33 of 33 GPU layers / 8,350 MiB observed peak GPU memory** on the existing P100 backend. The 7,793,710,624-byte download matches full SHA-256 `ef96d05a2ddf2cbb450d1af1ac3860ec769d3575bafa70692ee5609bda3fad7d`. This is capacity/serialization evidence, not a native coding/Gitea success or a new everyday-model recommendation.

Both the public Q6 built-in template and official ggml Q8 reference template complete the genuine tool call, its tool result and dependent history followup correctly. Built-in yields no nonempty reasoning in this short test; the reference configuration yields nonempty reasoning and retains it in the rendered next request. Templates differ in object-argument serialization and thinking prefill; they are explicitly separate configurations. The reference template is selected for the next reasoning trial.

Only the reference configuration receives the longer probes: exact markers at 16,164 / 59,934 / 79,929 actual input tokens all pass, taking 60.89 / 215.82 / 134.62 seconds. The later prompt can reuse a substantial prefix: these are not cold-cache benchmarks. Loading a 98k window and exercising about 80k input do not validate full-window coding. Aggregate observed study cgroup peaks are 6.56 GiB built-in / 4.40 GiB reference, including charged cache and supervisor; no study swap is observed. All 33 layers are reported on GPU; GPU allocation includes model, q4 KV, recurrent state and compute buffers.

The fresh strict postflight verifies all 20 model files, four owner profile hashes, selected owner source/pending work, original container IDs/images/configurations/running state, restored original Vibe alias/context and full unchanged Hermes-Codex state. The exact supervisor, backend containers and test network are removed. Model files remain in the usual `models/` directory. About 190 GiB free remains there.

[Machine-readable capacity/probe summary](capacity.json). Backend `b12723-abca69200` is unchanged; no CUDA/framework production upgrade, local model training or production model switch occurred.

## Next parts

The new development case is Auto Buddy idempotency, accurate documentation and live configurable room/trigger settings on a clean copy of the same committed Nicotine+ plugin tree. Native local terminal/file tools perform edits and tests; the scoped workspace publisher uses actual configured Gitea MCP for publication, with issue/fork/PR operations. The redundant remote edit tool is omitted in this new profile. The task does not name a forge host; selected Git origin and persistent project context supply that preference.

The checker is qualified against a working reference and deliberate regressions using the real offline Nicotine+3.3.11 plugin handler and buddy implementation. GUI delivery and network user watching are stubbed; no Soulseek connection occurs. There is no private-helper-signature publication gate. Original tests, public behavior, authored regressions, final claims and actual remote bytes are still independently checked after each turn. This is a new workflow configuration and a development case, not an untouched generalization holdout.

A retained VibeForged Q4 comparison is prospectively planned under the same new workflow and tasks, with its declared baseline sampler. Improvements over older remote-edit Beets cases cannot be attributed solely to MiMo. No actor result is claimed here yet.

The separate private [hermes-tool-training repository](/chatgpt-codex/hermes-tool-training) contains reviewed tool-trajectory validation, whole-family holdouts, resumable LoRA jobs, independent result comparison, exact-base merging and export preparation. Tiny synthetic CPU smokes establish machinery only. Real reviewed training data and actual training-PC GPU qualification remain required before a useful fine-tune.

Primary artifact references: [publisher](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B), [public Q6](https://huggingface.co/bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF), [official template reference](https://huggingface.co/ggml-org/MiMo-V2.6-Distill-Qwen-9B-GGUF).

Native launch admission subsequently stopped before inference because Docker's separate staging filesystem reached its reserve. The obsolete task-added IQ4 copy there was retired under the owner's cleanup authorization, restoring about112.76GiB free; main-folder20 and useful stagedQ3 are unchanged. See the cleanup report's staged-retirement receipt. This was a storage admission event, not a model-quality failure.
