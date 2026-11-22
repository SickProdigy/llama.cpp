# Part 2 evidence and replay

Verify the archive, extract into a new ignored directory, then verify its
manifest, exact source inventories, packet IDs, captured bodies and usage:

```bash
(cd evaluations/2026-11-22-compact-review && sha256sum -c part2-evidence.sha256)
mkdir -m 700 .git/compact-review-part2-replay
python3 - <<'PY'
import tarfile
with tarfile.open('evaluations/2026-11-22-compact-review/part2-evidence.tar.gz') as archive:
    archive.extractall('.git/compact-review-part2-replay', filter='data')
PY
python3 evaluations/2026-11-22-compact-review/verify_part2.py \
  --root .git/compact-review-part2-replay
```

Run `sha256sum` from the archive's directory, or supply its path to the checksum
command if running elsewhere. The structural verifier expects 649 regular files,
eight source packets, 41 complete responses, 35 scored reviews, five warm repeats,
one cache-interference repeat and one failed-suite control blocked without review.
This verifies captured evidence; it does not execute project tests, reverify
historical private HMACs or certify semantic correctness.

`controls/corpus-private.json` contains development expectations unblinded after
all calls. That file's original name is preserved for as-run controller provenance.
Those expectations, independent grader/reference code, future tasks and earlier
verdicts are absent from every model request. The archive excludes signing keys,
profiles, native memory/skill context, credentials, SQLite stores and private fresh
workflow checks. Source snapshots and the additional test-gap mutant are included.

On the owner's Debian Docker engine, an individual project-suite replay can use
the same already retained immutable image and isolated flags. The bind source is
a **server-local** path; substitute the extraction directory's actual engine path.
For this workspace:

```bash
ENGINE_EVIDENCE_ROOT=/srv/samba/media/Documents/prodigy/Coding-Programming/docker-containers2/llama.cpp/.git/compact-review-part2-replay
docker run --rm --pull never --user 1000:1000 --network none --read-only \
  --cap-drop ALL --security-opt no-new-privileges --memory 1g --cpus 1 \
  --tmpfs /tmp:rw,size=128m \
  --mount "type=bind,source=$ENGINE_EVIDENCE_ROOT/cases/case-b5da32b088/source,target=/workspace,readonly" \
  -w /workspace -e PYTHONDONTWRITEBYTECODE=1 -e PYTHONPATH=/workspace \
  --entrypoint timeout \
  sha256:97b08c5ce375113809299fc8c5dd86ae60600f618158d15fe4ad5fc9d7f4b7ae \
  -s KILL 90 python -m pytest -q -p no:cacheprovider
```

The failing-suite case is `case-5d28a90f44`; a nonzero exit is expected. A fresh
execution produces a new receipt/output identity and does not retroactively
change the historical critic's evidence. The test image is local; this is not
a claim that its SHA can be pulled from a public registry.

The framework suite for this repository stage is:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider hermes-profile/compact-review
```

Part 2 records 30 checks plus 20 subtests in Python 3.14.9 / pytest 9.1.1.
The archived frozen-library subset reproduces the 24 packet/transport checks used
for calibration; the additional publication-adapter tests are in the repository
stage commit. Later stages may add checks. These are execution/admission controls,
not measurements of model intelligence or proof that project tests are adequate.

The archived controllers are **as-run provenance**, with deliberately fixed owned
names and no replay of completed queues. New GPU experiments require a new state
namespace, baseline capture, isolated endpoints and a detached restoration guard.
Do not restart those historical controllers against their completed directories.
The retained file SHA, actual launch arguments, sampler, packet and full response
are provided; stochastic/numerical behavior need not match on another build,
offload path or host. Source context selection is heuristic, not whole-program proof.

Plugin source provenance follows the completed pilot's
[source notice](../2026-11-22-everyday-pilot/SOURCE-NOTICE.md). No native owner
instructions, profiles or private fresh-workflow graders are redistributed here.
