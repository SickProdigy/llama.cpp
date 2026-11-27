"""Verify saved measurements and published-source facts; no inference or behavior replay."""
from pathlib import Path, PurePosixPath
import ast, datetime, hashlib, json, sys, tarfile
p=Path(sys.argv[1]);files={};sha=lambda b:hashlib.sha256(b).hexdigest()
with tarfile.open(p)as t:
 for m in t:
  n=PurePosixPath(m.name)
  assert m.isfile()and not n.is_absolute()and'..'not in n.parts and m.name not in files and m.size<2*1024**2
  files[m.name]=t.extractfile(m).read()
assert sum(map(len,files.values()))<8*1024**2
read=lambda n:json.loads(files[n]);manifest=read('manifest.json')
assert set(files)==set(manifest)|{'manifest.json'}
for n,h in manifest.items():assert sha(files[n])==h,n
s=read('summary.json');rows=read('observations/memory.json');metrics=read('observations/request-metrics.json');phases=read('observations/phases.json')
assert not s['whole_workflow_pass']and len(phases)==3 and phases==s['phases']
assert abs(sum(x['coding_seconds']for x in phases)/60-s['coding_minutes'])<1e-9
assert all(x['CLI_exit']==0 and not x['external_timeout'] and x['independent_exit']==1 for x in phases)
assert len(rows)==s['resource']['samples']==634
assert not any(r.get('budget_guard_triggered')or'measurement_error'in r for r in rows)
assert max(r['total_cgroup_bytes']for r in rows)==s['resource']['peak_aggregate_cgroup_bytes']<=8*1024**3
assert max(r['total_process_pss_bytes']for r in rows)==s['resource']['peak_process_PSS_bytes']<=8*1024**3
assert max(r['total_cgroup_swap_bytes']for r in rows)==s['resource']['peak_study_swap_bytes']==0
assert min(r['model_disk_free_bytes']for r in rows)==s['resource']['minimum_disk_free_bytes']>=100*1024**3
assert min(r['staging_disk_free_bytes']for r in rows)==s['resource']['minimum_staging_free_bytes']>=100*1024**3
assert max(int(r['gpu_csv'].split(',')[0])for r in rows if r.get('gpu_csv','').split(',')[0].isdigit())==s['resource']['peak_GPU_MiB']==15926
assert len(metrics)==67 and len({m['id']for m in metrics})==67
assert all(m.get('usage')and not m.get('transport_error')and not m.get('backend_http_status')for m in metrics)
assert max(m['usage']['prompt_tokens']for m in metrics)==s['runtime_audit']['largest_completed_prompt']==81911
assert all(m['usage']['total_tokens']<=98304 and'length'not in m['finish_reasons']for m in metrics)
assert [m['id']for m in metrics if not m['tools_exposed']]==[57]
byid={m['id']:m for m in metrics};elapsed=lambda i:(byid[i]['end_epoch']-byid[i]['received_epoch'])/60
assert abs(elapsed(57)-s['compression_minutes'])<1e-9
assert abs(elapsed(58)-s['first_resumed_main_minutes'])<1e-9
assert abs(elapsed(57)+elapsed(58)-s['compression_plus_first_resumed_minutes'])<1e-9
assert byid[57]['usage']['prompt_tokens']==35054 and byid[57]['usage']['completion_tokens']==3311
assert byid[57]['finish_reasons']==['stop'] and byid[57]['usage']['prompt_tokens_details']['cached_tokens']==0
assert byid[58]['tools_exposed']and byid[58]['usage']['prompt_tokens_details']['cached_tokens']==0
state=read('observations/terminal-state.json');dt=datetime.datetime.fromisoformat
assert state['Status']=='exited'and not state['Running']and not state['OOMKilled']
assert abs((dt(state['FinishedAt'].replace('Z','+00:00'))-dt(state['StartedAt'].replace('Z','+00:00'))).total_seconds()/60-s['supervisor_wall_minutes'])<1e-9
def digest(index):return sha(json.dumps(index,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode())
def methods(label):
 tree=ast.parse(files['published/'+label+'/beetsbridge/__init__.py'])
 return {n.name:n for c in tree.body if isinstance(c,ast.ClassDef)for n in c.body if isinstance(n,ast.FunctionDef)}
base=methods('baseline')
for i in range(3):
 label='phase'+str(i);index=read('published/'+label+'/index.json');assert len(index)==40 and digest(index)==phases[i]['source_digest']
 for n in ['beetsbridge/__init__.py','beetsbridge/README.md','tests/test_beetsbridge.py']:
  assert sha(files['published/'+label+'/'+n])==index[n]
 assert files['published/'+label+'/tests/test_beetsbridge.py']==files['published/baseline/tests/test_beetsbridge.py']
 ms=methods(label);worker=ms['_import_worker'];assert len(worker.args.args)==2 and worker.args.vararg is None
 assert ast.dump(worker,include_attributes=False)==ast.dump(base['_import_worker'],include_attributes=False)
 calls=[x for x in ast.walk(ms['_timer_elapsed'])if isinstance(x,ast.Call)and isinstance(x.func,ast.Attribute)and x.func.attr=='Thread']
 assert len(calls)==1
 args=next(k.value for k in calls[0].keywords if k.arg=='args');assert isinstance(args,ast.Tuple)and len(args.elts)==2
 assert b'beetscancel'not in files['published/'+label+'/beetsbridge/__init__.py']
assert phases[1]['source_digest']==phases[2]['source_digest']
assert len(read('observations/frozen-source-bindings.json'))==s['frozen_code_files_verified']==132
pub=s['publication'];pr=read('observations/PR-single-get.json');issue=read('observations/issue-single-get.json');forge=read('observations/independent-forge.json')
assert issue['state']=='closed'and issue['number']==1 and issue['user']=='hermes-agent'
assert pr['head']['sha']==pub['head_SHA']==phases[2]['captured_remote_head']
assert pr['state']=='open'and not pr['merged']and forge['upstream_baseline_blobs_verified']==40
assert pub['published_authored_tests']==0 and pub['issue_closed_single_get_verified']
q=s['preservation'];assert q['required_configuration_models_profiles_owner_invariants_passed']and not q['strict_preservation_passed']and not q['codex_entire_snapshot_unchanged']
assert s['restoration_qualification']['Codex_changed_fields']==['started']and s['cleanup']['passed']and s['owner_preservation']['passed']
assert 'hermes-codex'in s['strict_restoration_error']['traceback']
controls=read('audits/real-nicotine-controls.json')['results']
assert [x['passed']for x in controls[0]['results']]==[True,False,False,False]
assert all(x['passed']for x in controls[1]['results'])and not any(x['passed']for x in controls[-1]['results'])
assert controls[-1]['plugin_source_SHA256']==sha(files['published/phase2/beetsbridge/__init__.py'])
aux=read('audits/current-iq4-r2-completed-aux57-history-boundary-audit.json');assert all(aux['all_three_literal_user_tasks_retained'])
assert aux['historical_prefix_boundary']=={'auxiliary_input_contains_PR2_URL':False,'auxiliary_input_contains_published_phase1_README_heading':False,'resumed_main_contains_PR2_URL':True,'resumed_main_contains_published_phase1_README_heading':True}
print(json.dumps({'passed':True,'archive_SHA256':sha(p.read_bytes()),'manifest_files':len(manifest),'whole_workflow_pass':False,'scope':'Saved observations plus static published-source consistency; not inference, complete behavior replay, independent signature verification, or an autonomous reliability rate.'}))
