# Goal investigation protocol

Primary coding development: six models, two fresh synthetic utility tasks each,
one valid conversation per task, 98,304 context, q4 KV, temperature 0.2,
8,192 output ceiling, 600 seconds and 30 iterations. Higher output ceiling
is an intentional separately labeled change from earlier 4,096-token tests.
Independent private behavior checks plus frozen original smoke checks; edited
candidate tests alone do not determine success. Harness permission failures
are excluded, preserved, and do not count as model failures or repetitions.
A matched extension adds existing Qwen3.8 9B Q5 and FlashModel 9B Q5.

Full contribution holdout: settings zero/invalid-input defect in the dedicated
public evaluation repository, frozen main aa7bdf7cbb8ed42bbe3c6a61d18c8f7cb747d153.
Vibe Q4, Fable Q4, Fable Q6, two independent sessions each. Each first request
asks for a contribution without enumerating tools. A follow-up asks for README
examples and updating the same contribution. Persistent contribution policy
and engineering AGENTS profile supply stable operating conventions. This is
a complete configured system test, not an unassisted model-weight comparison.
Tool discovery is explicitly off; focused tools are directly visible. Scoped
MCP prevents cross-trial answer leakage/default-branch writes; own prose edits
and multiple feature commits remain allowed. Independently verify actual
remote bytes, issue/PR direction, test execution, and follow-up behavior.

Real-code holdout prepared before model trials: nicotineplus-plugins commit
84afaf401b29753b6810e4f92f253e0d28637dbf, booksearch catalog response shapes.
Four of seven independent checks error on the original; a private reference
passes all seven. Agent receives symptoms and expected behavior, not a patch.
Vibe Q4 and Fable Q6 each get ordinary and bulk-context versions. Bulk input
contains 49,925 Qwen tokens of other actual repository files; target booksearch
files are read from the selected checkout. This is a bulk-reference coding
stress test, not a full-window reliability claim. Native tests use the existing
standard-library booksearch suite. Full discovery has a known pre-existing
announcer import error because pytest is absent; do not attribute it to a model.

Read routing/source ablations are separate, three independent sessions per cell.
Metadata-only answers can be sufficient for simple identification. Pagination
and owner hints are not credited with improvement if both conditions pass.

Before full contribution trials, promote Qwen3.8 Q5 and/or FlashModel Q5 if
each passes both independent development coding tasks. This development-based
selection changes cohort size, not holdout scoring or prompts. Fable Q4 remains
a precision-comparison control even though its queue task failed.

For real-repository validation, also promote at most one compact candidate:
Qwen3.8 or FlashModel must pass the private settings checks and create a PR
with at least two feature-branch commits in both full-workflow repetitions.
If both qualify, select the lower summed workflow elapsed time. This is a
selection rule, not a substitute for independent remote and honesty review.

Fork lifecycle: Gitea permits reusing the automation account's existing fork.
The dedicated upstream begins without one; the first successful contribution
can create it, later trials must inspect/reuse it and create fresh lease-prefixed
branches. Record this difference when comparing elapsed time. Do not claim every
model created a new fork, or treat a correct reuse as a failure. Main stays frozen
and other trials' feature refs, issues and PR contents are hidden by the gateway.

Selected-context development comparison: after the first Vibe Q4 full-workflow
trial ignored the selected target in the system environment hint, prepare a
separate profile adding the native `selected-project` hook. It appends actual
Git root/branch/HEAD/remotes near each user turn, with credentials removed.
No patch hints, changed task request, tool-argument correction or extra write
authority. Vibe Q4 and Qwen3.8 Q5 get two fresh full sessions each under this
profile, after the original four-model contribution cohort. Preserve original
failures. Settings is now a development task for this profile comparison,
not a new untouched holdout. Native SDK context smoke passed before inference.

The real booksearch holdout will use the same selected-project context hook
for all its candidates, alongside the previously prepared engineering policy.
A compact candidate may qualify from two successful contribution repetitions
under either complete profile, using the same selection criteria; select at
most one. Record this profile addition before any real-code model trials.

Before any real-code inference, strengthen that private grader to nine checks:
include mapping/numeric author fields alongside malformed top-level/result-list
shapes and mixed scalar result entries. Accept skipping the malformed item or
normalizing its author, provided the later valid book still reaches the user.
The original now errors on six of nine checks; the private reference passes
nine. Original seven booksearch tests remain frozen. This is a pre-trial grader
revision, not an outcome-dependent change; retain its revision in the manifest.

Identity correction before stock-model comparison: runtime label `qwen38-q5`
is Empero's community distillation (`empero-ai/Qwen3.8-9B-Distill-GGUF`), not an
official stock Qwen release. Its results remain valid under that identity.
The filename alone was misleading; both live hashes now match the earlier
verified publisher downloads. Add the existing stock Qwen3.5 9B Q5_K_M from
Unsloth's quantization of Qwen's release as a separate two-task development
control before the selected-context cohort. If both primary coding tasks pass,
promote it to two full selected-context contribution sessions. A compact real-
code candidate can qualify from that complete profile too. No new download.

Before any selected-context contribution inference, also make the isolated
session's transport capabilities explicit in that profile: no direct Git
network or Git credentials; forge access is through the configured MCP and
workspace publisher. Original contributions already instructed MCP publication,
but did not explicitly describe the network restriction. Fable's credential/
DNS troubleshooting showed why this environment fact matters. V2 therefore
compares a combined context-and-capability profile, not a pure causal estimate
of message placement or of the context hook alone. Keep the original negative
traces and this limitation. The ordinary user requests remain unchanged.


Operator-only SDK transport smokes (no model inference) first verified existing
and one-new-file publication plus a second commit. A three-new-file smoke then
reproduced another circuit-breaker interaction: routine 404 metadata probes
tripped the server cooldown before commit. Publisher 0.1.1 uses bounded paginated
remote trees before/after the commit; the same real SDK smoke then passed.
Original contribution cohort keeps its frozen 0.1.0 source. The later V2 profile
uses 0.1.1 from a separately named source directory and records plugin hashes.
This is another disclosed profile change, not evidence of a weight-only or
context-only effect. No model has been credited for operator smoke commits.


Also include Gemma E4B Q5 in the revised full profile, two sessions: its earlier
prescribed-edit contribution results were strong, and its fresh URL fix passed,
although the in-place queue contract failed. This is a small instruction-model
comparison under the stronger project profile, not removal of that earlier
failure. It can qualify for the compact real-code slot using the same two-full-
session rule. This selection is recorded before revised-profile inference.

During the original Empero contribution repetitions, branch-list auditing found
an isolation defect: native branch records use `commit_sha`, while the gateway
filter expected nested `commit`. Other trial branch names/commit IDs leaked in
list metadata. Attempts to read those foreign refs were still blocked, so no
other trial's patch contents were returned. Preserve per-run metadata audits;
treat affected forge-navigation traces as exploratory, rather than an entirely
clean isolation comparison. The revised gateway filters the actual flat shape,
with an additional test using the observed native payload. It is a separately
named V2 source; the original active gateway remains frozen. This is another
disclosed environment correction in the revised profile.

After the original contribution cohort finished and before any V2 contribution
or real-code inference, extend the general engineering policy: reproduce the
reported failure against original code, preserving exact input values/types,
and check that the regression distinguishes before from after. Empero tested
string "0" (already working) while leaving numeric 0 broken in both original
contributions. This rule contains no task-specific expected result or patch;
apply it to every revised-profile project. Preserve the old policy and per-run
workspace snapshots. Valid alternative solving sequences are not automatically
failed solely for omitting a specific test-before-edit command; code outcomes,
test honesty and actual published state remain independently graded.


The confirmed stock Qwen control passed both development tasks. Include it in
ordinary/bulk real-code validation regardless of the settings-workflow outcome,
so the regular-versus-community comparison is actually measured on a real
repository. That native-code stage should not exclude the stock control solely
for a forge-stage failure. Keep Vibe Q4/Fable Q6, plus at most one other compact
candidate satisfying the earlier full-session rule. This selection change is
recorded before any real-code inference; real-code and forge outcomes remain
separate, and every settings failure remains in the report.

After real-code validation, run one separately labeled cache-precision probe.
Choose a file that passed both ordinary and bulk private checks; if none does,
choose the most passed cases, then lower summed elapsed time. Re-run that same
ordinary/bulk task pair under the same complete native profile, sampler, output
cap, model weights and 98,304 context, changing only K/V cache from q4_0 to f16.
Measure actual loaded/active VRAM; a load/OOM failure is a configuration result,
not a model reasoning failure. This is a development-selected paired diagnostic,
not another fresh holdout. No additional model download or weight conversion.

Final pre-trial real-grader audit: accept equivalent unavailability wording for
malformed overall responses and allow partial-result warnings alongside the
usable book. Do not require one exact new error sentence or one exact partial-
result list length. Existing frozen tests still protect established formatting
and callbacks. Nine cases remain; original errors on six and private reference
passes nine. This broadening happened before any real-code model request, with
revision recorded in the manifest; it is not an outcome-dependent regrade.


Before the first real-code request, complete the project test environment:
pytest 9.1.1, pluggy 1.6.0 and iniconfig 2.3.0 are installed from SHA-verified
public wheels into a separate appended dependency directory. Existing Hermes
packaging 26.3 and Pygments 2.21.0 remain unchanged. A separate immutable image
is used only for real-project evaluation, not the production service. Full
original baseline: 83 tests and two subtests pass. Agent project instructions
advertise both the focused stdlib command and complete pytest command. Offline
graders have writable temporary space and bounded execution. Grade all project
tests, including newly named regression files, rather than only one filename.
The optional compact selection requires a successful PR with at least one
commit; documentation in the initial commit is valid and a mandatory second
commit must not reject an otherwise complete first-turn contribution.

The final full-workflow arena uses a byte-identical replica of the real Nicotine
plugins source, with its actual provider/worker caller. Its per-session tool
volume contains only that runner/plugins and optional bulk reference; parameters
arrive through stdin and do not expose the later followup before that turn.
Publisher 0.1.2 permits new files within the selected plugin and tests folders;
this avoids prescribing a specific regression filename. Original V1/V2 sources
and measurements remain frozen. These are harness improvements, not model
performance gains. New test issues are saved then closed; PRs remain unmerged.


Sampling sensitivity is preregistered before its inference: after the KV-only
probe, repeat ordinary/bulk native real-code sessions for Fable Q6 with its
published generation temperature 1.0, top-p .95, top-k 20; and stock Qwen3.5 Q5
with its published precise-coding temperature .6, top-p .95, top-k 20, min-p 0,
presence penalty 0, repeat penalty 1. Keep q4 KV, weights, prompt, policy,
98,304 context, output cap and practical time budget fixed. Explicitly set
min-p 0 for both publisher profiles; the matched baseline backend used .05.
These are sampling-profile comparisons, not temperature-only causal estimates.
Sources: https://huggingface.co/tvall43/Qwen3.6-14B-A3B-FableVibes/blob/main/generation_config.json
and https://huggingface.co/Qwen/Qwen3.5-9B#best-practices.
A final real-source full workflow may select a successful profile from these
comparisons. Such selection is development use, not an independent leaderboard.


Before the sampling outcomes, freeze final full-workflow selection: prefer a
profile with private cases, immutable original project suite and actual model-
executed successful checks in both ordinary/bulk sessions. Rank by number of
such full native passes, preserved original suites, private cases passed, lower
measured peak VRAM, then elapsed time. If no profile fully qualifies, label the
selected candidate exploratory rather than successful. Run two fresh complete
real-source contribution sessions (ordinary and bulk) with that exact selected
cache/sampling profile, then independently clone and grade published branches.
No model-written success narrative or operator transport smoke is a pass.


Budget clarification and final workflow limit, before full-real inference:
the historical parameter named call_limit is passed to Hermes max_iterations;
it is an iteration limit, not an exact individual tool-call count (parallel
tool calls can exceed it). Retain the matched native comparisons at 30 iterations
and 600 seconds. Fable ordinary reached that iteration limit while revising its
new tests. Give final real-source full contributions 60 iterations and 1,200
seconds per user turn, with a 2,500-second external whole-session limit. This is
a separately labeled generous-budget workflow profile, not a claim that the
shorter-budget model differences are intrinsic capability ceilings. Selection
also requires the candidate's full edited test suite to pass; passing private
checks and immutable originals does not excuse failing new regression tests.


Context-policy finding before full-real inference: Fable's long conversation
triggered repeated compaction. The native SDK preflight confirms a correctly
pinned 98,304 window; although the base configuration default is .50, this image
raises windows below 512K to an effective .75 trigger. After the 8,192 output
reservation, the actual default trigger is 67,584 input tokens. Do not describe
this as a 32K context-detection bug or assume the raw .50 value is effective.
A second SDK preflight confirms an explicit .85 setting yields a 76,595 trigger.
Use that policy for the final generous-budget full profile, together with the
previously tested local-Qwen auxiliary compression override: max_tokens 8192,
chat_template_kwargs.enable_thinking false. Keep compaction enabled and record
actual engine metadata. Primary native/cache/sampler comparisons retain their
original default policy. The full profile is a combined practical setup test,
not a causal compression-only or model-only comparison. Compaction attempts,
success/failure and resulting model-facing context must be reported separately
from simple backend context capacity.


Final full-workflow bug report includes one concrete reproduction, introduced
before that cohort: catalog JSON {"docs": null} lets TypeError escape from the
original worker. Baseline trace already confirms it. This resembles a normal
issue with an input/error rather than an instruction to make a specific edit.
The user-facing symptom, response contract and mixed-result requirement remain.
No source patch, test code or other input examples are supplied. One of the nine
independent checks now corresponds to the disclosed reproduction; report one
reported case plus eight additional withheld cases, not nine unseen cases.
The initial symptom-only native trials remain unchanged and visible. This is a
clearer-report development workflow profile, not a replication with identical
input or an assertion that the agent inferred this reproduction unaided.


Different-family extension, declared before its inference: the first stock Qwen
real-code run also failed private and candidate-suite checks. Re-evaluate the
already retained GPT-OSS 20B MXFP4 file on the same symptom-only native ordinary/
bulk pair after the sampling cohort. Keep .2 temperature, q4 KV, 98,304 context,
8,192 output, 30 iterations and 600 seconds; measure load/VRAM separately. The
live hash matches its pinned ggml-org download. No new model download, no deleted
small useful models. Append this pair to final candidate selection. A load/OOM
failure does not count as a reasoning failure. A .2 result is not a claim that
all GPT-OSS sampling profiles have been exhausted.
If GPT-OSS is selected, its final compression auxiliary uses an 8,192 cap with
reasoning_effort low; do not pass the Qwen-specific enable_thinking flag. Native
SDK HTTP serialization smoke checks both compression forms without inference.


Final capacity probe, before full inference: F16 Vibe loads at 98,304 with
approximately 10.1 GiB active VRAM, and the live models endpoint reports native
training context 262,144. Do not assume 98K is the P100's maximum window. For the
selected final Qwen setup try native 262,144; for GPT-OSS try native 131,072.
Read actual n_ctx_train after loading and refuse extrapolation beyond it. If the
larger launch fails, preserve the configuration failure and fall back to the
previously tested 98,304. Record actual engine context, compression trigger,
metadata, launch settings and peak memory. This is a combined practical setup
probe, not an identical-context comparison to the 98K native cohort. The task
still contains about 49,925 Qwen reference tokens plus conversation, so a loaded
262K window is not evidence of correct coding across 262K input tokens. No RoPE
scaling, weight conversion or additional model download is introduced.

## Separate existing 35B offload control (prepared before inference)

After the durable primary cohort, test the existing full Qwen3.6 35B A3B
UD-Q4_K_XL file with 24 CPU expert layers and 98,304 context, one ordinary and
one bulk-reference complete session. This is a larger practical configuration,
not a matched weight-only comparison. Use the publisher's precise-coding
sampler (.6 temperature, .95 top-p, top-k 20, min-p 0, presence penalty 0,
repeat penalty 1) and explicit thinking preservation. The actual GGUF embedded
template was parsed and supports both enable_thinking and preserve_thinking.
The same frozen task, independent checks, general policy, publication scopes,
output limit and time/iteration budgets remain. Record offload latency, host
and GPU memory; no additional model download or quantization. No model has
yet run this configuration.

## Complete publisher-setting diagnostic (preregistered before inference)

After the primary and larger-file cohorts finish and restore, run two complete
ordinary/bulk pairs using existing files: stock Qwen3.5 9B Q5 at its .6 coding
sampler with min-p 0 and thinking enabled, then GPT-OSS MXFP4 at temperature
1.0/top-p 1.0 with top-k/min-p filtering disabled and low reasoning effort.
Both retain q4 KV and the same native context sizes as the primary (262,144
and 131,072), frozen bug, scope, tools, general policy, 8,192 output ceiling,
60 iterations and 1,200 seconds per user turn. First-turn snapshots are saved
by the separately versioned runner. This is a practical configuration comparison,
not a pure temperature effect. Preserve all primary failures. The earlier
stock .6 pair planned before the controller interruption never started; it is
not prior evidence for this complete workflow. No new weights are required.

## Installed tree-ref defect and ref-safe continuation

During V4 Vibe bulk, a valid 40-character branch accepted commits but tree
reads by branch name failed. Operator controls reproduced 39/41-character
success, 40-character failure, and commit-SHA success. Stop and snapshot that
unfinished trial without a completion score; it is publication-harness affected.
Three completed V4 sessions remain valid observed results (GPT-OSS ordinary/
bulk and Vibe ordinary). Previously unstarted stock V4 sessions are not results.

Focused 0.1.6 and publisher 0.1.3 resolve this branch case to a verified actual
commit SHA; the scope proxy separately permits only SHA reads learned from
this trial's own fork-branch metadata. Foreign branch metadata remains hidden.
54 plugin checks and eight isolation checks pass. A real native SDK/scoped-MCP
preflight publishes two commits, verifies remote blobs and creates a correctly
directed PR on a 40-character branch; operator issues are closed with readback.
An initial preflight hit clone ownership and cleanup response-shape mistakes;
these are disclosed operator setup errors, not model trials. The successful
transport effects were separately audited without extra writes.

Resume with a fresh Vibe bulk session and the two stock sessions under ref-safe
V9 IDs and first-turn source snapshots. Subsequent larger-model/publisher
profiles use this same corrected transport before their first inference. The
combined comparison spans disclosed tool revisions; do not describe it as a
strict matched-version causal experiment. User task, private grader, general
policy, context/budgets and model sampler remain unchanged for V9. No private
input or patch hint is sent to a model to compensate for the defect.

Secondary quality audits, added after observed defects: run candidate-written
tests with original target code substituted, and run actual published project
tests at an alternate root (/checkout) after original-project baseline passes
there. Neither supplies private cases to models or changes the frozen primary
nine checks. Record failed-before/green-after as insufficient if the expected
behavior is wrong. Record hardcoded /workspace tests as portability failures.
Future sampler configurations pass native SDK serialization and two-response
stream/tool/reasoning-history mock preflights before model inference. Correct
nonstandard SDK parameters into extra_body before those trials start; no
scored run used the earlier untested flat custom kwargs. Use recognizable
family aliases, including gpt-oss-20b, and verify real outgoing requests too.

## Public outcome check and a demonstrated private-worker false negative

Add a supplemental version of the same nine checks through the actual
booksearch_command(room=Books) entry point, with controlled provider HTTP
responses, normal threads observed to settle, and fake Nicotine event dispatch.
The original still fails six defect cases and passes three controls. A private
operator alternative reference catches unexpected errors around the background
worker: it passes all nine public outcomes and all 83 original tests, while
the earlier direct-worker diagnostic rejects its array-root case (8/9).
This demonstrates an implementation-location false negative in using only
that private method as the outcome oracle. No reference patch is shown to models.

Keep the original nine-case worker scores unchanged as diagnostics. Select
for actual public-command behavior, original regressions, actual published
code and honest usable tests; inspect any disagreement instead of rejecting
a valid outer-boundary fix. Same payloads do not count as nine additional
bugs. These supplemental checks do not validate a real Nicotine GUI or prove
race freedom. Unsettled alternative async implementations require manual
audit. All six completed model sessions also fail the public route, so the
observed negative conclusions remain. Larger models were only beginning
inference when this operator-only control completed.

## Broader second-task selection (before any API-task inference)

Do not gate all breadth testing on a perfect score for one response-shape
task. After the current profile comparisons complete, select up to two
different weight files for the independent confirmed API transfer-ownership
task. For each file use its best complete profile: prioritize full public
command outcomes, then repaired defect cases summed across ordinary/bulk,
verified forge/followup completion, honest meaningful validation, then elapsed
time. Preserve both input conditions rather than cherry-picking a file's best
single run. If no profile fully qualifies, these are explicitly exploratory
comparisons of the closest candidates, not successful substitutes for the
first task. Booksearch failures remain part of any overall recommendation.

Use two fresh ordinary-input API sessions per selected profile, each with a
retained README followup and the same actual profile sampler/cache/context/CPU
offload. The seven frozen HTTP/caller cases are four defects plus three
controls. Before model inference the original fails four; the private reference
passes seven and preserves all 83 original tests. Candidate fixture edits
cannot change the embedded immutable HTTP test helper. This task broadens
evidence; it does not convert one or two successes into unattended reliability.
The earlier perfect-booksearch-only promotion rule is superseded by this
breadth diagnostic; no API model run or outcome informed the revision.


Before any Qwen3.8-adapted inference, extend the booksearch cohort with the newly
released Hermes-trained Qwen3.8 27B public merged IQ3_XXS quant. The candidate
was identified from its publisher's actual Hermes/terminal evaluations, not our
booksearch outcomes. Use thinking off, temperature .8/top-p1 with no top-k/min-p
cutoff, 98,304 context and q4 KV, two fresh ordinary/bulk sessions with the same
task, policy, budgets, tools and README followup. Plain decoding, no MTP/vision.
Verified pinned public download must preserve 100 GiB reserve. This is a complete
configuration comparison, not evidence of adapter or quantization effects.
Finish this extension after the already queued sampler cohort and before
selecting up to two different weightfiles for the API task. Retain all previous
booksearch failures. BF16/vLLM publisher results do not establish P100 outcomes.


Context-packaging diagnostic registered before inference: the 35B bulk trace
shows the full 207K-character active user/reference packet replayed after
compaction while the original remains in protected history. The actual server
rejects a 119,824-token request against 98,304 capacity. Retain this failed
configured-system result, classify the runtime/context contribution, and do
not attribute the entire outcome to model weights.

After API breadth testing, run at most two additional fresh booksearch bulk
conversations: the confirmed affected 35B complete profile and the strongest
other distinct file. Carry exact selected model/sampler/context/tools/budgets.
Use the same actual reference text and task, but seed a fixed neutral prior
conversation fixture: two short warmup exchanges, the user reference packet,
and a neutral receipt. The active user message is the unchanged short task.
These operator-provided fixture exchanges are not claimed model outputs or
executed tools. They place the large historical packet outside the native
compressor's first-three-row protected head; it can be summarized normally.
The retained README followup remains unchanged. No native engine patch or
private grader feedback is applied. A no-inference native-head/input preflight
passes before any diagnostic model call. This is a separately labeled packaging
probe, not a replacement of original failures or a causal accuracy estimate
from single unseeded samples. Final export must wait for this last cohort too.


Refinement before any context-diagnostic model inference: a native replay
control proves the installed compactor emits two copies without a message UID
and one with it. A native SDK/store/stream/tool mock proves normal persistence
assigns user UIDs; the original direct-SDK runners supplied no store. Therefore
the 35B overflow is a harness/runtime interaction, not a clean model comparison
against normal persisted Hermes. Keep its observed wrong code, failing tests,
time budget and actual oversized request; flag the context limitation.

Replace the previously planned two-distinct-files packaging probe with TWO
controls of the SAME confirmed affected 35B complete configuration. Both use
the native persistence interface, not manual UID injection. First retain the
original active-user reference layout; then use the historical-reference fixture.
The second condition seeds its explicitly synthetic neutral history through
Hermes' native session flush and requires native message IDs before the actual
model turn. These two controls still use unchanged task/reference/followup,
weights, sampler, context, tools and budgets. They run after API breadth trials.
This decision is recorded before either diagnostic model receives a request.
The history probe changes packaging relative to the first persisted control;
normal persistence relative to the old SDK-only run is reported separately.
No production runtime or native core source is patched. No further model
cohorts are planned after these bounded controls.


Before any adapted-model or API inference, apply the native-persistence
correction to those future stages too (v6 runner, normal store, auto-title off).
The currently running publisher-sampler cohort stays frozen on v5 for both
stock/GPT profiles; preserve those results. The newly researched adapter and
all API candidates now use the corrected common runtime, which is disclosed
as a scaffold difference from earlier book trials. Model-specific weights,
aliases, samplers, output cap, context and CPU offload remain exactly selected.
This supersedes carrying the old store-less SDK runtime into API testing: the
inference configuration is carried, and the caller/runtime is corrected equally
for every API candidate. No model receives private checks or solution feedback.
Idle adapter/context waiters are recreated after source updates so cached
Python imports cannot silently retain the old controller.


One conditional specialist extension, registered before any inference/download:
After the adapted cohort, independently grade actual public behavior and run
Qwen3-Coder30B A3B Instruct only if no earlier fresh run passes all nine public
book checks. A skipped/unsupported public path instead requires manual review;
it does not automatically justify another model download. This is the sole
remaining optional model file, not another series of pruned fine-tune variants.
It is a purpose-trained non-thinking coding checkpoint not covered by older
Qwen2.5 Coder failures. If triggered: public Unsloth UD-IQ3_XXS, pinned metadata
in MODEL-OPTIONS; preserve 100 GiB reserve and verify full SHA before loading.
Try 98,304 context, all GPU, then a predeclared four CPU-expert-layer fallback
only on load failure. Use native persistence/title off, same frozen book task,
ordinary/bulk pairing, README followup, 8192 output and 1200s/60 iterations per turn.
Publisher sampling .7/.8/topk20/repeat1.05, minp0, nonthinking-only model; the
publisher's much larger output recommendation is not claimed tested. Exact
SDK/store/tool/history preflight must pass before inference.

API model selection waits for this stage's completed/skipped/failed disposition.
If triggered the book selection pool grows to nine profiles/eighteen sessions;
otherwise it stays eight/sixteen. Still select up to two different weightfiles
for two fresh API sessions each, then the two fixed 35B persistence/packaging
controls. At most 24 fresh conversations in this final sequence. All older
failures remain. Booksearch is now a development-selection task; the API bug
remains unseen by every agent session until its own stage. No further model
candidates are planned after this one conditional coding specialist.

## Finalist selection amendment: preserve the ordinary-workflow lead

Recorded while the conditional coder file is still downloading, before any
coder conversation or API-task inference. Keep the two-file / four-API-session
bound; do not add another model cohort. The previous aggregate-only ordering
could discard the best normal repository agent because a front-loaded artificial
reference packet has equal weight with an ordinary request. Research on natural
context growth and the observed dense-model prefill penalty expose this scope
mismatch. Ordinary selected-checkout work is the principal intended usage.

Select as follows, using completed independently reviewed booksearch results:

1. Retain any file with a fully correct public-command fix first (at most one
   new distinct file can now qualify). Otherwise protect one slot for the
   strongest ordinary-input contribution with an actual first-turn upstream PR,
   independently passing edited/original tests, and at least one genuine added
   regression against original code with the correct behavior contract. Order
   eligible files by ordinary public defect count, then validation/honesty,
   then elapsed time. An unexecuted/broken test or wrong-contract assertion does
   not satisfy this requirement.
2. Fill the other slot with a different file using the previously recorded
   full-public-outcome / summed-ordinary-and-bulk-defects / forge / validation /
   elapsed ordering. Compare complete profiles, not a mixture of their best
   individual runs. If the protected ordinary lead already appears in the
   aggregate top two, the selection is unchanged.
3. Preserve every bulk failure, runtime-affected classification and older
   profile result. This is an explicit development-selection amendment, not a
   claim that normal input is the only real use case. API prompts and frozen
   graders remain unchanged and unseen by models; no API outcome informed it.

Currently the adapted 27B ordinary run is eligible (4/6, actual PR and meaningful
HTTP parsing regressions); its bulk failure remains 0/6 with an empty diff at
the deadline. The pending coder cohort can supersede it under the same rule.
Maximum final sequence remains 18 book + four API + two context conversations.

Selection clarification while coder bulk is still running: the ordinary lead
is protected in either case. If a newly full-correct public fix and that lead
are different files, those are the two finalists. If they are the same file,
fill the second slot by the aggregate ordering. If no full-correct file exists,
use the protected ordinary lead plus the best other aggregate file. This keeps
both the code-correctness priority and the ordinary-workflow safeguard explicit.

## One conditional longer-budget diagnostic

Recorded after adapted API run 1, before any extended-budget inference. That
run produced a patch passing all seven frozen HTTP checks, immutable original
tests, and a genuine new HTTP regression. It was inspecting its final diff at
1,195 seconds and interrupted at 1,200 before publication. This is evidence of
resource censoring, rather than a reason to reject the weight file outright.

Keep the four primary API sessions and two context controls unchanged. After
those finish, allow **at most one** additional fresh ordinary API conversation
for the adapted profile if neither primary adapted API run completed the whole
workflow and at least one correct, meaningfully tested patch was time-limited.
Use 2,400 seconds per user turn, unchanged 60 iterations, 8,192 output cap,
sampler, model, context, tools, original prompt, README followup and graders.
Supply no previous patch, grader result or correction to the model. The fixture
and scope remain fresh and other trials stay hidden. If the condition is not
met, record a skip; no extra inference is needed.

This is a post-hoc development diagnostic, not an extra primary repetition or
an isolated causal estimate: its fresh unseeded trajectory can differ. Report
its budget separately and retain every 20-minute failure. A later success would
show one completed longer-budget session, not unattended reliability. There are
no further model/configuration cohorts after this bounded diagnostic regardless
of outcome: maximum final sequence is 24 primary/control conversations plus
this one diagnostic. Finish cleanup, restoration, documentation and delivery.

Timing interpretation: each model profile's backend is loaded before its trial
controller starts. Trial elapsed includes agent/workspace preparation, copying
and independent post-checks; it excludes that backend weight load and any model
download. Agent elapsed and first-tool offsets come from the native runner.
Backend startup is retained separately in launch/properties/log artifacts.
Sessions, histories and worktrees are fresh, but the server is not restarted
between a profile's conversations: exact-prefix KV reuse can benefit later
prefill. It cannot expose a divergent prior answer, but cold/warm timing and
unseeded trajectories are not controlled speed benchmarks. Preserve measured
latencies as workload observations rather than a hardware speed multiplier.

## Post-hoc API preservation control: primary seven checks are insufficient

Review of the published second adapted API patch found an extra cleared-batch
normalization. A completed batch that already reports `Completed, Succeeded`
now reports `Completed, Aborted` after API clear. Added a separate public HTTP
positive control using the immutable original fixture: original and the first
minimal adapted patch pass; the actual second published patch fails. Apply
this same post-hoc control to every API candidate. Preserve the primary
seven-case grader and all its scores/SHA; this is additional regression evidence,
not a retroactively predeclared primary case. Models receive no feedback.

A targeted test-strength diagnostic also removes only the second patch's
reported foreign-row guard, leaving its extra cleared normalization. The edited
model suite still passes, while the primary ownership cases fail. Its added
HTTP test is red on original for a different reason (an API-cleared snapshot's
Queued state versus a newly demanded Aborted state); it does not require the
GUI-cleared foreign-row fix. Failing original source alone therefore did not
establish meaningful coverage. Keep this diagnosis distinct from copied-algorithm
simulation tests, and assess outcomes through public behavior rather than
requiring one internal implementation.


## Late native-scratch compatibility diagnostic (operator-only)

During the final extended-budget conversation, native write_file rejected
/opt/data/cache/scratch/repro.py because the frozen evaluator sets
HERMES_WRITE_SAFE_ROOT=/workspace. The native system prompt explicitly tells
the agent to write temporary probes in its scratch directory. The same
contradiction caused a denied scratch write in primary adapted API1 at 725.732
seconds. Both agents recovered by using the selected checkout; do not label
those individual denials as model inability to write a reproduction.

Keep all scored controllers, live sessions, prompts and graders unchanged.
A separate no-inference disposable-container preflight uses the same native
file/terminal tools and tests the supported colon-separated roots:
HERMES_WRITE_SAFE_ROOT=/workspace:/opt/data/cache/scratch.
Nine checks pass, including the original denial control, scratch write/patch/
execution, ordinary checkout writes, and credential/sibling/symlink denials.
No operator credential or real profile is mounted. Its source, output and
runtime file-safety hash are retained; this is not another model conversation
or a whole-workflow success. The recommended selected-project configuration
now includes the native scratch root. Actual scored write-policy restrictions
and their timing friction remain disclosed, without rescoring failed code.
