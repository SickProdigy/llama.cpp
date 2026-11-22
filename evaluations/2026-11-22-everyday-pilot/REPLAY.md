# Replaying the independent checks

Verify `evidence.sha256`, extract `evidence.tar.gz` into an empty directory,
and run the commands below from that extracted directory. No model, credentials,
Gitea access, or production profile is needed for these checks.

Use Python 3.14.9 to match the recorded test environment. The independent checks
use the standard library and stub Nicotine+ interfaces. The repository tests also
require pytest; the recorded version is 9.1.1. A real Nicotine+ application is not
installed in the evaluation image.

```bash
CHECKOUT="$PWD/reference-controls" PHASE=2 python3 harness/hidden_checks.py
CHECKOUT="$PWD/reference-controls" python3 harness/supplemental_arr_redirects.py
python3 -m pytest -q -p no:cacheprovider source-baseline/tests
python3 -m unittest discover -s next-run-recorder -p 'test_recorder.py' -v
```

The private reference correction should pass all 16 primary checks and all 20
supplemental redirect scenarios. The original repository has 83 tests plus two
subtests. The four recorder tests exercise an offline proposal for a later run;
that proposal was not deployed during this pilot.

To evaluate a captured patch, change `CHECKOUT` to its extracted source directory:

```bash
CHECKOUT="$PWD/runs/review-announcer/turn2/local-source" PHASE=2 \
  python3 harness/hidden_checks.py Announcer
```

Select `Beets`, `Announcer`, or `Arr` for the corresponding family. Use `PHASE=0`
for the original bug or `PHASE=1` for its documentation followup; `PHASE=2` also
enables the dependent feature checks. Running every family against a single
case's checkout will also test untouched plugins and is not that case's score.

Local drafts are under `runs/<arm>-<family>/turn<N>/local-source`. Authenticated
published snapshots, when a commit actually reached Gitea, are under
`published-source/`. Use the forge snapshot and manual audit to identify the
actual submitted commit. A passing local draft does not establish publication.

The captured repository tests may include model edits. To assess preservation,
use the immutable-original-test audit and its log, which run the original test
files against candidate code. To assess regression relevance, inspect the
original-target comparison and manual failure analysis: failure caused by a
missing new feature API alone does not reproduce the original bug.

The frozen existing-suite command selects top-level `tests/`. It does not
automatically include tests added beneath a plugin. Nested test files receive
separate candidate/original paired runs in `nested-model-tests-audit.json`;
the earlier top-level-only result is retained and annotated. For example, the
unassisted Announcer initial patch adds `announcer/tests/test_announcer.py`:
those ten tests pass individually, but default repository-root pytest discovery
fails on its duplicate module name with the existing `tests/test_announcer.py`.
The baseline root discovery passes. Passing the two directories separately is
not a passing combined suite. The independent preservation audit also checks
internal spaces in literal room names, beyond the frozen simple trim cases.

These commands check code behavior. They do not replay native Hermes sessions,
establish documentation truth, verify conversational claims, recreate forge
permissions, or validate long-session memory and compression. The full private
profile, system prompts, credentials, and SQLite contents are intentionally
excluded. Consult the protocol, measurements, manual audits, and source notice
for those boundaries. Redirect checks use loopback servers and fake keys;
they do not contact real Arr services or cover every TLS/URL-normalization case.

The posthoc HTTPS fixture additionally needs the `openssl` executable to create
a disposable certificate. It uses only loopback fake servers:

```bash
CHECKOUT="$PWD/reference-controls" python3 harness/posthoc_arr_https.py
CHECKOUT="$PWD/runs/review-arrrequests/turn1/local-source" \
  python3 harness/posthoc_arr_https.py
```

The reference follows legitimate same-origin HTTPS redirects and safely refuses
the cross-origin target. The captured review README-turn code raises
`AttributeError` on redirects. The fixture temporarily trusts only its own
self-signed test certificate inside the audit process; it does not change the
candidate source or production TLS policy. See the recorded audit for original,
reference, unassisted, and final review sources. These checks do not establish
complete TLS or certificate-security coverage.

Before extraction, the repository's evaluation directory also supports:

```bash
python3 verify_evidence.py
```

This verifies the archive SHA, gzip integrity, all declared member hashes,
forbidden private filenames, omitted reviewer execution transcripts, and the
seven archived-code replay results and log hashes. It requires the committed
sidecars and replay logs alongside the archive. Public verification needs no
credentials; the operator additionally scanned supplied known private values
without publishing them. See `artifact-validation.json` for scope and results.
