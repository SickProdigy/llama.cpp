"""Verify saved resource evidence consistency, not coding quality or reliability."""
from pathlib import Path,PurePosixPath
import json,hashlib,tarfile,sys
E=Path(__file__).resolve().parent;key=sys.argv[1];assert key in ['q3','devstral','glm'];label='resource-'+key;archive=E/(label+'-evidence.tar.gz');sha=lambda b:hashlib.sha256(b).hexdigest();assert sha(archive.read_bytes())==(E/(label+'-evidence.sha256')).read_text().split()[0]
with tarfile.open(archive)as t:
 members=t.getmembers();assert all(m.isfile()and not PurePosixPath(m.name).is_absolute()and'..'not in PurePosixPath(m.name).parts for m in members);assert len({m.name for m in members})==len(members);files={m.name:t.extractfile(m).read()for m in members}
j=lambda n:json.loads(files[n]);manifest=j('manifest.json')['sha256'];assert set(files)==set(manifest)|{'manifest.json'}
for n,h in manifest.items():assert sha(files[n])==h,n
assert not any(any(part in ['profiles','baseline','receipt-key','state.db','AGENTS.md']for part in PurePosixPath(n).parts)for n in files)
reg=j('controls/remaining-resource-controller-registration.json');assert sha(files['source/candidate_resource_controller.py'])==reg['controller_sha256'];assert sha(files['controls/remaining-resource-protocol.json'])==reg['protocol_sha256'];protocol=j('controls/remaining-resource-protocol.json');model=protocol[key];identity=j('runtime/model-identity.json');assert identity['sha256']==model['sha256']and identity['bytes']==model['expected_bytes']and identity['file']==model['file'];assert j('runtime/runtime-restoration.json')['restored'];assert j('controls/remaining-resource-'+key+'-preservation.json')['all_29_original_model_metadata_unchanged'];assert j('controls/remaining-resource-'+key+'-owner-preservation.json')['passed']
summary=j('summary.json');assert json.loads((E/(label+'-summary.json')).read_text())==summary
if key=='glm'and 'controls/glm-cache-equality-preactor-amendment.json'in files:
 amendment=j('controls/glm-cache-equality-preactor-amendment.json');old_protocol_bytes=files['controls/remaining-resource-protocol-before-glm-cache-equality-fix.json'];old_protocol=json.loads(old_protocol_bytes);old_reg=j('controls/remaining-resource-controller-registration-before-glm-cache-equality-fix.json')
 assert sha(old_protocol_bytes)==old_reg['protocol_sha256']==amendment['old_protocol_sha256']
 assert sha(files['controls/remaining-resource-protocol.json'])==amendment['new_protocol_sha256']
 assert sha(files['controls/glm-cache-equality-preactor-amendment.json'])==reg['GLM_cache_equality_pre_actor_amendment_sha256']
 assert old_reg['controller_sha256']==reg['controller_sha256']==amendment['controller_unchanged_sha256']
 assert old_protocol['glm']==amendment['prior_glm_parameters']and model==amendment['new_glm_parameters']
 expected=json.loads(json.dumps(old_protocol['glm']))
 for layout in expected['layouts']:
  assert layout['cache_k']=='q4_0'and layout['cache_v']=='f16';layout['cache_v']='q4_0'
 assert expected==model
 prior='prior-attempts/unequal-declared-cache-types/'
 result=j(prior+'layout0/result.json');assert not result['resource_probes_completed']and result['backend_state']['ExitCode']==1 and not result['backend_state']['OOMKilled']and not result['GPU_OOM_log_marker']and not result['retry_next_GPU_layout']
 assert b'model does not support different K (q4_0) and V (f16) cache types'in files[prior+'layout0/backend.log']
 assert j(prior+'runtime-restoration.json')['restored']and j('controls/remaining-resource-glm-cache-types-attempt1-preservation.json')['all_29_original_model_metadata_unchanged']and j('controls/remaining-resource-glm-cache-types-attempt1-owner-preservation.json')['passed']
 pins=j('controls/glm-cache-equality-source-pins.json');assert pins==amendment['source_pins']==j('source/glm-cache-equality/pins.json')
 for pin in pins:assert sha(files['source/glm-cache-equality/'+PurePosixPath(pin['path']).name])==pin['sha256']
count=0
for row in summary['layouts']:
 prefix=row['layout'];assert j(prefix+'/result.json')==row['result'];launch=j(prefix+'/launch.json');assert launch['layout']in model['layouts'];assert '--ctx-checkpoints'in launch['argv']and launch['argv'][launch['argv'].index('--ctx-checkpoints')+1]=='2'
 samples=[json.loads(s)for s in files[prefix+'/samples.jsonl'].decode().splitlines()];good=[r for r in samples if all(k in r for k in ['total_cgroup_bytes','total_process_pss_bytes','total_cgroup_swap_bytes'])];assert row['samples']==len(samples)and row['complete_samples']==len(good);assert row['measurement_error_samples']==sum('measurement_error'in r for r in samples);assert row['guard_samples']==sum(bool(r.get('budget_guard_triggered'))for r in samples)
 if good:assert row['peaks']=={k:max(r[k]for r in good)for k in ['total_cgroup_bytes','total_process_pss_bytes','total_cgroup_swap_bytes']}
 for name,probe in row['probes'].items():
  p=prefix+'/'+name;capture=j(p+'/capture.json');inp=j(p+'/input.json');request=j(p+'/request.json');raw=files[p+'/response.bin'];response=json.loads(raw);assert capture==probe['capture']and inp==probe['input'];assert capture['body_complete']and sha(raw)==capture['response_sha256'];assert response['usage']==capture['usage'];assert response['usage']['prompt_tokens']==inp['rendered_tokens'];assert inp['rendered_tokens']+request['max_tokens']<inp['context'];assert response['choices'];count+=1
result={'passed':True,'manifest_files':len(manifest),'layouts':len(summary['layouts']),'complete_responses':count,'not_coding_or_Gitea_quality_proof':True,'scope':'Checks retained bytes, pins, token/measurement consistency and restoration audits. Does not rerun inference or establish whole-host peak fit.'};(E/(label+'-validation.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
