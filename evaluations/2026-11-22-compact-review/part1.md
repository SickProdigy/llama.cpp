# Part 1 — compact review packet and execution prerequisites

Part 1 is complete. Parts 2 and 3 remain; the overall goal is active.
No production deployment, reviewer inference, Gitea write or fresh bug workflow
occurred in this part.

## Measured result

All 15 completed-pilot review attempts were reconstructed as development packets.
Old raw packet text measured 33,928–45,034 tokens;
compact packet text measured 3,813–7,308 tokens using the same
loaded VibeForged Q4 tokenizer for both. Median reduction: 86.9%.
All 15 fit 32 KiB and the 7,500-packet-text-token target. Largest packet:
27,609 UTF-8 bytes. The separate reviewer system text is 193 tokens.
These counts omit rendered chat-template overhead; each reviewer must be measured
with its own tokenizer and actual wire usage in Part 2. This does not demonstrate
review latency, detection accuracy or end-to-end benefit.

[Summary](part1-summary.json), [CSV](part1-measurements.csv),
[full measurements](part1-packets/measurements.json), [framework checks](part1-validation.json).

## What changed

The experimental library at `hermes-profile/compact-review/` represents the
actual base plus exact publication mutation once as complete unified diffs.
Related unchanged tests/docs come from the actual candidate tree, never adjacent
unpublished scratch changes. A generic AST pass also retains unchanged local
state writers, direct callees and referenced class defaults. This keeps lifecycle
hooks visible without hard-coded bug names or private grader hints. It is a
one-hop heuristic, not complete whole-program analysis. Missing context requires
abstention; oversized packets are refused rather than silently truncated.

The library signs trusted execution receipts with a per-case private HMAC key,
binds them to the exact source digest and declared runtime identity, and checks
the latest required suite result. Newer failures/timeouts, wall-clock ties,
source changes, forged receipts, stale approvals, pipelines, incomplete coverage,
malformed reviewer JSON and missing test/documentation assessments block
publication. Reviewer approval still is not a correctness oracle. A test can be
irrelevant despite a genuine passing run; documentation assessment remains a
model judgment evaluated independently later.

Nineteen framework regression tests pass in the pinned Python 3.14.9 evaluation
image, with no network/profile/Docker socket available to the test container.
The positive execution test runs an actual unittest against its bound temporary
source tree. Other tests deliberately exercise failure/tampering controls.
These are framework tests, not nineteen model-workflow successes.

## Evidence and limits

Packet receipts in this historical size replay are explicitly labeled historical
observations, filtered to source-verified tool messages no later than the original
review request. They are not newly authenticated current test passes and cannot
authorize publication. Original private receipt tails are used only by the local
tokenizer for the old-size measurement and are never copied into compact packets.
The public old baseline and exact proposed mutations supply source context; no
reference fix, private grader or future task is supplied.

Historical cases are development evidence, not fresh scored cases. Raw old
packets contain private owner context and are not published, so their exact
original-size replay requires retained private records. New compact packets are
published for inspection. Source is derived from the same committed 40-file
baseline as the [completed pilot](../2026-11-22-everyday-pilot/investigation.md);
its [source notice](../2026-11-22-everyday-pilot/SOURCE-NOTICE.md) still applies.

Original Hermes/llama/Codex container IDs, images, configuration, start times and
restart counts, four profile-file hashes and 29 retained model-file metadata match
before/after observations. All services remain running; original VibeForged and
98,304 context remain active. Free model storage: 124.14 GiB, above 100 GiB reserve.
No model download, quantization, GPU reload or profile modification was made.

## Next parts

Part 2 measures actual reviewer requests and false positives/detections, then
freezes transport/deadlines and a justified configuration. It compares 27B with
an appropriate retained faster reviewer. Model-specific token counts, schema
behavior, cold/cache effects and timeout capture must be measured. A faster model
that requires swapping the 27B off the same P100 may lose its apparent advantage;
switch/load and actor-cache costs must be reported. Only the retained 4B is below
4 GiB on disk; this alone does not prove it can coexist with the 27B's observed
13,094 MiB residency. No co-resident fit or GPU-upgrade need is assumed.

Part 3 uses new symptom-led bugs, frozen private independent checks and dependent
followups, with actual upstream issues/personal-fork commits/PRs. It separately
verifies behavior, preservation, test relevance, docs, receipts, ownership and
publication. The selected configuration must be justified by Part 2 data; the
experiment can finish with a negative result. No unattended reliability claim
will follow from a small sample. Each GPU-testing part must restore and verify
the original stack before its delivery commit.
