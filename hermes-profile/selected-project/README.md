# Selected project context

This optional hook supplies the selected checkout's root, branch, HEAD and
origin/upstream URLs with each user turn. It uses Hermes's native `pre_llm_call`
context mechanism. The user can ask an ordinary repository question without
repeating the forge, namespace or local directory. The repository is selected
once for the project session; this plugin does not select projects from messages.

```yaml
plugins:
  enabled: [selected-project]
  entries:
    selected-project:
      settings:
        workspace_root: /workspace
```

Merge these keys into the existing selected-project profile. Mount the actual
checkout there and set the agent/terminal cwd consistently. This is not a reason
to point a general multi-repository gateway at one arbitrary project.

The hook reads local Git metadata with bounded subprocess calls. It does not
contact a forge, modify tool arguments, grant write authorization, edit files,
or supply a task solution. HTTP/SSH user information, query strings and URL
fragments are removed before remote URLs enter model context. Local filesystem
remotes are omitted. A missing/non-root checkout produces no injected context.
Hermes preserves the original typed request separately from injected context.

The image evaluated here supports plugin context injection into the user
message. Six temporary-Git unit checks and a native SDK hook registration smoke
pass; dated full-agent trials determine whether the context improves behavior.
A registered hook alone does not demonstrate better model reliability.

From `hermes-profile`, run `python3 test_selected_project.py`.
