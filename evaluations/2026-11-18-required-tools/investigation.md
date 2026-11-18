# Hermes contribution workflow with focused Gitea tools

## Decision

VibeForged v2 Q4_K_M is the leading everyday candidate on this P100. FableVibes
Q4_K_M is a close alternative; Qwen3.5-9B Q5_K_M offers a smaller memory footprint
but made a wrong-target issue attempt in a fresh repetition. An additionally
downloaded Qwen tool-calling fine-tune did not improve the complete workflow.
These are small controlled samples, not production reliability estimates.

The largest improvement came from the tool interface. This evaluation changed
runtime/tool configuration and tested existing weights; it did **not** train or
fine-tune model weights. The earlier native-interface results remain valid for
that interface, but they no longer describe the best tested setup.

## What changed

The optional [focused Gitea plugin](../../hermes-profile/gitea-focused/README.md)
exposes 15 operations over the existing authenticated MCP registry handlers.
Branch, exact-edit and PR fields are required. PR upstream and fork identifiers
are separate, and the native head reference is constructed from those fields.
Writes verify the authenticated fork owner and actual upstream parent. Read
results present bounded text and public URLs. No operator supplies missing model
arguments or repairs a conversation during a scored run.

Native repository `get` was absent from the curated server surface. The isolated
same-account MCP clone adds canonical **read-only** `repo_read`; it does not
broaden native write methods. Model-visible tools change from 42 to 32, replacing
25 multiplexed Gitea tools with the 15 focused tools. Non-Gitea schemas match.

A later read-only ergonomics probe found two server constraints: Gitea rejects
`.` as a malformed directory component, while the native directory tool rejects
an empty `path` before making the request. Version 0.1.2's attempted empty-path
normalization therefore remained broken; the affected VibeForged probe is
excluded from model grading. Fable's same-phase fork attempt occurred before
any directory read and remains a model routing failure.
Version 0.1.3 reads the root using `get_repository_tree` instead; non-root paths
still use the native directory reader. The later rechecks are a separate phase.
No file-name guessing or silent HTTP fallback was added.

## Controlled test setup

- Actual full Hermes `AIAgent` loop with Discord platform selection, fresh
  disposable profiles and conversations; no messages sent through Discord.
- Same Hermes image and llama.cpp b12464-d3c3e242c, Tesla P100 16 GiB.
- Context 98,304, one slot, q4 K/V; main output 4,096, temperature 0.2.
- Existing MCP principal `hermes-agent`; operator/plugin credentials never
  stand in for model-originated actions.
- Contribution cap 300 seconds / 20 model tool calls, read cap 180 / 16;
  fresh-fork and long-context diagnostic budgets are recorded in their manifests.
- Guard blocks unexpected targets, edits, tools, settings, duplicate/ambiguous
  writes and merges before dispatch. It does not correct model arguments.
- Full contribution prompt specifies upstream, fork, unique branch, one exact
  README replacement, exact issue/PR title and body, read-backs and final URLs.
- Independent public API checks verify resources, parents, heads/bases, exact
  committed content and a one-file diff. The native trace determines whether
  this run performed a write: an artifact created later never credits an earlier
  failed run.

The complete prompts, schemas, requests, native/model call traces, code hashes,
results and sampling/property snapshots are retained in the sanitized archive.
This is deliberately a narrow agent mechanics test. It does not establish
independent feature design, code quality, test execution or arbitrary-repository
correctness.

## Fresh complete workflow results

Each model has one pilot and fresh repetitions, with distinct README corrections
and branches. The pilot requires an exact two-paragraph PR body; repetitions
require just `Refs #N`. These phases are preserved separately in the CSV rather
than represented as identical prompts. No corrective user hints are supplied.

| Model | Correct new issue + branch + exact commit + upstream PR | All requested read-backs and final URLs too |
|---|---:|---:|
| VibeForged v2 Q4_K_M | 3/3 | 2/3 |
| FableVibes Q4_K_M | 3/3 | 1/3 |
| Qwen3.5-9B Q5_K_M | 2/3 | 2/3 |
| Qwen3.5-9B toolcall-preview Q4_K_M | 0/2 | 0/2 |

VibeForged omitted the post-commit file read in one repetition. Fable verified
the edit but omitted the requested file URL in two runs. Qwen attempted its
issue in the fork once; the guard prevented that write. The preview model
committed the correct pilot edit but repeatedly omitted requested PR body text;
its simpler-body fresh repetition attempted a commit outside the working fork
and was stopped. Its separate **PR-only** success is not a fresh full pass.

One initial Fable pilot is **unscored**: the harness incorrectly refused to
repeat a failed file read after the model had successfully created the missing
branch. The retry ledger now advances after confirmed mutations, with regression
checks. Repeated ambiguous/successful writes remain blocked. Its clean fresh
rerun is the scored pilot above; the original trace remains available.

## Ordinary read requests remain a release limitation

The same broad prompts were also run as fresh read-only tasks:
`Find my SonicRatings repo and tell me what it does.` and
`Look over sickprodigy/sick-cogs and suggest one useful new cog that isn’t already there.`

SonicRatings explanations were useful, but VibeForged again described the rename
from SPTNR as a fork without supporting evidence. Qwen and Fable did not make
that particular claim in these repetitions. On the cog review, Qwen drifted to
web search, VibeForged to terminal, and Fable attempted a fork. All were blocked
before those actions. The preview model stayed on MCP and proposed a genuinely
absent weather cog, but claimed 29 cogs where the root lists 33 directories; a
useful proposal is not a fully grounded review.

Fixing root-directory handling is necessary infrastructure work, not sufficient
behavior tuning: both later VibeForged and FableVibes root-tree rechecks still attempted a fork
on the read-only request. This is a real model routing failure, distinct from
the excluded broken-root adapter probe. The guard prevented the mutation; the
plugin alone is not intent-aware and should not be described as providing that
protection.

**No tested setup is established as a reliable unattended general agent.** The
recommendation is VibeForged for explicit bounded contribution tasks, retaining
Fable as an alternative. General reviews should keep mutation tools unavailable
or remain supervised. Do not infer that all basic repository tasks are solved
because the explicit contribution scripts succeed.

## Native versus focused PR-only diagnostic

On the same Qwen Q5 model and existing verified committed branch, the native
interface made seven calls in 81.9 seconds without creating a PR. With the same
prompt the focused interface opened and read back [PR #11](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/pulls/11)
in two model calls / 45.0 seconds. This is evidence of interface usability on
that task, not a throughput benchmark or a full-workflow pass. Cache state and
internal read calls differ.

The preview model later created [PR #20](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/pulls/20)
when its diagnostic prompt requested only `Refs #15`. Its earlier strict-body
failure therefore does not mean it is incapable of making a PR.

## Fresh fork and useful-context diagnostics

VibeForged created the previously absent personal fork `hermes-agent/SonicRatings`
from `sickprodigy/SonicRatings`, then created [issue #24](https://gitea.rcs1.top/sickprodigy/SonicRatings/issues/24),
a feature branch and an exact README edit, and opened [upstream PR #25](https://gitea.rcs1.top/sickprodigy/SonicRatings/pulls/25).
Independent checks confirmed the parent, one-file diff, correct head/base and
body, all three read-backs and requested URLs. It took 59.6 seconds / 12 model
calls / 19 internal native calls, with no argument rejection. This is separate
from the three same-fixture repetitions above and includes a **new model-created
fork**, not the old operator-created nicotine fixture.

A separate read-only conversation contained 52,145 user tokens of inert random
archive material with early/middle/late markers, plus the normal agent/tool
instructions. The largest reported request was **64,290 prompt tokens**.
VibeForged retrieved all markers exactly and read the requested README heading
through MCP in one model tool call / two inference requests, taking 152.2 seconds.
Both captured requests retained the full archive; there was no compression event.
Peak GPU allocation was **9,082 MiB**. The 128,272 prompt-token sum is usage
across both requests, not a 128k context window.

This supports useful retrieval and one real tool action at approximately 64k
input. It does not establish long coding-session quality, full-window retrieval
at 98,304, or a million-token context. Keep the measured 98,304 loaded setting.

VibeForged and FableVibes files are each 7.88 GiB (8.47 GB decimal); Qwen Q5 is
6.13 GiB (6.58 GB decimal). GPU use includes weights, reserved KV cache and
compute allocations; file size alone does not predict it.

## Model provenance and disk management

Downloaded [am17an/Qwen3.5-9B-toolcall-preview-GGUF](https://huggingface.co/am17an/Qwen3.5-9B-toolcall-preview-GGUF),
revision `02fe3b87e1c2ccd5989edadbde131a33bb3ae601`, file
`Qwen3.5-9B-9b-v5s1-imat-Q4_K_M.gguf`, 5,629,108,960 bytes (5.24 GiB).
Verified SHA256:
`6e0665f447c8e33e24b923f53094e45a319b30c837ac316efb8d2817573135cb`.
The publisher describes an experimental multi-turn tool fine-tune. Local results
above determine suitability here, rather than its training claims.

All four compared GGUFs declare 262,144 context. Declared capacity is not a
validated useful-context measurement. Quantization reduces weight storage;
context caches and compute buffers also consume VRAM. We retain the measured
98,304 setting instead of extrapolating to a million tokens.

Removed two repeatedly failing Qwen3-14B Q4/Q5 files, the unstable and too-heavy
Qwen2.5-Coder-14B Q6, and an orphan DeepSeek MTP auxiliary file that is not a
standalone chat model. Logical space removed: 33.01 GiB. Container references
were checked before deletion. After the new 5.24 GiB download approximately
250 GiB remained free, well above the enforced 100 GiB download reserve.

Small task models and Ollama embeddings were preserved, along with VibeForged,
FableVibes, Qwen9B and other candidates with useful evidence or distinct roles.
The preview model is retained as a research candidate, not selected as default;
its successful PR diagnostic means it is not an across-the-board failure.
Exact deletion reasons, sizes, GGUF metadata and verified download provenance
are retained separately.

## Runtime and operational scope

The focused tools were evaluated in disposable profiles and a same-account MCP
clone. They are committed as an **optional profile**, not silently installed in
the normal gateway. The normal Hermes configuration, native MCP allowlist,
credentials and Portainer stack definitions are preserved. The normal backend
returns to VibeForged Q4 at 98,304 after evaluation. To reproduce the improved
write results, enable the focused profile as documented; selecting the model
alone does not reproduce the tool-interface change or temperature-0.2 override.
The independent `hermes-codex` instance is untouched.

The test plugin's write allowlist contains only the explicitly selected test
upstream(s). An operator should configure intended working repositories before
using it beyond this fixture. Its policy is not a sandbox against unrelated
process-level shell/HTTP tools. Actual Discord gateway message handling and
long-lived existing chat histories were not scored.

All test PRs/issues remain available for review; nothing was merged or closed.
Upstream default branches are checked after testing. Temporary containers,
volume and private credential-bearing evaluation snapshots are removed only
after the sanitized archive is verified. The separate cleanup record reports
that post-export step.

## Reproduction and evidence

[Example exact prompt](example-prompt.txt), [per-run matrix](runs.csv),
[independent resource verification](verification.json),
[resource versus strict completion summary](workflow-summary.json),
[long-context verification](longcontext-verification.json),
[model/disk cleanup](model-cleanup.json) and
[download verification](download-verified.json) accompany this report.

`evidence.tar.gz` retains the sanitized prompts, schemas, requests, results,
model-facing and internal native calls, harness code and property/GPU samples.
The member manifest and archive SHA256 are verified after export. Credential
values, email addresses and unrelated repository metadata are redacted. Private
profile archives, environment/Docker inspection snapshots and full third-party
model cards are excluded. Original pilot runs predate per-run code hashing;
later runs include hashes and matching source versions. Version 0.1.0's module
was reconstructed from the committed pre-root implementation by removing the
native-call hook, and its hash matches the captured diagnostic runs.

Local checks: 24 profile tests and 28 guard/retry-ledger tests passed. The actual
MCP preflight separately checks identity, fork metadata, bounded readable files,
root listing, loaded schema visibility and the direct-native blocking hook.
Mocked unit tests are not substituted for the real model-originated Gitea writes.
