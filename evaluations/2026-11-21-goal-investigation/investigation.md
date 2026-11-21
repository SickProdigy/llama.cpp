# P100 Hermes repository-agent investigation

**Best tested supervised candidate: the Hermes-adapted 27B IQ3XXS profile.**
Its final API contribution has a correct minimal fix, genuine regression
coverage and a verified upstream issue / personal-fork commit / upstream PR.
Independent HTTP behavior, original tests and completed-download preservation
pass. Its README still overgeneralizes terminal states, so it needs review.

No configuration qualified for an unattended whole workflow. The same model's
strongest ordinary Booksearch run repairs 4/6 defect cases and publishes its
README followup; two author-field cases remain broken. Its bulk-reference run
reaches the deadline without a patch. This is a practical supervised lead,
with known failures, rather than an editor-agent equivalent.

The completed study contains 18 primary Booksearch conversations across nine
profiles/seven weight files, four primary API conversations, two fixed context
controls and one conditional post-hoc budget diagnostic: 25 conversations.
These span two bug families, not 25 independent coding tasks. The final
diagnostic finished both turns within the old 20-minute per-turn allowance;
the larger allowance does not establish a causal improvement.

[Exact supervised-candidate configuration](supervised-candidate.json) records
the public checkpoint revision/hash, actual backend launch, effective request
sampler and limits. Use normal persistence, a real selected checkout, focused
Gitea 0.1.6, workspace publisher 0.1.3 and the selected-project hook. The native
scratch compatibility correction is separately preflight-verified and was not
applied to the scored sessions. Production VibeForged remains the default;
runtime and delivery verification are recorded below.

## Read these results

- [Fresh real-source matrix](fresh-matrix.md), [case identities](book-case-matrix.md)
  and [per-run CSV](fresh-results.csv).
- [Independent API results](api-matrix.md) and [per-run CSV](api-results.csv).
- [Exact finalist configurations and selection rationale](finalist-profiles.json).
- [Exact protocol and pre-inference amendments](protocol.md).
- [External methods and primary-source research](research.md).
- [Detailed development observations and historical results](development-notes.md).
- [Optional tested tool/profile components](../../hermes-profile/README.md).

The matrix distinguishes behavior, tests, actual publication, first-turn versus
followup publication, honesty, context and elapsed time. A PR is not a correct
fix. Six defect cases are six inputs to one bug family, **not six independent
coding tasks or a production success percentage**. Ordinary and bulk cells are
one fresh conversation each, not repeated IID accuracy estimates.

## What was tested

The real-source arena preserves 40 tracked files from
`sickprodigy/nicotineplus-plugins` at
`84afaf401b29753b6810e4f92f253e0d28637dbf`. Its disposable Gitea upstream is
`chatgpt-codex/hermes-eval-nicotine-20261121`, baseline
`b6eb9a4a4c69e5aa751b768ca68ea5a0bb092278`. The agent works as `hermes-agent` in
its fork. Reusing an existing correct fork is valid; each run does not
necessarily create a new fork. No upstream/default branch writes or merges are
part of the test.

The task supplies a symptom and one reproduced `{"docs": null}` response. It
asks for investigation, a fix, regression coverage and a contribution. It does
not supply a patch or an MCP call sequence. The same conversation then receives
a README request. Bulk runs additionally receive approximately 207,001 characters
/ 49,925 Qwen tokens of other real repository files, excluding the target module.
That packet is a stress condition, not a recommended normal coding workflow.

The full immutable baseline is 83 tests plus two subtests. Agents can use native
terminal/file tools in a real writable selected checkout. Private grading and
future task material remain outside their environment. Isolated scoped MCP
allows the actual forge operations while hiding other trials' solutions and
preventing default-branch publication. This validates a small selected-project
workflow, not arbitrary dirty multi-repository worktrees.

## What changed in the tests and tools

1. **Independent outcomes.** Model-authored tests are checked alongside immutable
   original tests and withheld behavior cases. Added tests are also run against
   original target code: passing there proves they did not catch the defect;
   failing still requires review for wrong contracts or broken fixtures.
2. **Public behavior.** A frozen private-worker diagnostic could reject a valid
   outer thread-boundary fix. A private control proved this. The same nine
   inputs are now also exercised through the real command and observed threads.
   This public route decides behavior; the old worker result stays diagnostic.
   Fake Nicotine dispatch is used; there is no live GUI or race-freedom claim.
3. **Actual published bytes.** Independently clone the PR or fork branch, verify
   remote HEAD and rerun behavior/original tests. Reconcile successful commit
   calls with actual commit history before assigning an initial published tree.
   A local passing patch is not assumed to be what was published.
4. **Retained followup.** Grade the first contribution separately from the later
   README turn. One stock run only opened its issue/PR after that followup;
   another model changed its code during the documentation request.
5. **Transport fixes.** Focused 0.1.6 and workspace publisher 0.1.3 resolve
   40-character branch names to commit SHAs before tree reads. Real scoped SDK
   preflight verified two commits and exact remote blobs. Operator preflights
   are not model wins. All 54 plugin/hook unit checks and eight proxy-isolation
   checks pass. The three completed V4 cells (GPT-OSS medium ordinary/bulk and
   Vibe ordinary) retain focused 0.1.5 / publisher 0.1.2; their actual branches
   did not encounter the 40-character failure. Later cells use 0.1.6 / 0.1.3.
   Frozen sources and per-run hashes preserve this disclosed revision change;
   it is not a strictly matched-tool-version comparison.
6. **Actual wire configuration.** Verify serialized samplers, context, streamed
   tool calls and retained reasoning, rather than trusting configuration text.
   Native SDK-only custom fields belong inside `extra_body`. Later cohorts use
   native persistence and disable unrelated automatic title generation.

A late compatibility check found a genuine prompt/policy mismatch: Hermes
advertises its native scratch directory for probes, but the evaluator permits
file-tool writes only under /workspace. Primary adapted API1 and the final
budget diagnostic each encountered this denial and recovered in the checkout.
A separate [nine-check native preflight](native-scratch-preflight.json) verifies
the supported two-root configuration, now documented in the profile guide.
Scored fixtures stay frozen. This is avoidable harness friction, not a reason
to excuse independently wrong code or claim an untested model-quality gain.

The independent API ownership bug supplies a second task after model selection.
Its grader uses actual HTTP requests with four formerly failing cases and three
controls. Two fresh ordinary conversations per selected weight file are planned;
booksearch failures remain part of the recommendation. Selection rules are
recorded before API inference in the protocol, including protecting the best
ordinary genuine contribution from being excluded by the artificial bulk stress.

## What the results suggest

The failures are complementary. Adapted 27B ordinary handles the overall JSON
shapes and mixed entries, but misses bad author fields. GPT-OSS medium bulk
handles both author cases and mixed entries, but misses some overall shapes.
No single primary session combines all those repairs. This suggests incomplete
contract coverage and validation as a recurring problem; it does not identify
a training or quantization cause.

Stock Qwen's .2/.6 pairs have the same aggregate defect count but repair
different inputs. GPT's publisher/low pair has cleaner saved format logs and
worse code. Qwen3-Coder fits and decodes faster but fails both booksearch runs.
File size, extra precision, a larger loaded window and clean tool formatting
are each insufficient selection rules on their own. These are observations
from small, differing profiles, not isolated causal estimates.

API run 1 adds an important positive: the adapted model produced a correct
minimal ownership guard and meaningful HTTP regression, but hit the time cap
before publication. Run 2 completed the real PR/README path and passed the
frozen seven cases, yet introduced an unrelated completed-batch clear-state
regression. A separate post-hoc HTTP preservation control proves that failure;
original and the first minimal patch pass. Its added test also passes with the
reported foreign-row guard removed, so being red on original was insufficient
proof of relevant regression coverage. The primary score is retained, while
this additional check and review prevent a whole-workflow pass.

GPT-OSS API run 1 also passes all seven ownership cases and the extra
preservation control. Its actual feature commit, however, contains an invalid
escaped-slash test URL. The agent repairs that URL locally after committing but
does not republish; independent local tests pass while the delivered suite
fails. The new test also passes against original API code after that unrelated
URL repair. This demonstrates why local, remote and relevant regression results
are separate columns rather than a single green test flag.

A live inspection of GPT-OSS API run 2 shows repeated patch arguments missing
`path` or `old_string`, alongside nonunique edits and literal `patch: "???"`.
The supplied native schema describes the required replace-mode fields, but its
JSON `required` list contains only `mode` because the tool supports two modes.
The rejection messages match the actual submitted arguments; this is not
evidence of arguments being lost by the transport. Conditional schema
constraints or simpler edit tools are a future interface experiment, not a
verified fix or a reason to erase this run.

GPT-OSS API run 2 publishes a class-body override referencing `Plugin` before
that name is defined. Both local and actual delivered code fail import with
`NameError`; the HTTP cases cannot execute. The agent ran and observed pytest's
collection failure, but committed the broken code during the README followup.
It creates no issue or PR and adds no regression test. This is an unusable
implementation, not a measured zero-of-four HTTP repair rate.

The final adapted API diagnostic contributes the correct minimal ownership
guard through issue 26 / PR 27, with a genuine original-red/fixed-green HTTP test.
Both initial and final published trees pass all seven primary cases, original
and edited tests, portability and the additional completed-clear control.
The model actually ran the 22/23-test API suite and corrected its first mistaken
red attempt (which had stashed away the new test). Independent full-project
checks are separate operator evidence.

The README followup still says a missing or foreign terminal row always means
Completed Aborted, overlooking an already-complete own file and successful
API-clear preservation. Code/test/forge review therefore passes while the
whole-workflow review fails. The descriptive distinction is post-hoc, does not
change primary grades and does not imply an unattended success rate. First turn
1,159.004 seconds and followup about 378.378 both fit the old 1,200-second
per-turn cap; this is a fresh positive code contribution, not proof that the
40-minute setting caused success.

## Runtime and practical capacity

| Component | Actually tested |
| --- | --- |
| GPU | Tesla P100, 16,384 MiB; driver 535.261.03 |
| Hermes | CLI 0.23.3 (2026.9.24), source `caafe538`; Python 3.14.9, OpenAI SDK 2.54.0 |
| llama.cpp | `b12464-d3c3e242c`; source `d3c3e242c16b8cbf51400fad410cd69b22d64f35` |
| Primary per-turn allowance | 60 iterations / 1,200 seconds; 8,192 output tokens |
| Backend | One slot, q4 K/V cache; model-specific loaded context and CPU experts |
| Project checks | Separate pinned project-test image; production image unchanged |

The Hermes package's `pyproject.toml` placeholder `0.0.0` is not the installed CLI
version. Runtime provenance records the actual image IDs and immutable digests.
Model names alone are insufficient: the complete sampler, context, cache,
reasoning and offload configuration is part of each result. Per-trial elapsed
excludes backend weight loading/downloads; exact-prefix caching can help later
fresh conversations. These are workload timings, not cold-start speed tests.

The adapted 27B file is 11,637,692,064 bytes and peaked at 13,094 MiB with 98,304
context loaded. Its bulk first tool took 612.881 seconds; under this deadline,
large-prefill latency is material even when memory fits. Loading a 98k/262k
window does not validate code quality throughout that window, and no 1M-token
P100 coding capability is established.

The observed 98,304-token profile reserves 8,192 output tokens and applies its
.85 compression threshold to the remaining input allowance: the actual native
threshold is 76,595 tokens. The loaded context is therefore not a promise that
98k tokens of repository content can be inserted before compaction. System
instructions, tool schemas and accumulated results also consume the window.

## Confirmed context-replay limitation

One original 35B bulk run sent both its roughly 208k-character active user packet
and a roughly 208k-character inflight-task replay. The backend rejected 119,824
tokens against a 98,304 limit. This run's store-less SDK caller omitted message
UIDs, so it was not equivalent to the normal persisted Hermes session.

Native controls show that IDs fix duplication with a plain summary carrier,
but **not every carrier layout**: a summary with tool calls can trigger the
conservative protected-head fallback and duplicate the task even with IDs.
Normal persistence aligns the caller; it does not fully fix this native path.
Do not blame this overflow solely on weights or promise that an update fixes it.

The two fixed controls use the same affected 35B profile and normal persistence:
large active-user reference versus the same reference as eligible historical
context with a short active task. Seeded history is explicitly an operator
fixture, not claimed genuine earlier model conversation. Inspect actual replay
and provider errors, as well as patch quality; packaging alone is not an
accuracy improvement claim. No framework/CUDA patch is applied to production.

The completed persisted active-reference control triggered real compaction.
Its next main request contains one 217,511-character user summary/reference,
not two giant messages; the backend accepted it without the earlier overflow.
It then spent the remaining allowance re-prefilling that large rebuilt prompt.
The trial stopped at 1,200.077 agent seconds with a feature commit and a closed
upstream issue, no PR or README followup. The actual published patch repairs
0/6 behavior cases: `docs or []` produces the wrong no-results contract. Edited
92 tests, original 83 and portability pass. Its 16 targeted Booksearch tests
were actually run by the model; the broader green checks are operator audits.
Runtime progress and code correctness remain separate.

The historical-reference control completed normally with issue 24 / PR 25 and
three reconciled commits including its README followup. After actual compaction,
serialized message text fell from 270,187 to 51,249 characters; the giant reference
was gone, while the exact 519-character initial task and its unavailable
requirement remained. This verifies useful task retention and reference removal
in that fixture, not naturally grown long-session reliability.

| Same 35B profile, native persistence | Active reference | Historical reference |
| --- | ---: | ---: |
| First tool, seconds | 364.871 | 323.758 |
| Giant reference after first compaction | One 217,511-character user message | None |
| Public defects repaired /6 | 0 | 2 |
| Existing controls preserved /3 | 3 | 3 |
| Actual contribution | Commit + closed issue 23, no PR | PR 25 + README followup |

The historical patch still maps malformed null docs to ordinary no-results;
it repairs root-array and mixed-entry cases but misses four defects. Its
79-test unittest run and final 11-test targeted run really passed; independent
pytest sees 87 edited and 83 original tests, all passing. Some added coverage is
genuine, but the null expectation and README generalizations are wrong. Thus
runtime progress does not qualify either control as a correct whole workflow.
This pair has different model-generated histories and is not an isolated causal
accuracy or end-to-end speed estimate. Persistence alone also does not fix the
separately reproduced tool-carrier fallback.

## Routing, historical evidence and limits

All 30 recovered read conversations completed without mutations; all 18 ordinary
SonicRatings requests' scoped reads selected `sickprodigy` and used Gitea. Two
answers used search metadata alone. Both reader versions and owner-hint
conditions completed, so this does not demonstrate an improvement rate from
hints/pagination. Some explanations still reversed source semantics or claimed
exceptions were handled when they were not.

Older synthetic and guided-publication results are useful diagnostics, but do
not supersede novel-fix failures. A controller restart lost much of their raw
local coding evidence. Thirty actual read conversations, five published source
snapshots and a Fable sampling conversation survived and were re-audited. Lost
raw runs are not reconstructed. See development notes for recorded historical
scores, exclusions and the exact evidence boundary.

This is a small development study with configuration changes and unseeded
samples. Model size, training, weight/KV precision, samplers and context differ;
these are practical profile comparisons, not causal estimates of one factor.
The selected API task broadens evidence but does not establish unattended
reliability. Front-loaded references and seeded history do not recreate natural
context growth through many dependent code changes and repeated compactions;
that remains a separate future gate. Spare 2070/5080 options remain unmeasured
on those cards. Published cases are now development evidence; future broad
reliability claims need fresh tasks and natural dependent context growth.

## Delivery and deployment

New public GGUF downloads are hash/revision pinned; no weights were trained or
quantized locally. Preserve the 100 GiB model-disk reserve and existing useful
small/task models. A faster or larger GPU is not yet a demonstrated solution to
remaining code-quality failures.

Experimental plugins and defaults are optional. The everyday Hermes container
has no selected programming checkout mounted; an editor-like workflow first
needs a real project root and consistent terminal cwd. Debian's programming
storage is server-local and exported to Windows; edits are already shared.
Resolve actual Docker-engine binds rather than cloning to obtain those edits.

Final verification restores the original VibeForged alias at 98,304 context.
The llama endpoint is healthy; original Hermes/llama images, environment,
commands, users and mounts match the saved state. Eight selected profile files,
including configuration/authentication policy, match their original hashes.
The configured Gitea MCP is healthy and separate Hermes-Codex remains running.
Experimental candidate/profile changes have not replaced the production default.

The disposable upstream has no open issues. All 11 model PRs remain open and
unmerged (operator smoke PR 6 is separate), all 15 published feature heads match
the audited commits, and upstream main remains the frozen baseline. Test
contributions do not modify the owner's original Nicotine repository.

Only the two new failed large nonfinalists were removed, after exact-size/SHA
and stopped-consumer checks. All other GGUFs were unchanged. Free space at
cleanup was about 125.3 GiB, preserving the 100 GiB reserve; download/source hashes
allow reproducibility without retaining those failed weights.

Delivered-source checks pass: 54 plugin/hook units, eight proxy-isolation units,
plus nine separate native-scratch operator checks. Those are infrastructure
checks, not extra model successes. No local weight training/quantization or
production framework/CUDA update was performed.

[Evidence archive](evidence.tar.gz) and [SHA256](evidence.sha256) preserve the
explicitly allowlisted source, requests, results and reviews. The archive's
manifest lists redacted files and hashes of exported bytes; original runtime
hashes are provenance, and redacted source bytes may differ. Credentials,
private profiles and reference solutions are excluded. Historical raw-evidence
loss and tool/runtime revision differences remain disclosed. Git history
records delivery of the study and optional profile components.
