"""Validate saved control evidence consistency, not private output semantics or replay."""
from pathlib import Path
import hashlib,json,sys,tarfile

def verify(path):
 with tarfile.open(path)as t:
  members=t.getmembers();assert all(m.isfile()and not m.name.startswith('/')and'..'not in Path(m.name).parts for m in members)
  data={m.name:t.extractfile(m).read()for m in members};assert len(data)==len(members)
 manifest=json.loads(data.pop('manifest.json'));assert set(manifest['files'])==set(data)
 for n,b in data.items():assert hashlib.sha256(b).hexdigest()==manifest['files'][n]
 scope=json.loads(data['scope.json']);assert scope['actor_or_forge_actions']is False and scope['not_a_main_agent_quality_trial']and scope['all_originals_restored'];assert scope['context']==98304 and scope['output_cap']==8192
 stages=[json.loads(data[k+'/observations.json'])for k in ['native-q4-kv','wrapped-q4-kv','native-fp16-kv']];model=stages[0]['model'];backend=stages[0]['backend_image']
 for s in stages:
  assert s['model']==model and s['backend_image']==backend;assert s['originals_restored_and_metadata_preserved']and s['owner_pending_work_preserved']and s['cold_selected_model_page_cache_confirmed']
  r=s['resource'];assert r['all_41_layers_on_GPU']and r['guards']==0 and r['peak_study_swap_bytes']==0 and r['minimum_disk_free_bytes']>=100*1024**3;assert r['peak_aggregate_cgroup_bytes']<=8*1024**3 and r['peak_aggregate_process_pss_bytes']<=8*1024**3
  for v in s['variants']:
   c=v['capture'];assert c['transport_complete']and c['actual_cached_tokens']==0 and c['uncached_prefill_confirmed'];assert c['usage']['completion_tokens']<=8192 and c['usage']['total_tokens']<=98304;assert c['model_tools_or_forge_actions_enabled']is False
   assert v['semantic_result'] in ['unusable','structural_only_unfaithful','faithful_checkpoint']
   assert isinstance(v['semantic_basis'],str)and v['semantic_basis']
 original,wrapped,fp16=stages;assert len(original['variants'])==len(fp16['variants'])==3 and len(wrapped['variants'])==2
 for a,b in zip(original['variants'],fp16['variants']):assert a['variant']==b['variant']and a['capture']['sampler']==b['capture']['sampler']and a['capture']['usage']['prompt_tokens']==b['capture']['usage']['prompt_tokens']
 assert fp16['layout']['cache_k']==fp16['layout']['cache_v']=='f16'
 return {'passed':True,'stages':3,'variant_captures':8,'verification_scope':'Archive integrity and saved observation consistency; manual semantic judgments are documented, not independently replayed.'}
if __name__=='__main__':print(json.dumps(verify(Path(sys.argv[1]or'auxiliary-precision-controls-evidence.tar.gz')),indent=2))
