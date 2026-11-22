# Everyday Hermes pilot on the P100 — November 22, 2026

**The Hermes-adapted 27B remains a supervised candidate, not a qualified everyday
autonomous replacement. No full workflow passed in this pilot.** It can produce
useful local fixes and real Gitea contributions, but authored tests and successful
publication repeatedly miss behavior or documentation errors. Keep the existing
VibeForged production default unchanged.

This study validates the previously selected candidate on three additional bug
families. It does not rank every retained model. See the [six-workflow matrix](matrix.md),
[18-turn measurements](measurements.md), [review findings](review-findings.md),
[full protocol](protocol.md), and [public replay commands](REPLAY.md).

## Candidate and conditions

See the [exact prompts](task-prompts.json) and [candidate manifest](candidate.json).

The file is `netprojects/Qwen3.8-27B-hermes-adapted-GGUF` revision
`6a786a26437f9210d5da0954208c7335ee0a55e1`,
`Qwen3.8-27B-hermes-IQ3_XXS.gguf`,11,637,692,064 bytes, SHA256
`390a54c26ed8fc42a558f073e5745b7c0c1922086bbcc07e2e6357a7b527c345`.
This exceeds the earlier approximate8GB file preference but fits this tested
16,384 MiB P100: observed resident use is13,094 MiB with 98,304 context, q4_0 K/V,
one slot and full GPU offload. This does not establish million-token operation.

Actual native requests use temperature 0.8, top_p 1, top_k 0, min_p 0,
repeat_penalty 1, presence_penalty 0, thinking disabled and an 8,192 output cap.
The same candidate's stateless critic uses 4,096. All 317 recorded in-turn request
bodies match those settings. Backend CLI defaults are not the effective request
sampler. Exact manifests, image/source hashes and request-setting checks are in
the archive. The backend is b12464-d3c3e242c; the native test image adds
Python 3.14.9 and pytest 9.1.1. The Hermes core Git commit is unavailable; no commit
identity is invented.

Each arm uses its own persistent native Hermes profile, retaining normal SOUL,
skills, memory loading, hooks and policies. Production environment/auth, MCP
tokens and old sessions are excluded. The pilot enables the memory tool while
retaining memory/skill write approval; this differs from production's disabled
memory-tool setting. Two actual skill-content reads occur in each initial
workflow, twelve total. No explicit memory-tool invocation occurs. A mock-driven
native preflight verifies persistence/resume, staged memory writes and scratch
execution; it is not a scored demonstration of autonomous memory writing.

The actor runs as UID 1000 with a read-only root filesystem, writable isolated
profile and real selected Git checkout at `/workspace`. Native scratch is
allowed at `/workspace:/opt/data/cache/scratch`. The source is committed
Nicotine+ plugins HEAD `84afaf401b29753b6810e4f92f253e0d28637dbf`,
tree `60e59671ae0973188ae90ac46f7cfec1c06bfd8f`; five pending owner files are excluded
and preserved. These are server-local Debian files also exported to Windows.
No actual Nicotine+ application, music library or Arr service is used.

Configured repository facts, authenticated identity and focused Gitea tools
supply ownership inference. Frozen requests ask for an upstream issue,
personal-fork fix and upstream PR without naming GitHub as an alternative.
Scoped disposable arenas prevent unrelated writes. This measures inference
within that configured tool surface, not spontaneous issue creation or an
unconstrained choice among hosting services.

## Tasks and independent results

There are six fresh native logical sessions: Beets queued import, Announcer
comma-containing room names and Arr redirect credentials, in unassisted and
prepublication-review arms. Each receives an initial symptom-led bug task,
README followup and dependent feature request. Followups resume native state;
profiles persist within each arm. Private graders, reference fixes, future
requests and operator findings never reach actor or critic.

Original source reproduces all three bugs. The reference corrections pass all 16
frozen final checks, all 20 supplemental HTTP redirect scenarios and the 83
original tests plus two subtests. Model source, immutable original tests, edited
model tests, actual published trees and documentation are assessed separately.
Posthoc controls are labeled rather than retroactively changing frozen scores.

**Beets:** both arms improve direct disable/shutdown behavior and add meaningful
regressions. An old waiting worker can still run after disable/reload. Both final
local drafts pass4/5 checks; their README lifecycle guarantee is too broad.
The review draft handles an additional deferred-worker cancellation race better,
but no delivered critic feedback explains that difference. The unassisted arm
publishes its initial fix and README, not its feature; the review arm publishes
no code.

**Announcer:** both final local drafts pass6/6 frozen checks. The unassisted arm
publishes all three commits with correctly directed issue/PR, but its helper
collapses internal spaces in valid literal room names. Its status command also
changes empty defaults from `none` to blank. New nested tests pass separately,
while default root pytest discovery fails because of duplicate test-module names.
The review arm has a locally passing patch and truthful local-only final answer,
but no remote code or PR. A supplemental None-input robustness change lies
outside normal GUI string input and is not treated as a proven normal-GUI bug.

**Arr:** the unassisted patch blocks foreign-origin credentials but rejects valid
relative same-origin Location values and breaks legitimate chains. Its final
local draft passes3/5 checks; the actual published older branch passes2/5 because
its new setting never reaches Gitea. The README's50-hop urllib default is false:
this Python inherits `max_redirections=10` and `max_repeats=4`. Loops can stop earlier.

The review patch passes5/5 frozen checks and all 20 HTTP scenarios, but direct
HTTPS and HTTPS redirects differ: direct GET works; redirects raise uncaught
AttributeError because a field is initialized only in http_request, not HTTPS
processing. Original/reference code preserve legitimate same-origin TLS
redirects. Its README incorrectly describes certificate changes as an origin
predicate check. The final feature setting is documented correctly for its HTTP
behavior, but the contribution remains unpublished.

Both Arr patches change network mock seams. Immutable-original failures at those
seams alone do not prove broken production routing. The final review actor
actually runs13 module tests:2 fail and 11 pass. It then fixes one fake function;
the independent final root run has1 failure,88 passes and two subtests. No final
answer or successful rerun is invented. API-preserving counterfactuals show
meaningful foreign-key assertions, while one opt-out test can be fooled by a
flag-ignoring implementation whose generic loop error contains the expected
words. Constructor errors on original code are not relevant regression proof.

## Context and automatic review

Native archive-mode compression occurs in both Arr features. The unassisted
checkpoint takes 563.085 backend seconds and the next main request360.289;
recorded main input falls from 82,103 to 37,741 tokens. The review checkpoint takes
539.221 seconds and the next main request359.802; input falls from 82,104 to 36,359.
Those costs already belong to native turn budgets.

All three frozen requests are admitted unchanged and in order in each logical
workflow. The unassisted child retains all three verbatim; the review child
retains initial and feature requests, with the README query only in its archived
parent. The initial raw-retention audit reports that loss and is preserved.
Final admission proof is separate from the still-false complete raw-history
retention flag. Lineage, a generated summary or resumed tools do not certify
summary fidelity or general memory reliability.

A generic source-verified native user-role continuation also follows one
length-truncated Beets answer. It is disclosed separately from human requests.
The earlier profile's declared compression threshold must not be assumed to be
the live native gateway threshold; the source observation and actual checkpoint
requests are retained.

The critic sees already-issued tasks, the exact pending mutation, adjacent
source and visible tool receipts. It has no tools or private grader/reference.
All 15 real reviews exceed the 240-second caller deadline; no semantic decision
reaches the actor. Of their late outputs, six meet the strict JSON schema, seven
do not, and two are unknown/incomplete. One late README-only packaging concern
is grounded; other findings include soft suggestions and false assertions about
redirect chains or already-removed test cleanup. Known lifecycle, documentation
and HTTPS errors are missed. Timeout blocking is not defect detection.

Caller waits total3,601.513 seconds. Observed critic backend time totals
6,584.063 seconds, a lower bound with one timing record missing. Two critic API
usage records are missing; one response has only an 8,192-byte prefix, with
separate server timing and no recovered final decision. An offline recorder
proposal passes four mocked regressions; it was not deployed during the pilot.

Initial tool-enabled model-request latency is 111.025–139.351 seconds; the first
persisted native tool receipt appears 136.744–173.973 seconds after turn startup.
These are not times to a correct Gitea write.

Native turn wall times sum 10,643.649 seconds unassisted and 17,705.737 seconds with
review. These single stochastic task pairs do not estimate causal review cost
or equal actor compute. Main, auxiliary and review work share one P100 slot and
the same turn budget. Do not add backend seconds to wall time. Largest recorded
input is82,104 tokens, not a certified peak for incomplete requests. Token sums
include repeated/cached prompts and are lower bounds where usage is missing.
GPU use is sampled; initial adoption and failed-controller buffering leave gaps.
CPU/RAM/energy were not continuously measured.

## Preservation, evidence and limitations

Authenticated final clones confirm published heads/trees and zero-commit personal
branches, correct upstream/personal direction and unchanged upstream mains.
Three test issues are closed. Three actual PRs remain open and unmerged in the
disposable arenas. No PR is merged and the owner's selected checkout is untouched.

Original Hermes and llama.cpp container identities, images, configuration and
mounts are restored. The original VibeForged alias and 98,304 context report healthy.
Separate Hermes-Codex has the same identity, configuration, start time and restart
count. Four checked original profile files and all five pending owner-file hashes
match. All 29 retained model files have unchanged recorded names/sizes/mtimes;
124.21 GiB remained free at final preservation, above the 100 GiB reserve. No model
was downloaded, deleted or locally quantized. Scoring containers and recorded task helpers are removed, along with the
helpers' attached anonymous volumes and empty private network; private evidence remains.

Startup/adoption faults, console attachment loss, proxy lease recovery and native
session-ID rotation required operator recovery. Frozen tasks, grader/reference,
model and sampler remain unchanged; no corrective task replay occurs. These are
not clean unattended trials. See the protocol for all recovery boundaries and
for late review completion reconciled from later immutable snapshots.

The [sanitized archive](evidence.tar.gz) and [SHA256](evidence.sha256) retain source,
checks, exact mutation proposals, curated receipts, provenance hashes and costs.
Private profiles, owner instructions/skills, complete system/HTTP transcripts,
SQLite data and credentials are excluded. Public behavior replay is possible;
byte-identical private-profile inference is not. The archive itself is checked
with all seven documented commands in [replay validation](replay-validation.json).
[Artifact/privacy verification](artifact-validation.json) checks 2,205 manifest
entries and the complete public package against supplied known private values;
[public verifier](verify_evidence.py) supports credential-free structural checks.
The exporter scan recovery and a nonsecret public-username exclusion are disclosed
in the protocol. See [source notice](SOURCE-NOTICE.md).

This small pilot does not establish unattended reliability, real Nicotine+
acceptance, memory-write effectiveness, exhaustive TLS/URL safety, or performance
on another GPU. Faster hardware could reduce measured latency; this study does
not show it repairs logical or documentation errors. Keep the 27B file for bounded
supervised work. A later review experiment could test smaller evidence packets,
a faster/separate critic and a deadline matched to measured prefill, under a new
protocol; none is claimed as a verified fix here.
