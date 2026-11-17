# Nicotine plugins: bounded fork/issue probe — November 17, 2026

## Result

Neither model-driven attempt completed the workflow. A separate direct MCP
control proved that the same `hermes-agent` connection can fork the repository
and obtain an accepted issue-creation response. The created issue cannot yet be
read back while the test fork reports `has_issues: false`.

| Model-driven variant | Seconds | Tool attempts | Fork created | Issue created | Early stop |
|---|---:|---:|---|---|---|
| Current VibeForged profile | 88.9 | 6 | No | No | Terminal/curl fallback blocked before execution |
| Same prompt, personal-account API note added to test profile | 35.9 | 10 | No | No | Unrelated process-management tool blocked before execution |

These are two different profile conditions, not repeated equivalent samples or
an estimate of general reliability. No Qwen comparison or first/second-prompt
rerun was performed. This new write probe is separate from previous read-only
advice scores.

## Fixture and exact prompt

The owner approved `sickprodigy/nicotineplus-plugins` and destination
`hermes-agent`. The source has 40 checked-out files totaling 222,981 bytes. Its pinned main tree is
`84afaf401b29753b6810e4f92f253e0d28637dbf`.

> Using the configured Gitea MCP, fork sickprodigy/nicotineplus-plugins into your
> hermes-agent account as hermes-mcp-test-20261117-vf-144838. Verify the new fork.
> In that fork, open exactly one issue titled "MCP workflow test 20261117-vf-144838"
> with the body "Created by the Hermes MCP workflow test. No implementation
> requested." Read the issue back and return the fork URL and issue URL. Stop
> there. Do not change code, create branches or pull requests, edit the upstream,
> change connections, or substitute GitHub/browser/terminal actions. If a step
> fails, report the exact error and any resources already created.

The actual prompt is retained verbatim in each run's `prompt.txt` in the archive;
line wrapping above is for readability. Neither run received corrective user
messages during execution.

## Model behavior and early-stop guard

Both attempts incorrectly supplied `org: hermes-agent` to `repo_write(method:
fork)`. That parameter names a Gitea organization. `hermes-agent` is a personal
user: independent user lookup succeeds and organization lookup returns 404.
The model also tried repository-read methods excluded by the configured method
allowlist and, in the second attempt, wrong branch/directory file reads that
contributed to MCP cooldown.

The second variant appended this note to its **disposable test profile only**:

> For Gitea fork operations, org means an organization, not a personal user
> account. Use get_me to verify the authenticated account. When the requested
> destination is that personal account, omit org to use the authenticated
> personal-account default.

The model still supplied the wrong `org` field. Neither variant created a fork
or attempted issue creation. Both stopped before their off-task tool executed.
No terminal credential-reading/curl fallback was allowed to run.

The guard permits only the exact named fork and the exact issue title/body in
that fork, plus relevant Gitea reads and internal skill reads. It enforces a
180-second limit and a 12-call dispatch budget. Rejected arguments can receive
one corrected retry; ambiguous successful writes cannot be blindly repeated.

The first guard allowed the same rejected fork request twice, contrary to the
intended no-identical-retry rule. This harness limitation is recorded, not hidden.
The second guard added rejected-call fingerprints; six guard tests cover that
case, wrong upstream writes, off-task tools, exact issue body, duplicate creates,
and ambiguous fork responses. The first run still fails under either rule.
Both exact runner versions are retained. No timeout was needed.

## Direct control: same MCP account, no model

No resource existed after either model attempt. To separate model argument
failure from service capability, a direct control used the **same Hermes MCP
connection and credentials**, omitting `org` so the fork targets the authenticated
personal account. It did not use an operator's broader credentials to create
resources and must not be counted as a model success.

- **Fork created and verified:**
  [hermes-agent/hermes-mcp-test-20261117-vf-144838](https://gitea.rcs1.top/hermes-agent/hermes-mcp-test-20261117-vf-144838).
  Public repository metadata confirms its parent is
  `sickprodigy/nicotineplus-plugins`; an authenticated MCP tree read confirms
  the expected source tree SHA.
- **Issue creation accepted:** `issue_write(method: create)` returned issue
  number 1 with the exact requested title/body. Independent fork metadata now
  reports one open issue.
- **Issue read-back failed:** both `issue_read(method: get)` and independent
  public API/page checks returned 404. The fork reports `has_issues: false`.
  The issue URL is `/hermes-agent/hermes-mcp-test-20261117-vf-144838/issues/1`,
  but it is not presented as a working UI link.

The direct control initially expected the compact fork-write response to include
its parent object and stopped on that assertion. Independent repository metadata
then verified the parent; the fork call was not repeated. The continuation made
one issue-creation call and one issue-read call.

An operator MCP attempt to enable only this fork's Issues setting was rejected:
`method "update" is not enabled by the --tools allowlist`. No setting or MCP
permission was changed. The disabled Issues feature is consistent with the
read-back failure; a successful recheck after enabling it is still needed to
confirm recovery. The create response alone is not a complete workflow pass.

## Next step

Enable Issues on this test fork using an account with the required repository
settings access, then recheck **existing issue #1** through Hermes MCP. Do not
create another fork or duplicate issue to retry this read-back. The current
MCP allowlist cannot toggle that setting. Future combined fork/issue tests must
account for the issue feature on newly created forks; alternatively, separate
fork and issue-creation probes using an approved issues-enabled fixture.

This is a more useful next target than more repository-advice prompts: it exposes
personal-account argument handling and actual write/read-back capability. It
also demonstrates why a direct tool control and an agent success must be scored
separately.

## Runtime and evidence

The current live VibeForged Q4 model ran at 98,304 context, 4,096 main output,
using the full AIAgent loop with Discord platform selection in disposable
containers. No Discord messages were sent. The live Hermes image is
`sha256:c18f0a2090b1df335b7edb2805f4ee4c407a433d9ad929d2a9aa23f0ce6cdc04`;
llama.cpp is `b12429-9fba51d2c`, image
`sha256:9015dd57ae26f9d8208cf50d67147bf1821dd82344241d1f6b6cb5aacebd0e66`.
Those differ from November 16 and are not pooled with that comparison.

- [Model attempt results](model-results.csv)
- [Sanitized evidence](evidence.tar.gz), [member manifest](evidence-manifest.json)
  and [archive checksum](evidence.tar.gz.sha256)
- [Independent state and runtime checks](verification.json)

Requests, schemas, effective tool arguments, responses, runner versions and guard
tests are retained. Private profile snapshots, raw Docker inspections and auth
stores are excluded; credential values and unrelated repository metadata are
redacted. These harness scripts require a fresh private profile and this
workspace's Docker resources; they are an operational record, not a portable
one-command benchmark.

The source main tree and its three open issues remain unchanged; its fork count
increased by one as expected. No code, upstream issue, additional branch, PR or repository
settings were changed. The original containers/images/model/configuration,
credentials and endpoints were verified unchanged, and Hermes was restored after
each run. The extra API note was not deployed. Temporary local test resources
are removed after evidence verification. The test fork and accepted issue remain
for owner review; no cleanup deletion was authorized.
