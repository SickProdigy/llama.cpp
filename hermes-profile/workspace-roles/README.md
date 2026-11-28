# Verified workspace forge roles

This optional context hook complements `selected-project`. It reads the selected
Git origin and the configured Gitea MCP account/repository metadata, then supplies
explicit upstream and personal-fork identities with each user turn. It does not
edit tool arguments, create repositories, grant permissions, supply code fixes,
or decide whether a task deserves a contribution.

```yaml
plugins:
  enabled: [selected-project, workspace-roles]
  entries:
    workspace-roles:
      settings:
        workspace_root: /workspace
        public_url: https://gitea.rcs1.top
```

Merge the configuration into the intended isolated Hermes profile. Native MCP
discovery must expose read-only `get_me` and `repo_read(method: get)` through
`mcp-gitea-hermes`, even when its model-facing toolset is hidden. Each context
uses two reads for a selected upstream, or three for a selected fork. It has no
cache, so changing remotes, account or ancestry is reflected on the next turn.

For an upstream checkout, the proposed fork is the authenticated account plus
the upstream repository name. Its existence is **not** implied. For a selected
personal fork, its actual name and verified parent are retained. An origin owned
by another account remains an upstream/ancestry source, never the working
account. A conflicting `upstream` remote, other forge host, malformed metadata,
missing dependency or transport failure produces only an unavailable notice.
Raw transport errors, credentials, user profile fields and repository prose are
never injected. Existing mutation checks and allowlists remain authoritative.

This is an optional experimental interface change. Unit checks and actual native
transport/context admission are prerequisites; only fresh model trials can show
whether it improves completion. It is not deployed to the owner default.

Run `PYTHONDONTWRITEBYTECODE=1 python3 hermes-profile/test_workspace_roles.py`.
