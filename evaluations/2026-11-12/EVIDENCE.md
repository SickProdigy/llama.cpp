# Evidence layout

`runs.csv` records each fresh session and each three-turn history sequence.
`aggregate.json` contains fresh-session counts. Qualitative grades are manual;
`fixture-cog-catalog.json` records the exact develop inventory used to check
novelty, and `grading-evidence.json` contains targeted supporting excerpts.

`evidence.tar.gz` contains sanitized evidence with SHA-256 hashes listed in
`evidence-manifest.json`:

- `runs/<candidate>-L<level>-R<repeat>/request-*.json`: actual OpenAI-compatible
  bodies sent by Hermes, including assembled system prompt, schemas, tool
  messages and auxiliary compression requests. No authorization headers were
  captured. The first request shows the initial visible tool surface.
- `calls.json`: actual underlying dispatch, arguments, result, elapsed time,
  and whether a prohibited external mutation was blocked.
- `result.json`: complete model answers and conversation messages when the
  run returned; timeouts may lack this file. `summary.json`, `timeout.json`,
  `agent.log` and captured requests retain partial-run evidence.
- `discovery.json`, `selection.json`, `surface.json`, `props.json`: registered
  MCP tools, selected toolsets, agent schemas and backend properties.
- `harness/`: evaluator scripts, controller logs, historical log excerpt,
  manual grades and version/image metadata. `gpu/`: five-second GPU samples.

Scored model comparisons use the full shipped `AIAgent` conversation loop.
They are not direct backend tool-call tests. Calibration attempts are excluded.
A history sequence is one three-turn conversation, not three fresh repeats.
The random seed is inherited; nine runs do not establish a population success
rate or statistical significance. Timings include different tool workflows and
warm prompt caches, so they are not isolated model-speed measurements.

The scripts are an operational record for this workspace, with absolute paths,
original-container dependencies and a private local profile prerequisite. They
are not a portable one-command benchmark. To rerun, take a new private profile
snapshot and inspections, freeze new fixture refs, pin image IDs, and recheck
tool schema/guard behavior before scoring. Never reuse exported redacted values
as credentials. Do not blindly rerun controller scripts against a live stack.

Private profile archives, raw Docker inspections, auth stores and credential
values are deliberately excluded. Known deployed secrets and bearer values
are redacted from exported text. Endpoints and fixture identities are retained.
No training, remote issue writes, commits or pushes were performed.

File-read counters use actual dispatch arguments: `readable_file_reads` means
`with_lines: true`; `bounded_file_reads` additionally specifies a positive finite end line at or beyond the start.
They count attempts, including failed reads. Administration mutation counts
come from dispatched connection actions; guessed unknown names rejected before
dispatch remain visible in captured requests. Error counts deduplicate retained
tool results by call ID, so replayed history does not inflate counts. Full
failure text and fallback order are retained in the request/result evidence.
History CSV token deltas subtract the preceding cumulative Hermes counters.

Token fields are Hermes-reported main-loop counters. Auxiliary generation and
unfinished streamed requests may not be included; their requests, compression
telemetry and available backend timing logs are retained separately.
