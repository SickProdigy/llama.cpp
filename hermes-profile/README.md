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


## Selected project engineering profile

[General engineering defaults](engineering-defaults.md) can be installed as
`AGENTS.override.md` in an explicitly selected checkout. They require reading
project instructions, preserving contracts and valid tests, using the existing
check command, and reporting actual results. They contain no task-specific fix.
Keep a session-only overlay untracked using `.git/info/exclude` when it should
not become part of the contribution.

The optional [workspace publisher](gitea-workspace/README.md) connects normal
local terminal/file work to the focused MCP contribution tools. Its configuration
pins one selected repository root, starting commit and file scope. Registering
the plugin is not evidence of a working contribution; the dated full-agent
investigation records actual issue/commit/PR results and limitations.

Programming directories such as `/srv/samba/media/Documents/prodigy` are local
to Debian and exported to Windows; Debian and Docker access those existing
files directly. Resolve a project bind against the active Docker engine and
its actual mounts, rather than guessing a host path from the editor path. The
November 21 runtime has only its data directory mounted; its `/opt/hermes` cwd
does not correspond to an editor-selected repository. Select/mount the existing
project before evaluating normal local code editing. Do not clone or pull just
to obtain edits already present on that server-local filesystem.


## November 21 experimental profile and limits

The current novel-fix evaluation uses Hermes 0.23.3, normal terminal/file tools,
a clean selected checkout, focused 0.1.6, workspace publisher 0.1.3 and the
selected-project hook. Policy is injected outside the checkout, so the model
cannot accidentally stage an operator overlay. The focused native MCP toolset
is discovered internally and hidden from the model. Branches with exactly
40 characters are resolved to actual commit SHAs before tree verification,
working around the installed MCP tree-ref ambiguity. This repair has real
transport preflight coverage; it does not establish model code quality.

Main output in this experimental profile is 8,192, rather than the older
4,096 setting above. Compression has an explicit 8,192 summary cap and .85
threshold; GPT-OSS uses low reasoning for compression instead of Qwen template
arguments. Samplers and loaded contexts differ by named profile: copy the
complete measured configuration, not only the weight filename. Check actual
outgoing requests after changes, including nested `extra_body` custom fields.

The ordinary production model/profile remains separate. Do not treat these
optional plugins as an unattended coding guarantee: actual novel-fix results,
quality review and deployment status are in the
[active investigation](../evaluations/2026-11-21-goal-investigation/investigation.md).

Evaluation isolation also suppresses inherited memory/skills and automatic
background review. In this pinned Hermes version, the background review writes
memory/skill insights **after delivery**; it is not a pre-publication code critic.
Disabling it does not explain away incorrect patches that already passed the
agent's own checks. These evaluation flags keep trials independent; they are
not a claim that the everyday gateway, with all memory/skill integrations,
has identical latency or behavior. A separate code review remains necessary.


### Native scratch writes in a selected checkout

Hermes advertises its profile scratch directory for temporary scripts. If you
set a write-safe root for the selected checkout, also allow that scratch root.
For the evaluated container paths, the Hermes service environment entry is:

```yaml
HERMES_WRITE_SAFE_ROOT: "/workspace:/opt/data/cache/scratch"
```

Use the actual mounted checkout and scratch paths reported by that profile.
The colon-separated setting is supported by the pinned native file tools.
A separate [nine-check native preflight](../evaluations/2026-11-21-goal-investigation/native-scratch-preflight.json)
verifies scratch write/patch/execution, checkout writes, and continued denials
for profile credentials, sibling-prefix paths and symlink escapes.

This compatibility correction was identified during the final diagnostic.
The scored conversations retain their original checkout-only write root;
no end-to-end model improvement is claimed from this operator preflight.
