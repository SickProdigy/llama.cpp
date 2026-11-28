# Selected-workspace contribution publisher

This optional Hermes plugin publishes code that the model has already edited
and checked in an explicitly selected Git checkout. It uses the configured
Gitea MCP transport; it does not acquire credentials, implement fixes, run
tests, create a fork, or open a PR. The focused contribution plugin handles
those forge operations separately. Evaluation/deployment status belongs to the
dated investigation, not to the presence of this source directory.

Configure a session with a fixed checkout root, immutable starting commit,
allowed upstream repository and explicit file scope:

```yaml
plugins:
  enabled: [gitea-focused, gitea-workspace]
  entries:
    gitea-workspace:
      settings:
        workspace_root: /workspace
        baseline_ref: FULL_STARTING_COMMIT_SHA
        allowed_upstream_repositories: [owner/project]
        allowed_paths: [src/helper.py, README.md]
        public_url: https://gitea.rcs1.top
```

Merge this into the existing profile, preserving unrelated settings. The
focused plugin needs its own matching upstream allowlist. Keep the authenticated
native MCP transport available internally, hide its model-facing toolset, and
expose the focused/workspace toolsets. For the tested directly visible profile,
set `tools.tool_search.enabled: "off"`; a top-level `tool_search` setting does
not configure discovery. Do not apply that setting to every unrelated profile.

The selected project must actually be mounted at `/workspace`, writable by the
agent user, and selected as both agent and terminal cwd. Set the image's
`HERMES_WRITE_SAFE_ROOT=/workspace`. Preserve Git history and the starting
commit; an unrelated synthetic baseline is unsuitable for publishing an actual
fork contribution. Put permanent engineering conventions in the session
environment hint, as the corrected evaluation does. If a workspace policy file
is used instead, ensure it is intentionally tracked or ignored: this publisher
collects nonignored untracked files too. An operator-created policy file blocked
an earlier trial when the model included it in its contribution.

The evaluated workflow starts from a clean isolated checkout. Selecting an
arbitrary dirty working tree can include unrelated allowed files; this prototype
does not distinguish edits that predate the current request. Configure the
starting commit and scope when opening the selected project session, and review
its diff before publishing. General shared dirty-worktree use is not validated.

`gitea_commit_workspace` takes the personal fork owner/name, existing feature
branch and commit message. It checks authenticated ownership, upstream parent
and nondefault branch. It collects changes since the configured baseline,
including untracked nonignored files, then submits a bounded MCP batch with
remote file SHAs and verifies resulting blob SHAs. UTF-8 source files are
bounded to 200 KB; explicit allowed paths and Python tests under `tests/` are
accepted. Outside-root targets, symlinks, unexpected paths and duplicate
publication of unchanged content are rejected. A later README/code change can
be published to the same branch. Deletions require an existing remote file.

A successful publisher result establishes remote file hashes, not code quality
or test success. Run appropriate project checks first and independently review
the actual diff and PR direction. This small-task publisher is not a general
replacement for Git: large/binary changes and complex renames need another
workflow.

Run checks from `hermes-profile`:

```bash
python3 test_workspace_publish.py
```

These unit checks use temporary Git repositories and mocked MCP responses.
Only dated full-Hermes trials establish real remote contribution behavior.


Version 0.1.1 reads paginated remote trees before and after each commit, bounded
to 5,000 entries. It does not probe missing file paths: three expected 404s from
new files triggered the installed SDK's server-wide circuit breaker in a real
operator smoke. The corrected SDK/MCP smoke publishes and verifies three new
files. Thirteen temporary-Git behavior checks cover this path and pagination.
The dated report distinguishes operator transport smokes from model trials.

Version 0.1.2 optionally accepts `allowed_path_prefixes`, such as
`[booksearch/, tests/]`, for a selected task that may need a new module or data
fixture. Exact allowed paths remain supported and directory scopes default to
empty. Prefixes must be normalized relative directories ending in `/`; sibling
prefixes and path traversal do not match. Any symlink component is rejected,
including a parent directory that points elsewhere within the repository.
These options grant file scope only, preserving fork ownership, upstream
allowlist, nondefault branch and content-size checks. Seventeen behavior checks
cover the combined publisher. Each evaluated profile pins its actual version.

Version 0.1.3 resolves 40-character branch names through bounded paginated
branch metadata before each tree lookup. It refreshes the SHA after committing
so verification reads the new head. This repairs a reproduced installed tree
endpoint edge case; it does not rename branches or repair model arguments.
Twenty publisher checks pass, including changed heads and pagination. A real
scoped SDK/MCP smoke verifies two commits and exact remote blobs on such a
branch, plus a correctly directed upstream PR. Operator preflight issues are
closed and this smoke is not a model coding success.

Version 0.1.4 adds optional `explicit_object_ids: true` under this plugin's
settings. Successful responses provide `verified_commit_sha` and `commit_url`
before the file results, whose hashes are named `blob_sha`. A file blob hash
identifies file content and cannot be used as a commit link. The default remains
the earlier response format with file `sha` fields and no extra branch read.

The option reads the remote feature-branch head after writing, then verifies
the changed blobs against that exact commit. `verified_commit_sha` identifies
the verified snapshot; it does not establish exclusive authorship or guarantee
that a concurrent writer has not moved the branch afterward. If head metadata
cannot be verified, the tool reports that the write returned but verification
failed; it never constructs a commit link from a blob hash. Twenty-six unit
checks pass, including pinned snapshot verification, missing metadata, deletions
and the existing 40-character branch behavior. This option has not yet received
a real native transport or model-quality qualification. The running Announcer
comparison uses its previously pinned 0.1.3 copy, without this option.
