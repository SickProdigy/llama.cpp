"""Verify saved evidence consistency, not private behavior or model reliability."""
from pathlib import Path,PurePosixPath
import hashlib,json,tarfile,statistics
R=Path(__file__).resolve().parent;archive=R/'native-q4-fresh-evidence.tar.gz';sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(archive.read_bytes())==(R/'native-q4-fresh-evidence.sha256').read_text().split()[0]
with tarfile.open(archive)as t:
 members=t.getmembers();assert all(m.isfile()and not PurePosixPath(m.name).is_absolute()and'..'not in PurePosixPath(m.name).parts for m in members);assert len({m.name for m in members})==len(members);files={m.name:t.extractfile(m).read()for m in members}
manifest=json.loads(files['manifest.json'])['sha256'];assert set(files)==set(manifest)|{'manifest.json'}
for name,digest in manifest.items():assert sha(files[name])==digest,name
for name in files:
 assert not any(part in ['profiles','baseline','AGENTS.md','state.db','receipt-key']for part in PurePosixPath(name).parts),name
 assert not name.endswith(('.request.json','.response.txt','/independent.log')),name
 assert not any(part.startswith('independent')for part in PurePosixPath(name).parts),name
j=lambda name:json.loads(files[name]);summary=j('summary.json');assert json.loads((R/'native-q4-fresh-summary.json').read_text())==summary
samples=[json.loads(line)for line in files['runtime/memory-samples.jsonl'].decode().splitlines()];good=[r for r in samples if all(k in r for k in ['total_cgroup_bytes','total_process_pss_bytes','total_cgroup_swap_bytes','host'])];m=summary['measurements'];assert len(samples)==m['sample_count']and len(good)==m['complete_aggregate_sample_count']
for field,raw in [('peak_observed_cgroup_bytes','total_cgroup_bytes'),('peak_observed_all_process_PSS_bytes','total_process_pss_bytes'),('peak_observed_experiment_swap_bytes','total_cgroup_swap_bytes')]:assert m[field]==max(r[raw]for r in good)
assert m['measurement_error_sample_count']==sum('measurement_error'in r for r in samples)
assert m['resource_guard_samples']==sum(bool(r.get('budget_guard_triggered'))for r in samples)
for direction in ['in','out']:assert m['global_pswp'+direction+'_delta_pages']==good[-1]['host']['pswp'+direction+'_pages']-good[0]['host']['pswp'+direction+'_pages']
records=[j(name)for name in sorted(files)if name.startswith('requests/')];complete=[r for r in records if r['capture_complete_without_transport_error']];assert len(records)==m['HTTP_records']and len(complete)==m['completed_HTTP_records_without_transport_error'];assert sum(r['client_transport_error_present']for r in records)==m['transport_error_record_count'];assert sum(not r['backend_body_complete']for r in records)==m['incomplete_backend_body_record_count']
latency=[r['end_epoch']-r['backend_start_epoch']for r in complete];assert m['HTTP_latency_seconds']==dict(min=min(latency),median=statistics.median(latency),max=max(latency),sum=sum(latency));assert m['maximum_completed_prompt_tokens']==max(r['usage'].get('prompt_tokens',0)for r in complete)
previous=None;roots=[]
for phase,count in enumerate([86,86,91]):
 prefix='phases/'+str(phase);local=j(prefix+'/local-grade/grade.json');remote=j(prefix+'/remote-grade/grade.json');assert local['source_digest']==remote['source_digest'];a=j(prefix+'/local-grade/source-sha256.json');b=j(prefix+'/remote-grade/source-sha256.json');assert a==b
 for kind in ['local-grade','remote-grade']:
  grade=j(prefix+'/'+kind+'/grade.json');assert all(grade[k]==0 for k in ['project_exit','preservation_exit','independent_exit']);assert grade['not_fed_to_models']
  assert str(count)+' passed'in files[prefix+'/'+kind+'/project.log'].decode();assert '83 passed'in files[prefix+'/'+kind+'/preservation.log'].decode()
 if previous is not None:
  changed=sorted(n for n in set(previous)|set(a)if previous.get(n)!=a.get(n));assert changed==(['announcer/README.md']if phase==1 else['announcer/README.md','announcer/__init__.py','tests/test_announcer.py'])
 previous=a;run=j(prefix+'/run.json');assert run['exit_code']==0 and not run['external_timeout'];roots.append(run['native_session_fingerprints']['logical_root']);forge=j(prefix+'/forge-readback.json');assert forge['scope_state']['issue']==3 and forge['scope_state']['pr']==4 and not forge['pr']['merged'];assert forge['pr']['head']['repo']=='hermes-agent/hermes-wide-q4-20261123'and forge['pr']['base']['repo']=='chatgpt-codex/hermes-wide-q4-20261123'
assert len(set(roots))==1
assert j('runtime/runtime-restoration.json')['restored'];assert j('audits/native-q4-fresh-preservation.json')['codex_entire_snapshot_unchanged'];assert j('audits/native-q4-fresh-owner-preservation.json')['passed'];assert j('audits/native-q4-fresh-cleanup.json')['passed']
audit=summary['independent_final_audit'];assert audit['audit_complete']and audit['not_actor_feedback']and audit['fresh_primary'];assert audit['README_pending_callback_reenable_qualification']and audit['final_answer_plugin_vs_project_test_scope_inaccurate']and audit['final_PR_description_updated_for_feature'];assert audit['test_issue_verified_closed']and audit['PR_preserved_open_unmerged']
result={'passed':True,'manifest_files':len(manifest),'memory_samples':len(samples),'HTTP_records':len(records),'completed_HTTP_records':len(complete),'private_behavior_not_reexecuted':True,'scope':'Saved evidence consistency only; independent source/behavior audits and private inputs remain separate. No autonomous reliability claim.'};(R/'native-q4-fresh-validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
