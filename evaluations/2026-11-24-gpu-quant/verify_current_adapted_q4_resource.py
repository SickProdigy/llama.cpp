"""Validate saved observations, not rerun inference or score coding ability."""
from pathlib import Path,PurePosixPath
import sys,json,hashlib,tarfile,re
p=Path(sys.argv[1]);sha=lambda b:hashlib.sha256(b).hexdigest()
with tarfile.open(p)as t:
 f={}
 for m in t:
  name=PurePosixPath(m.name);assert m.isfile()and not name.is_absolute()and'..'not in name.parts and m.name not in f;f[m.name]=t.extractfile(m).read()
read=lambda n:json.loads(f[n]);manifest=read('manifest.json');assert set(f)==set(manifest)|{'manifest.json'}
for n,h in manifest.items():assert sha(f[n])==h,n
s=read('summary.json');P=read('current-adapted-q4-resource-protocol.json');r=read('current-adapted-q4-resource-controller-registration.json');key=s['candidate'];assert key=='adapted-q4-current'
for file,field in [('current_adapted_q4_resource_controller.py','controller_sha256'),('current-adapted-q4-resource-protocol.json','protocol_sha256'),('model_cache_probe.py','cache_helper_sha256')]:assert sha(f[file])==r[field]
pin=P[key];assert s['public_pin']==pin;identity=read('observed/model-identity.json');assert identity==s['model_identity']and identity['sha256']==pin['sha256']and identity['bytes']==pin['expected_bytes'];results=read('observed/finished.json')['results'];assert results==s['all_layout_results'];i=s['selected_layout_index'];assert 0<=i<len(results)==i+1;assert [x['layout']for x in results]==pin['layouts'][:len(results)];assert all(not x.get('resource_probes_completed')for x in results[:i]);assert results[i]['resource_probes_completed'];layout=results[i]['layout'];assert layout==s['selected_layout'];root='observed/layout'+str(i)+'/'
for j,fail in enumerate(results[:i]):
 assert fail['GPU_OOM_log_marker']and fail['retry_next_GPU_layout'];assert not fail['backend_state']['OOMKilled'];log=f['observed/layout'+str(j)+'/backend.log'].decode().lower();assert any(x in log for x in ['cuda error: out of memory','cuda out of memory','cudamalloc failed','cuda_error_out_of_memory'])
placement=f[root+'placement-at-ready.log'].decode();counts=re.findall(r'offloaded (\d+)/(\d+) layers to GPU',placement);assert counts and all(int(a)==min(layout['gpu_layers'],66)and int(b)==66 for a,b in counts);assert s['selected_placement_lines']==[l for l in placement.splitlines()if any(t in l for t in ['offloaded ','model buffer size','KV buffer size','compute buffer size'])];rows=[json.loads(x)for x in f[root+'samples.jsonl'].splitlines()];m=s['selected_memory'];assert len(rows)==m['samples'];assert not any('measurement_error'in x or x.get('budget_guard_triggered')for x in rows)
for a,b in [('total_cgroup_bytes','peak_aggregate_cgroup_bytes'),('total_process_pss_bytes','peak_process_PSS_bytes'),('total_cgroup_swap_bytes','peak_study_swap_bytes')]:assert max(x[a]for x in rows)==m[b]
assert m['peak_study_swap_bytes']==0;assert m['peak_aggregate_cgroup_bytes']<=P['host_aggregate_limit_bytes'];assert m['peak_process_PSS_bytes']<=P['host_aggregate_limit_bytes'];assert max(int(x['gpu_csv'].split(',')[0])for x in rows if x.get('gpu_csv','').split(',')[0].isdigit())==m['peak_GPU_MiB']
for a,b in [('model_disk_free_bytes','minimum_original_free_bytes'),('staging_disk_free_bytes','minimum_staging_free_bytes')]:assert min(x[a]for x in rows)==m[b]>=P['minimum_disk_reserve_bytes']
for name,c in s['probes'].items():
 n=root+name+'/';assert read(n+'capture.json')==c and c['body_complete'];assert sha(f[n+'response.bin'])==c['response_sha256'];response=read(n+'response.bin');assert response['usage']==c['usage'];body=read(n+'request.json');sizing=read(n+'input.json');assert sizing['rendered_tokens']==c['usage']['prompt_tokens'];assert sizing['context']==layout['context'];assert c['usage']['prompt_tokens']+body['max_tokens']<layout['context'];assert c['usage']['total_tokens']<=layout['context']
for target,x in s['synthetic_marker_checks'].items():
 n=root+'prompt'+target+'/';actual=read(n+'retrieval-check.json');content=read(n+'response.bin')['choices'][0]['message'].get('content');assert actual['content']==content and actual['expected']=='capacity-check-'+target;assert x==dict(actual,exact_match=content==actual['expected'])
assert read('observed/runtime-restoration.json')['restored'];assert s['cleanup']['passed']and s['preservation']['passed'];assert read('observed/selected-file-cache-after-original-stop.json')['mincore_cached_page_bytes_after']==0;assert s['tool_check']==read(root+'tool-check.json');print(json.dumps({'passed':True,'archive_sha256':sha(p.read_bytes()),'manifest_files':len(manifest),'layouts_observed':len(results),'selected_layout':layout,'completed_probes':len(s['probes']),'not_coding_or_forge_qualification':True}))
