"""Derive forge roles from selected Git remotes and read-only Gitea metadata."""
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urlsplit

PREFIX = "mcp__mcp_gitea_hermes__"
NAME = re.compile(r"[A-Za-z0-9_.-]+")


def decode(value):
    for _ in range(6):
        if isinstance(value, str):
            value = json.loads(value)
        elif isinstance(value, dict) and ("error" in value or value.get("isError")):
            raise ValueError("Gitea metadata unavailable")
        elif isinstance(value, dict) and set(value) == {"result"}:
            value = value["result"]
        else:
            return value
    raise ValueError("Unexpected metadata envelope")


def repository(value):
    if not isinstance(value, str):
        raise ValueError("Missing repository identity")
    parts = value.split("/")
    if len(parts) != 2 or any(not NAME.fullmatch(p) or p in (".", "..") for p in parts):
        raise ValueError("Invalid repository identity")
    return tuple(parts)


class WorkspaceRoles:
    def __init__(self, root, public_url, transport):
        if not root:
            raise ValueError("workspace-roles requires an explicit workspace_root")
        self.root = Path(root).resolve()
        public = urlsplit(public_url)
        if public.scheme not in ("http", "https") or not public.hostname or public.username or public.password:
            raise ValueError("public_url must identify the configured Gitea service")
        if public.path not in ("", "/") or public.query or public.fragment:
            raise ValueError("public_url must be an origin without a path, query or fragment")
        self.host = public.hostname.lower()
        self.web_origin = (public.scheme, self.host, public.port or (443 if public.scheme == "https" else 80))
        self.transport = transport

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-C", str(self.root), *args], stderr=subprocess.DEVNULL, timeout=2
        ).decode().strip()

    def remote(self, value):
        # Drop credentials/query/fragment by projecting only host and identity.
        if "://" not in value:
            match = re.fullmatch(r"(?:[^@\s]+@)?([^:\s]+):(.+)", value)
            if not match:
                raise ValueError("Remote is not a forge URL")
            value = "ssh://" + match[1] + "/" + match[2].lstrip("/")
        parsed = urlsplit(value)
        if parsed.scheme not in ("http", "https", "ssh", "git") or parsed.hostname != self.host:
            raise ValueError("Remote is outside configured Gitea")
        port = parsed.port  # Validate even SSH/git port syntax.
        if parsed.scheme in ("http", "https") and (parsed.scheme, parsed.hostname, port or (443 if parsed.scheme == "https" else 80)) != self.web_origin:
            raise ValueError("Remote HTTP origin differs from configured Gitea")
        path = parsed.path.removeprefix("/")
        if path.endswith(".git"):
            path = path[:-4]
        return repository(path)

    def native(self, name, args):
        value = decode(self.transport(PREFIX + name, args))
        if not isinstance(value, dict):
            raise ValueError("Expected metadata object")
        return value

    def info(self, owner, repo):
        info = self.native("repo_read", {"method": "get", "owner": owner, "repo": repo})
        if repository(info.get("full_name")) != (owner, repo):
            raise ValueError("Repository identity mismatch")
        if not isinstance(info.get("default_branch"), str) or not info["default_branch"]:
            raise ValueError("Missing default branch")
        if type(info.get("fork")) is not bool:
            raise ValueError("Missing fork metadata")
        return info

    def facts(self):
        if Path(self.git("rev-parse", "--show-toplevel")).resolve() != self.root:
            raise ValueError("Selected root is not a repository root")
        origin = self.remote(self.git("remote", "get-url", "origin"))
        try:
            explicit_upstream = self.git("remote", "get-url", "upstream")
        except subprocess.CalledProcessError:
            explicit_upstream = None
        explicit_upstream = self.remote(explicit_upstream) if explicit_upstream is not None else None
        me = self.native("get_me", {})
        login = me.get("login")
        if not isinstance(login, str) or not NAME.fullmatch(login) or login in (".", ".."):
            raise ValueError("Missing authenticated login")
        selected = self.info(*origin)
        if selected["fork"]:
            parent = selected.get("parent")
            upstream = repository(parent.get("full_name") if isinstance(parent, dict) else None)
            if upstream == origin:
                raise ValueError("Invalid self-parent")
            upstream_info = self.info(*upstream)
        else:
            upstream, upstream_info = origin, selected
        if explicit_upstream is not None and explicit_upstream != upstream:
            raise ValueError("Git upstream conflicts with verified repository ancestry")
        own_fork_selected = selected["fork"] and origin[0] == login
        fork_repo = origin[1] if own_fork_selected else upstream[1]
        return {
            "authenticated_actor": login,
            "selected_origin_repository": "/".join(origin),
            "upstream_owner": upstream[0],
            "upstream_repo": upstream[1],
            "upstream_default_branch": upstream_info["default_branch"],
            "issue_and_PR_destination": "/".join(upstream),
            "fork_owner": login,
            "fork_repo": fork_repo,
            "fork_name": fork_repo,
            "personal_fork_status": "verified_selected_fork" if own_fork_selected else "derived_destination_existence_not_checked",
            "provenance": "Selected Git origin and read-only configured Gitea get_me/repo_read metadata; refreshed for this context",
            "scope": "Identity facts only. Existing tool permissions still apply. Verify/create the personal fork as needed, use a feature branch, and leave upstream PRs unmerged.",
        }

    def context(self, **kwargs):
        try:
            facts = self.facts()
        except Exception:
            # Never publish raw transport exceptions: they may contain secrets.
            return {"context": "Workspace forge roles unavailable: selected Git remotes and configured Gitea identity/ancestry could not be verified. Resolve metadata before selecting a write destination."}
        return {"context": "Verified workspace forge roles (read-only metadata):\n" + json.dumps(facts, ensure_ascii=False, indent=2)}


def register(ctx):
    from tools.registry import registry
    roles = WorkspaceRoles(ctx.get_config("workspace_root", ""), ctx.get_config("public_url", ""), registry.dispatch)
    ctx.register_hook("pre_llm_call", roles.context)
