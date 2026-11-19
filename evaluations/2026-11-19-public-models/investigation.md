# Public GGUFs on the P100: actual Hermes/Gitea workflows

November 19, 2026. This is a new comparison, with fresh VibeForged and FableVibes
controls. Results from older protocols are not pooled into these counts.

## Recommended use

Ministral 3 8B Instruct Q5 is the strongest new compact candidate for bounded
contributions through the focused Gitea tools. Three fresh matched contributions
passed all resource, read-back and URL checks in 68–78 seconds, and a separate
temperature-zero contribution also passed. Only 3/6 read answers across those
matched batches passed whole-answer grounding; it is not a reliable unattended
repository reviewer. Its native-tool contribution failed. The 14B sibling also failed its separate
native contribution: it supplied the personal fork owner as the upstream
`repo_write.fork` source, and the guard stopped it before RPC, after 174 seconds.
No issue, branch, commit or PR was created in that diagnostic. Keep the existing
VibeForged everyday runtime unchanged while evaluating the optional focused
profile; no model-only replacement solved broad repository work here.

The official 14B sibling fit at 98k (12,824 MiB observed peak), but its matched
contribution skipped issue/PR read-backs, and its proposed polling cog overlapped
the existing predictions question/outcome voting, durations, results and
management. Reaction voting could be a distinct extension; the conservative
novelty failure is an explicit manual judgment, not an objective claim that a
poll-named directory already exists. It inspected only main, not those details
or develop. The concise SonicRatings explanation was correct; its Spotify
reference is corroborated by the independent README, although this run read
only metadata. These qualifications are retained with the grades.

Seven verified new files total approximately 63.5 GiB, with approximately
181 GiB free afterwards. No new model is deleted as an all-tests-fail dud:
each produced a correct core explanation or a verified contribution in at least
one profile. Original small-task models are preserved. GPT-OSS and full Qwen35B
are oversized experiments outside the approximate 8 GB file preference; they
work but did not demonstrate a broad-review advantage. See the
[retention record](model-retention.json). The 100 GiB reserve was maintained.

## What this measures

These are complete Hermes AIAgent conversations using its Discord-platform tool
selection, not a synthetic tool-call parser benchmark. The model must choose
and execute the configured Gitea MCP operations. Two ordinary read requests
precede an explicitly authorized contribution: open an upstream issue, verify
and reuse the personal fork, create a feature branch, commit one exact README
correction, open an upstream PR, read the resources back and return all URLs.
The exact prompts, tool schemas, inference requests, remote responses and
independent checks are retained in the sanitized archive.

The contribution test measures a supplied, bounded documentation change. It
does not prove autonomous bug diagnosis, implementation, test execution or
fresh-fork creation. Reusing the existing verified fork is not credited as
creating one. Off-task tools and read-only mutations are stopped before RPC;
a blocked attempt is a routing failure, even if no damage occurs.

The [protocol](protocol.md) defines the limits. Primary runs use temperature
0.2, q4 KV, one slot, output cap 4,096 and loaded context 98,304. Separate
publisher samplers, cache diagnostics, repetitions and native-tool runs remain
separate in [runs.csv](runs.csv) and [summary.json](summary.json).

## Primary results

See the [matched testing matrix](matrix.md) for file sizes, read grades, strict
contributions, latency and observed memory. Read grades include factual checks;
a completed response alone does not pass.

## Hardware and provenance

Intel i7-8700 (12 logical CPUs), approximately 62.5 GiB system RAM and NVIDIA
Tesla P100 16 GiB. Existing llama.cpp b12464-d3c3e242c and Hermes images are
reused; immutable image/configuration evidence is verified privately. The full
35B model uses CPU expert offload and a separate 600-second contribution budget.
Tests run sequentially while other home-server services remain running; timing
is an observed end-to-end measurement, not an isolated throughput benchmark.
GPU sampling is every three seconds, so reported peaks are observed samples.
Allocated context is not a claim about practical full-window performance.

Only existing publisher GGUF files are downloaded. Every new file is pinned to
a repository revision and verified against its published length and SHA256.
There is no weight training, conversion or quantization. Concatenating HTTP
byte ranges reconstructs the original published bytes. KV cache and sampling
settings are inference settings, not model weight conversion.

[Download provenance](download-plan.json) covers the initial public cohort;
the follow-up official Ministral 14B file and its verification are also retained
in the evidence archive. Willhar AgentTuned is deferred, not failed: only an
18.4 GB dense F16 file was found, with no prepared compact public quant.

## Repeated finalist and diagnostic findings

Ministral 3 8B Instruct Q5 completed three focused-tool contributions at the
matched 0.2 temperature, including all requested read-backs and URLs. Its read
quality did not repeat as cleanly: the first review checked main and develop,
but a later review checked only main and proposed event scheduling/reminders
that already exist in `calendarevents` on develop. Two metadata-only explanations
also asserted unsupported maintainer/fork-history details. The basic purpose
was still correct. The conservative whole-answer grounding grades distinguish
that from an entirely wrong repository explanation.

A separate temperature-zero run, motivated by the publisher's recommendation
and those repeated factual errors, again completed the contribution and proposed
a plausible activity cog, but repeated the unsupported maintainer attribution.
It does not demonstrate that lowering temperature solves grounding problems.
The original automatic diagnostic was skipped after clean primary completion;
the later manual diagnostic and its reason are both preserved.

With the original native multiplexed tool surface, Ministral 8B's review
attempted local files and its contribution omitted the supplied issue body,
then repeated the same invalid request. No issue was created in that run. The
MCP clone adds canonical read-only repository metadata access; its write
permissions match the configured account. This is an interface diagnostic,
not a claim of testing a byte-identical deployed server configuration.

The 8B long-context probe passed: three markers spread through an inert random
archive plus a real MCP README read were returned correctly, with 63,104 tokens
in the last inference request and no archive compression. It took 370.716
seconds at an observed peak of 10,046 MiB. The sum across two requests is
125,979 input tokens, not a 126k-token context window. This is retrieval and tool
use at about 63k input, not full-window coding validation.

The full Qwen 35B hybrid completed its grounded explanation in 168.123 seconds
and its strictly verified contribution in 154.322 seconds, peaking at 11,012
MiB. Its review timed out after fifteen model calls. Initial prompt processing
was much slower than later warm processing; the backend timings are retained.
This works, but provides no observed review advantage to justify its 22.36 GB
file and CPU offload over the compact candidates in this small sample.

Ornith's separate q8 KV review still timed out; one cache comparison cannot
establish a general cache-quality effect. Armand's publisher sampler completed
a contribution that failed under the primary sampler, while its read review
still tried terminal. Flash's alternate coding sampler completed a review but
misidentified the `coc` Clash of Clans cog as Code of Conduct, and its generated
Docker example was not grounded in the supplied configuration instructions.

## Interpretation and grading caveat

Downloaded file size did not predict total VRAM: the 6.06 GB Ministral 8B
file peaked at 10,046 MiB, while the 8.47 GB VibeForged control peaked at
9,082 MiB under the same loaded context and cache settings. Architecture, KV
layout and compute buffers matter alongside weight size. The 12.11 GB GPT-OSS
file also fit at 98k, peaking at 12,260 MiB. These are observed profiles, not
a universal memory formula.

Fine-tuning labels do not reliably predict success in this setup. Models with
and without an agent-specific fine-tune completed real contributions through
focused tools, while broad repository reviews remained fragile. Structured
required fields and distinct upstream/fork identifiers have a demonstrated
benefit; switching weights alone did not fix the native interface.

There is no controlled causal proof that model size, quantization type or
sampling caused the differences. Base models, architectures, templates and
published training differ. This cohort deliberately tests useful available
files rather than manufacturing matched local quantizations. Small samples
support a shortlist and bounded supervised use, not reliability percentages.

A correction to earlier qualitative notes: the actual SonicRatings search
metadata says `(sptnr fork)`, including in the retained November 18 capture.
`fork: false` on Gitea does not disprove imported fork ancestry. The phrase
“sptnr fork” alone must not be graded as unsupported. Attributing maintenance
to a person/account called `sptnr`, or asserting unchanged fork contents without
comparison, goes beyond that evidence. Older CSV scores have not been silently
rewritten; this clarification limits their historical qualitative labels.

All primary runs have identical focused Gitea schemas and frozen runner,
guard, profile-preparation and plugin source hashes. Hermes exposes an
additional mode/patch option in its unrelated local patch schema for GPT-OSS;
the complete schemas are retained and this difference is disclosed rather than
claiming byte-identical full tool surfaces. Local patch was forbidden throughout.

## Audit trail

- [Per-run metrics and grades](runs.csv), [grouped phases](summary.json), and
  [independent remote verification](verification.json).
- [Manual read grades](manual-grades.json) retain reasons and interpretation.
- [Evidence archive](evidence.tar.gz), [member hashes](evidence-manifest.json)
  and [archive SHA256](evidence.tar.gz.sha256) retain prompts, schemas, requests,
  responses, launch flags, GPU samples, runner sources and selected provenance.
- Credentials, private profiles, Docker environment/inspection dumps, unrelated
  repository metadata and email addresses are excluded or redacted. Full
  third-party model cards are not republished.

Idle controller handoffs were interrupted only while waiting for downloads,
then resumed. No scored conversation was stopped by an operator to improve a
result; guard stops and preset time limits remain failures.

The runs created 14 upstream test issues and 13 upstream PRs, all left open
for inspection; nothing is merged or closed.
The upstream default branch was independently verified unchanged. All 48
recorded task runs are retained: 27 primary tasks across nine files, plus 21
separately labeled repetitions/diagnostics, including the long probe. The normal
Hermes profile, MCP allowlist, model and service configurations were restored
and independently checked after cleanup; the focused plugin remains optional,
not deployed live. Disposable containers, their anonymous home volumes, the
evidence volume and private credential snapshots were removed. See the
[restoration checks](final-restoration.json) and [cleanup record](cleanup.json).
