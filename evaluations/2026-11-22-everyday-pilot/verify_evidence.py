"""Verify archive structure, manifest, replay linkage and optional private credentials.

Run without options for public verification. An operator may provide known secret
values as a JSON list on stdin with --credential-values-stdin; values are never
printed or written. Matching includes URL/base64 and nested JSON escaping.
"""
from pathlib import Path
import argparse, base64, gzip, hashlib, json, sys, tarfile, urllib.parse

p = argparse.ArgumentParser()
p.add_argument('--credential-values-stdin', action='store_true')
p.add_argument('--extra-file', action='append', default=[])
args = p.parse_args()
root = Path(__file__).resolve().parent
archive = root / 'evidence.tar.gz'
secrets = set(json.load(sys.stdin)) if args.credential_values_stdin else set()
patterns = set()
for value in secrets:
    if not isinstance(value, str) or len(value) < 8:
        continue
    for variant in [value, urllib.parse.quote(value, safe=''), base64.b64encode(value.encode()).decode()]:
        for _ in range(4):
            patterns.add(variant.encode())
            variant = json.dumps(variant)[1:-1]
def scan(payload, label):
    assert not any(value in payload for value in patterns), 'Known credential matched: ' + label

sha = hashlib.sha256(archive.read_bytes()).hexdigest()
assert (root / 'evidence.sha256').read_text().split()[0] == sha
with gzip.open(archive, 'rb') as compressed:
    while compressed.read(1024 * 1024):
        pass  # Read through the gzip footer/CRC once.
for path in [*root.rglob('*'), *[Path(x) for x in args.extra_file]]:
    if path.is_file() and path != archive:
        scan(path.read_bytes(), str(path.relative_to(root)) if path.is_relative_to(root) else path.name)
with tarfile.open(archive, 'r:gz') as tar:
    members = tar.getmembers()
    names = [m.name for m in members]
    assert len(names) == len(set(names))
    manifest = json.load(tar.extractfile('export-manifest.json'))
    assert set(names) == set(manifest['files']) | {'export-manifest.json'}
    forbidden = {'AGENTS.md', 'SOUL.md', '.env', 'auth.json', 'state.db', 'console.log'}
    for member in members:
        name = member.name
        path = Path(name)
        assert member.isfile() and not path.is_absolute() and '..' not in path.parts
        assert path.name not in forbidden and not name.endswith(('.gguf', '.request.json', '.response.txt'))
        payload = tar.extractfile(member).read()  # One read per member, not per pattern.
        scan(payload, name)
        if name in manifest['files']:
            expected = manifest['files'][name]
            assert len(payload) == expected['bytes']
            assert hashlib.sha256(payload).hexdigest() == expected['sha256']
        if '/forge/reviews/' in name and name.endswith('-review.json'):
            record = json.loads(payload)
            evidence = record.get('input', {}).get('execution_evidence')
            assert evidence is None or 'omitted_from_export' in evidence
        if name.startswith('request-metrics/'):
            assert 'messages' not in json.loads(payload)
    baseline_files = sum(name.startswith('source-baseline/') for name in names)
    assert baseline_files == 40
replay = json.loads((root / 'replay-validation.json').read_text())
assert replay['passed'] and len(replay['checks']) == 7 and replay['archive_sha256'] == sha
for row in replay['checks']:
    assert row['expected_recorded_behavior_reproduced'] and row['exit_code'] == 0
    assert hashlib.sha256((root / row['log']).read_bytes()).hexdigest() == row['log_sha256']
print(json.dumps({'passed': True, 'archive_sha256': sha, 'archive_bytes': archive.stat().st_size,
                  'manifest_entries_verified': len(manifest['files']), 'archive_members': len(names),
                  'baseline_source_files': baseline_files, 'replay_checks_verified': 7,
                  'credential_values_checked': len(secrets), 'credential_variants_checked': len(patterns),
                  'credential_scope': 'Supplied known values only; public structural verification needs no secrets.',
                  'private_profiles_raw_requests_sqlite_and_owner_instructions_excluded': True,
                  'explicit_partial_critic_prefix_exception': 'controls/announcer-doc-critic-partial-response.txt',
                  'credential_redacted_files': manifest['credential_redactions']}, indent=2))
