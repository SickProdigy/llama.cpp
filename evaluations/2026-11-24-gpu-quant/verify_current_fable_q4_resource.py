"""Verify saved capacity observations, not coding quality or private behavior."""
import hashlib, json, sys, tarfile
from pathlib import Path, PurePosixPath

archive = Path(sys.argv[1])
with tarfile.open(archive) as tar:
    files = {}
    for member in tar.getmembers():
        path = PurePosixPath(member.name)
        assert member.isfile() and not path.is_absolute() and '..' not in path.parts
        assert member.name not in files and member.size<=16*1024**2
        assert sum(map(len,files.values()))+member.size<=128*1024**2
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
# Q8 additions: actual placement, both reserves and requested/actual token headroom.
assert key=='fable-q4-current-thinking' and 'extra-registration.json'in files
placement=files['observed/layout0/placement-at-ready.log'].decode()
assert 'offloaded 41/41 layers to GPU'in placement
assert summary['placement_lines']==[l for l in placement.splitlines()if any(t in l for t in ['offloaded 41/41','model buffer size','KV buffer size','compute buffer size'])]
assert min(r['staging_disk_free_bytes']for r in rows)==summary['minimum_staging_disk_free_bytes']>=protocol['minimum_disk_reserve_bytes']
assert set(summary['probes'])=={'tool','tool-result','tool-followup','prompt16000','prompt60000','prompt80000'}
for name,capture in summary['probes'].items():
    base='observed/layout0/'+name+'/'
    body=read(base+'request.json');sizing=read(base+'input.json');usage=capture['usage']
    assert sizing['context']==summary['context']==98304
    assert sizing['rendered_tokens']==usage['prompt_tokens']
    assert sizing['rendered_tokens']+body['max_tokens']<summary['context']
    assert usage['total_tokens']==usage['prompt_tokens']+usage['completion_tokens']<=summary['context']
assert read('cleanup.json')['passed']and read('preservation.json')['passed']
for target,row in summary['synthetic_marker_checks'].items():
    base='observed/layout0/prompt'+target+'/'
    check=read(base+'retrieval-check.json');content=read(base+'response.bin')['choices'][0]['message'].get('content')
    assert check['expected']=='capacity-check-'+target and check['content']==content
    assert row==dict(check,exact_match=content==check['expected'])
assert summary['direct_tool_call_correct']==read('observed/layout0/tool-check.json')['valid_tool_call']
assert summary['dependent_tool_history_check']==read('observed/layout0/tool-followup-check.json')
assert min(int(r['gpu_csv'].split(',')[1])for r in rows if r.get('gpu_csv'))==summary['minimum_GPU_free_MiB']
# Derive actual tool validity and retained lineage, rather than trusting a flag.
first=read('observed/layout0/tool/response.bin')['choices'][0]['message'];valid=False
for call in first.get('tool_calls')or[]:
    try:valid=valid or(call.get('function',{}).get('name')=='lookup_record'and json.loads(call['function']['arguments'])=={'name':'memory-probe'})
    except(ValueError,TypeError,KeyError):pass
assert valid==summary['direct_tool_call_correct']==read('observed/finished.json')['results'][0]['tool_call_correct']
assert valid,'This completed six-probe cell must contain an actual valid tool call'
initial=read('observed/layout0/tool/request.json');pending=read('observed/layout0/tool-result/request.json')
assert pending['messages'][:len(initial['messages'])]==initial['messages']and pending['messages'][len(initial['messages'])]==first
answers=pending['messages'][len(initial['messages'])+1:];assert len(answers)==len(first['tool_calls'])
for message,call in zip(answers,first['tool_calls']):
    assert message['role']=='tool'and message['tool_call_id']==call['id']and json.loads(message['content'])=={'name':'memory-probe','code':'tool-history-capacity-ok'}
answer=read('observed/layout0/tool-result/response.bin')['choices'][0]['message'];assert not answer.get('tool_calls')
follow=read('observed/layout0/tool-followup/request.json');assert follow['messages'][:-2]==pending['messages']and follow['messages'][-2]==answer
assert read('observed/layout0/tool-followup/response.bin')['choices'][0]['message'].get('content')==summary['dependent_tool_history_check']['content']
for name in summary['probes']:
    body=read('observed/layout0/'+name+'/request.json')
    assert body['seed']==20261123 and body['max_tokens']==pin['probe_output_cap']==16384
    for k,v in pin['sampler'].items():assert body[k]==v
assert summary['original_preservation']['Codex_full_recorded_state_unchanged']and summary['original_preservation']['both_staged_model_metadata_unchanged']
assert min(r['staging_disk_free_bytes']for r in rows)>=protocol['stage_abort_threshold_free_bytes']==102*1024**3
selection=read('retained-selection.json');assert selection==summary['retained_selection_source']
assert hashlib.sha256(files['retained-selection.json']).hexdigest()==protocol['public_selection_source_sha256']
for field in ['repo','revision','file','expected_bytes','sha256']:assert selection['public_pin'][field]==pin[field]
assert read('header-comparison.json')==summary['header_comparison']and summary['header_comparison']['same_shapes_template_count']
assert hashlib.sha256(files['source/admission-launch.py']).hexdigest()==protocol['admission_sha256']['launch_current_fable_q4_resource.py']
launch=read('observed/layout0/launch.json')['argv'];assert launch[launch.index('-m')+1]=='/models/'+pin['file']and launch[launch.index('--fit')+1]=='off'and launch[launch.index('--load-mode')+1]=='none'
print(json.dumps({'passed': True, 'candidate': key, 'manifest_files': len(manifest), 'memory_samples': len(rows), 'completed_probes': len(summary['probes']), 'coding_quality_not_validated': True, 'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}))
