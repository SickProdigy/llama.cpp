"""Check saved evidence consistency and source bindings; does not rerun private model/grader inputs."""
from pathlib import Path,PurePosixPath
import json,hashlib,tarfile,copy,sys
sha=lambda b:hashlib.sha256(b).hexdigest()
def validate(files):
 read=lambda n:json.loads(files[n]);manifest=read('manifest.json');assert set(files)==set(manifest)|{'manifest.json'}
 for n,h in manifest.items():assert sha(files[n])==h,n
 s=read('summary.json');final=s['independent_final_audit'];assert final['audit_complete']and not final['overall_workflow_passed'];assert all(final[k]is False for k in ['initial_repair_passed','documentation_passed','feature_passed','publication_passed','semantic_summary_passed']);assert final['cold_independent_MCP_qualification_not_established']
 protocol=read('controls/protocol.json');fingerprints=protocol['private_code_fingerprints']
 for name in ['reasoning_native_controller.py','model_cache_probe.py','resolve_native_oneshot.py','reasoning_runtime_wire_preflight.py']:assert sha(files['source/'+name])==fingerprints[name]
 for name in ['scope_proxy.py','llm_proxy.py']:assert sha(files['source/harness/'+name])==fingerprints['harness/'+name]
 pin=read('controls/model-pin.json');assert s['model']['sha256']==pin['sha256']and s['model']['bytes']==pin['expected_bytes'];assert read('runtime/model-identity.json')==s['model'];assert read('runtime/runtime-restoration.json')['restored']and read('audits/cleanup.json')['passed'];assert read('audits/preservation.json')['codex_entire_snapshot_unchanged'];assert read('audits/owner-preservation.json')['passed']
 ready=files['runtime/backend-ready-placement.log'];assert sha(ready)==read('runtime/placement-check.json')['log_sha256'];assert b'offloaded 41/41 layers to GPU'in ready
 requests=[read(n)for n in sorted(files)if n.startswith('requests/')and n.endswith('.json')];assert len(requests)==134 and all(r['backend_complete']and not r['transport_error_present']for r in requests);assert sum(r['purpose']=='compression'for r in requests)==1;assert all('length'not in r['finish_reasons']for r in requests);assert max(r['usage']['prompt_tokens']for r in requests)==s['runtime']['maximum_completed_main_prompt_tokens']==81965
 assert all(r['usage']['prompt_tokens']+r['usage']['completion_tokens']<=98304 for r in requests);assert [r['id']for r in requests if not r['requested_full_output_cap_fits']]==[95];assert min(r['actual_context_headroom']for r in requests)==16339
 rows=[json.loads(x)for x in files['runtime/memory-samples.jsonl'].splitlines()];m=s['runtime']['measurements'];assert len(rows)==m['samples']==m['complete_samples']==234
 for field,reported in [('total_cgroup_bytes','peak_aggregate_cgroup_bytes'),('total_process_pss_bytes','peak_process_PSS_bytes'),('total_cgroup_swap_bytes','peak_study_swap_bytes')]:assert max(r[field]for r in rows)==m[reported]
 assert max(int(r['gpu_csv'].split(',')[0])for r in rows if r.get('gpu_csv'))==m['peak_GPU_MiB']==8964;assert m['peak_study_swap_bytes']==m['guard_samples']==m['measurement_errors']==0;assert m['peak_aggregate_cgroup_bytes']<=8*1024**3
 phases=s['runtime']['phases'];assert abs(sum(p['elapsed_seconds']for p in phases if p['phase']>=0)-s['runtime']['coding_elapsed_seconds'])<1e-6;assert all(not p['external_timeout']for p in phases)
 coding=[p for p in phases if p['phase']>=0];assert all(p['CLI_resume_handle_SHA256']==coding[0]['CLI_resume_handle_SHA256']for p in coding);assert coding[-1]['physical_segments']==2 and coding[-1]['CLI_resume_handle_SHA256']!=coding[-1]['physical_effective_tip_SHA256']
 for phase,totals in [(0,'2 failed, 86 passed, 2 subtests passed'),(1,'2 failed, 86 passed, 2 subtests passed'),(2,'4 failed, 90 passed, 2 subtests passed')]:
  g=read(f'phases/{phase}/grade.json');assert g['project_exit']==g['independent_exit']==1 and g['preservation_exit']==0;assert totals.encode()in files[f'phases/{phase}/project.log'];assert b'83 passed, 2 subtests passed'in files[f'phases/{phase}/preservation.log']
 pub=read('audits/publication-independent-readback.json');branch=json.loads(read('remote/connected-final-branches.json')['content'][0]['text']);before=read('controls/fixture-admission.json');assert branch[0]['commit_sha']==before['main_revision'];assert json.loads(read('remote/connected-final-issues.json')['content'][0]['text'])==json.loads(read('remote/connected-final-prs.json')['content'][0]['text'])==[];assert read('audits/fork-independent-readback.json')['actor_auth_fork_GET_status']==pub['actor_auth_own_fork_GET_status']==404;assert not pub['final_actor_publication_claim_supported']
 coupling=s['MCP_read_control_coupling'];assert coupling['read_control_proxy_wrong_target_errors']==3 and coupling['native_rejection_count_at_first_coding_pause']==4 and coupling['next_native_rejection_count']==5;assert s['independent_initial_audit']['MCP_fresh_independent_health_not_established']
 aux=s['auxiliary_semantic_audit'];assert not aux['semantic_summary_passed']and aux['model_output_embedded_in_next_main_reference_context']and aux['all_three_user_requests_retained_verbatim'];assert aux['auxiliary_usage']==next(r['usage']for r in requests if r['id']==96);assert aux['auxiliary_usage']['completion_tokens']==85
 fresh=read('audits/cancel-reschedule-control.json');assert fresh['reference_positive']and not fresh['candidate_passed'];assert s['independent_feature_audit']['plugin_collected']==19 and s['independent_feature_audit']['plugin_passed']==15;assert read('controls/excluded-preactor-setup-failure.json')['model_calls']==0
 return s
if __name__=='__main__':
 a=Path(sys.argv[1]);files={}
 with tarfile.open(a)as t:
  for m in t:
   p=PurePosixPath(m.name);assert m.isfile()and not p.is_absolute()and'..'not in p.parts and m.name not in files;files[m.name]=t.extractfile(m).read()
 validate(files);controls={}
 edits={'false_workflow_pass':lambda s:s['independent_final_audit'].update(overall_workflow_passed=True),'hidden_summary_failure':lambda s:s['auxiliary_semantic_audit'].update(semantic_summary_passed=True),'hidden_read_control_coupling':lambda s:s['MCP_read_control_coupling'].update(native_rejection_count_at_first_coding_pause=1)}
 for name,edit in edits.items():
  bad=copy.deepcopy(files);s=json.loads(bad['summary.json']);edit(s);bad['summary.json']=json.dumps(s).encode();manifest=json.loads(bad['manifest.json']);manifest['summary.json']=sha(bad['summary.json']);bad['manifest.json']=json.dumps(manifest).encode()
  try:validate(bad)
  except AssertionError:controls[name]=True
  else:raise AssertionError('Altered evidence accepted: '+name)
 print(json.dumps({'passed':True,'archive_SHA256':sha(a.read_bytes()),'files_checked':len(files),'coherently_rehashed_negative_controls_rejected':controls,'scope':'Saved consistency/source bindings only; private model/grader behavior not replayed'},indent=2))
