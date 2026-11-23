"""Offline source/capture/memory consistency, not model correctness or new inference."""
from pathlib import Path,PurePosixPath
import argparse,json,hashlib,re
p=argparse.ArgumentParser();p.add_argument('--root',required=True,type=Path);root=p.parse_args().root
manifest=json.loads((root/'manifest.json').read_text())['sha256']
for name,digest in manifest.items():
 path=PurePosixPath(name);assert not path.is_absolute()and'..'not in path.parts
 assert not any(x in name for x in ['receipt-key','auth.json','.env','tasks.json','initial_checks.py','feature_checks.py'])
 f=root/name;assert f.is_file()and not f.is_symlink()and hashlib.sha256(f.read_bytes()).hexdigest()==digest,name
registration=json.loads((root/'controls/resource-controller-v2-registration.json').read_text())
assert hashlib.sha256((root/'source/resource_controller_v2.py').read_bytes()).hexdigest()==registration['controller_sha256']
assert hashlib.sha256((root/'controls/resource-protocol-v2.json').read_bytes()).hexdigest()==registration['protocol_sha256']
summary=json.loads((root/'controls/resource-v2-baseline-summary.json').read_text());assert summary['registered_sampled_resident_budget_met'] and not summary['resident_or_host_guard_triggered']
rows=[json.loads(line)for line in(root/'layout/samples.jsonl').read_text().splitlines()];pss=[];gpu=[]
for row in rows:
 raw=row['backend_memory_raw'];m=re.search(r'^Pss:\s*(\d+) kB',raw,re.M)
 if m:pss.append(int(m.group(1))*1024)
 swap=re.search(r'FILE /sys/fs/cgroup/memory.swap.current\n(\d+)',raw);assert swap and int(swap.group(1))==0
 try:gpu.append(int(row['gpu_csv'].split(',')[1]))
 except(ValueError,KeyError,IndexError):pass
assert max(pss)==summary['layouts'][0]['memory_peak_bytes']['Pss']<=8*1024**3
assert max(gpu)==summary['layouts'][0]['gpu_peak_used_MiB']
launch=json.loads((root/'layout/launch.json').read_text())['argv'];assert launch[launch.index('--load-mode')+1]=='none';assert launch[launch.index('-ngl')+1]=='999'
assert all(not x.get('resident_budget_guard_triggered') and not x.get('host_memory_guard_triggered') for x in rows)
probes=0
for name in ['tool','prompt16000','prompt60000']:
 q=root/'probes'/name;req=json.loads((q/'request.json').read_text());cap=json.loads((q/'capture.json').read_text());raw=(q/'response.bin').read_bytes();body=json.loads(raw);i=json.loads((q/'input.json').read_text());assert hashlib.sha256(raw).hexdigest()==cap['response_sha256'];assert cap['body_complete'];assert cap['usage']==body['usage'];assert body['usage']['prompt_tokens']==i['rendered_tokens'];assert cap['finish_reason']==body['choices'][0]['finish_reason'];assert req['max_tokens']==512 and req['seed']==20261123
 if name=='tool':
  f=body['choices'][0]['message']['tool_calls'][0]['function'];assert f['name']=='lookup_record'and json.loads(f['arguments'])=={'name':'memory-probe'}
 else:
  target=int(name.removeprefix('prompt'));assert abs(i['rendered_tokens']-target)<=target*.05;assert body['choices'][0]['message']['content'].strip()=='capacity-check-'+str(target)
 probes+=1
assert json.loads((root/'runtime/runtime-restoration.json').read_text())['restored']
x=json.loads((root/'layout/exit-state.json').read_text());assert not x['oom_killed'];assert x['memory_limit']==x['memory_swap_limit']==8*1024**3
print(json.dumps({'passed':True,'manifest_files':len(manifest),'complete_probes_verified':probes,'memory_samples':len(rows),'sampled_residency_under_8GiB_verified':True,'not_new_inference_or_agent_correctness':True},indent=2))
