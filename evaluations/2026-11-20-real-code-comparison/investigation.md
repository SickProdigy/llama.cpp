# Real-code comparison and implicit Gitea routing — November 20, 2026

**FableVibes completed the real code-fix workflow; VibeForged did not.**
Fable's patch passed independent helper checks, but its issue/PR explanation
contains unsupported details. This supports a supervised Fable trial, not
unattended reliability or a clean whole-answer factual pass.

## Same symptom-led code task

| Model | Seconds | Visible / native calls | Result |
|---|---:|---:|---|
| Gemma 4 E4B Q5, earlier reference | 138.928 | 7 / 7 | Issue #75 and branch; two invalid edits, no commit/PR; proposed logic wrong |
| VibeForged v2 Q4 | 192.408 | 9 / 8 | Terminal attempt blocked before execution; no issue, branch, code or PR |
| FableVibes Q4 | 136.472 | 12 / 19 | Issue #76, branch, correct one-line commit, upstream PR #77, all read-backs and final URLs |

The two new runs use the same prompt and frozen guard as Gemma, except model
and fresh run/branch identifiers. No operator patch or corrective hint was
supplied. Full protocol: [protocol.md](protocol.md). Gemma remains a historical
reference, not a new run in this archive.

Fable changed only the `_bounded_int` exception tuple to include
`OverflowError`. Both infinity signs now fall back to the default; NaN,
None, invalid text, numeric text, in-range values, lower/upper clamping and
float truncation retain expected behavior. All ten isolated helper cases pass;
the baseline fails the two infinity cases. This does not validate Nicotine+
GUI/config integration or prove behavior for every possible numeric object.
The patch was inspected before the independent helper execution.

- [Model-created issue #76](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/issues/76)
- [Model-created PR #77](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/pulls/77)

PR direction, single-file diff, issue reference, file/issue/PR read-backs and
all three final URLs were independently checked. No merges, closes or
upstream-default-branch code changes were performed.

## Remaining factual mistakes

Fable's issue/PR incorrectly groups NaN with the uncaught infinity failure:
`int(NaN)` already raises the caught ValueError. It also adds an unsupported
Python 3.14+ qualification, a YAML configuration path/reproduction procedure,
and a startup-crash claim that were not established by its MCP reads. It
suggests pytest without verifying a test suite. It accurately states that its
MCP session could not run tests; it does not claim to have executed them.
Therefore code/workflow success is distinct from grounded documentation.

VibeForged stayed on Gitea for eight calls, then attempted terminal despite
the task's MCP-only constraint. That is a tool-selection failure, not evidence
that it necessarily would have written the wrong Python patch.

## Persistent routing preference

Live Hermes already has an `agent.environment_hint` directing owner's
repositories, including name-only requests, to configured Gitea MCP first,
using registered tools and never guessing a GitHub URL or changing connections.
The preference is persistent; it should not require repetition in user prompts.
No credentials or complete runtime configuration are published here.
The configured preference was left unchanged for comparison.

Separate fresh-session routing probes use the short request
`Find my SonicRatings repo and tell me what it does.` Results are recorded
separately from the explicit contribution workflow and factual answer grading.

## Short-request routing results

| Model | Seconds | First completed tool seconds | Calls | Route result |
|---|---:|---:|---:|---|
| FableVibes Q4 | 56.038 | 40.609 | 2 | Gitea search, then README; no write/alternative attempt |
| VibeForged v2 Q4 | 82.329 | 52.250 | 4 | Gitea search, README, root and source directory; no write/alternative attempt |

Both had 98,304 loaded context and peaked at 9,082 MiB, as did their code-fix
runs. Both answers summarized the retrieved README. The companion-project
GitHub link in the answers is explicitly in that README; no GitHub tool or
browser lookup occurred. Routing is scored separately from exhaustive
whole-answer factual verification. One read sample per model cannot establish
general inference reliability.

## Next direction

Prefer a supervised FableVibes Q4 plus focused-tools trial for the next real
repository task. No extra guided retry was needed to produce a working patch;
Fable succeeded on the matched symptom-led prompt. A guided workflow remains
an option if later failures show a specific need. Do not treat the current
persistent preference as a guarantee that a model will follow it, or the
focused-profile routing results as live native-profile results. No weight or
hardware change is indicated by this comparison.

## Operational state

Original runtime restoration, unchanged upstream main, archive integrity and
exact task-resource cleanup are recorded alongside the sanitized evidence.
No model download, quantization, driver/image change or everyday model/profile
switch is part of this evaluation. The optional focused plugin remains a test
profile, so focused results do not establish the deployed native interface's
reliability. Small samples do not establish a model success percentage.
