# Hermes forge routing investigation — November 12, 2026

## Scope and method

This evaluates the shipped Hermes Agent conversation loop, tool discovery, tool
execution, compression, and final answers against the configured Gitea MCP.
It does not infer Hermes success from direct llama.cpp function-call probes.
`hermes-codex` is outside scope. No commits, pushes, or remote repository writes are
part of this comparison. Original containers and configuration are retained
for restoration.

Every scored fresh session runs in a new Docker container using the deployed
Hermes image ID. Each starts from the same private snapshot of configuration,
SOUL, skills, empty memory directory, plugin configuration, and cache. Session
DBs and conversation history are absent. Background skill review is disabled
to prevent between-run self-modification; normal memory loading and context
files remain enabled. The original live Hermes service is stopped during model
comparisons. Local terminal and code execution are available inside disposable
containers. The evaluation dispatcher records and blocks connection mutations
and remote forge writes; it does not remove their advertised schemas from the
baseline. A blocked attempt remains an attempted action in the score. This
limits what can be inferred about recovery after an administration attempt.

The core `AIAgent` runs use Hermes's CLI platform tool selection, including its
automatically merged configured MCP server. These are complete model/tool
conversation runs, not Discord delivery tests. Current Discord selection also
includes Gitea but adds platform capabilities such as TTS/vision. Successful
CLI runs alone do not establish historical gateway-session exposure parity.

VibeForged sampling is inherited from its model defaults: temperature 1.0,
top-k 20, top-p approximately 0.95, min-p approximately 0.05, random seed.
Qwen3.5-9B is a separate model/configuration candidate with its native
temperature 0.8 and top-k 40; its other listed sampler settings match. The
first Qwen preflight stopped before inference because the cross-model sampler
parity check detected this difference; that attempt is excluded. Subsequent
Qwen runs check against their own frozen sampler reference. Thus Q4/Q6 are
the matched quantization comparison (with the model-identity caveat below); Qwen-versus-VibeForged is not a sampling-isolated
architecture comparison. The actual
Hermes requests, including any extra sampling fields, are recorded. Q4 and Q6
use 98,304 context, q4_0 K/V cache, one slot, all GPU layers, and a 4,096 token
Hermes output cap. Prompt cache can persist in the model server across runs;
cache-read usage is recorded, and these timings are not cold-start benchmarks.
Temporary backends inherit the image healthcheck for port 8080 while serving
11430, so their Docker health label is not used as readiness evidence;
readiness/model/context are checked on the actual 11430 `/props` endpoint.
The restored original container retains its Compose healthcheck.

## Scoring definitions

Routing compliance requires a successful configured Gitea repository operation
and no GitHub connection/search/URL attempt during the scored turn. GitHub
attempts remain a failure even if the model later recovers. Tool calls that
read a `.github` directory **through Gitea** are not GitHub attempts.

Task quality is scored independently: **Pass** means the requested response is
complete, grounded, has the requested number of ideas, and has no known
material factual or novelty defect. **Partial** means the core answer is
useful but has a material defect; **Fail** covers incorrect/ungrounded or
incomplete outcomes. Hermes's own `completed: true` is not sufficient for a
pass. Material defects change the project purpose/workflow, a proposal's
feasibility rationale, or its claimed novelty. Peripheral category slips are
noted but do not automatically invalidate an otherwise grounded primary idea.
Elapsed time, excessive reads, repeated errors, and spill/compression
behavior are also reported rather than hidden inside a completion flag.

The external turn limit is 600 seconds, checked every five seconds, without a
model-visible wrap-up instruction. Observed timeout duration can exceed the
limit by that polling/grace interval. Initialization/container wall time is
logged separately from turn elapsed time. One readable-stage startup was
interrupted by a watchdog race before Python import completed, before any
request/result directory existed; it is excluded. The watchdog was corrected
to require a running container and a turn-start marker newer than container
startup. Previously scored timeouts have valid turn markers at about 600s. All completed early Q4 runs were
under the limit, so the added external watchdog did not change them.

## Fixtures and fixed prompts

Fixture verification is separate from scored sessions and uses real MCP reads.
`sickprodigy/sptnr` redirects to `sickprodigy/SonicRatings`. Searching `sptnr`
returns the old `CopyBot/sptnr` mirror rather than the owner's renamed project.
The Level 1 fixture was therefore changed once to SonicRatings. Preliminary
old-name runs and harness calibration runs are excluded from scored results.
The remaining prompts retain the user's wording. Each candidate receives the
same three prompts three times, with no manual corrections or tool hints:

1. `Find my SonicRatings repo and tell me what it does.`
2. `Look over sickprodigy/sick-cogs and suggest one useful new cog that isn’t already there.`
3. `Review sickprodigy/sick-cogs and suggest five useful new cogs that aren’t already there. Explain why each would fit.`

Gitea search confirms the owner's SonicRatings repository and the Sick-Cogs
repository. Both fixture search results currently report `private: false`;
this tests the default forge choice for the owner's Gitea repositories, not
private-repository authorization. Sick-Cogs is case insensitive through the
API. Its `main` root has 40 entries at
`762f67b86b137a77a1965bba6f3688665ed92537`; `develop` has 57 entries at
`4c63518a09f2610db201fcb8a16ed72a65d50c9d`. The SonicRatings README blob is
`e25e51f9d2ac93ffe2638abbb23ba052bc0633c1`. Gitea's configured method allowlist
rejects `repo_read(method="get")`, while direct file/tree/search reads work.
A failed aggregate method is not proof that the repository is missing.

## Historical evidence, distinct from new measurements

The cited log uses UTC timestamps. The initial explicit Gitea request occurred
November 10 at 9:25 p.m. EST (November 11, 02:25 UTC), in session
`20261111_021723_ab09bf63`. The sequence is recoverable from `agent.log.1` and
read-only queries of the existing Hermes session DB:

- Earlier conversation began with a public web-research request at 02:17 UTC.
- At 02:25:29, the Gitea request started with **63 history messages**. Its log
  reports only **16 visible / 2 deferred** tools.
- At 02:25:31, the first model action was
  `manage_connections({"action":"connect","connectors":["github"]})`.
  The response said `github` was not a hosted connector slug.
- The model requested connection status, tried installing the nonexistent
  `litegraph` MCP, and used hosted/MCP action variants incorrectly.
- At 02:25:53 it requested `authorize` for `mcp-gitea-hermes`. That path removed
  cached OAuth tokens. The server immediately answered MCP requests with
  HTTP 200/202; the administration result said the server responded but no
  OAuth token was obtained. The configured server uses `GITEA_ACCESS_TOKEN`,
  supplied on the MCP server side, rather than requiring a Hermes OAuth flow.
- At 02:25:58 the actual `tool_search` result had `total_available: 2`, no
  matches for `git search repos`, and only browser/terminal sources. Gitea
  was absent from this session's discovery inventory despite earlier startup
  logs registering 25 MCP tools. At 02:28:03 a guessed connector wildcard was
  also unavailable. Thus tool exposure/scope or the cached session inventory
  contributed; registration is not equivalent to per-turn availability.
- Enabling the existing MCP was reported connected at 02:27:59 and again
  later, but the model continued trying OAuth, guessed tool names, terminal,
  and code execution. The 30-call turn ended without the requested issue.
- Later user requests to remove GitHub/GitLab led to further install/connect/
  authorize attempts rather than removing that route. The whole recorded
  session has 170 tool calls, including 44 connection-administration calls,
  and no valid Gitea repository-tool invocation.

This sequence does **not** demonstrate that OAuth token cleanup broke Gitea
authentication. New fixture reads through the same configured MCP succeed.
It does demonstrate routing drift, wrong administration semantics, missing
Gitea in historical per-session discovery, and substantial prior history.
The exact historical wire payload was not retained, so the underlying cause
of that historical inventory discrepancy is not established by the log alone.

## Current prompt and tool exposure

The deployed Hermes image identifies itself as 0.23.1, commit
`3b421578588243f920886e6fe79a6faa87ea026e`, built November 10. llama.cpp reports
`b12282-aa75ff323`; the configured Gitea MCP server is 1.13.0. Current fresh CLI selection exposes 14 core tools and
27 deferred tools (25 Gitea tools plus two other deferred capabilities).
`manage_connections` is a directly visible schema; Gitea tools are behind
`tool_search` / `tool_describe` / `tool_call`, with names listed in the bridge
catalog. Disabling GitHub skills does not remove connection administration or
GitHub web/terminal routes.

A concrete guidance conflict exists: `agent.environment_hint` and the
`gitea-workflow` skill name legacy `mcp_gitea_search_repos` / `mcp_gitea_*`
tools. The deployed registry instead names these
`mcp__mcp_gitea_hermes__search_repos` / `mcp__mcp_gitea_hermes__*`.
Preliminary request evidence includes a call to the legacy name, an explicit
"not a known tool name" error, then discovery or GitHub fallback. Other
preliminary runs chose GitHub before that error, so this mismatch is a real
contributor, not a complete explanation of every routing failure.

For the captured first Q4/Q6 comparison requests, tool schemas are byte-for-
byte identical and the system prompt differs only in its model identity line.
The request `model` field also changes with the active alias. The chat template
and sampler properties are checked against the Q4 reference before each
subsequent run. The visible model identity accounts for a small prompt-token
count difference; this is not a blinded model-identity experiment.

The assembled CLI prompt also contains the automatic coding posture: it calls
the agent a coding partner inside the user's codebase and recommends terminal
inspection. Source `agent/coding_context.py` confirms that `auto` applies only
to interactive coding surfaces in a detected code workspace; messaging
platforms do not receive this brief. This is competing guidance in the CLI
comparison, not proof of a cause in the historical Discord turn. A messaging/
gateway validation must therefore be distinguished from these CLI results.

## Compression request budget finding

In the new Q6 Level 1 repetition 1, captured main requests specify
`max_tokens: 4096`, but the compression request does not specify an output cap.
The unchanged server command still has `--n-predict 512`. Hermes logged
`summary_truncated_failure` and discarded the summary, with an estimated
76,322 context tokens against a 70,656 effective threshold. This is a separate
runtime budget issue; the model weights still fit GPU memory. It does not
explain the earlier fresh Q4 GitHub attempts, which also occurred without
compression. The Qwen 98,304 history run later reproduced this failure at about 71k
estimated tokens; its backend log likewise records a 512-token summary
generation. Changing the compression/backend default budget must be evaluated
as a separate factor after the weight comparison.

## New scored results

These are new ordinary-language tests, distinct from the historical guided
issue-write probes in the README. Every row contains three fresh repetitions
of each of the three fixed prompts. A combined pass requires both correct
configured-forge routing and a materially correct answer.

| Candidate | Gitea used | GitHub attempted | Routing pass | Content pass | Both pass | Median turn |
|---|---:|---:|---:|---:|---:|---:|
| VibeForged v2 Q4_K_M · 98,304 | 2/9 | 8/9 | 1/9 | 1/9 | 0/9 | 194.7s |
| VibeForged v2 Q6_K · 98,304 | 6/9 | 4/9 | 5/9 | 1/9 | 0/9 | 326.6s |
| Qwen3.5-9B Q8 · 65,536 | 7/9 | 3/9 | 6/9 | 4/9 | 3/9 | 91.5s |
| Qwen3.5-9B Q8 · 98,304 | 5/9 | 4/9 | 5/9 | 3/9 | 3/9 | 127.9s |
| Qwen 9B · 65,536 · connections removed | 5/9 | 4/9 | 5/9 | 1/9 | 0/9 | 116.3s |
| Previous + direct tool schemas | 9/9 | 1/9 | 8/9 | 0/9 | 0/9 | 150.3s |
| Previous + readable bounded file guidance | 9/9 | 0/9 | 9/9 | 1/9 | 1/9 | 75.8s |

Content partial/fail grades, timeouts, first tools, tool errors, exact idea
counts/grounding notes, token counters and GPU samples are in `runs.csv` and
the evidence archive. Q4 and Q6 each have one content pass, three partials and
five failures; Q6 additionally has two wall-clock timeouts. Qwen 65k has four
content passes, three partials and two failures; Qwen 98k has three passes,
four partials and two failures. None of the four baseline candidates passed
a five-idea review completely. Some correct answers used GitHub and therefore
fail routing. Conversely, successful Gitea reads frequently preceded inaccurate
or incomplete answers.

The small repeated sample supports the operational finding that Q6 did not
solve this workload; it does not establish a statistically significant
quantization effect. Qwen 65k is the strongest baseline here, but three combined
passes in nine is inadequate for a reliable default agent. Increasing its
context did not improve the combined pass count and increased median elapsed
time. Native Qwen sampling differs from VibeForged as documented above.

### Runtime and memory

All tested models loaded successfully on the P100, with nested
`chat_template_caps.supports_tools`, `supports_tool_calls` and
`supports_object_arguments` true. No CUDA OOM was observed. Sampled peak GPU
memory was 9,084 MiB (Q4), 11,684 MiB (Q6), 9,474 MiB (Qwen 65k), and
9,922 MiB (Qwen 98k). Idle observations were 9,028, 11,630, 9,350 and 9,798
MiB respectively. Five-second samples can miss transient peaks.

Median first API-call latencies were 3.8s (Q4), 5.5s (Q6), 3.3s
(Qwen 65k) and 3.7s (Qwen 98k), across nine fresh runs each.
The CSV records first API-call latency separately from full-turn elapsed time.
These first calls often reuse backend prompt cache; they are not cold model
load or time-to-first-token measurements. Server `--n-predict 512` remained
unchanged throughout this matrix; main requests explicitly used 4,096.

### Evidence pointers

See [evidence layout](EVIDENCE.md), [per-run metrics and grades](runs.csv),
[history turn metrics](history-turns.csv), [aggregate counts](aggregate.json),
and [sanitized requests, logs and harness](evidence.tar.gz). Archive paths
below are relative to its root:

- `runs/q4-baseline-L1-R3/request-001.json`: stale Gitea tool identifier.
- `runs/q6-baseline-L1-R1/request-001.json`: matched main request and tool
  exposure; compare Q4's first request to see model identity as the only
  system-prompt difference.
- `runs/q6-baseline-L1-R1/request-009.json`: auxiliary summary request without
  `max_tokens`; `agent.log` records aborted truncated summaries and
  `harness/q6-backend.log` records 512-token generations.
- `runs/q6-baseline-L1-R2/`: repeated base64 decode failures and timeout.
- `runs/qwen9-common98-L3-R3/`: completed-looking answer that duplicates
  gitforge, tickets and calendarevents.
- `harness/historical-log-excerpt.txt`: original log lines around 28,403,
  including the administration/authentication sequence; this is historical,
  not part of the new score matrix.

The novelty catalog comes from local Git objects at the exact Gitea-verified
`develop` SHA, not a stale local main ref. Red core overlap is checked against
its [official Audio guide](https://docs.discord.red/en/stable/cog_guides/audio.html).
Its [official Trivia guide](https://docs.discord.red/en/stable/cog_guides/trivia.html)
also verifies custom question lists, categories, timed answers and leaderboards.
The Q4 answer claiming OpenWeather needs no API key conflicts with the
[official current-weather API](https://openweathermap.org/api/current), which
requires `appid`. Targeted excerpts are retained in `grading-evidence.json`.

## Diagnosed mechanisms and proposed repair boundaries

The evidence supports several distinct mechanisms, rather than one confirmed
root cause:

1. **Tool selection:** fresh sessions can discover Gitea but still choose public
   GitHub routes. Connection administration is an eager tool, and disabling
   GitHub skills does not disable it or general web access. Historical discovery
   additionally lacked Gitea entirely; the precise session-specific reason is
   not recoverable from the retained logs.
2. **Missing scope rule:** the current hint prioritizes MCP for configured
   *private* services and describes explicitly named Gitea searches, while the
   verified fixtures are public and ordinary prompts omit the forge. A concise
   default for the owner's repositories would fill a demonstrated gap; repeated
   generic “use tools” instructions would not.
3. **Stale tool identifiers:** environment/skill examples reference a namespace
   absent from the actual tool registry. Correcting those examples is a bounded
   repair, but cannot explain runs that choose GitHub before any name error.
4. **Read representation:** `get_file_contents` defaults to base64. Repeated
   copying/decoding errors and synthesis from incompletely decoded content are
   visible in the traces. In the direct-schema five-idea repetition 2,
   `agent.message_sanitization` logs an unrepairable `execute_code` call
   containing a copied base64 README, then substitutes empty arguments.
   Copying large encoded text consumes the main output budget as well as
   adding decoding work. `with_lines: true` provides readable text. This is an
   existing tool argument, not a newly invented configuration option.
5. **Context management:** omitted auxiliary output budgets inherit 512 tokens
   from the server. Q6 backend logs show exact 512-token generations for failed
   summaries. More context/precision does not repair this output-budget path.
6. **Repository reasoning:** plausible ideas are justified with invented cog
   behavior, or duplicate features on `develop`/Red core after main-only reads.
   Routing fixes alone cannot establish answer correctness. The existing
   `sick-cogs-conventions` skill already instructs checking both stable and
   develop, real `info.json` layout, exact idea counts and no review-time
   writes. Several failed runs loaded that skill. These failures are not
   evidence that another repetition of those rules is missing.

The MCP allowlist also advertises a generic repository-read method that the
configured server rejects. Search, directory and file reads still work, so this
is a method/permission-surface inconsistency rather than demonstrated broken
credentials. Preserve the access token and review the allowlist separately.

The offered `web_extract` tool also repeatedly returns that SearXNG is a
search-only backend; the original configuration has no separate extraction
backend selected. These fallback errors are recorded, not attributed to weight
quantization. Retaining web search does not require pretending URL extraction
is operational. No external extraction provider or new credential was added.

## Training decision

Do not train from these runs yet. First repair and validate tool exposure,
namespace/default-forge scope and the compression budget separately. The
remaining model-quality target is concrete: choose the configured forge from
ordinary owner/repo language; use valid bounded reads; ground descriptions in
returned text; compare candidate ideas against active branches and Red core;
and preserve requested counts after history/compression.

If those failures persist after runtime fixes, curate reviewed complete
Hermes trajectories rather than isolated function-call examples. Include
ordinary public/private owner-repo lookups, renamed repositories, missing-file
recovery, readable file arguments, disabled administration, branch-specific
novelty checks, unrelated web-research tasks, and history/compression cases.
Label wrong-forge attempts and fabricated inventory claims as failures even
when the final answer looks plausible. Hold out repository identities and
prompt paraphrase families; score fresh runs and history sequences separately
with the same routing/content split. Do not reuse this small repeated ladder
as both training data and the sole acceptance test.

## Configuration experiments and recommendation

Across all scored runs, the eight observed `manage_connections` calls are
status reads: no connection mutation or remote repository-write attempt was
dispatched. Historical connect/install/authorize activity is separate evidence.
Fresh GitHub attempts use web, browser, terminal or code routes instead.

The configuration chain uses Qwen3.5-9B Q8 at 65,536 with the same native
sampler and output caps. Each step changes one factor relative to the preceding
step and repeats all nine fresh cases plus a separate three-turn sequence:

1. Remove `connections` from `platform_toolsets.cli`. The captured request has
   16 schemas instead of 17; Gitea remains deferred, and web search remains.
   This prevents advertised connection administration, but four of nine fresh
   runs still attempt GitHub through other tools. It is containment, not a
   sufficient default-forge policy.
2. Set `tools.tool_search.enabled: 'off'` while retaining step 1. The request
   has 40 direct schemas, including all 25 Gitea tools, no bridge and no
   connection administration. All nine use Gitea, eight avoid GitHub, but
   none is a complete content pass. Successful discovery/dispatch is distinct
   from understanding the returned repository content.
3. Retain steps 1–2 and append one specific environment-hint sentence asking
   for `with_lines: true` and bounded `start_line`/`end_line` excerpts. This
   fills the demonstrated representation gap; it does not repeat the existing
   branch/count/no-write rules. Its presence is verified in the actual system
   prompt. It is an instruction-adherence experiment, not forced UTF-8 output.

In step 3, 5 of 21 file-read attempts use `with_lines: true`,
and 0 specify a positive finite end-line bound. The actual arguments
matter: ignored guidance leaves base64 decoding in place, and readable mode
without bounds can still produce large spilled results. In particular, the
second five-idea run again emits unrepairable copied-base64 code arguments.
The tested hint does not establish a deterministic readable-output default.
A server/client adapter that changes defaults would be new code, not a
supported YAML setting verified by this investigation.

No candidate qualifies as a reliable ordinary-repository agent on this ladder.
Do not switch to Q6 as a routing repair. Qwen 65k is the strongest baseline
candidate for further validation, but its three combined passes in nine are
insufficient for automatic adoption. Direct Gitea schemas are the clearest
observed routing improvement; they do not establish factual or novelty quality.
These small, sequential, stochastic samples are not a full factorial experiment
or proof that either configuration change causes a population-level rate change.

Before further model tuning, correct the obsolete tool examples, replace the
private-only/explicit-Gitea scope ambiguity with a concise default for the
owner's repositories (public and private), align advertised MCP methods with
the server allowlist, and give auxiliary compression requests an explicit
adequate output budget. These are identified repairs, **not isolated successful
fixes measured here**. A larger backend default budget is a possible summary
workaround; it was deliberately not changed in this matrix. Preserve web search
for unrelated research and configure a real extraction backend only if needed.

Connection removal was tested for CLI selection. Discord/API use their own
platform tool selections; removing CLI administration alone does not configure
those surfaces. Validate the selected allowlists and schemas through the native
gateway before making a production reliability claim. No native gateway/API
conversation validation or new issue-write test was performed.

## Separate history sequences

One sequence per row uses the same three prompts in order without manual hints.
The GitHub columns show explicit tool attempts per turn, not links quoted in an
answer. Reusing prior authoritative Gitea content is not by itself routing drift.

| Sequence | Turn seconds | Completed flags | GitHub attempts per turn |
|---|---|---|---|
| q4-history | 61.6 / 121.7 / 115.1 | True / True / True | 2 / 1 / 0 |
| q6-history | 319.3 / 77.5 / 18.3 | True / False / False | 0 / 0 / 0 |
| qwen9-history | 57.0 / 228.8 / 330.3 | True / True / True | 0 / 8 / 4 |
| qwen9-history98 | 131.8 / 519.2 / 255.5 | True / False / True | 0 / 3 / 4 |
| qwen9-no-connections-eager-history | 59.9 / 114.5 / 54.9 | True / True / True | 0 / 0 / 0 |
| qwen9-no-connections-history | 199.4 / 132.2 / 81.6 | True / True / True | 0 / 0 / 0 |
| qwen9-readable-history | 91.4 / 146.4 / 288.4 | True / True / True | 0 / 0 / 0 |

Q4 already uses GitHub in its first turn. Q6 stays on Gitea but later turns fail
context/compression. Both baseline Qwen sequences start on Gitea and use GitHub
later; fresh review prompts also use GitHub, so history alone is not established
as the cause. Qwen 98k reaches the 30-tool limit on turn 2 and later confuses
SonicRatings' rating-sync purpose with the Sick-Cogs Navidrome cog.

The no-connections and direct-schema sequences avoid GitHub throughout, while
content quality varies. The direct-schema sequence has useful later Search and
five-domain proposals; its first lookup still invents a playlist condition.
These positive history outcomes do not erase the failed fresh repetitions.
The readable-guidance sequence starts with an accurate lookup, then invents
TikTok/Clanker inventory and duplicates calendars while incorrectly applying a
Subsonic pattern to YouTube. Repeated decoding and malformed arguments persist.
See manual per-turn notes and full answers in the evidence. No successful summary compression occurred
in these scored baseline sequences; truncated attempts are retained separately.

Core-overlap checks use official [Audio](https://docs.discord.red/en/stable/cog_guides/audio.html),
[Trivia](https://docs.discord.red/en/stable/cog_guides/trivia.html),
[Filter](https://docs.discord.red/en/latest/cog_guides/filter.html), and
[ModLog/Core](https://docs.discord.red/en/stable/cog_guides/core.html) references.
A proposed Fortnite player-stat integration also lacked a validated provider
contract: Epic's [public Data API](https://dev.epicgames.com/documentation/fortnite/using-fortnite-data-api-in-fortnite?lang=en-US)
documents aggregate island metrics, not personal player information. A concept
can be novel while its asserted API mechanism still needs correction.

## Restoration and retained evidence

The original Q4 container/configuration is restored, including 98,304 context,
q4 K/V, one slot, 4,096 main output cap and the original backend default of 512.
`restoration.json` records unchanged container IDs/images, commands, environment,
mounts, published ports, and hash comparisons for original configuration/credential/skill
files, plus backend properties and health. `restored-mcp.json` records an
authenticated read as the expected Gitea principal and unchanged fixture refs.
The native gateway process is checked separately from the core evaluator.

Only README/evaluation documentation and sanitized evidence are retained.
Private snapshots and temporary evaluation resources are removed after export
verification. Original credentials/endpoints are preserved. No remote issue
writes, training, commits or pushes were performed; hermes-codex is untouched.
