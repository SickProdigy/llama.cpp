"""Check saved capacity evidence; never infer real coding or rerun model inference."""
from pathlib import Path,PurePosixPath
import hashlib,json,sys,tarfile
archive=Path(sys.argv[1]);sha=lambda b:hashlib.sha256(b).hexdigest()
with tarfile.open(archive)as tar:
 files={}
 for m in tar:
  p=PurePosixPath(m.name);assert m.isfile()and not p.is_absolute()and'..'not in p.parts and m.name not in files;files[m.name]=tar.extractfile(m).read()
read=lambda p:json.loads(files[p]);manifest=read('manifest.json');assert set(files)==set(manifest)|{'manifest.json'}
for p,h in manifest.items():assert sha(files[p])==h,p
protocol=read('protocol.json');assert sha(Path(__file__).with_name('iq4-resource-protocol.json').read_bytes())==sha(files['protocol.json']);reg=read('registration.json');assert reg['controller_sha256']==sha(files['controller.py'])and reg['protocol_sha256']==sha(files['protocol.json'])and reg['cache_helper_sha256']==sha(files['model_cache_probe.py'])and reg['download_source_sha256']==sha(files['download_owned_adapted_iq4.py'])
s=read('summary.json');identity=read('observed/model-identity.json');pin=protocol['adapted-iq4'];assert identity==s['model_identity']and identity['file']==pin['file']and identity['bytes']==pin['expected_bytes']and identity['sha256']==pin['sha256'];assert s['not_coding_quality']and s['failed_layouts_not_model_quality_failures']and read('observed/runtime-restoration.json')['restored'];assert read('owner-preservation.json')['passed']
for name,value in read('preservation.json').items():
 if isinstance(value,bool):assert value,name
finished=read('observed/finished.json')['results'];assert len(finished)==len(s['layouts']);selected=[]
for index,row in enumerate(s['layouts']):
 prefix='observed/layout'+str(index)+'/';result=read(prefix+'result.json');assert result==finished[index]==row['result'];assert result['layout']==pin['layouts'][index]
 launch=read(prefix+'launch.json')['argv'];layout=result['layout']
 for flag,value in [('--ctx-size',str(layout['context'])),('-ngl','99'),('-ub',str(layout['ubatch'])),('--fit','off'),('--cache-type-k','q4_0'),('--cache-type-v','q4_0'),('--load-mode','none')]:assert launch[launch.index(flag)+1]==value
 cache=read(prefix+'selected-file-cache-before-layout.json');assert cache['mincore_cached_page_bytes_after']==0
 rows=[json.loads(l)for l in files[prefix+'samples.jsonl'].decode().splitlines()];good=[r for r in rows if all(k in r for k in ['total_cgroup_bytes','total_process_pss_bytes','total_cgroup_swap_bytes','model_disk_free_bytes','staging_disk_free_bytes'])];assert len(rows)==row['samples']and len(good)==row['complete_samples']and len(rows)-len(good)==row['measurement_error_samples']
 assert row['peak_GPU_MiB']==max(int(r['gpu_csv'].split(',')[0])for r in good if r.get('gpu_csv'))
 assert row['peak_cgroup_bytes']==max(r['total_cgroup_bytes']for r in good)and row['peak_PSS_bytes']==max(r['total_process_pss_bytes']for r in good)
 assert row['peak_study_swap_bytes']==max(r['total_cgroup_swap_bytes']for r in good)==0
 assert row['guard_samples']==sum(bool(r.get('budget_guard_triggered'))for r in rows)==0
 for field,rawfield in [('minimum_original_model_disk_free_bytes','model_disk_free_bytes'),('minimum_staging_disk_free_bytes','staging_disk_free_bytes')]:assert row[field]==min(r[rawfield]for r in good)>=100*1024**3
 if not result['resource_probes_completed']:
  assert result['GPU_OOM_log_marker']and result['retry_next_GPU_layout']and not result['backend_state']['OOMKilled'];log=files[prefix+'backend.log'].decode(errors='replace').lower();assert any(v in log for v in ['cuda error: out of memory','cuda out of memory','cudamalloc failed','cuda_error_out_of_memory'])
 else:
  selected.append(index);ready=read(prefix+'ready.json');assert ready['props']['default_generation_settings']['n_ctx']==layout['context'];assert len(row['probes'])==5
  for name,capture in row['probes'].items():
   assert capture==read(prefix+name+'/capture.json')and capture['body_complete'];request=read(prefix+name+'/request.json');tokens=read(prefix+name+'/input.json')['rendered_tokens'];assert capture['usage']['prompt_tokens']==tokens and tokens+request['max_tokens']<layout['context']
assert len(selected)<=1 and s['selected_layout_index']==(selected[0]if selected else None)and s['capacity_pass']==bool(selected)
print(json.dumps({'passed':True,'manifest_files':len(manifest),'selected_layout_index':s['selected_layout_index'],'GPU_fit_observed':s['capacity_pass'],'not_coding_quality':True,'archive_SHA256':sha(archive.read_bytes())}))
