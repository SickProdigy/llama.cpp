# Hermes contribution workflow comparison — November 18, 2026

## Finding

**None of the three models completed the requested upstream issue → fork
branch → exact file fix → upstream PR workflow in the final comparison.**
Qwen3.5-9B Q5 got furthest: it created the upstream issue, created its fork
branch and committed the exact requested edit. It could not open the PR, even
in a separate PR-only follow-up. FableVibes gave the best answers in the small
read-only sample. These are different strengths; neither establishes a reliable
unattended contribution agent.

## Final write comparison

Only the three `*-matched-contribution` runs below determine this comparison.
Each used a fresh full AIAgent conversation, the same frozen Discord profile,
the same 42 tool schemas, the same final guard and the same sampling. Schema
and guard hashes match across all three runs. Distinct small README corrections
prevent duplicate contributions; the task instructions and operation sequence
are otherwise the same. This is one run per model, not a reliability estimate.

| Model | Upstream issue | Fork branch | Exact file commit | Upstream PR | Time | Calls | Result |
|---|---|---|---|---|---:|---:|---|
| VibeForged v2 Q4_K_M | #9 | Created | No | No | 142.6s | 9 | Tried to create the branch again during the file update |
| Qwen3.5-9B Q5_K_M | #10 | Created | Yes | No | 127.3s | 10 | Repeated PR creation without head/base after validation error |
| FableVibes Q4_K_M | No | No | No | No | 63.8s | 4 | Tried opening the issue under the wrong upstream owner |

VibeForged first omitted file content/edits. After feedback it supplied an
entire regenerated README, but still requested a new branch with the name of
the branch it had already created. That call was blocked. Its regenerated text
also changed whitespace beyond the approved replacement; no file write ran.

Qwen omitted the branch name once, then corrected it; it omitted the file path
and payload once, then supplied a valid targeted `edits` operation. That commit
really exists. At the PR step it twice emitted only `method`, `owner` and `repo`,
without `head`, `base`, title or body. The identical retry was stopped.

FableVibes supplied `owner: nicotineplus` instead of the explicitly requested
`sickprodigy`. The issue write was blocked before dispatch. This is an attempted
wrong-target write, not an issue actually created in another repository.

All runs reused the previously created, independently verified fork
`hermes-agent/hermes-mcp-test-20261117-vf-144838`. No model earned a fresh-fork
creation pass. The existing fork and upstream main both started at
`84afaf401b29753b6810e4f92f253e0d28637dbf`.

## Read-only tasks

The unchanged prompts were:

1. `Find my SonicRatings repo and tell me what it does.`
2. `Look over sickprodigy/sick-cogs and suggest one useful new cog that isn’t already there.`

| Model | SonicRatings | Time | Broader repository review | Time |
|---|---|---:|---|---:|
| VibeForged Q4 | Correct MCP reads; useful summary with unsupported fork claim | 32.5s | Failed: guessed master, hit MCP cooldown, attempted web_search | 24.3s |
| Qwen Q5 | Correct MCP reads; added unsupported Node.js and fork claims | 59.0s | Failed: read directory listings, then attempted local read_file | 24.4s |
| FableVibes Q4 | Passed grounded explanation | 50.5s | Passed: proposed one message-search cog using MCP | 97.5s |

Independent SonicRatings metadata says `fork: false`, and the project describes
SPTNR as its former name. Its tree has a Python project and no package.json.
Fable inspected the sick-cogs develop branch; independent main/develop tree and
default-branch ReadMe checks found no existing message-history-search cog.
That is a narrow novelty check, not validation of an implementation.

Do not pool these six single observations with the earlier nine-session
matrices. The backend build and test conditions differ. Fable's better showing
here does not erase the November 13 failures or establish a general success rate.

## Separate diagnostics

**Fable: existing issue, MCP-only tools, temperature 0.2.** With 25 tools and a
shorter prompt, it successfully read issue #8, but changed the supplied fork
identifier from `20261117` to `20261118`. After two wrong-repository calls it
attempted another fork, received the real 409 that the repository was already
forked, and hit the three-error MCP cooldown. It then incorrectly claimed it
could not read the issue and that the service needed restarting. No new fork,
commit or PR resulted. Time: 75.7s, nine calls, maximum completed input 11,862
tokens. This alternate setup did not demonstrate a successful implementation.

**Qwen: PR-only follow-up.** A new conversation received the actual committed
fork branch for issue #10 and an explicit source, destination, title and body.
It queried a nonexistent `hermes-agent/nicotineplus-plugins` repository with a
malformed head reference, listed upstream PRs, and claimed the source branch
was missing. Independent API reads confirm the supplied fork branch and exact
commit exist. It never dispatched a PR-create call. Time: 78.2s, two calls.
The setup's issue/branch/commit state was seeded; those state flags are not new
model actions in this diagnostic.

Neither diagnostic rescues a failed scored turn or counts as a full pass.
Their prompts, tool schemas and traces are retained separately.

## Hardware and settings

| Model | GGUF GB (decimal) | GGUF GiB | Sampled active VRAM | Context |
|---|---:|---:|---:|---:|
| VibeForged Q4_K_M | 8.47 | 7.89 | 9,082 MiB | 98,304 |
| Qwen3.5-9B Q5_K_M | 6.58 | 6.13 | 7,472 MiB | 98,304 |
| FableVibes Q4_K_M | 8.47 | 7.89 | 9,082 MiB | 98,304 |

Tesla P100 16 GiB; one slot; q4 K/V; 4,096 main output; temperature 1, top-k 20,
top-p 0.95, min-p 0.05, repeat penalty 1, presence/frequency penalty 0 for the
final comparison. llama.cpp `b12464-d3c3e242c`, image
`sha256:0eee1b477a28c1bd8806885d50447caa302eef5c977846f1177330def5fcd185`;
Hermes image
`sha256:c18f0a2090b1df335b7edb2805f4ee4c407a433d9ad929d2a9aa23f0ce6cdc04`.
The final cold first calls took 49.0–51.5s; the read-only probes reused the
backend's prompt cache and their first calls took 3.3–7.9s. Do not confuse those
warm measurements with cold latency or compare early failures as faster successes.

No CUDA OOM occurred. Final write input peaks were 18,352–26,614 completed
prompt tokens; the largest completed input across these probes was 28,587.
These failures occurred far below the configured context limit. More context
would not itself correct the missing fields, wrong owners or changed identifiers.

## Guard validation and discarded preliminary runs

The final guard passed 23 regression checks, including actual native success
responses. It permits only manifested upstream issue/PR writes and the exact
fork branch/file operation. It allows one corrected validation attempt per
operation/tool, stops identical rejected retries, and caps a contribution at
300 seconds and 20 tool calls. Reads use 180 seconds/16 calls; the PR-only
probe uses 180 seconds/eight calls. No corrective user hints were injected.
Validation feedback is supplied by the guard before unsafe/incomplete writes;
this is a guarded agent evaluation, not an uninstrumented production turn.

Six preliminary write probes are preserved but **excluded from the final
comparison**. The initial guard omitted an allowed fork operation, prematurely
stopped missing-branch validation, and enforced issue-before-fork ordering as a
hard stop. Later probes exposed another harness error: successful native branch
and file writes return JSON strings (`Branch Created` and `Committed 1 file(s)
to branch …`), not objects. The guard initially failed to record those successes
and consequently stopped later operations. Independent state records the real
partial resources; those stops are not evidence of model inability.

Those problems were corrected and the final three-model comparison used the
same verified guard/schema hashes. Earlier traces remain ungraded even where
they also contain genuine model mistakes. Seventeen model sessions total are
retained: six read probes, six preliminary write probes, three final write
probes and two separate diagnostics. This is not seventeen equivalent trials.

## Direct same-account MCP control

A non-model control used the actual Hermes MCP connection as `hermes-agent`,
verified upstream issue #4, created a fork branch, committed precisely that
issue's README wording change, opened upstream
[PR #7](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/pulls/7)
with `Refs #4`, and read the file and PR back. The control first exposed the
success-string bookkeeping bug; it resumed only after independently confirming
the existing file commit, without repeating branch or file creation.
Independent API checks verify one changed file, the exact expected content,
the correct cross-fork head/base, an open/unmerged PR and unchanged upstream main.
This establishes the connection's capability and permissions, **not a model pass**.

## Practical conclusion

For the current stack, Qwen Q5 is the strongest candidate for guarded write-step
experiments and has the smallest memory footprint; Fable is worth using in
further read/review comparisons. VibeForged is not an established winner for
this contribution workflow. None has demonstrated the complete requested
workflow without intervention in this comparison.

An inference worth testing next is a narrower Gitea tool interface with explicit
required fields for each operation. Current multiplexed schemas leave `branch`
optional on branch_write, all file path/payload alternatives optional on
create_or_update_file, and `head`/`base` optional on pull_request_write; the
omissions cluster at exactly those points. This has not been proved to fix the
models. No production tool schema, credential, connection or model setting was
changed to manufacture a pass. The evidence does not support attributing the
result simply to fine-tuning, parameter count or available context.

## Retained resources, restoration and evidence

Upstream test issues [#4](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/issues/4),
[#5](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/issues/5),
[#6](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/issues/6),
[#8](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/issues/8),
[#9](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/issues/9) and
[#10](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/issues/10)
remain open. The direct-control PR #7 is the only PR created by this evaluation.
Qwen's exact model-authored change is retained on
[its fork branch](https://gitea.rcs1.top/hermes-agent/hermes-mcp-test-20261117-vf-144838/src/branch/mcp-test-20261118-qwen9-q5-matched-contribution/README.md).
Other partial test branches and the prior fork/issue remain for owner review.
Nothing was merged, closed or remotely deleted; upstream main is unchanged.

The original Hermes and llama.cpp containers, images, commands, environments
and mounts were restored, with the original VibeForged model at 98,304 context.
Live config.yaml and .env hashes match their initial snapshots. This exercised
the full AIAgent loop with Discord profile selection in disposable containers;
it did not send Discord messages or establish gateway delivery parity.

- [Final model results](model-results.csv) and [read-only grades](read-results.csv)
- [Independent verification](verification.json) and [runtime restoration](final-restoration.json)
- [Sanitized raw evidence](evidence.tar.gz), [member hashes](evidence-manifest.json)
  and [archive checksum](evidence.tar.gz.sha256)
- [Task-resource cleanup](cleanup.json)

Exact prompts, model requests, effective tool arguments/responses, result
messages, schemas, GPU samples, guard versions, regression checks and fixture
snapshots are retained. Credentials, email addresses and unrelated repository
identifiers/descriptions are redacted. Private profiles, auth stores and raw
Docker inspections are excluded. The scripts are an operational record that
requires a private profile and this Docker environment, not a portable benchmark.
