# Everyday Hermes pilot — protocol and disclosed deviations

Status: completed. The original protocol was frozen before candidate inference. Task, grader, reference and harness hashes are recorded in frozen-protocol.json; final results and sanitized evidence accompany this protocol. Dated recovery and supplemental-audit sections disclose deviations and limitations.

The candidate is the pinned Qwen3.8-27B Hermes-adapted IQ3_XXS artifact in [the supervised candidate manifest](../2026-11-21-goal-investigation/supervised-candidate.json). The target is the P100 16 GiB, 98,304-token context and the same effective request sampler/output cap. No model download or quantization is needed for this pilot.

## What changes from the previous study

Use the installed native `hermes chat --cli --oneshot` path and its gateway, SQLite persistence and resumed session IDs. Do not construct `AIAgent` directly. Mount a real isolated Git checkout at `/workspace`, with selected-project discovery and configured Gitea upstream/personal-fork ownership. Allow native scratch writes through `/workspace:/opt/data/cache/scratch`.

Clone the normal profile into isolated per-arm storage. Preserve normal memory/skill approval policies and record every deliberate configuration difference. Current production enables memory loading but disables the memory tool through `agent.disabled_toolsets`; the isolated pilot explicitly removes memory from that disabled-toolset list and adds it to the CLI toolsets. Memory and skill write approval remain enabled: native memory changes may be staged rather than saved. Do not quietly describe unchanged disabled tools as working memory. Keep background memory/skill learning distinct from the experimental prepublication reviewer.

## Workloads and isolation

Three fresh bug families, each with an initial contribution and two dependent user followups. One followup checks documentation; another extends related behavior. Prompts are identical across arms and frozen before inference. Followups use the same native session and its naturally accumulated context; no synthetic context padding or corrective hints based on private graders.

Use separate upstream/fork arenas and persistent profiles for unassisted and automatic-review arms. Start each family in a fresh session. Within an arm, normal memory may persist across families; cross-arm patches, histories, memories and forge references must remain inaccessible. Main-agent mounts exclude private graders, reference implementations, future prompts and Docker access.

The owner's selected source checkout contains pending edits. The benchmark starts from an isolated committed snapshot at `84afaf401b29753b6810e4f92f253e0d28637dbf`; owner pending files are hashed and preserved. This is experimental isolation, not a claim to include those pending changes.

## Independent grading

Before inference, reproduce each bug locally with fake data and validate independent positive preservation controls and a reference correction. Grade the submitted code, relevant regression tests against the original defect, existing behavior, documentation truth, actual test-execution evidence, issue placement upstream, personal-fork commits and PR contents. Read back published blobs and commit IDs; do not accept a conversational completion claim as publication evidence. Keep local-only, partial and failed outcomes visible.

Automatic review gets only the task already given, the actual proposed changes, visible repository context and available execution evidence. It receives no private grader or reference patch. Intercept publication to prevent unreviewed commits/PR updates; verify enforcement, stale-change handling and timeout behavior before scored runs. Record reviewer findings, revisions, false positives and unresolved findings separately from independent scores.

## Costs and limits

Record main and auxiliary request counts, input/output tokens, wall time, GPU peak, context growth and compression events. Attribute automatic review requests and delay separately. Review adds compute and may use the workflow's run budget; disclose that confound. A three-family pilot cannot establish unattended reliability or a statistical success rate. If natural history never triggers compression, it does not validate long-session compaction.

## Operational completion

Keep useful models and at least 100 GiB free on the model filesystem. Preserve credentials, owner-managed settings and the separate Hermes-Codex stack. Use only disposable forge arenas; close test issues after evidence capture, restore the original runtime and verify its configuration and health. Publish sanitized, reproducible evidence and limitations, then commit and push the authorized evaluation work.

## Frozen execution plan

Run Beets/plain, Beets/review, Announcer/review, Announcer/plain, Arr/plain, Arr/review. Each workflow receives three identical-across-arm prompts: initial bug contribution, dependent README followup, and a related feature followup. Followups resume the exact native session; each bug begins in a fresh session. Native configuration is 60 iterations and a 1,800-second run budget per turn, with a 2,100-second external guard. The run budget is not treated as a guaranteed wall-clock cutoff; actual elapsed time is recorded. Followups retain the session's original creation policy.

The reviewer uses the same pinned candidate in a separate stateless request, without tools, with up to 4,096 output tokens and 240 seconds per call, at most four calls per turn. It gates commits and PR prose; initial issue creation is not reviewed. Its input is current task history, original/proposed source, exact forge payload and persisted model-visible tool receipts. It has no private grader or future prompts. The review delay consumes main native run time. This is an extra-compute intervention, not an equal-compute comparison.

Both private disposable arenas have the identical original committed source tree 60e59671ae0973188ae90ac46f7cfec1c06bfd8f. The operator granted Hermes collaborator access only in those arenas because connector allowlists do not expose collaborator/settings management. Agents receive no forge credentials and can reach forge operations only through a scoped MCP proxy. Forks and issues must be created by the tested model's tools. Branch prefixes prevent test collisions and are supplied as neutral repository configuration.

Each agent mounts only its arm's persistent profile and current authenticated Git clone. Clones include the owner's locally excluded repository AGENTS instructions, also locally excluded in the test checkout. Profiles clone normal configuration, SOUL, skills, memories, plugins and hooks; production environment/auth/session stores are not copied. Messaging platforms, dashboard and telemetry are disabled; local model/MCP endpoints, iteration budget, selected checkout, compression threshold and contribution plugins are configured in isolation.

Independent preflight evidence: all 16 behavior checks pass private reference corrections; original source fails defect/new-feature checks. Both original and corrected trees pass all 83 existing tests plus two subtests. Native cloned-profile smoke testing confirms effective sampler, selected Git facts, skill reading, scratch execution, memory approval staging, SQLite persistence and history after container restart. These are mock-model infrastructure checks, not candidate task successes.

## Infrastructure incidents retained separately

Two startup attempts are retained outside scored results. The first recorder ran as root with all capabilities dropped and could not write a UID-1000-owned record mount; no model request reached the backend. During cleanup, an archival attempt failed on parent-directory permissions and sockets; that subsequent startup was interrupted before inference. Both original runtimes were restored and configuration signatures checked before fresh profiles were created. Recorders now run as UID 1000 and pass an actual write preflight.

In the active cohort, the first two toy reviewer probes raced the proxy listener and got connection-refused errors. Those are unavailable reviewer measurements, not incorrect model decisions. The third, a correct code/documentation control, returned approval. Any later replay must be labeled diagnostic and must not be used to conceal these errors.

A chat interruption later ended the host-side controller while the first scored native CLI and gateway continued running inside Docker. A detached Docker supervisor adopted the exact existing Docker exec ID, native session and original elapsed-time budget without resubmitting the task or restarting inference. The frozen task, grader and model configuration remain unchanged. The first turn's buffered GPU samples were lost with the host process; sparse earlier observations and durable samples after adoption remain. Report the sampling gap rather than claiming a fully observed peak. Model HTTP request/response evidence continues in the independent recorder.

The test backend image's default Docker healthcheck probes port 8080 although this server runs on 11430. Its unhealthy label is therefore not a model failure: the configured 11430 health endpoint returns HTTP 200 and inference is active. Final production restoration requires checking the original configured endpoint and container health separately.

After the unassisted three-turn Beets workflow finished, the first review-arm bootstrap failed before agent creation: the detached root controller had created the proxy record directory as UID 0, while the proxy runs as UID 1000. Startup checks caught the write failure. The original runtime was restored and configuration signatures matched. That bootstrap is an infrastructure exclusion, not a model trial.

The continuation retains the completed unassisted workflow and executes the remaining five frozen cases. Its only per-case provisioning change is to give the proxy record directory UID 1000 before startup. A generated source file and hash record that change. Model requests, tasks, graders, reference corrections, review policy and budgets remain unchanged. Recorder restarts use a separate directory, preserving all earlier raw requests and responses.

Once the recorder listener was ready, the same three toy reviewer fixtures were rerun separately: the reviewer rejected the deliberately wrong code and documentation and approved the correct control. Earlier connection failures remain archived; these toy results do not count as real workflow successes. Interrupted requests with no final usage record are included explicitly, and their aggregate token totals are lower bounds.

The first review-arm bug turn reached the external guard with no published commit, issue or PR. The next native followup was refused because Hermes had fenced the interrupted admission as unknown. The controller's query-to-session lookup returned no accepted message and mislabeled that refusal as a lost session. This is a recovery limitation of the workflow and harness, not evidence of a different session or a completed followup. The rejected console attempt is retained separately.

The second continuation keeps the completed first review turn and its exact session, checkout and profile. It calls the native `hermes sessions discard <session> --yes` management command before resumed followups, records the response, then submits each unchanged frozen task. On the first restart Hermes reported no unknown admission remaining; SQLite confirms the dependent README query was subsequently accepted in the original session. The native command acknowledges interrupted work without replaying it. No source correction, private test result or reviewer hint is given to the actor. Any such recovery is operator assistance and excludes an unattended-success interpretation. Newly started bug families remain fresh sessions; model settings, grader, prompts and reviewer policy remain frozen.

A further restart limitation was found during the resumed review README turn: the scoped MCP server originally kept its branch lease only in memory. The restarted server rejected one commit with “Create the feature branch first” and hid the existing feature branch from a listing. These are infrastructure effects, not model ownership errors. The operator stopped the proxy, retained and merged the first-turn and followup call records, and restored the exact previously captured lease. Authenticated readback as `hermes-agent` confirmed that the branch existed at the untouched initial base; no code had been published. The recovery variant also restores previous review-attempt counts and approved keys and fails closed if a future restart would need committed-state reconstruction. New cases with empty record directories retain their original behavior. The frozen original harness files are preserved separately; actual runtime variant hashes and the intervention are disclosed. No private test findings or corrective source hints were sent to either model. The resumed turn is consequently an assisted recovery observation, not a clean unattended trial.

The resumed review README turn reached the external guard. Before the next feature prompt, native `sessions discard` acknowledged the interrupted admission. The exact feature query was admitted in the same session, but the conversation transcript initially remained unchanged while an earlier turn lease was still recorded. A new lease was acquired 271.815 seconds after followup startup, 0.546 seconds after the old lease expired; subsequent inspection found the third user message. No force unlock, resubmission or extra time was used. The user-message timestamp was backdated to request creation and is not proof of transcript insertion time. Record observed insertion bounds and lease timing separately from token-generation time. This recovery overhead consumes the frozen external budget and limits an equal-time model-quality comparison.

Before either Arr workflow began, the operator froze a separate supplemental HTTP coverage check: 301/302/303/307/308 across same-origin authentication, cross-port redirects, protocol-relative cross-port redirects and same-origin-to-cross-origin chains. These 20 fake/local scenarios are outside the primary 16 checks; primary tasks, graders, references and model settings remain unchanged. The original code preserves all five same-origin scenarios but leaks the fake key in the 15 cross-origin scenarios; the reference passes all 20. Controls were also repeated in a read-only, network-isolated child container with only the checkout and two grader modules, no profile or Docker socket. The observer will evaluate both local and actually published Arr snapshots with these checks; results are supplemental, never task feedback, and must not be quietly substituted for the primary score. They do not test real Arr deployments, TLS downgrade or every URL-normalization edge case.

## Reviewer transport and evidence limitations

The prepublication reviewer uses the same local candidate in a separate stateless
request. Its caller deadline is 240 seconds; a cold prompt of roughly 40,000
tokens can take longer than that just to process on this P100. The recorder may
therefore observe a late decision after the gate has already rejected publication
on timeout. Late findings are assessed descriptively and never counted as
delivered feedback or a cause of subsequent actor corrections. Timeout blocking
alone is not successful defect detection. The settings remain fixed throughout
the paired pilot.

One late nonstreaming review response was captured only through its first 8,192
bytes. The recorder forwarded each chunk immediately and stopped reading when
writing to the disconnected caller raised BrokenPipeError. The partial outer
JSON cannot establish a complete decision or API usage. Separate server timing
and token counters are retained with their own provenance; they do not fill in
missing API usage. Published token sums remain lower bounds where usage is
missing. A manually reviewed partial critic prefix is an explicit exception to
the exclusion of raw HTTP transcripts; full actor requests and system prompts
remain private.

An offline proposal under `next-run-recorder/` buffers a complete nonstreaming
upstream body before attempting downstream headers or writes. Four mocked
transport tests cover connected delivery, large-response body and header
disconnects, and unchanged streaming cancellation behavior. The original
recorder fails the disconnect regressions; the proposal passes all four. This
proposal was not deployed during the pilot, makes no model calls in its tests,
does not recover the missing response tail, and does not solve reviewer latency.

The final forge audit independently reads back every existing contribution
branch, including branches recorded as having zero commits. It also discovers
all actor-authored issues and PRs in both disposable upstreams and reconciles
them against captured workflow references. Harness state alone is insufficient
evidence that no publication occurred.

## Supplemental test-discovery audit

The original regression-relevance helper searched top-level `tests/` only. An
unassisted patch added tests beneath `announcer/tests/`, exposing that coverage
gap. The original results remain, annotated with their scope; a separate paired
audit runs nested model tests against candidate and original code while retaining
the nested test files. A default repository-root pytest audit also checks test
integration in both local and actually published snapshots. Identical source
fingerprints can reuse one result. Original and reference root-discovery controls
pass. These operator checks are supplemental to the frozen 16 behavior checks;
they were not provided to the actor or critic and did not alter their tasks.
Passing selected test directories separately is not a passing combined suite.

## Native continuation messages

A strict audit of persisted user-role rows found one extra row in the
unassisted Beets feature turn. It exactly matches the pinned Hermes runtime's
generic output-limit continuation message. The preceding assistant row has
`finish_reason=length`; the provider recorded 8,192 output tokens, and the
continuation was persisted about 0.00026 seconds later. Source inspection
confirmed the constant and the native truncation handler that appends it.
This was native recovery, not an operator correction or private-grader hint.

The session audit retains the initial strict-check failure and separately
reports these native control rows. It still requires the exact frozen task
sequence, distinct sessions across workflows, and the same session for dependent
followups. Only the source-verified exact continuation, following an assistant
length truncation, receives that classification; arbitrary system-prefixed or
unmatched user rows are not ignored. The raw transcript therefore contains more
than the three human task messages in that workflow. Native continuation is
part of the tested stack and does not establish successful task completion.

The earlier candidate manifest's numeric compression trigger is not a live
measurement of this native pilot. The configured fraction is 0.85 and recorded
native requests have an 8,192-token output allowance, but the pinned gateway
helper omits the constructor `max_tokens` field used by the built-in compressor
for output reservation. A pure source-level kwargs probe records this distinction
without instrumenting or changing the actor. The source-derived trigger can
therefore differ from a calculation that reserves the request's output allowance.
No successful compression or retention result is inferred from the configured
fraction, request size, or absence of persisted compaction flags. This diagnostic
is separate from scored model behavior.

## Native archive-mode compression and final-case continuation

During the unassisted Arr feature, native Hermes made a source-verified streaming
checkpoint request (22,455 input / 3,272 output tokens; 563.085 backend seconds),
then created an explicit child session with the parent ending for compression.
The next main request used 37,741 prompt tokens versus 82,103 before compaction;
its uncached prefill/generation took another 360.289 seconds. All three exact
frozen human queries remain in the child, and tool execution continued. The
summary contains historical prefix facts that are stale relative to its retained
tail. This is evidence of actual compression and continuation, with limited
retention observations, rather than proof of general memory reliability.

The original 2,100-second external guard still stopped the CLI (durable exact
exec event: exit137; reconstructed elapsed2,117.287 seconds). The controller's
literal session-ID assertion then prevented its normal capture. An operator
recovered the immutable child snapshot, tool receipts and authenticated fork
readback without replaying the task or changing inference. Its final feature
was local only. Early GPU samples buffered in the failed controller were lost;
the late observer's limited samples do not replace full-turn coverage. An initial
host-Python grading pass is retained separately; final grading uses pinned native
Python 3.14.9.

Only the remaining fresh review-assisted Arr workflow uses continuation3. It
accepts a changed session ID solely along explicit native oneshot parent/child
compression ancestry, tested against unrelated/reverse/cyclic/foreign-source
cases. Frozen Gate code and policy remain unchanged; exact-current-query receipt
lookup tracks child sessions. Prior fifteen turns are retained. Frozen tasks,
private graders/reference, model, sampler, budgets and profile policy are
unchanged. No task replay, corrective hints or private grader material reaches
either model. See native-compression-audit.json and the recovery provenance.

## Posthoc HTTPS preservation and regression discrimination

After the review-assisted initial and README snapshots, an additional isolated
loopback TLS fixture checks direct GET, absolute and relative same-origin
redirects, and cross-origin redirects. It uses an ephemeral self-signed fake
certificate inside the audit container's temporary filesystem. Only this
network-isolated fixture trusts that certificate; candidate and production TLS
settings are untouched. The generated private key is deleted and not exported.
This is a supplemental preservation audit, separate from the frozen primary
checks and the twenty HTTP scenarios frozen before both Arr workflows.

The original and reference code preserve legitimate same-origin HTTPS redirects.
The review patch's direct HTTPS GET works, but redirects raise an uncaught
AttributeError: its http_request callback initializes a field that HTTPS requests
do not receive. Both early review snapshots pass the HTTP fixtures despite this
gap. The unassisted patch preserves absolute same-origin TLS redirects but still
rejects relative Location values. Final-feature source is audited separately.

API-preserving counterfactual tests additionally ignore only the unassisted
allow_redirects flag, and disable only the review patch's origin predicate while
retaining incidental error wording. Actual tests pass; mutants fail at the
missing refusal and leaked-key assertions respectively. This distinguishes
meaningful behavioral coverage from failure due solely to a missing constructor
argument, changed mock seam, or incidental error string. None of these findings
is supplied to actor or critic.

## Late gate completion across turn boundaries

A review call may start within a native turn but finish its 240-second caller
wait after that turn's immutable snapshot. The final audit reconciles review
records by their global filename across later completed snapshots and attributes
them to their recorded original phase. It does not alter earlier snapshots or
count duplicate copies as extra attempts. Backend metrics are still attributed
by request arrival, with missing capture explicitly unknown. Candidate audits
use the cumulative captured calls to identify the exact original mutation.

## Final child-session retention audit

The review Arr feature also triggered native archive-mode compression: the
checkpoint used 27,594 input/2,551 output tokens and 539.221 backend seconds; the
next main request used 36,359 input tokens and 359.802 seconds. Its incoming
source session retains all three exact frozen human queries in order. The child
retains initial and feature queries verbatim, but not the README followup.
Do not claim all three original messages remained verbatim after compression.

The initial final validator required every current child to retain the complete
raw task prefix and correctly reported this loss. That failing artifact is
preserved. The final audit separately proves exact admissions in the incoming
native source session, explicit source-verified compression ancestry, and that
current raw user rows are an ordered frozen subset including the current query.
It still reports false for complete current raw-history retention. Arbitrary
extra user input, reordered or altered admission tasks, and unrelated session
changes remain failures. This operator audit refinement does not change tasks,
models, graders, reference, or any model result; all six full workflows fail.
Summary fidelity is not certified from lineage or message counts.

A trusted post-run audit launcher initially lacked DAC_OVERRIDE while reading
its UID 1000-owned private bind. Its failed launch was retained privately; the
trusted administrative launcher was corrected and audits reran in the pinned
image. Actor isolation and scored inference permissions were unchanged.

## Final archive verification

The original export completed archive creation but reread gzip members for
every credential variant during its final scan. The operator stopped that
redundant scan and verified the same archive bytes using one read per member,
the same URL/base64/JSON-escape variant construction, gzip integrity, member
hashes and structural privacy exclusions. All seven documented behavior replay
commands match the final archive SHA. The archived original exporter remains
unchanged; the efficient public verification helper is shipped alongside it.

The broad environment-name collector also classified a dashboard username as a
secret because its key contains AUTH. That value is already a public repository
owner in historical README URLs and is absent from the private secret seed set.
It is excluded from the secret-value set, without changing credentials or those
URLs. Passwords/tokens and the private seed set remain checked. The archive's
earlier conservative redactions are retained. See artifact-validation.json for
counts and limitations; no private credential values are published.
