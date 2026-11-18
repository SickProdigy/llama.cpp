# Focused Gitea tools for the local Hermes instance

This optional Hermes plugin replaces the model-facing multiplexed Gitea tools
with 15 smaller operations. Mutation arguments are required by JSON Schema:
issue title/body, branch names, exact edit text and PR source/destination.
All operations still use the existing authenticated Gitea MCP transport. There
is no direct HTTP fallback, credential handling, automatic retry or weight tuning.

The PR tool accepts upstream owner/repo and fork owner/repo/branch separately,
checks the actual fork parent and authenticated owner, then constructs the native
`owner:branch` head. The edit tool performs one targeted text replacement on an
existing feature branch. It cannot create another branch or replace an entire
file through a separate content mode. Default-branch edits and writes outside
the configured upstream allowlist are refused. A pre-tool hook rejects direct model calls to the hidden native namespace,
including stale calls from old conversation history. Internal bridge dispatch
still uses the native registry handlers. Disable the plugin to return a profile
to the original native interface. Read results normalize the native
line-JSON representation to bounded readable text and present public Gitea URLs.
Directory reads use the repository tree for empty, `.`, `/` and `./` root paths;
the native directory reader rejects both `.` and an empty path.
ordinary paths are passed through unchanged.

## Requirements and configuration

Use this only for the paired `hermes-agent` instance. Native MCP discovery must
remain enabled: the plugin calls its registered handlers even when their toolset
is hidden from the model. The MCP server must expose `repo_read(method: get)`;
adding the read-only canonical `repo_read` name to its existing `GITEA_TOOLS`
allowlist enables this. Do not enable all `repo_write` methods as a substitute.

Copy this directory to `hermes-agent/data/plugins/gitea-focused/`, then merge:

```yaml
plugins:
  enabled:
    - gitea-readable-defaults
    - gitea-focused
  entries:
    gitea-focused:
      settings:
        allowed_upstream_repositories:
          - sickprodigy/nicotineplus-plugins
        public_url: https://gitea.rcs1.top
```

Add the `gitea-focused` toolset to the platform's saved list and suppress the
native `mcp-gitea-hermes` toolset via `agent.disabled_toolsets`. Keep the MCP
server itself enabled. Preserve the other selected tools; an explicit platform
composite can opt into default-off Discord tools, so compare the resulting
schemas with the old surface instead of assuming the tool count stays fixed.
The evaluated profile explicitly suppresses `discord` and `discord_admin` to
preserve the original surface. Update the environment hint's old native tool
names to the focused names; do not leave instructions to send `with_lines` to
`gitea_read_file`, which supplies readable mode itself.

An empty upstream allowlist denies mutations. Configure only the intended test
or working repositories. This is an ordinary tool-level policy, not isolation
against code running with the agent process's credentials.

Restart Hermes after configuration changes. Validate loaded schemas, authenticated
identity, exact fork parent and one readable file before testing mutations.
Deployment status and model results belong to the dated evaluation report.

## Checks

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 hermes-profile/test_gitea_focused.py
```

Tests cover required fields, native payload mapping, personal fork semantics,
fork ownership/parent checks, default-branch protection, exact edits, error
propagation, response serialization, readable text and public links. Real MCP
preflight and model-controlled writes are evaluated separately; mocked transport
checks are not evidence of a successful remote mutation.
