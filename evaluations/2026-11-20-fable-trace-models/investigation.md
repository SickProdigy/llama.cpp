# Fable-trace model comparison — November 20, 2026

**None of the three new candidates displaced FableVibes for this MCP workflow.**
Qwable and Qwopus selected Gitea for an ordinary request but chose the agent's
fork, then attempted local file search during the code task. Parable could not
meet the current context configuration. Keep FableVibes plus focused tools as
a supervised trial candidate; the deployed everyday runtime remains unchanged.

Three public Q5 GGUFs were downloaded and SHA256-verified. Six conversations
were scored: routing and code fix for a fresh Fable control, Qwable and Qwopus.
Parable has a separate runtime/context exclusion, not two invented model failures.
No weights were trained, converted or quantized locally.

## Results

| Model | Public file GB | Loaded context | Peak GPU MiB | Ordinary request | Real code workflow |
|---|---:|---:|---:|---|---|
| FableVibes Q4 control | 8.47 | 98,304 | 9,082 active | Gitea, correct owner; 90.155 s | Correct patch, issue #78 / PR #79, all read-backs/URLs; 207.736 s; repository-assisted |
| Qwable 9B Q5 | 6.47 | 98,304 | 7,368 active | Gitea, agent fork selected; 75.976 s | Local search_files blocked; 171.282 s; no writes |
| Parable Qwen3 8B Q5 | 5.85 | 40,960 observed | 9,868 loaded idle | Not run at required context | Context exclusion; no inference/task launched |
| Qwopus Fable 4B Q5 | 3.16 | 98,304 | 4,742 active | Gitea, agent fork selected; 52.576 s | Local search_files blocked; 42.763 s; no writes |

Times are recorded agent conversation time, excluding model loading. Model
order, cache reuse, request sizes and different work performed limit speed
comparisons. A quickly stopped failure is not fast task completion. Actual
first-completed-tool times and per-run details are in [runs.csv](runs.csv).
Loaded context is not proof of full-window coding; no new long-input trial was
performed in this cohort.

The original symptom-led prompt and guard are unchanged except run/model/branch
identifiers. Read first, then full task; temperature .2, 4096 output, q4 K/V,
one slot. Sources, tool schemas and actual sampler fields matched in all six
requests. Full budgets and caveats: [protocol.md](protocol.md).

## Fable control: working patch, assisted diagnosis, inaccurate prose

Fable changed only `_bounded_int`'s exception tuple to include `OverflowError`.
Independent tests after patch inspection pass all ten cases: both infinity
signs, NaN, None, invalid strings, numeric strings, in-range values, lower/upper
clamping and float truncation. The baseline fails the two infinity cases.
These isolated helper tests do not establish live Nicotine+ config/GUI behavior.

It created [issue #78](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/issues/78)
and [upstream PR #79](https://gitea.rcs1.top/sickprodigy/nicotineplus-plugins/pulls/79).
The issue is now closed; the PR is unchanged. Fork parent, PR head/base,
single-file diff, issue reference, correct read-backs and final URLs were
independently checked. Upstream main did not change.

Fable listed all issues and read prior issue #76 before its edit. That prior
issue contains the answer, so this is **repository-assisted workflow success**,
not an independent repeat of its earlier diagnosis. It copied the earlier
issue's erroneous NaN failure claim and unsupported Python-version, YAML-path
and startup-crash details. It accurately states that its MCP session did not
execute tests. Code/resource success must not be presented as fully grounded
issue/PR prose or a general coding reliability percentage.

## Qwable and Qwopus: remote-source navigation failed

Qwable read source through line 180, then tried searching `/opt/hermes` for
`def _bounded_int`. Qwopus read the first default source range, then tried
searching `/opt/hermes` for `_bounded_int`. Neither read the helper near line
256 or reached an edit. The guard blocked local search before execution.
Neither created an issue, branch, commit or PR. These are tool-selection/source
navigation failures, not evidence of an incorrect proposed Python fix.
Neither code run read the prior test issue containing the answer.

Their ordinary requests used Gitea search, a directory read and README read,
so host routing worked. Both selected `hermes-agent/SonicRatings` instead of
`sickprodigy/SonicRatings`; distinguish route selection from finding the right
owner. Core purpose summaries were supported by the README, but that does not
repair target selection or establish exhaustive factual accuracy of all detail.
Qwopus's companion GitHub link was in the README, not a GitHub tool detour.

## Parable: context compatibility, not reasoning

The pinned GGUF declares Qwen3 architecture and 40,960 context, matching the
source config's 40,960 positions with no declared scaling. The stock backend
accepted the launch but exposed only 40,960 in `/props`, despite requesting
98,304. The readiness check therefore timed out and excluded it before any
Hermes inference. GPU use was a loaded idle measurement, not an active peak.
No OOM, architecture rejection or demonstrated reasoning failure occurred.
A separate shorter-context/scaling investigation would change the conditions;
this run does not establish that such a configuration would or would not work.

## What this means for the next step

Training on coding traces alone did not predict MCP discipline. Both new
scored models drifted toward local search after a partial remote read. That
suggests remote-source navigation and tool availability are useful next
configuration targets; these few observations do not prove a training-data
cause. More GPU capacity or a different quant would not directly repair the
observed tool choice.

Keep the persistent Gitea preference; do not require the user to repeat it.
A future profile trial should explicitly distinguish `sickprodigy` as the
owner's namespace from `hermes-agent` as automation, and test that on ordinary
requests. No such profile change was slipped into this matched comparison.
Focused results do not establish the live native interface's reliability.

## Retention and restoration

After saving sanitized evidence, removed only this cohort's new Qwable and
Parable GGUFs, rechecking their publisher SHA256 before removal. Qwable offered
no improvement here; Parable misses this stack's context requirement. This is
a local retention decision, not a universal model-quality judgment. Preserve
the small Qwopus file as a possible reading/helper backup, not an agent default.
Its 4,742 MiB P100 result does not establish 2070/5080 performance.

Removed 12.32 GB (11.47 GiB); existing models were untouched. About 147.2 GiB
remains free, above the 100 GiB reserve. Provenance and reasons are retained in
[model-retention.json](model-retention.json).

The only new issue (#78) was closed after its pre-close body/state was saved.
No comments, PR closures or merges were added. Original images, command,
environment, mounts and Hermes config bytes were verified unchanged; VibeForged
at 98,304 context is restored, Hermes-Codex untouched. Exact temporary-resource
cleanup and evidence integrity are recorded in cleanup.json and the manifest.
