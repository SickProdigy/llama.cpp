# Current Fable Q6: coding/Gitea workflow fails

November 26: retained Fable Q6_K completes the three dependent natural requests
in **36.67 coding minutes**, versus Q8's 38.68. Total supervisor wall time,
including load, grading and restoration, is **40.39 minutes**. Neither is a
successful full workflow. Q6 uses 11,566 MiB peak sampled GPU versus Q8's
14,624 MiB, leaving 3,058 MiB more headroom under the tested layout.

This is a current-runtime comparison: both bind owner-derived Hermes C9 plus
pinned test dependencies, llama.cpp fee/b12723, the corrected transparent recorder,
98,304 context, all 41 GPU layers, q4_0 KV, checkpoints 2, cache RAM 512, fit off,
load mode none, temperature 1/top-p .95/top-k 20, thinking enabled, main output
16,384 and auxiliary output 8,192. Each has a fresh isolated no-session profile,
process/gateway and private disposable upstream. No preliminary model read or
private grader feedback is supplied. The [exact three requests](beets-natural-task-queries.json)
match the recorded query hashes: lifecycle repair, accurate docs, then optional-folder
cancellation, with actual upstream issue/personal fork/PR publication throughout.

| Turn | CLI seconds | Exit | Project / original / independent |
|---|---:|---:|---|
| Lifecycle repair | 484.17 | 1 | 0 / 0 / 1 |
| Documentation | 254.69 | 0 | 0 / 0 / 1 |
| Cancellation feature | 1,461.51 | 1 | 2 / 0 / 1 |

There is no external timeout. First and final answers stop at the iteration limit;
the first says it will apply a fix but makes no edit. The docs turn changes and
locally commits only the README; actual final Git readback confirms that commit.
The feature patch and debug files remain uncommitted. No teacher repairs are made.

## Source and tests

The lifecycle dispatch/worker path remains unchanged, so already-dispatched or
serialization-waiting work can still start after disable/reload. The new cancellation
command handles pending timers but not already-dispatched work. Catching a named
folder validation error sets the target to `None`, which selects cancel-all and
cancels unrelated pending folders. Supplementary frozen-snapshot observations
corroborate both defects with mocked import boundaries; no media is imported.

Some requested behavior is preserved: manual imports with automation off still
dispatch; cancel-all removes two pending timers and reports two; later new work
dispatches. These partial successes do not satisfy lifecycle/cancellation safety.
Independent suites report five failure records over three methods in each early
turn and eight over six methods finally; failure records are not distinct bug counts.

The complete final project run fails collection at `parse_test.py:101`: a copied
`01|` line prefix is invalid Python. A supplementary exact authored-file run that
bypasses this unrelated-to-test-file artifact produces **15 pass / 1 fail**; its
named-folder test also cancels the other folder. This does not replace the failed
whole-project result. All eight original Beets test names remain, five methods are
AST-identical, three change with fixture refactoring. The refactor globally patches
`threading.Timer` without restoration. An added already-started-work test never
starts a worker, so does not verify that claim. The frozen original suite passes
83 tests/2 subtests each turn; it does not cover the required lifecycle repair.

The final README is unchanged from the docs turn: cancellation is undocumented,
shutdown/re-enable claims exceed implemented safety, and the queued-work wording
is contradictory. Existing setup instructions remain, but the requested complete,
accurate user documentation is not delivered.

## Gitea and claims

Fresh preactor checks verify all 40 upstream baseline blobs and actor access with
both identities; actual native Gitea read plus readonly-write rejection pass without
inference or forge mutations. The actor then makes **19 proxy calls**, all searches,
identity or reads, with **10 out-of-scope denials**. It guesses repository names
and owners despite the exact Git/fixture facts being supplied. Its docs answer
attributes failure to permissions and requests GitHub `gh`; that is a grounding
failure, not evidence that the correctly configured Gitea fixture was inaccessible.
All recorded proxy calls are reads; focused-tool failures before the proxy are not
assumed absent. Independent final authenticated API reads verify the upstream's
40 blobs unchanged, **zero issues, zero PRs, actor fork 404**. There is no owned
issue to close. A local README commit is not remote publication.

## Context, memory and latency

All **148 requests** have complete usage records, with no unmatched requests,
HTTP/transport errors or output-length finishes. Largest input is **83,555** tokens.
Four requests reserve more output than their remaining context (shortfalls
218/906/1,363/1,635 tokens), but actual total usage fits 98,304 each time. These
are headroom risks, not observed overflows; actual corrected-recorder overflow
recovery remains unexercised.

One nonthinking auxiliary request uses 27,798 input/31 output tokens and takes
81.85 seconds. Its 120-character response is literal README `read_file` tool markup,
not a faithful checkpoint; no tool runs in that response. Native snapshot ancestry
confirms one compression rotation and all exact task hashes/CLI ancestry. All
three literal user requests remain in the final main request. Lifecycle nonrepair,
wrong forge targets and inaccurate docs already occur before compression, so
summary quality cannot explain the entire failure.

All 41 layers are explicitly on GPU. Buffers: GPU model 10,392.38 MiB, host model
397.85 MiB, GPU KV 540 MiB, GPU compute 229.01 MiB. Across 220 samples with
ten-second pauses: no measurement errors, guards or study swap; aggregate charged
cgroups peak 7,460,638,720 bytes and process PSS 2,618,326,016 bytes. Charged file
cache is included; this is not CPU transformer offload. Samples may miss transient
peaks. Both disk reserves remain above 100 GiB.

Original runtime identity/configuration/alias/context, four profile hashes,
30 original model metadata entries, 40 owner files/pending edits and Codex state
are independently preserved/restored. Exact owned backend, agent, proxies,
network and terminal supervisor are removed. Credentials and owner settings are
unchanged. The [capacity record](resource-fable-q6-current-thinking.md) contains
full public file/revision/SHA pins; no new download is required for this run.

[Reviewed observations](native-fable-q6-current-thinking-cold-beets-summary.json),
[SHA256](native-fable-q6-current-thinking-cold-beets-summary.sha256),
[observer validation](native-fable-q6-current-thinking-cold-beets-validation.json).
Validation checks observation/source consistency, not model success or a public
private-grader replay. This single matched pair establishes neither a generally
better quantization nor autonomous reliability. Higher precision does not rescue
the workflow in this sample; the slower adapted 27B Q4's prior correct contribution
remains a separate useful lead requiring a current-runtime comparison.
