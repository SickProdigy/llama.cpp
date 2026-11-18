# Local Hermes Gitea read defaults

This plugin belongs to the paired `docker-containers/hermes-agent` instance.
It does not configure `hermes-codex` or change llama.cpp model weights.

Hermes's supported `pre_tool_call` hook supplies omitted arguments for the exact
configured tool `mcp__mcp_gitea_hermes__get_file_contents`: readable UTF-8 output,
start line 1, and a 160-line excerpt. Later reads can advance the range. Explicit
raw requests and explicit ranges are preserved; recognized binary file paths and
other tools are unchanged. Paths, branches and repository names remain the
model's responsibility. Calls made outside the normal agent hook path are not
intercepted. No network or disk operations occur inside the hook.

The installation location is the local Hermes home:
`hermes-agent/data/plugins/gitea-readable-defaults/`. Copy the two plugin files
there and add `gitea-readable-defaults` to `plugins.enabled` in that instance's
existing configuration, retaining other entries. A disabled-list entry wins over
an enabled entry. Restart that Hermes instance after installation. Hermes must
support `pre_tool_call` directives with `action: modify`; the evaluated 0.23.1
image does. Revalidate the hook after runtime/tool-namespace updates.

Run the behavior checks from this directory:

```bash
python3 test_readable_defaults.py
```

The evaluation archive also retains the native-loader and real MCP-dispatch
preflight, plus the actual model-emitted and effective dispatched arguments.
The source here makes the small runtime plugin reviewable without extracting
that archive. Live deployment status belongs to the dated evaluation report.

The companion local-provider compression setting tested with this stack is:

```yaml
auxiliary:
  compression:
    extra_body:
      max_tokens: 8192
      chat_template_kwargs:
        enable_thinking: false
```

Merge those keys into the existing compression task, preserving its other
settings. This setting is specific to the evaluated local Qwen-compatible
llama.cpp backend; do not transfer its template arguments to an unrelated API
provider. The main agent output cap remains 4,096. The dated report records the
other tested routing/skill changes; the archive's profile repair script is a
snapshot-specific reproducer, not a general-purpose configuration installer.

## Focused contribution interface

The optional [gitea-focused plugin](gitea-focused/README.md) exposes separate
required-field issue, fork, branch, edit and PR operations over the existing MCP
connection. It verifies fork ownership and parent relationships, restricts
writes to an operator-configured upstream list, and blocks model calls to the
hidden native namespace. Its readable-file output also avoids double-encoded
line JSON. This is tool/runtime tuning, not model-weight training.

Keep native MCP discovery enabled while hiding its toolset from the model.
The MCP allowlist must include the read-only `repo_read` operation. The guide
explains profile selection and compatibility hints. A normal loaded-profile
preflight must pass before deployment; unit checks alone do not prove remote
mutation success.
