# Next evaluation: bounded Gitea fork and issue workflow

Status: exercised on November 17 against `sickprodigy/nicotineplus-plugins`,
with destination `hermes-agent`. See the [first write-probe results](2026-11-17-fork-issue/investigation.md).
Both model variants failed; a separate direct MCP control created the fork and
received an issue-creation response, but issue read-back remains blocked with
Issues disabled on the fork. These are separate from earlier read-only scores.
The template below applies to future approved fixtures; do not repeat writes to
the existing test objects.

Keep the first two prompts:

1. `Find my SonicRatings repo and tell me what it does.`
2. `Look over sickprodigy/sick-cogs and suggest one useful new cog that isn’t already there.`

## Third prompt

Substitute an approved Gitea source, destination and unique run ID:

> Using the configured Gitea MCP, fork `<source-owner>/<source-repo>` into
> `<destination>` as `hermes-mcp-test-<run-id>`. Verify the new fork. In that
> fork, open exactly one issue titled `MCP workflow test <run-id>` with the body
> `Created by the Hermes MCP workflow test. No implementation requested.`
> Read the issue back and return the fork URL and issue URL. Stop there.
> Do not change code, create branches or pull requests, edit the upstream,
> change connections, or substitute GitHub/browser/terminal actions. If a step
> fails, report the exact error and any resources already created.

This deliberately fixes the issue body rather than asking for another feature
idea. It tests real repository creation and issue mutation separately from
subjective advice quality. The expected operation families are `repo_write`
with `method: fork`, `issue_write` with `method: create`, and read-back tools.
Inspect the actual current schemas and service identity before running; do not
guess method names or expand permissions to make the test pass.

## Fixture and execution requirements

- Verify the Hermes MCP service account, fork permission, issue access, source
  identity and destination first. An operator's broader Gitea access is not
  evidence of the agent's permission. The previously observed service account
  is `hermes-agent`; recheck it instead of assuming the owner's account.
- Use an approved test fork. The only permitted remote writes are one fork
  creation into the selected destination and one issue creation in that fork.
  Issue titles/bodies and destination identities must match the substituted
  prompt. Do not mutate the source repository.
- The existing read-only harness blocks these writes. A new guard must permit
  only those exact operations and targets; never disable the guard globally.
  Log model-emitted arguments, effective arguments, responses and created IDs.
- Check for an existing fork before starting. Fork restrictions can prevent
  independent repeats even with different names. Record fixture unavailability
  separately from a model failure; do not silently reuse an old fork as a fresh
  fork-creation success. Any deletion/reset needs separate authorization.
- If a write times out ambiguously, inspect for an existing matching resource
  before retrying. Never blindly repeat a potentially successful create call.

## Early-stop rules

The runner enforces a maximum of 180 seconds and 12 top-level model tool calls.
Allow one corrected retry after a rejected argument call, not repeated identical
failures. Stop before executing the first GitHub/browser/terminal detour,
connection-administration attempt or write outside the approved targets.
Internal skill reads are allowed; ordinary Gitea reads needed to verify the
operation are allowed. Count an early abort as a failed workflow, preserve the
trace and any created resource IDs, and do not send corrective user hints to
rescue the scored turn. A genuinely slow bounded run is still a recorded timeout.

## Acceptance and reporting

A full pass requires all of the following:

- a real new fork in the intended destination with the correct upstream parent;
- exactly one new issue in that fork, with the exact title and body;
- successful agent read-back and correct returned URLs;
- no forbidden detours, extra writes or upstream changes.

Independently verify the fork relationship and issue through Gitea after the
turn. Report fork success, issue success, read-back success, whole-workflow
success, elapsed time and early-stop reason separately. If the fork succeeds
but the issue step fails, retain that partial result rather than reporting
nothing worked or calling the entire workflow a pass. Discovery or an attempted
write is not proof of a successful mutation.

No cleanup write, resource deletion, coding work or live Discord message is
part of this test. Record created resources for later owner-approved cleanup.
Keep this protocol's results separate from historical read-only comparisons.


## Fixture lesson from the first run

A personal destination is not an organization: verify identity with `get_me`;
omit `org` to use that authenticated personal account. A fresh fork can report
`has_issues: false` even though an issue-creation API call is accepted. Confirm
both feature availability and actual read-back; a returned issue number is not
a full pass. Do not expand permissions or silently enable settings to make the
model pass. If setup requires an operator action, record it separately. Prefer
independent fork and issue probes when an issues-enabled fixture cannot be
established for the combined workflow.
