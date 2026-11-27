"""Saved-source and measurement consistency; no inference or behavioral replay."""
from pathlib import Path,PurePosixPath
import ast,datetime,hashlib,json,sys,tarfile
p=Path(sys.argv[1]);f={};sha=lambda b:hashlib.sha256(b).hexdigest()
with tarfile.open(p)as t:
 for m in t:
  n=PurePosixPath(m.name);assert m.isfile()and not n.is_absolute()and'..'not in n.parts and m.name not in f and m.size<3*1024**2;f[m.name]=t.extractfile(m).read()
assert sum(map(len,f.values()))<15*1024**2
r=lambda n:json.loads(f[n]);manifest=r('manifest.json');assert set(f)==set(manifest)|{'manifest.json'}
for n,h in manifest.items():assert sha(f[n])==h,n
s=r('summary.json');ph=r('observations/phases.json');mem=r('observations/memory.json');metrics=r('observations/request-metrics.json');assert not s['whole_workflow_pass']and ph==s['phases']and len(ph)==3
assert abs(sum(x['coding_seconds']for x in ph)/60-s['coding_minutes'])<1e-9
assert [x['exit_code']for x in ph]==[0,0,1]and all(not x['external_timeout']and x['project_exit']==x['preservation_exit']==0 and x['independent_exit']==1 for x in ph)
assert len(mem)==s['resource']['samples']==200
assert not any(x.get('budget_guard_triggered')or'measurement_error'in x for x in mem)
for a,b in [('total_cgroup_bytes','peak_aggregate_cgroup_bytes'),('total_process_pss_bytes','peak_process_PSS_bytes')]:assert max(x[a]for x in mem)==s['resource'][b]<=8*1024**3
assert max(x['total_cgroup_swap_bytes']for x in mem)==s['resource']['peak_study_swap_bytes']==0
for a,b in [('model_disk_free_bytes','minimum_disk_free_bytes'),('staging_disk_free_bytes','minimum_staging_free_bytes')]:assert min(x[a]for x in mem)==s['resource'][b]>=100*1024**3
assert max(int(x['gpu_csv'].split(',')[0])for x in mem if x.get('gpu_csv','').split(',')[0].isdigit())==s['resource']['peak_GPU_MiB']==8964
assert len(metrics)==len({x['id']for x in metrics})==115
assert all(x.get('usage')and not x.get('transport_error')and not x.get('backend_http_status')and'length'not in x['finish_reasons']and x['usage']['total_tokens']<=98304 for x in metrics)
assert max(x['usage']['prompt_tokens']for x in metrics)==s['runtime_audit']['largest_completed_prompt']==83321
assert sum(not x['tools_exposed']for x in metrics)==1 and s['runtime_audit']['auxiliary'][0]['literal_tool_markup']
assert all(s['runtime_audit']['all_user_tasks_literal_in_final_main_request'])
state=r('observations/terminal-state.json');dt=lambda x:datetime.datetime.fromisoformat(x.replace('Z','+00:00'));assert not state['Running']and not state['OOMKilled']and state['ExitCode']==0
assert abs((dt(state['FinishedAt'])-dt(state['StartedAt'])).total_seconds()/60-s['supervisor_wall_minutes'])<1e-9
digest=lambda x:sha(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode())
base=r('source/baseline/index.json');assert len(base)==40
for i in range(3):
 label='phase'+str(i);index=r('source/'+label+'/index.json');assert len(index)==42 and digest(index)==ph[i]['source_digest']
 for n,h in index.items():assert sha(f['source/'+label+'/'+n])==h,n
 assert sorted(n for n in set(index)|set(base)if index.get(n)!=base.get(n))==ph[i]['changed_paths']
module=f['source/phase2/beetsbridge/__init__.py'];tree=ast.parse(module);methods={x.name:x for c in tree.body if isinstance(c,ast.ClassDef)for x in c.body if isinstance(x,ast.FunctionDef)}
assert ast.dump(methods['_import_worker'])==ast.dump(next(n for c in ast.parse(f['source/baseline/beetsbridge/__init__.py']).body if isinstance(c,ast.ClassDef)for n in c.body if isinstance(n,ast.FunctionDef)and n.name=='_import_worker'))
assert not any(isinstance(x,ast.Attribute)and x.attr=='_disabled'for x in ast.walk(methods['_import_worker']))
base_methods={n.name:n for c in ast.parse(f['source/baseline/beetsbridge/__init__.py']).body if isinstance(c,ast.ClassDef)for n in c.body if isinstance(n,ast.FunctionDef)}
for name in ['disable','shutdown_notification','loaded_notification','_schedule','_timer_elapsed','_import_worker','_validated_folder']:assert ast.dump(methods[name])==ast.dump(base_methods[name])
tests=lambda data:{(c.name,n.name):ast.dump(n)for c in ast.parse(data).body if isinstance(c,ast.ClassDef)for n in c.body if isinstance(n,ast.FunctionDef)and n.name.startswith('test_')}
original_tests=tests(f['source/baseline/tests/test_beetsbridge.py']);assert len(original_tests)==8
for i,total in enumerate([14,14,19]):
 current=tests(f['source/phase'+str(i)+'/tests/test_beetsbridge.py']);assert len(current)==total and all(current.get(k)==v for k,v in original_tests.items())

assert b'beetscancel'in module and b'del self._pending[pending_folder]'in module
forge=r('observations/forge.json');assert forge==s['forge']and forge['actor_fork_GET_status']==404 and forge['upstream_baseline_blobs_verified']==40 and not forge['issues']and not forge['pull_requests']and not forge['explicit_observed_issues']
assert s['preservation']['Codex_full_recorded_state_unchanged']and s['owner_preservation']['passed']and s['cleanup']['passed']
controls=r('audits/real-nicotine.json')['results'];assert [x['passed']for x in controls[0]['results']]==[True,False,False,False]and all(x['passed']for x in controls[1]['results'])and [x['passed']for x in controls[-1]['results']]==[True,False,False,True]and controls[-1]['plugin_source_SHA256']==sha(module)
claims=r('audits/final-claims.json');assert len(claims)==3
for c in claims:assert sha(c['final_text'].encode())==c['final_text_SHA256']
review=r('audits/semantic-review.json');assert not review['whole_workflow_pass'];assert 'maximum number of tool-calling iterations'in review['forced_final_request']['native_framework_message'];assert 'complete'in claims[0]['final_text']and 'Blocker:'in claims[2]['final_text']
assert review['native_endings'][2]['native_end_reason']=='tool-calling iteration cap with generated final response'
assert len(r('observations/frozen-code-bindings.json'))==135
assert s['model']['sha256']=='21aa4b0b28090469e8a319c889451df2f1ea6aad27ac3818c8c8a86f86d5bc9e'and s['model']['bytes']==8465553920
print(json.dumps({'passed':True,'archive_SHA256':sha(p.read_bytes()),'manifest_files':len(manifest),'whole_workflow_pass':False,'scope':__doc__}))
