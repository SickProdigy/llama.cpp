"""Verify saved observations and audit bindings; does not rerun private behavior tests."""
from pathlib import Path,PurePosixPath
import hashlib,json,sys,tarfile,re
sha=lambda b:hashlib.sha256(b).hexdigest()
archive=Path(sys.argv[1]);files={}
with tarfile.open(archive)as tar:
 for m in tar:
  p=PurePosixPath(m.name);assert m.isfile()and not p.is_absolute()and'..'not in p.parts and m.name not in files;files[m.name]=tar.extractfile(m).read()
read=lambda p:json.loads(files[p]);manifest=read('manifest.json');assert set(files)==set(manifest)|{'manifest.json'}
for p,h in manifest.items():assert sha(files[p])==h,p
s=read('summary.json');key='adapted-iq4';label='native-'+key+'-beets';assert s['candidate_key']==key and len(s['phases'])==3
protocol=read('controls/protocol.json');assert protocol['context']==65536 and protocol['candidate']==key
assert protocol['private_code_fingerprints']['iq4_native_controller.py']==sha(files['source/iq4_native_controller.py'])
assert read('runtime/placement-check.json')['observed_layer_counts']==[['66','66']]
assert read('runtime/placement-check.json')['all_layers_offloaded']and read('runtime/placement-check.json')['automatic_fit_disabled']
identity=read('runtime/model-identity.json');assert identity==s['model']and identity['sha256']=='d25b50a2bfdfba157c2baf959f298d706d70083255bab95232ffcd40fbafcaba'and identity['bytes']==15321491104
launch=read('runtime/backend-launch.json');args=launch['argv'];assert launch['props']['default_generation_settings']['n_ctx']==65536
for flag,value in [('--ctx-size','65536'),('-ngl','99'),('-ub','64'),('--fit','off'),('--cache-type-k','q4_0'),('--cache-type-v','q4_0'),('--load-mode','none')]:assert args[args.index(flag)+1]==value
assert read('runtime/runtime-restoration.json')['restored']and read('audits/cleanup.json')['passed']
for name in ['preservation','owner-preservation']:
 audit=read('audits/native-'+key+'-beets_lifecycle-'+name+'.json')
 for n,v in audit.items():
  if isinstance(v,bool):assert v,(name,n)
phase_audits=['initial-manual-audit','README-manual-audit','feature-manual-audit']
for index,phase in enumerate(s['phases']):
 run=read('phases/'+str(index)+'/run.json');assert all(phase[k]==v for k,v in run.items());assert run['phase']==index
 audit=read('audits/'+key+'-beets-'+phase_audits[index]+'.json');assert audit['audit_complete']and audit['not_actor_feedback']
 kind='remote-grade'if phase['remote_grade']is not None else'local-grade';grade=read('phases/'+str(index)+'/'+kind+'/grade.json');hashes=read('phases/'+str(index)+'/'+kind+'/source-sha256.json');assert audit['source_digest']==grade['source_digest']and audit['source_SHA256']==hashes
 for k in ['local-grade','remote-grade']:
  if phase[k.replace('-','_')]is not None:assert phase[k.replace('-','_')]==read('phases/'+str(index)+'/'+k+'/grade.json')
final=read('audits/'+key+'-beets-final-audit.json');assert final==s['independent_final_audit']and final['audit_complete']and final['not_actor_feedback']
context=read('audits/'+key+'-beets-context-instruction-audit.json');assert context['audit_complete']and context['operator_continuations_or_corrective_hints']==0
assert final['initial_repair_completed']and not final['feature_completed']and not final['requested_README_update_completed']and not final['remote_publication_completed']and not final['overall_workflow_completed_correctly']
assert read('phases/2/local-grade/grade.json')['independent_exit']==1
assert not read('audits/'+key+'-beets-feature-manual-audit.json')['feature_completed']
for index,phase in enumerate(s['phases']):
 observed=next(r for r in context['phases']if r['phase']==index);fp=phase['native_session_fingerprints'];assert fp['cli_resume_handle']==observed['CLI_resume_handle_SHA256']and fp['effective_sid']==observed['physical_effective_SID_SHA256']and fp['incoming_sid']==observed['incoming_CLI_handle_SHA256'];assert fp['cli_resume_handle']==fp['logical_root']
paths={'native-adapted-iq4-beets-cleanup.json':'audits/cleanup.json','iq4-context-semantic-audit.json':'controls/context-semantic-audit.json','iq4-compression-runtime-diagnosis.json':'controls/actual-compression-timeout-diagnosis.json','iq4-buffer-placement-breakdown.json':'runtime/initial-buffer-placement-breakdown.json','iq4-test-helper-accounting-audit.json':'runtime/test-helper-accounting.json','aux-budget-getter-controls.json':'controls/aux-budget-getter-controls.json'}
for name,digest in final['evidence_SHA256'].items():
 target=paths.get(name)
 if target is None:
  target=('controls/'if '-test-adequacy/'in name else'audits/')+name
 assert target in files and sha(files[target])==digest,(name,target)

rows=[json.loads(l)for l in files['runtime/memory-samples.jsonl'].decode().splitlines()];good=[r for r in rows if all(k in r for k in ['total_cgroup_bytes','total_process_pss_bytes','total_cgroup_swap_bytes','host'])];m=s['measurements'];assert m['sample_count']==len(rows)and m['complete_aggregate_sample_count']==len(good)
for field,raw in [('peak_observed_cgroup_bytes','total_cgroup_bytes'),('peak_observed_all_process_PSS_bytes','total_process_pss_bytes'),('peak_observed_experiment_swap_bytes','total_cgroup_swap_bytes')]:assert m[field]==max(r[raw]for r in good)
assert m['peak_GPU_MiB']==max(int(r['gpu_csv'].split(',')[0])for r in good if r.get('gpu_csv'))
assert m['resource_guard_samples']==sum(bool(r.get('budget_guard_triggered'))for r in rows)
for field,raw in [('minimum_model_disk_free_bytes','model_disk_free_bytes'),('minimum_staging_disk_free_bytes','staging_disk_free_bytes')]:assert m[field]==min(r[raw]for r in good)>=100*1024**3
requests=[read(p)for p in files if p.startswith('requests/')];assert len(requests)==m['HTTP_records']==context['HTTP_records']
incomplete=[r for r in requests if not r['backend_body_complete']or r['transport_error_present']]
assert {47,49}.issubset({r['id']for r in incomplete})and not context['all_HTTP_complete']
assert m['incomplete_HTTP_records']==len(incomplete)==len(context['incomplete_HTTP_records'])
assert m['incomplete_backend_seconds']==sum(r['end_epoch']-r['backend_start_epoch']for r in incomplete)
diagnosis=read('controls/actual-compression-timeout-diagnosis.json');assert diagnosis['observed_effective_idle_seconds']==300 and diagnosis['observed_effective_total_ceiling_seconds']==600
assert diagnosis['native_deterministic_fallback']['failure_class']=='stall_deterministic_fallback'and diagnosis['native_deterministic_fallback']['commit_status']=='committed'and diagnosis['native_deterministic_fallback']['actual_next_main_message_count']==31
assert diagnosis['native_deterministic_fallback']['operator_stop_or_continuation_count']==0
for failure in [diagnosis['summary_record'],diagnosis['second_identical_summary_record']]:
 observed=next(r for r in incomplete if r['id']==failure['id']);assert observed['received_epoch']==failure['received_epoch']and observed['end_epoch']==failure['end_epoch']
buffers=read('runtime/initial-buffer-placement-breakdown.json');assert buffers['source_ready_log_SHA256']==read('runtime/placement-check.json')['log_sha256']
parsed=[]
for line in buffers['exact_buffer_lines']:
 match=re.search(r'(CUDA0|CUDA_Host)\s+(model|output|KV|rotation|RS|compute) buffer size =\s*([0-9.]+) MiB',line);assert match;parsed.append({'backend':match[1],'kind':match[2],'MiB':float(match[3])})
assert parsed==buffers['buffers']and any(r['backend']=='CUDA_Host'and r['kind']=='model'and r['MiB']>0 for r in parsed)
assert s['coding_elapsed_seconds']==sum(p['elapsed_seconds']for p in s['phases'])
assert context['largest_completed_prompt_tokens']==m['maximum_completed_prompt_tokens']
print(json.dumps({'passed':True,'archive_SHA256':sha(archive.read_bytes()),'files':len(files),'saved_evidence_consistency_only':True,'not_private_behavior_test_reexecution':True}))
