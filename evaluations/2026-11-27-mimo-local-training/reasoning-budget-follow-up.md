# Candidate follow-up: bounded reasoning

The pinned b12723 source at `abca6920035ed77c1d80eaf23d066e9d3a7c5b23`
already implements a reasoning-token budget. This is a source finding, not a
runtime or model-quality qualification. The current Q8/Q6/Vibe/Thinking
comparison keeps its registered unrestricted reasoning configuration.

The CLI accepts `--reasoning-budget N`: `-1` is unrestricted, `0` ends thinking
immediately, and a positive value limits thinking tokens. The chat endpoint
accepts `reasoning_budget_tokens` and the alias `thinking_budget_tokens`, with
the CLI setting as fallback. It passes the budget to the sampler when the
selected chat template exposes thinking end tags. This differs from
`max_tokens`, which limits the overall generated completion, and from disabling
thinking in the template.

Primary source, inspected in the exact local pinned checkout:

- [Argument registration](https://github.com/ggml-org/llama.cpp/blob/abca6920035ed77c1d80eaf23d066e9d3a7c5b23/common/arg.cpp#L3783).
- [Chat-request translation and template-tag condition](https://github.com/ggml-org/llama.cpp/blob/abca6920035ed77c1d80eaf23d066e9d3a7c5b23/tools/server/server-common.cpp#L1672).
- [Request-field validation](https://github.com/ggml-org/llama.cpp/blob/abca6920035ed77c1d80eaf23d066e9d3a7c5b23/tools/server/server-schema.cpp#L354).
- [Reasoning sampler setup](https://github.com/ggml-org/llama.cpp/blob/abca6920035ed77c1d80eaf23d066e9d3a7c5b23/common/sampling.cpp#L323).

After the matched quantization comparison, a useful isolated experiment would
compare unrestricted main reasoning against a 2,048-token main reasoning budget.
Keep the selected weights, template, sampler, seed, 98k context, overall
16k main/8k auxiliary caps, native tool schemas and publication permissions
fixed. Explicitly preserve unrestricted auxiliary reasoning rather than letting
the main provider override silently change compression too. Verify actual
main/aux HTTP serialization and the template's budget enforcement first, then
qualify genuine tool-call/result/history behavior before any scored trial.

Use fresh independent tasks and the same full correctness, meaningful
regression, documentation and real Gitea publication requirements. Record
latency and actual retained compression ancestry. Keep private reasoning out of
reports and training data. A faster partial fix does not qualify as a workflow
pass. The cap cannot remove input-prefill cost and may reduce answer quality;
neither outcome has been measured here. A separate auxiliary-budget experiment
would need its own registration.
