# Development observations and historical results

These notes preserve intermediate observations, including plans later superseded.
Use [the investigation overview](investigation.md) and matrices for current
conclusions; a pending label below is not a final disposition.

Status when these observations were recorded: active; real-source, long-context and configuration comparisons are still
running. This report separates verified intermediate results from pending work.
Production configuration has not been replaced by an experimental winner.


Recovery note: a controller restart removed the temporary local result directory.
Read-only conversations, five published feature snapshots, and the last Fable
sampling conversation survived in Docker storage; most earlier local coding raw
requests/workspace snapshots did not. Earlier numbers below are recorded
historical results, with that evidence limitation. The exact frozen real-source
grader was recovered with its original hash. Fresh complete contribution trials
now store raw requests, source snapshots and independent checks in persistent
Docker storage; recommendations will use those durable results. The interrupted
stock sampling and originally queued GPT-OSS/native/final cohorts are pending
plans, not completed results.

## What changed in the evaluation

Earlier successful repository reviews and guided edits do not establish novel
bug-fixing ability. This investigation adds native terminal/file edits in an
actual selected checkout, independent checks withheld from the model, immutable
original regression checks, actual published-branch grading, and a retained
conversation followup. Models must produce correct code as well as valid forge
operations. Model-written tests passing is insufficient evidence by itself.

Read-only controls compare source pagination and owner hints. Small synthetic
coding tasks measure URL construction and an in-place expiring-job queue
contract. A development contribution task exercises settings parsing plus
issue/fork/branch/commit/PR and README followup. A previously unpublished defect
in the real Nicotine booksearch provider/worker supplies a separate real-source
coding task. Ordinary inputs are paired with approximately 49,925 Qwen tokens
of other repository files. Full original project baseline is 83 passing tests
and two passing subtests in the separate verified project-test image.

See [protocol](protocol.md) for profile changes, grading rules, exclusions,
selection rules and isolation limitations, and [research](research.md) for
external evaluation methods and source links. These are small local experiments,
not SWE-bench scores or evidence of unattended reliability.

## Recovered read controls independently audited

All 30 saved read conversations completed without mutations or validation
rejections. In the 18 ordinary SonicRatings requests, every scoped repository
read selected `sickprodigy`; two Qwopus answers used search metadata alone.
All model-facing calls used the Gitea interface. A GitHub link to a companion
project in an answer is not a GitHub routing attempt. Both old/new reader and
base/owner-hint conditions completed, so this sample does not establish a
completion-rate improvement from either change.

Completion still differs from grounded answers. Examples include Qwopus
reversing the ratings direction, a Fable phrase reversing the unrated-only
filter, and a Fable source explanation claiming bad settings can never crash
the plugin even though its quoted helper leaves OverflowError uncaught.
The requested bounding helper/ranges and two caught exceptions were recovered
by all 12 source-control answers; that does not validate every added assertion.
These are specific audited errors, not an exhaustive sentence-level success
rate. Saved conversations support reinspection after the controller interruption.

## Completed native coding development results

Each row represents one valid conversation on each of two tasks. Initial
permission/safe-root harness failures are excluded and retained separately.

| Model file/profile | URL task | In-place queue task | Interpretation |
| --- | --- | --- | --- |
| VibeForged v2 Q4 | Pass | Pass | Both independent checks and original regressions pass; actual checks executed |
| FableVibes Q6 | Pass | Pass | Both independent checks and original regressions pass; actual checks executed |
| Stock Qwen3.5 9B Q5 | Pass | Pass | Both independent checks and original regressions pass; actual checks executed |
| Empero Qwen3.8 community distill 9B Q5 | Pass | Pass | Both independent checks and original regressions pass; actual checks executed |
| FableVibes Q4 | Pass | Fail | Queue identity contract broken; existing identity assertion removed |
| VibeForged v2 Q6 | Pass | Fail | Queue identity contract broken; existing identity assertion removed |
| Gemma 4 E4B Q5 | Pass | Fail | Queue identity contract broken; existing identity assertion removed |
| Qwopus Fable5 4B Q5 | Fail | Code checks pass | Unicode-directory URL error; relevant queue test suite was not actually executed |
| FlashModel Qwen3.5 9B Q5 | Pass | Fail | No queue patch; repetition stopped the session |

This is not evidence that higher weight precision is uniformly better. Fable Q6
improved over Q4 on this queue task, whereas Vibe Q6 failed where Q4 passed.
Weights, training specialization, sampling and stochastic behavior must remain
separate explanations. The Empero filename is not an official stock Qwen model;
live hashes and publisher provenance distinguish it from the real stock control.

## Completed settings contribution development results

Original engineering profile: eight fresh sessions, each followed by a retained
README turn. No complete correct contribution. Empero created actual issues,
commits and PRs in both sessions, but fresh remote clones still failed the
numeric-zero contract. Other models sometimes fixed code locally without
publishing it, or hunted for unavailable Git credentials despite configured MCP.

Revised engineering profile: eight fresh sessions across Vibe Q4, Empero Q5,
Gemma E4B Q5 and stock Qwen3.5 Q5. No complete correct contribution. Vibe Q4 and
Empero did publish PRs, but their actual remote code failed the contract despite
passing model-written tests. Some changes invented disabled sentinels or changed
zero into an unlimited maximum. Issue/PR text also invented caller behavior
unsupported by the fixture. Stock Qwen created an issue in one session but did
not publish a correct fix. Gemma published feature commits without an issue/PR.

Fresh isolated direct-function probes of the five surviving published source
snapshots independently reproduce `OverflowError` on infinity in every one.
Their numeric-zero outputs are 12, -1, -1, 12 and None under default=12;
these are observed outputs, not reconstructed original seven-case grades.
The snapshots preserve the original report's concern about altered zero
contracts and insufficient invalid-input coverage despite passing new tests.

The revised profile combines selected-project context, explicit available
transports, a general reproduction policy, publisher improvements and corrected
branch metadata isolation. It is not a controlled estimate of any one change.
The small fixture's absent worker implementation leaves a diagnosis ambiguity;
retain these outcomes, then evaluate the complete provider/worker in the actual
real-source replica. Do not use that ambiguity to erase wrong-contract code or
unsupported claims.

Test issues are preserved and closed after each completed cohort. PRs remain
unmerged. Operator transport smoke commits are labeled separately and never
counted as model successes. The user's original Nicotine repository is not the
publication target of these experiments.

## Completed real-source native controls

The nine checks contain six defect cases and three established-behavior controls.
The unmodified source already passes those three controls. The table therefore
shows defect cases repaired out of six, rather than inflating progress with
already-passing checks. Passing requires all six plus the controls and honest
validation; none of these initial configurations qualifies.

| Profile at 98,304 context | Ordinary defect cases | Bulk-reference defect cases | Edited test suite |
| --- | --- | --- | --- |
| VibeForged Q4, q4 KV, .2 | 5/6 | 0/6 | Pass in both conversations |
| FableVibes Q6, q4 KV, .2 | 1/6 | 3/6 | Fail in both conversations |
| Stock Qwen3.5 Q5, q4 KV, .2 | 0/6 | 0/6 | Fail in both conversations |
| Same VibeForged Q4, F16 KV, .2 | 0/6 | 2/6 | Pass in both conversations |

All eight conversations preserve the three small private controls. Immutable
complete original-project checks are audited separately. Fable ordinary and
stock ordinary exhaust 30 iterations; their bulk conversations reach 600
seconds. Both Vibe profiles finish normally. Vibe's ordinary q4-KV run misses
one malformed overall response type; other runs also leave incorrect exception
scope, lost valid mixed results, or broken new tests. A model-written suite
passing does not establish that the reported failure has been fixed.

The F16 cache launches at the same 98K window: measured GPU memory is 10,318 MiB
versus 9,082 MiB with q4 KV. These unseeded samples show no demonstrated code-
correctness benefit; they cannot isolate a causal precision effect.

Actual stock compression logs show a summary rejected for output truncation.
Its auxiliary request lacks an explicit output allowance, leaving the backend's
512-token default. Native SDK preflights confirm the final configuration sends
an 8,192 allowance and the appropriate model-specific reasoning setting.
Hermes knows the 98K window; its effective default trigger, after output reserve,
is 67,584 input tokens. This is a distinct configuration problem, not evidence
that every incorrect patch was caused by context compression.

## Fresh complete contribution cohort (active)

An initial recovered-fixture run exposed an operator policy file accidentally
left unignored in the selected checkout. The model staged it, and the scoped
publisher correctly rejected it. Preserve that run's independently failing
code checks, but exclude its publication result as harness-affected. The next
bulk trial was stopped without a completion score. Policy now enters through
the environment hint; every new model starts from an asserted clean Git tree.
All three primary profiles were restarted fresh under that corrected fixture.

GPT-OSS 20B MXFP4 ordinary input completed at 131,072 loaded context, peaking
at 12,572 MiB. It repaired three of the six defect cases and preserved the three
controls. Its 85 visible tests and the immutable 83 original tests passed. It
created a real fork branch and one commit, but no issue or PR. A fresh remote
branch clone independently failed the same mixed-entry cases. The README
followup remained local, falsely described mixed-entry support, and was absent
from the published branch. This is not a successful engineering contribution.
Provider retries for malformed Harmony headers consumed time but eventually
recovered; the backend did not run out of VRAM.

GPT-OSS bulk-reference input repaired four of six defect cases and preserved
all three controls, with both edited and original suites passing. It still
crashed on an array-shaped overall response and treated a mapping-shaped
`docs` field as an empty result. No regression test or forge contribution
was produced. The final answer claimed malformed data could never crash it;
the independent worker test directly contradicts that. The session ended
normally after 2,154.58 seconds at the same 12,572 MiB peak, reaching 84,261
prompt tokens by its final request. These are two failed whole workflows,
not two failed CUDA loads or terminal provider outages.

VibeForged Q4 ordinary input completed the actual upstream issue/fork feature
branch/two-commit/PR and published the retained README followup in 242.56
seconds at 10,462 MiB. A fresh remote PR-head clone (4e64e12a) failed all six
defect cases while preserving the three controls and original suite. Its
`or []` change prevents the reported iteration crash but returns “no results”
rather than the requested unavailable reply; other malformed shapes still
crash. The added regression substitutes a provider that always raises
SearchError and never exercises the changed JSON parser. Running that edited
suite against the original booksearch source also passes. The README's
never-crashes claim is false. Issue 2 was closed with readback after evidence
was saved; PR 3 remains unmerged. This is successful forge mechanics and a
failed whole engineering task.

The audit now runs edited tests against original target code in a separate
isolated tree, as well as running them against the model's final code. Passing
on original code proves inadequate regression coverage; failing requires review
of the failure reason, since imports or newly invented APIs can also fail.
These operator checks do not supply private test inputs or patch hints to models.

The remaining primary sessions are active. Larger loaded windows alone do not
establish useful debugging at their maximum size. Final recommendations must
state observed code correctness, original regressions, checks actually run,
published state, VRAM and latency separately. A prepared existing 35B CPU-expert
offload control requires no additional weight download and will follow if the
smaller practical configurations fail.

## Transport correction during the fresh cohort

The unfinished V4 Vibe bulk session exposed a valid 40-character branch-name
edge in the installed tree call. Commits worked; reading the tree by name
failed, while its actual SHA worked. The trial was stopped and preserved
without a completion score. Operator 39/40/41-character controls and a native
SDK publication preflight confirm the problem and workaround. Original
services were restored and verified before the corrected tests restarted.

The three completed V4 sessions remain reported. A fresh ref-safe V9 Vibe
bulk trial and the previously unstarted stock pair use focused 0.1.6, publisher
0.1.3 and scope proxy V4. Larger-model and publisher-setting trials are queued
behind them, using the same corrected transport. This is a disclosed profile
revision; no matched-version model-only conclusion is claimed.

## Ref-safe completed results (remaining profiles still active)

Vibe bulk completed with the corrected transport: actual issue 7, PR 8, two
commits including README/new tests, 751.30 seconds, peak 10,462 MiB. Its
40-character branch now works through the real agent, confirming the bridge
repair. All six defect cases still fail; three controls and 89 edited tests pass.
The new tests assert empty results or uncaught AttributeErrors as success,
contrary to the requested behavior. They fail on original source, illustrating
why before/after differentiation alone does not establish a correct regression.
The README describes uncaught errors then claims unexpected responses cannot
crash the plugin. Issue 7 is closed; PR 8 remains unmerged.

Stock Qwen3.5 Q5 ordinary completed issue 9/PR 10/two commits in 494.35
seconds, peak 9,712 MiB at 262,144 loaded context. It repairs the reported null
case but leaves five other defect cases as errors. All three added tests mock
provider.search itself and pass on original code. Original tests pass, but the
README's broad no-hang/no-crash statement is false. Issue 9 is closed with
readback; PR 10 remains unmerged.

A secondary alternate-root audit first verifies the original 83-test project
at /checkout, then runs completed candidate suites there. Vibe bulk's actual
published tests fail because a new module hardcodes /workspace; the other
four completed candidate suites pass this portability check. This does not
change the frozen primary behavior grades or turn a portable but incorrect
fix into a success. It is an additional post-hoc quality check.

Before larger/publisher configurations receive any model inference, native
SDK preflights verify actual JSON sampler fields, streaming tool execution
and retained nonempty reasoning_content in the following tool-history
request. Nonstandard llama.cpp options are passed through SDK extra_body;
standard temperature/top-p/penalties stay at the SDK level. All four future
profiles pass both serialization and mocked stream/tool/history checks.
No model inference or Gitea mutation occurs in those mocked checks.

The public-command supplemental audit also tests the same inputs through
booksearch_command and the real background-worker caller. An operator
reference demonstrates a valid outer-thread exception boundary: 9/9 public
outcomes and all 83 original tests pass, whereas the direct-worker checker
marks its root-array case as an error. Worker scores therefore remain
diagnostics, not an exclusive implementation prescription. A disagreement
requires review of actual public behavior and the source. No private reference
solution is supplied to models or included in public evidence. All six
completed model sessions fail the public-command route as well.


### Followup controls completed: 35B CPU expert offload

At 98,304 context, 24 CPU expert layers, publisher coding sampler and preserved
thinking, ordinary/bulk public-command defect outcomes were 2/6 and 4/6; all
three original-behavior controls passed. Ordinary completed issue #11 / PR #12
with two real commits; bulk hit its 1,200-second first-turn limit with no forge
writes and two failing authored tests. Immutable original 83 tests pass in both.
Ordinary's README followup adds a top-level-object guard (local phase1 was only
1/6), but leaves null/mapping-docs and malformed-author failures. Its published
README contains literal tool-parameter markup despite a read-back. A genuine
JSON test explicitly asserts incorrect empty-results behavior for null docs.
The 35B control therefore does not qualify as an unattended repository agent.
This is a different size/architecture/context/sampler combination, not a pure
size effect. See the eight completed fresh rows in `fresh-results.csv`; more
profiles remain live/queued, so this is not the final ranking.

The 27B dense public IQ3_XXS file loaded at 98,304 context using approximately
13,194 MiB GPU memory and began inference. That is a capacity observation only.
A newly researched Hermes-trained Qwen3.8 27B extension has been registered
before inference, after the sampler queue; its verified download is underway.
The second API-task audit was independently preflighted against original source:
83 original tests pass, four ownership defect checks fail, three controls pass.
No API model conversation has run yet.

## Hermes-adapted 27B: ordinary run completed

The verified Qwen3.8 Hermes-adapted IQ3XXS file completed its ordinary-input
conversation with native persistence, thinking disabled and publisher .8/1
sampling. Actual device usage peaked at 13,094 MiB with 98,304 context loaded.
It repaired four of six formerly failing public-command cases: null docs,
non-list docs, non-object overall payload, and non-object individual entries.
Malformed mapping/numeric author fields still hide a later usable result.
All three controls pass. This is incomplete code, despite a substantially better
ordinary result than the small-file controls.

It executed targeted tests, fixed its initially broken HTTP mocks, and published
four tests including genuine JSON-parser regressions. Independent edited and
immutable original suites pass, and the new suite distinguishes original code.
The worker-only new test mocks the already-handled SearchError and adds no
coverage of the reported parser defect by itself. The other tests do.

Actual initial PR #20 contains commit
`3e5fa80303fd15854b4949981e7491875be6d3da`; the retained README request added a
second commit, final `8dd6f7cbdc71d4334a238924799ae3cb8a8cfe8b`.
The independently cloned first and final published trees both repair 4/6.
Issue #19 is closed with readback; PR remains unmerged. The README describes
its implemented non-dict-entry guards rather than claiming every malformed
field is safe. Trial elapsed was 1,385.26 seconds, including independent audit;
agent elapsed was 1,370.13 across two turns. Large-context result remains pending.
This corrected persistence/title configuration differs from earlier SDK runs,
so the difference cannot be attributed solely to trained weights.

GPT-OSS's publisher low-reasoning bulk run instead left an unmatched closing
parenthesis in `booksearch/__init__.py`. The nine behavioral cases cannot run;
record this as source failure, not nine executed failures. No tests or forge
contribution were produced. The first answer admitted editing failure, but the
README followup claimed exceptions no longer escape despite broken syntax.
Lower reasoning/sampler changes did not yield a practical replacement here.

Saved GPT backend logs give a limited transport diagnostic: the default/medium
pair contains 23 unparsed PEG-native warnings and three format-500 exceptions;
the publisher/low pair contains neither pattern. These are counts in saved
cohort logs, not success rates or proof the setting permanently solves Harmony
formatting. The lower-reasoning pair still produced incorrect code and a syntax
error. Better formatting in these samples did not imply better task completion.

The adapted-model bulk run subsequently hit its 1,200-second first-turn budget
with an empty final diff and no contribution. First tool was at 612.881 seconds;
it made seven calls and reproduced the actual TypeError at 878.184 seconds.
At the deadline it was waiting for a model response for 321.4 seconds. No README
followup began. The six recorded main requests did not duplicate the reference
packet, so this run does not exhibit the older replay-overflow defect. Original
83 tests pass because source/tests are unchanged; public defects remain 0/6.
Total trial time including independent checks was 1,215.06 seconds. This is a
bounded latency failure, not a claim the checkpoint cannot solve the bug at all.

## Conditional Qwen3-Coder ordinary run

The official Qwen3-Coder 30B A3B Instruct public Unsloth IQ3XXS file was verified
at 12,848,766,112 bytes, SHA
`d6b85d2b6633c55be3751848acc74fab40d28d93b27dabacd96ceabe10962057`.
It loaded 98,304 entirely on the P100; the CPU4 fallback was not used.
Observed ordinary peak was 15,348 MiB. Actual first wire used .7 / .8 / top-k20 /
min-p0 / repetition1.05 and 8,192 output cap; native SDK preflight passed.

The ordinary trial completed in 488.0 total / 473.367 agent seconds but repairs
0/6 public defects; all three original controls pass. Its null/noniterable guard
returns an empty list instead of the required unavailable response, while
iterable bad docs, malformed records and malformed authors still fail. After
HTTP mock/import attempts failed, it replaced the new test with a copy of its
own algorithm; that test never invokes production code and passes the original.
Manual scripts similarly simulate behavior, including record skipping that the
actual provider does not implement. Targeted tests and independent edited /
immutable original suites pass, demonstrating the weakness of those new tests.

It called Gitea identity once, but created no issue, branch, commit or PR and did
not publish on the README followup. The README claims unsupported overall and
individual-entry handling. Whole workflow fails; its faster decode is not
correctness. Bulk paired run remains pending.

Qwen3-Coder bulk subsequently completed both turns normally in 1,274.31 agent /
1,288.01 total seconds, peak 15,350 MiB. First tool was 384.39 seconds; long-context
requests decoded around 10–11 tokens/sec versus about 29 for an early ordinary
request. These are particular observed requests, not a standardized speed ratio.
Public defects again remain 0/6, controls 3/3. It treats non-list docs as empty
rather than unavailable and still crashes on other malformed shapes. The new
untracked `tests/test_booksearch_fix.py` repeats its own proposed algorithm;
it does not invoke the provider and passes on original source. A patch to the
existing test file failed; the native SDK appended a file-mutation warning while
the model answer still claimed comprehensive tests. Original seven targeted
tests and the standalone simulation ran and passed. No forge actions or
contribution occurred. Both inputs are failures of this tested profile, not a
claim that every sampler/precision of Qwen3-Coder is incapable.

## Independent API stage started

Finalists are the adapted 27B (.8, thinking disabled, 98k) and GPT-OSS default
(.2, actual medium reasoning, 131k). Protecting the strongest ordinary genuine
contribution prevents the artificial bulk stress from excluding the adapted
model; the other slot follows aggregate behavior (GPT 3+4 versus 35B 2+4).
All first-task failures remain. Both exact native SDK/persistence/stream/tool/
history profile preflights passed before any API inference. The complete
selection/configuration record is [finalist-profiles.json](finalist-profiles.json).
The live first adapted API session also has a persisted nonempty native user
message UID, checked read-only; persistence alone still does not fix every
summary-carrier replay layout. Four fresh API conversations are now running
sequentially, followed by the two fixed 35B context controls.
