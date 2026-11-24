"""Verify saved capacity observations, not coding quality or private behavior."""
import hashlib, json, sys, tarfile
from pathlib import Path, PurePosixPath

archive = Path(sys.argv[1])
with tarfile.open(archive) as tar:
    files = {}
    for member in tar.getmembers():
        path = PurePosixPath(member.name)
        assert member.isfile() and not path.is_absolute() and '..' not in path.parts
        assert member.name not in files
        files[member.name] = tar.extractfile(member).read()
manifest = json.loads(files['manifest.json'])
assert set(files) == set(manifest) | {'manifest.json'}
for name, digest in manifest.items():
    assert hashlib.sha256(files[name]).hexdigest() == digest, name
read = lambda name: json.loads(files[name])
summary, protocol = read('summary.json'), read('protocol.json')
key = summary['candidate']
pin = protocol[key]
if 'extra-registration.json' in files:
    registration=read('extra-registration.json')
    assert hashlib.sha256(files['controller.py']).hexdigest()==registration['controller_sha256']
    assert hashlib.sha256(files['protocol.json']).hexdigest()==registration['protocol_sha256']
    assert hashlib.sha256(files['model_cache_probe.py']).hexdigest()==registration['cache_helper_sha256']
    cache=read('observed/selected-file-cache-after-original-stop.json')
    assert cache==summary['selected_file_cache_after_original_stop'] and cache['mincore_cached_page_bytes_after']==0

identity = read('observed/model-identity.json')
assert identity['sha256'] == pin['sha256']
assert identity['bytes'] == pin['expected_bytes']
assert identity == summary['model_identity']
assert summary['public_pin'] == pin
assert read('observed/runtime-restoration.json')['restored']
assert read('observed/finished.json')['results'][0]['resource_probes_completed']
rows = [json.loads(line) for line in files['observed/layout0/samples.jsonl'].splitlines()]
assert rows and all('measurement_error' not in row for row in rows)
assert len(rows) == summary['samples']
assert max(int(row['gpu_csv'].split(',')[0]) for row in rows if row.get('gpu_csv')) == summary['peak_gpu_MiB']
for raw, reported in [('total_cgroup_bytes','peak_aggregate_cgroup_bytes'), ('total_process_pss_bytes','peak_process_PSS_bytes'), ('total_cgroup_swap_bytes','peak_study_swap_bytes')]:
    assert max(row[raw] for row in rows) == summary[reported]
assert summary['peak_study_swap_bytes'] == 0
assert summary['peak_aggregate_cgroup_bytes'] <= protocol['host_aggregate_limit_bytes']
assert summary['peak_process_PSS_bytes'] <= protocol['host_aggregate_limit_bytes']
assert not any(row.get('budget_guard_triggered') for row in rows)
assert min(row['model_disk_free_bytes'] for row in rows) >= protocol['minimum_disk_reserve_bytes']
for name, capture in summary['probes'].items():
    assert capture == read('observed/layout0/'+name+'/capture.json')
    assert capture['body_complete'] and capture['seconds'] > 0
    raw = files['observed/layout0/'+name+'/response.bin']
    assert hashlib.sha256(raw).hexdigest() == capture['response_sha256']
    assert json.loads(raw)['usage'] == capture['usage']
print(json.dumps({'passed': True, 'candidate': key, 'manifest_files': len(manifest), 'memory_samples': len(rows), 'completed_probes': len(summary['probes']), 'coding_quality_not_validated': True, 'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}))
