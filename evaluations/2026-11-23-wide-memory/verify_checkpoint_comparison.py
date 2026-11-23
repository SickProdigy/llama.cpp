"""Offline integrity/measurement audit, not a rerun or model-quality certificate."""
from pathlib import Path,PurePosixPath
import argparse,json,hashlib,re
p=argparse.ArgumentParser();p.add_argument('--root',required=True,type=Path);R=p.parse_args().root
sha=lambda b:hashlib.sha256(b).hexdigest();manifest=json.loads((R/'manifest.json').read_text())['sha256']
for n,h in manifest.items():
 f=PurePosixPath(n);assert not f.is_absolute()and'..'not in f.parts
 assert f.name not in ['request.json','backend.log','state.db','receipt-key','.env','auth.json','tasks.json','initial_checks.py','feature_checks.py']
 path=R/n;assert path.is_file()and not path.is_symlink()and sha(path.read_bytes())==h,n
reg=json.loads((R/'controls/cache-controller-registration.json').read_text());assert sha((R/'source/cache_capacity_controller.py').read_bytes())==reg['controller_sha256'];assert sha((R/'controls/cache-capacity-protocol.json').read_bytes())==reg['protocol_sha256']
identity=json.loads((R/'controls/cache-input-identity.json').read_text());assert identity['captured_requests']==12 and identity['unique_prompt_histories']==11
results=[]
for arm,count,oom in [('32',10,True),('2',12,False)]:
 root=R/arm;s=json.loads((root/'summary.json').read_text());assert s['completed_prefix_replays']==count and s['oom_killed_at_cleanup_snapshot']is oom and s['not_model_quality']
 argv=json.loads((root/'layout/launch.json').read_text())['argv']
 for k,v in [('--memory','6656m'),('--memory-swap','6656m'),('--ctx-size','98304'),('--ctx-checkpoints',arm),('-ngl','56'),('--cache-ram','512'),('--load-mode','none')]:assert argv[argv.index(k)+1]==v
 rows=[json.loads(line)for line in(root/'layout/samples.jsonl').read_text().splitlines()];cgs=[];pss=[];errors=0
 for row in rows:
  if row.get('measurement_error'):errors+=1;continue
  total_cg=0;total_pss=0
  for key in ['backend_memory_raw','supervisor_memory_raw']:
   raw=row[key];m=re.search(r'FILE /sys/fs/cgroup/memory.current\n(\d+)',raw);assert m;total_cg+=int(m.group(1));m=re.search(r'^Pss:\s*(\d+) kB',raw,re.M);assert m;total_pss+=int(m.group(1))*1024
   m=re.search(r'FILE /sys/fs/cgroup/memory.swap.current\n(\d+)',raw);assert m and int(m.group(1))==0
  assert row['aggregate_cgroup_current_bytes']==total_cg;assert row['aggregate_process_pss_bytes']==total_pss;cgs.append(total_cg);pss.append(total_pss)
 assert len(rows)==s['memory_sample_count'];assert max(cgs)==s['sampled_peak_aggregate_cgroup_bytes'];assert max(pss)==s['sampled_peak_main_plus_supervisor_PSS_bytes'];assert cgs and len(cgs)>=len(rows)*.9
 fragments=json.loads((root/'checkpoint-trace.json').read_text())['safe_numeric_fragments'];parsed=[]
 for f in fragments:
  m=re.fullmatch(r'created context checkpoint (\d+) of (\d+) \(pos_min = -?\d+, pos_max = -?\d+, n_tokens = \d+, size = ([0-9.]+) MiB\)',f['fragment']);assert m;assert m.group(2)==arm;parsed.append({'count':int(m.group(1)),'cap':int(m.group(2)),'size_MiB':float(m.group(3))})
 assert parsed==s['checkpoint_events'];assert max(v['count']for v in parsed)==s['max_checkpoint_count_observed']
 for c in s['captures']:
  q=root/'captures'/c['probe'];raw=(q/'response.bin').read_bytes();body=json.loads(raw);cap=json.loads((q/'capture.json').read_text());inp=json.loads((q/'input.json').read_text());assert sha(raw)==cap['response_sha256']==c['response_sha256'];assert cap['body_complete'];assert cap['usage']==body['usage']==c['usage'];assert body['usage']['prompt_tokens']==inp['rendered_tokens']==c['input_tokens'];assert body['usage']['completion_tokens']<=1
 state=json.loads((root/'layout/exit-state.json').read_text());assert state['oom_killed']is oom;assert state['memory_limit']==state['memory_swap_limit']==int(6.5*1024**3)
 assert json.loads((root/'runtime/runtime-restoration.json').read_text())['restored'];assert json.loads((root/'controls/preservation.json').read_text())['all_30_model_metadata_unchanged']
 results.append({'arm':int(arm),'complete_responses':count,'samples':len(rows),'measurement_errors':errors,'OOMKilled':oom})
assert results[0]['OOMKilled']and not results[1]['OOMKilled']
print(json.dumps({'passed':True,'manifest_files':len(manifest),'arms':results,'private_prompt_bodies_not_reconstructed':True,'not_model_quality_or_full_native_fit':True},indent=2))
