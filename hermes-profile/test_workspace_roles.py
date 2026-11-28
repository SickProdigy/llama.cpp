import copy
import importlib.util
import json
import pathlib
import subprocess
import tempfile
import unittest

path = pathlib.Path(__file__).parent / "workspace-roles/__init__.py"
spec = importlib.util.spec_from_file_location("workspace_roles", path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class Checks(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = pathlib.Path(tmp.name)
        self.git("init", "-b", "main")
        self.git("remote", "add", "origin", "https://gitea.example/upstream/project.git")
        self.login = "actor"
        self.rows = {"upstream/project": {"full_name": "upstream/project", "fork": False, "default_branch": "main"}}
        self.calls = []
        self.roles = m.WorkspaceRoles(self.root, "https://gitea.example", self.transport)

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args], stderr=subprocess.DEVNULL).decode().strip()

    def transport(self, name, args):
        self.calls.append((name, args))
        if name == m.PREFIX + "get_me":
            value = {"login": self.login, "email": "must-not-be-injected", "token": "also-private"}
        else:
            self.assertEqual(name, m.PREFIX + "repo_read")
            self.assertEqual(args["method"], "get")
            value = self.rows[args["owner"] + "/" + args["repo"]]
        return json.dumps({"result": json.dumps(value)})

    def facts(self):
        return json.loads(self.roles.context()["context"].split("\n", 1)[1])

    def fork(self, owner="actor", name="renamed"):
        key = owner + "/" + name
        self.rows[key] = {"full_name": key, "fork": True, "default_branch": "stable", "parent": {"full_name": "upstream/project"}}
        self.git("remote", "set-url", "origin", "https://gitea.example/" + key + ".git")

    def unavailable(self):
        self.assertIn("roles unavailable", self.roles.context()["context"])

    def test_upstream_and_actor_are_distinct_and_fork_is_not_assumed_existing(self):
        facts = self.facts()
        self.assertEqual((facts["upstream_owner"], facts["upstream_repo"]), ("upstream", "project"))
        self.assertEqual((facts["fork_owner"], facts["fork_repo"], facts["fork_name"]), ("actor", "project", "project"))
        self.assertEqual(facts["personal_fork_status"], "derived_destination_existence_not_checked")
        self.assertEqual(len(self.calls), 2)

    def test_selected_personal_fork_retains_renamed_repository(self):
        self.fork()
        facts = self.facts()
        self.assertEqual(facts["fork_repo"], "renamed")
        self.assertEqual(facts["issue_and_PR_destination"], "upstream/project")
        self.assertEqual(facts["upstream_default_branch"], "main")
        self.assertEqual(facts["personal_fork_status"], "verified_selected_fork")
        self.assertEqual(len(self.calls), 3)

    def test_other_accounts_fork_is_not_the_actor(self):
        self.fork(owner="other")
        facts = self.facts()
        self.assertEqual((facts["fork_owner"], facts["fork_repo"]), ("actor", "project"))
        self.assertEqual(facts["upstream_owner"], "upstream")

    def test_context_refreshes_account_and_remotes_without_cached_roles(self):
        self.assertEqual(self.facts()["fork_owner"], "actor")
        self.login = "second"
        self.fork(owner="second", name="other-name")
        self.assertEqual((self.facts()["fork_owner"], self.facts()["fork_repo"]), ("second", "other-name"))

    def test_consistent_upstream_remote_is_accepted(self):
        self.fork()
        self.git("remote", "add", "upstream", "git@gitea.example:upstream/project.git")
        self.assertEqual(self.facts()["upstream_repo"], "project")

    def test_conflicting_upstream_remote_is_not_guessed(self):
        self.git("remote", "add", "upstream", "https://gitea.example/other/project.git")
        self.unavailable()

    def test_foreign_and_local_remotes_cause_no_mcp_call(self):
        for remote in ("https://github.com/upstream/project.git", "/local/project", "file:///local/project", "https://gitea.example:8443/upstream/project.git", "ssh://gitea.example:bad/upstream/project.git"):
            with self.subTest(remote=remote):
                self.git("remote", "set-url", "origin", remote)
                self.unavailable()
                self.assertEqual(self.calls, [])

    def test_url_and_profile_secrets_are_not_injected(self):
        self.git("remote", "set-url", "origin", "https://user:secret-value@gitea.example/upstream/project.git?token=second-secret#private-fragment")
        text = self.roles.context()["context"]
        for private in ("secret-value", "second-secret", "private-fragment", "must-not-be-injected", "also-private"):
            self.assertNotIn(private, text)
        self.assertIn('"fork_owner": "actor"', text)

    def test_raw_transport_errors_are_not_published(self):
        def fail(*args):
            raise RuntimeError("Bearer private-secret https://name:password@host/")
        self.roles.transport = fail
        self.unavailable()
        self.assertNotIn("private-secret", self.roles.context()["context"])

    def test_malformed_identity_and_ancestry_fail_closed(self):
        original = copy.deepcopy(self.rows)
        for field, value in (("full_name", "different/project"), ("fork", "false"), ("default_branch", None)):
            self.rows = copy.deepcopy(original)
            self.rows["upstream/project"][field] = value
            with self.subTest(field=field):
                self.unavailable()
        self.rows = original
        self.login = "invalid/login"
        self.unavailable()

    def test_fork_missing_or_self_parent_fails_closed(self):
        self.fork()
        for parent in (None, {}, {"full_name": "actor/renamed"}):
            with self.subTest(parent=parent):
                self.rows["actor/renamed"]["parent"] = parent
                self.unavailable()

    def test_nested_root_is_not_silently_selected(self):
        child = self.root / "child"
        child.mkdir()
        roles = m.WorkspaceRoles(child, "https://gitea.example", self.transport)
        self.assertIn("unavailable", roles.context()["context"])
        self.assertEqual(self.calls, [])

    def test_constructor_requires_explicit_clean_service_origin(self):
        with self.assertRaises(ValueError):
            m.WorkspaceRoles("", "https://gitea.example", self.transport)
        for url in ("", "file:///tmp", "https://user:pass@gitea.example", "https://gitea.example/path", "https://gitea.example?token=secret"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                m.WorkspaceRoles(self.root, url, self.transport)


if __name__ == "__main__":
    unittest.main(verbosity=2)
