"""Verify saved evidence consistency, not private behavior or model reliability."""
from pathlib import Path,PurePosixPath
import hashlib,json,tarfile,statistics,sys
R=Path(__file__).resolve().parent;KEY,FAMILY=sys.argv[1:];assert KEY in ['q3','devstral','glm']and FAMILY in ['spam_enforcement','queued_announcements'];SHORT='spam'if FAMILY=='spam_enforcement'else'queue';LABEL='native-'+KEY+'-'+SHORT;RESTORE=('native-'+KEY+'-fresh-cp2/'+FAMILY).replace('/','-');MODULE='autospamignore'if FAMILY=='spam_enforcement'else'announcer';archive=R/(LABEL+'-evidence.tar.gz');sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(archive.read_bytes())==(R/(LABEL+'-evidence.sha256')).read_text().split()[0]
with tarfile.open(archive)as t:
 members=t.getmembers();assert all(m.isfile()and not PurePosixPath(m.name).is_absolute()and'..'not in PurePosixPath(m.name).parts for m in members);assert len({m.name for m in members})==len(members);files={m.name:t.extractfile(m).read()for m in members}
manifest=json.loads(files['manifest.json'])['sha256'];assert set(files)==set(manifest)|{'manifest.json'}
for name,digest in manifest.items():assert sha(files[name])==digest,name
for name in files:
 assert not any(part in ['profiles','baseline','AGENTS.md','state.db','receipt-key']for part in PurePosixPath(name).parts),name
 assert not name.endswith(('.request.json','.response.txt','/independent.log')),name
 assert not any(part.startswith('independent')for part in PurePosixPath(name).parts),name
j=lambda name:json.loads(files[name]);summary=j('summary.json');assert json.loads((R/(LABEL+'-summary.json')).read_text())==summary
samples=[json.loads(line)for line in files['runtime/memory-samples.jsonl'].decode().splitlines()];good=[r for r in samples if all(k in r for k in ['total_cgroup_bytes','total_process_pss_bytes','total_cgroup_swap_bytes','host'])];m=summary['measurements'];assert len(samples)==m['sample_count']and len(good)==m['complete_aggregate_sample_count']
for field,raw in [('peak_observed_cgroup_bytes','total_cgroup_bytes'),('peak_observed_all_process_PSS_bytes','total_process_pss_bytes'),('peak_observed_experiment_swap_bytes','total_cgroup_swap_bytes')]:assert m[field]==max(r[raw]for r in good)
assert m['measurement_error_sample_count']==sum('measurement_error'in r for r in samples)
assert m['resource_guard_samples']==sum(bool(r.get('budget_guard_triggered'))for r in samples)
for direction in ['in','out']:assert m['global_pswp'+direction+'_delta_pages']==good[-1]['host']['pswp'+direction+'_pages']-good[0]['host']['pswp'+direction+'_pages']
records=[j(name)for name in sorted(files)if name.startswith('requests/')];complete=[r for r in records if r['capture_complete_without_transport_error']];assert len(records)==m['HTTP_records']and len(complete)==m['completed_HTTP_records_without_transport_error'];assert sum(r['client_transport_error_present']for r in records)==m['transport_error_record_count'];assert sum(not r['backend_body_complete']for r in records)==m['incomplete_backend_body_record_count']
latency=[r['end_epoch']-r['backend_start_epoch']for r in complete];assert m['HTTP_latency_seconds']==dict(min=min(latency),median=statistics.median(latency),max=max(latency),sum=sum(latency));assert m['maximum_completed_prompt_tokens']==max(r['usage'].get('prompt_tokens',0)for r in complete)
audit=summary['independent_final_audit'];assert audit==j('audits/'+KEY+'-'+SHORT+'-final-audit.json');assert audit['audit_complete']and audit['not_actor_feedback']and audit['fresh_primary']
assert len(summary['phases'])==len(audit['observed_grades_by_phase'])==3
previous=None;roots=[];observed=[]
for phase in range(3):
 prefix='phases/'+str(phase);phase_summary=summary['phases'][phase];expected=audit['observed_grades_by_phase'][phase];assert 'local-grade'in expected
 kinds={k for k in ['local-grade','remote-grade']if prefix+'/'+k+'/grade.json'in files};assert kinds==set(expected)
 snapshots={}
 for kind in sorted(kinds):
  grade=j(prefix+'/'+kind+'/grade.json');assert grade==expected[kind]and grade['not_fed_to_models'];assert phase_summary[kind.replace('-','_')]==grade
  snapshots[kind]=j(prefix+'/'+kind+'/source-sha256.json')
  assert set(snapshots[kind])and all(len(v)==64 for v in snapshots[kind].values())
  for log in ['project.log','preservation.log']:
   raw=files[prefix+'/'+kind+'/'+log];assert sha(raw)==audit['test_log_sha256_by_phase'][phase][kind][log]
 assert phase_summary['remote_grade_absent']==('remote-grade'not in kinds)
 if 'remote-grade'in kinds:assert snapshots['local-grade']==snapshots['remote-grade']and expected['local-grade']['source_digest']==expected['remote-grade']['source_digest']
 else:assert phase_summary['remote_grade']is None
 current=snapshots['local-grade']
 if previous is not None:
  changed=sorted(n for n in set(previous)|set(current)if previous.get(n)!=current.get(n));assert changed==audit['source_changes_from_previous_phase'][phase]
 previous=current;run=j(prefix+'/run.json');assert run=={k:phase_summary[k]for k in run};roots.append(run['native_session_fingerprints']['logical_root'])
 assert run['elapsed_seconds']==audit['phase_actor_seconds'][phase]
 assert {k:run[k]for k in ['exit_code','external_timeout']}==audit['native_exit_by_phase'][phase]
 forge=j(prefix+'/forge-readback.json');assert forge==phase_summary['forge'];assert forge['scope_state']==audit['publication_scope_by_phase'][phase]
 if 'remote-grade'not in kinds:assert 'clone'not in forge
 if 'pr'in forge:assert not forge['pr']['merged']
 observed.append({kind:{k:expected[kind][k]for k in ['project_exit','preservation_exit','independent_exit']}for kind in sorted(kinds)})
posthoc_dispatch_source_checked=False
if 'controls/posthoc-dispatch-cleanup-result.json'in files:
 control=j('controls/posthoc-dispatch-cleanup-result.json');assert control['not_actor_feedback']and control['pinned_upstream_dispatcher_method_executed_without_body_changes'];assert control['source_sha256']==j('phases/2/local-grade/source-sha256.json')['announcer/__init__.py'];assert control['control_sha256']==sha(files['source/announcer_dispatch_cleanup_control.py']);pins={p['commit']:p for p in j('controls/upstream-dispatch-pins.json')if 'commit'in p}
 for row in control['results']:assert row['upstream_source_sha256']==pins[row['commit']]['sha256']and row['upstream_url']==pins[row['commit']]['url']
 posthoc_dispatch_source_checked=True
assert len(set(roots))==1 and roots[0]
restoration=j('runtime/runtime-restoration.json');assert restoration['restored'];before=j('runtime/runtime-before.json');after=restoration['after']
for service in before:
 for key in ['id','image','signature','running']:assert before[service][key]==after[service][key]
assert before['hermes-codex']==after['hermes-codex'];assert j('audits/'+RESTORE+'-preservation.json')['codex_entire_snapshot_unchanged'];assert j('audits/'+RESTORE+'-owner-preservation.json')['passed'];assert j('audits/'+LABEL+'-cleanup.json')['passed']
assert audit['publication_independently_audited']and audit['test_issue_cleanup_independently_verified']
result={'passed':True,'manifest_files':len(manifest),'memory_samples':len(samples),'HTTP_records':len(records),'completed_HTTP_records':len(complete),'private_behavior_not_reexecuted':True,'observed_grades_by_phase':observed,'posthoc_dispatch_source_fingerprint_checked':posthoc_dispatch_source_checked,'quality_classification':audit['classification'],'scope':'Saved bytes and observed outcome consistency only. Failed tests and absent publication remain failures/absence; not a coding-quality or autonomous-reliability certificate.'};(R/(LABEL+'-validation.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
