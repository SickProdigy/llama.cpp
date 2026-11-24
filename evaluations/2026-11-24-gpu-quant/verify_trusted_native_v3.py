"""Check saved native evidence bindings; do not rerun private behavior checks."""
from pathlib import Path,PurePosixPath
import hashlib,json,statistics,sys,tarfile
archive=Path(sys.argv[1])
sha=lambda raw:hashlib.sha256(raw).hexdigest()
with tarfile.open(archive)as tar:
    files={}
    for member in tar:
        p=PurePosixPath(member.name)
        assert member.isfile() and not p.is_absolute() and '..'not in p.parts and member.name not in files
        files[member.name]=tar.extractfile(member).read()
manifest=json.loads(files['manifest.json'])
assert set(files)==set(manifest)|{'manifest.json'}
for name,digest in manifest.items():assert sha(files[name])==digest,name
read=lambda name:json.loads(files[name])
s=read('summary.json');key=s['candidate_key'];family=s['family'];assert family=='beets_lifecycle'
protocol=read('controls/protocol.json')
public_protocol=Path(__file__).with_name('resource-protocol.json').read_bytes()
assert sha(public_protocol)==protocol['private_code_fingerprints']['gpu-quant-resource-protocol.json']
assert key in ['vibe-q4-trusted','vibe-q6-trusted']
assert protocol['resource_key']==key.removesuffix('-trusted') and protocol['single_query_mode']=='approve'
control=read('audits/'+key+'-beets-approval-policy-control.json')
assert control['passed'] and control['copied_original_mode']=='approve' and control['resolved_single_query_mode']=='approve'
assert control['model_calls']==control['forge_mutations']==0 and control['pure_code_result']['status']=='success' and control['pure_code_result']['output']=='4\n'
pin=json.loads(public_protocol)[protocol['resource_key']];identity=read('runtime/model-identity.json')
assert identity==s['model'] and identity['sha256']==pin['sha256'] and identity['bytes']==pin['expected_bytes'] and identity['file']==pin['file']
for helper in ['prepare_trusted_profile.py','probe_trusted_profile_code.py']:
    assert sha(files['source/'+helper])==protocol['private_code_fingerprints'][helper]
assert protocol['controller_source']=='trusted_native_controller_v3.py'
for name in ['resolve_native_oneshot.py','native_seeded_compression_handle_preflight_v3.py']:
    assert sha(files['source/'+name])==protocol['private_code_fingerprints'][name]
for name in ['native-lineage-owner-v3-decision.json','native-seeded-compression-handle-preflight-v3.json']:
    assert sha(files['controls/'+name])==protocol['private_code_fingerprints'][name]
assert read('controls/native-seeded-compression-handle-preflight-v3.json')['passed']
controller=protocol['controller_source']
assert sha(files['source/'+controller])==protocol['private_code_fingerprints'][controller]
if 'runtime/selected-file-cache-after-original-stop.json'in files:
    assert read('runtime/selected-file-cache-after-original-stop.json')['mincore_cached_page_bytes_after']==0
    assert sha(files['source/model_cache_probe.py'])==protocol['private_code_fingerprints']['model_cache_probe.py']
    admission=read('controls/fresh-coding-source-admission.json')
    assert admission['source_unchanged_after_read_control']and admission['source_digest']==admission['baseline_digest']
assert read('runtime/runtime-restoration.json')['restored']
assert read('runtime/placement-check.json')['all_layers_offloaded']
assert read('audits/cleanup.json')['passed']
final=read('audits/'+key+'-beets-final-audit.json')
assert final==s['independent_final_audit'] and final['audit_complete'] and final['not_actor_feedback']
for name,digest in final['evidence_SHA256'].items():
    path='controls/'+name if '/result.json'in name else 'audits/'+name
    if name=='native-'+key+'-beets-cleanup.json':path='audits/cleanup.json'
    assert sha(files[path])==digest,name
base=read('controls/immutable-baseline-source-sha256.json')
for phase in range(3):
    prefix=f'phases/{phase}/';row=s['phases'][phase];run=read(prefix+'run.json')
    for name in run:assert row[name]==run[name]
    for kind in ['local-grade','remote-grade']:
        name=prefix+kind+'/grade.json'
        if name not in files:
            assert kind=='remote-grade' and row['remote_grade_absent'];continue
        grade=read(name);assert grade==row['local_grade'if kind=='local-grade'else'remote_grade']
        source=read(prefix+kind+'/source-sha256.json')
        assert set(grade['changed_paths'])=={p for p in set(base)|set(source)if base.get(p)!=source.get(p)}
    suffix=['initial','README','feature'][phase]
    audit=read('audits/'+key+'-beets-'+suffix+'-manual-audit.json')
    source=read(prefix+audit['source_kind']+'/source-sha256.json') if audit['source_kind']in ['local-grade','remote-grade'] else read(prefix+'local-grade/source-sha256.json')
    assert audit['source_SHA256']==source
    kind='remote_grade' if audit['source_kind']=='remote-grade' else 'local_grade'
    assert audit['source_digest']==row[kind]['source_digest']
    assert audit['elapsed_seconds']==run['elapsed_seconds'] and audit['CLI_exit_code']==run['exit_code']
assert s['coding_elapsed_seconds']==sum(p['elapsed_seconds']for p in s['phases'])
metrics=[read(n)for n in sorted(files)if n.startswith('requests/')and n.endswith('.metrics.json')]
assert len(metrics)==s['measurements']['HTTP_records']
assert all(m['backend_body_complete']and not m['transport_error_present']for m in metrics)
assert len(metrics)==s['measurements']['completed_HTTP_records_without_transport_error']
assert max(m.get('usage',{}).get('prompt_tokens',0)for m in metrics)==s['measurements']['maximum_completed_prompt_tokens']
lat=[m['end_epoch']-m['backend_start_epoch']for m in metrics]
assert {'min':min(lat),'median':statistics.median(lat),'max':max(lat),'sum':sum(lat)}==s['measurements']['HTTP_latency_seconds']
context=read('audits/'+key+'-beets-context-instruction-audit.json')
for phase in context['phases']:
    assert phase['completed_phase']and phase['native_handoff_verified_from_actual_CLI_output_and_DB']
    handles=s['phases'][phase['phase']]['native_session_fingerprints']
    assert phase['physical_effective_SID_SHA256']==handles['effective_sid']
    assert phase['CLI_resume_handle_SHA256']==handles['cli_resume_handle']
    assert phase['incoming_CLI_handle_SHA256']==handles['incoming_sid']
    if not all(phase['all_tasks_so_far_present_verbatim']):
        assert phase['native_compression_segment_count']>1 and phase['native_summary_messages_SHA256']
        assert phase.get('summary_semantic_coverage_manually_audited'), 'Inspect actual summary coverage before publishing a complete audit'
    name=phase['last_complete_request'].replace('.request.json','.metrics.json')
    m=read('requests/'+name)
    assert m['private_saved_request_file_SHA256']==phase['saved_request_JSON_sha256']
    assert m['request_sha256']==phase['wire_request_SHA256']
dispatch=read('audits/'+key+'-beets-command-dispatch-control.json')
for result in dispatch['results']:
    if result['source_kind']=='candidate':assert result['candidate_module_SHA256']==read('phases/2/'+dispatch.get('candidate_source_kind','local-grade')+'/source-sha256.json')['beetsbridge/__init__.py']
for phase in [0,2]:
    root='controls/'+key+'-'+family+'-phase'+str(phase)+'-test-adequacy/'
    if root+'result.json'not in files:continue
    control=read(root+'result.json');grade=s['phases'][phase]['remote_grade']if control['source_kind']=='remote-grade'else s['phases'][phase]['local_grade']
    assert control['candidate']['receipt_payload']['source_digest']==grade['source_digest']
    assert read(root+'candidate/source-sha256.json')==read(f'phases/{phase}/'+control['source_kind']+'/source-sha256.json')
rows=[json.loads(line)for line in files['runtime/memory-samples.jsonl'].splitlines()]
assert rows and len(rows)==s['measurements']['sample_count'] and all('measurement_error'not in r for r in rows)
for raw,reported in [('total_cgroup_bytes','peak_observed_cgroup_bytes'),('total_process_pss_bytes','peak_observed_all_process_PSS_bytes'),('total_cgroup_swap_bytes','peak_observed_experiment_swap_bytes')]:
    assert max(r[raw]for r in rows)==s['measurements'][reported]
assert max(int(r['gpu_csv'].split(',')[0])for r in rows if r.get('gpu_csv'))==s['measurements']['peak_GPU_MiB']
assert not any(r.get('budget_guard_triggered')for r in rows)
assert s['measurements']['peak_observed_experiment_swap_bytes']==0
assert s['measurements']['peak_observed_cgroup_bytes']<=8*1024**3
assert s['measurements']['peak_observed_all_process_PSS_bytes']<=8*1024**3
assert min(r['model_disk_free_bytes']for r in rows)>=100*1024**3
print(json.dumps({'passed':True,'candidate':key,'manifest_files':len(manifest),'memory_samples':len(rows),'completed_HTTP':len(metrics),'observed_overall_quality_pass':final['overall_workflow_completed_correctly'],'private_behavior_not_reexecuted':True,'archive_SHA256':sha(archive.read_bytes())}))
