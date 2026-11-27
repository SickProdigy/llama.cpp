"""Verify saved IQ3 measurements and actual-source consistency; no model/behavior replay."""
from pathlib import Path,PurePosixPath
import ast,datetime,hashlib,json,sys,tarfile
p=Path(sys.argv[1]);files={};sha=lambda b:hashlib.sha256(b).hexdigest()
with tarfile.open(p)as t:
 for m in t:
  n=PurePosixPath(m.name);assert m.isfile()and not n.is_absolute()and'..'not in n.parts and m.name not in files and m.size<2*1024**2
  files[m.name]=t.extractfile(m).read()
assert sum(map(len,files.values()))<8*1024**2
read=lambda n:json.loads(files[n]);manifest=read('manifest.json');assert set(files)==set(manifest)|{'manifest.json'}
for n,h in manifest.items():assert sha(files[n])==h,n
s=read('summary.json');phases=read('observations/phases.json');rows=read('observations/memory.json');metrics=read('observations/request-metrics.json')
assert not s['whole_workflow_pass']and phases==s['phases']and len(phases)==3
assert abs(sum(x['coding_seconds']for x in phases)/60-s['coding_minutes'])<1e-9
assert all(x['CLI_exit']==0 and not x['external_timeout']and x['project_exit']==x['original_exit']==0 and x['independent_exit']==1 for x in phases)
assert len(rows)==s['resource']['samples']==198
assert not any(r.get('budget_guard_triggered')or'measurement_error'in r for r in rows)
for field,summary in [('total_cgroup_bytes','peak_aggregate_cgroup_bytes'),('total_process_pss_bytes','peak_process_PSS_bytes')]:assert max(r[field]for r in rows)==s['resource'][summary]<=8*1024**3
assert max(r['total_cgroup_swap_bytes']for r in rows)==s['resource']['peak_study_swap_bytes']==0
for field,summary in [('model_disk_free_bytes','minimum_disk_free_bytes'),('staging_disk_free_bytes','minimum_staging_free_bytes')]:assert min(r[field]for r in rows)==s['resource'][summary]>=100*1024**3
assert max(int(r['gpu_csv'].split(',')[0])for r in rows if r.get('gpu_csv','').split(',')[0].isdigit())==s['resource']['peak_GPU_MiB']==12904
assert len(metrics)==len({m['id']for m in metrics})==36
assert all(m.get('usage')and m['tools_exposed']and not m.get('transport_error')and not m.get('backend_http_status')and'length'not in m['finish_reasons']and m['usage']['total_tokens']<=98304 for m in metrics)
assert max(m['usage']['prompt_tokens']for m in metrics)==s['runtime_audit']['largest_completed_prompt']==47855
assert not s['runtime_audit']['auxiliary']and all(s['runtime_audit']['all_user_tasks_literal_in_final_main_request'])
state=read('observations/terminal-state.json');dt=lambda s:datetime.datetime.fromisoformat(s.replace('Z','+00:00'))
assert state['Status']=='exited'and not state['Running']and not state['OOMKilled']and state['ExitCode']==0
assert abs((dt(state['FinishedAt'])-dt(state['StartedAt'])).total_seconds()/60-s['supervisor_wall_minutes'])<1e-9
digest=lambda x:sha(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode())
base=files['published/baseline/beetsbridge/__init__.py'];assert base.count(b'self._stopping = False')==2
expected=base.replace(b'self._stopping = False',b'self._abandoned = False')
for i in range(3):
 label='phase'+str(i);index=read('published/'+label+'/index.json');assert len(index)==40 and digest(index)==phases[i]['source_digest']
 assert files['published/'+label+'/beetsbridge/__init__.py']==expected
 for n in ['beetsbridge/__init__.py','beetsbridge/README.md','tests/test_beetsbridge.py']:
  assert sha(files['published/'+label+'/'+n])==index[n]
  if n!='beetsbridge/__init__.py':assert files['published/'+label+'/'+n]==files['published/baseline/'+n]
 assert phases[i]['changed_paths']==['beetsbridge/__init__.py']and phases[i]['local_changed_paths']==[]
 assert phases[i]['source_digest']==phases[0]['source_digest']and phases[i]['captured_remote_head']==phases[0]['captured_remote_head']
 tree=ast.parse(expected);methods={n.name:n for c in tree.body if isinstance(c,ast.ClassDef)for n in c.body if isinstance(n,ast.FunctionDef)}
 assert any(isinstance(n,ast.Attribute)and n.attr=='_stopping'for n in ast.walk(methods['_timer_elapsed']))
 assert b'beetscancel'not in expected
assert len(read('observations/frozen-source-bindings.json'))==s['frozen_code_files_verified']==134
forge=read('observations/independent-final-forge.json');proof=forge['final_private_fork_source_proof'];pub=s['publication']
assert forge['actor_fork_GET_status']==200 and forge['actor_fork_is_fork']and forge['actor_fork_parent_id']==34354
assert forge['upstream_baseline_blobs_verified']==proof['all_actual_remote_blobs_verified']==40
assert proof['actual_blob_SHA256']==read('published/phase2/index.json')and proof['head']==pub['head_SHA']==phases[2]['captured_remote_head']
assert not forge['pull_requests']and pub['PR']is None and pub['published_authored_tests']==0 and not pub['README_changed']
assert forge['explicit_observed_issues']==[{'number':1,'state':'closed','creator':'hermes-agent','explicit_single_issue_GET':True}]
assert pub['issue_closed_single_get_verified']and s['strict_runtime_restored']and s['preservation']['codex_entire_snapshot_unchanged']and s['owner_preservation']['passed']and s['cleanup']['passed']
controls=read('audits/real-nicotine-controls.json')['results'];assert [x['passed']for x in controls[0]['results']]==[True,False,False,False]
assert all(x['passed']for x in controls[1]['results'])and not any(x['passed']for x in controls[-1]['results'])and controls[-1]['plugin_source_SHA256']==sha(expected)
assert all('_stopping'in x['error']for x in controls[-1]['results'][:3])
end=read('audits/native-endings-and-claims.json');assert [x['reported_failure_count']for x in end['phases']]==[8,5,5]
assert all(x['native_end_reason']=='repeated edit failure guard'and not x['generated_final_model_answer']for x in end['phases'])
assert 'Regression tests added in `tests/test_beetsbridge.py`'in end['issue_claim']['body']and end['issue_claim']['actual_tests_file_unchanged']
assert end['ordinary_gate_qualification']['actual_public_disable_call_failed']and not end['ordinary_gate_qualification']['private_heldout_grade_or_corrective_hint_fed_to_actor']
print(json.dumps({'passed':True,'archive_SHA256':sha(p.read_bytes()),'manifest_files':len(manifest),'whole_workflow_pass':False,'scope':'Saved observations and static published-source consistency only; not inference, full behavior replay, remote authentication replay, independent signature verification or autonomous reliability.'}))
