# Bounded evaluation: upstream issue, fork fix and upstream PR

Executed November 18 against the approved fixture. See the
[three-model comparison](2026-11-18-contribution/investigation.md): no final full
pass; native same-account control succeeded. The original runtime was restored.
The [November 17 results](2026-11-17-fork-issue/investigation.md)
remain historical: the direct control created its issue in a fork, and neither
model attempt passed. Preserve those resources and grades.

Keep the first two prompts unchanged:

1. `Find my SonicRatings repo and tell me what it does.`
2. `Look over sickprodigy/sick-cogs and suggest one useful new cog that isn’t already there.`

## Third prompt

Before running, select one independently verified small README correction and
substitute exact text below. Use the same task instructions across models.
When reusing one upstream, use equivalent distinct one-line corrections to avoid
duplicate contributions, and record those differences. An identical-correction
comparison requires isolated fixtures or an explicitly approved reset.

> Using only the configured Gitea MCP, contribute this documentation fix to
> `sickprodigy/nicotineplus-plugins`: in `<path>`, replace `<old-text>` with
> `<new-text>`. First open exactly one issue in that upstream repository titled
> `MCP contribution test <run-id>`, explaining the correction. Fork into your
> `hermes-agent` personal account, or verify and use your existing fork. Create
> branch `mcp-test-<run-id>` in your fork and commit only that correction there.
> Open exactly one PR from that branch to the upstream default branch, with
> `Refs #<upstream-issue-number>` in its description. Read back the issue,
> changed file and PR, and return their URLs. Leave the PR open for review.
> Do not commit directly to upstream, merge or close anything, change repository
> settings or connections, or use GitHub/browser/terminal alternatives. If a
> step fails, report the error and resources already created, then stop.

The issue and PR belong to upstream; the branch and commit belong to the fork.
Fork Issues need not be enabled. Test repository selection as well as arguments.

The concrete run manifest fixes issue and PR titles/bodies for traceability.
Corrections are deliberately small documentation edits; success proves bounded
MCP operations, not arbitrary code-repair ability. No model-created fresh fork
was scored when an existing fork was reused.

## Fixture and guard requirements

- Verify the actual Hermes MCP identity and schemas, upstream Issues/PR access,
  and fork branch/file permissions. Missing permissions are fixture blockers;
  never broaden permissions during a scored run.
- Check existing issues, PRs and forks first. Avoid duplicate contributions.
  Record fork reuse separately: it cannot earn a new-fork creation pass.
  Repeated comparisons require distinct approved fixtures or a documented reset;
  do not silently reuse a completed correction as a fresh equivalent test.
- Record upstream default branch and commit SHA, and verify the fork parent and
  base content before running.
- Prepare a run manifest with exact repositories, issue title/body, fork name,
  branch, file path, permitted replacement and PR title/base/head/body template.
  Adapt the guard before execution: the old fork/issue guard is insufficient.
- Permit only one upstream issue, optional fork creation, one branch and one
  file commit in the fork, and one upstream PR. Validate the exact diff and
  cross-repository PR direction before dispatch. Never disable the guard.
- Log emitted/effective arguments, responses and resource IDs. After ambiguous
  timeouts, check whether a write succeeded before retrying it.
- A personal account is not an organization; use the actual schema's personal
  fork semantics after checking identity with `get_me`.

## Early stopping

Use 300 seconds and 20 top-level tool calls for this longer workflow. These are
new limits, separate from the old 180-second/12-call probe. Allow one corrected
argument retry per operation/tool; block repeated identical failures. Stop before any forbidden
detour, settings change, upstream code write or write outside the manifest.
Ordinary Gitea reads and internal skill reads are allowed. Preserve partial
resources and traces; do not rescue a scored turn with corrective user hints.

## Acceptance and reporting

Independently verify each stage:

- Exactly one upstream issue describing the correction.
- Correct fork parent; report creation versus reuse separately.
- Named branch and exact requested file diff committed only in the fork.
- Open upstream PR with the correct fork head and upstream base, referencing
  the upstream issue and containing only the approved change.
- Agent read-back and correct issue, file/branch and PR URLs.
- No forbidden detours, extra writes, settings changes or merges.

Report stage results, elapsed time and stopping reason separately. Direct MCP
controls are not model passes. Keep these results separate from historical
read-only and fork/issue probes. The upstream default branch stays unchanged.
Leave the PR open; deletion, issue closure, merging and Discord messages are
outside the test. Record resources for later owner-approved cleanup.

## Native response preflight

Before scoring, exercise guard state handling against the actual MCP response
formats. Branch/file success can be JSON strings rather than objects. Validate
that branch and commit state advance and that valid subsequent writes remain
allowed. Keep preliminary harness failures ungraded and preserve their partial
resources; do not turn them into model failures. Independently verify writes,
including after ambiguous timeouts, before retrying.

## Historical fixture lesson

The earlier fork-issue probe encountered disabled Issues on the new fork. That
setting is irrelevant to this revised upstream-issue workflow. Its later manual
enablement and successful read-back do not change the original model grades.
