"""Verify saved evidence integrity/consistency, not reexecute the private native call."""
from pathlib import Path
import json,hashlib,tarfile,copy,sys
sha=lambda b:hashlib.sha256(b).hexdigest()
def validate(files):
 manifest=json.loads(files['manifest.json']);assert set(files)==set(manifest)|{'manifest.json'}
 for name,digest in manifest.items():assert sha(files[name])==digest,name
 s=json.loads(files['summary.json']);r=json.loads(files['registration.json']);p=json.loads(files['protocol.json']);native=s['native'];call=s['recorded_calls'][0]
 assert sha(files['source/controller.py'])==r['controller_sha256'];assert sha(files['protocol.json'])==r['protocol_sha256']
 for name,key in [('worker.py','native_compression_worker.py'),('preflight.py','preflight_native_compression_worker.py'),('llm_proxy.py','harness/llm_proxy.py')]:assert sha(files['source/'+name])==r['additional_source_sha256'][key]
 assert native['input_history_SHA256']==r['additional_source_sha256']['native-adapted-iq4/beets_lifecycle/llm-records/00048.request.json']
 assert s['model_identity']['sha256']==p['adapted-iq4-compression']['sha256']
 assert s['classification']=='runtime control only, not coding or forge quality';assert native['control_not_coding_quality']and native['full_native_CLI_or_GUI_not_exercised']and native['no_tools_or_forge_enabled']
 assert native['passed']and native['made_progress']and not native['used_fallback'];assert native['messages_before']>native['messages_after']>0
 assert native['native_guarded_facade_used']and native['native_aux_budget']==5400 and native['native_host_budgets']==[5400,5400]
 assert len(s['recorded_calls'])==1 and call['wire_progress_requested']and call['stream']and call['actual_progress_frames']>0
 m=call['metrics'];assert not m.get('transport_error')and m['finish_reasons']==['stop'];assert 0<m['usage']['completion_tokens']<=call['output_cap'];assert m['usage']['prompt_tokens']+call['output_cap']<=native['native_context'];assert abs(native['elapsed_seconds']-(m['end_epoch']-m['received_epoch']))<10
 assert s['stream_probe']['HTTP_complete']and s['stream_probe']['progress_supported']and not s['stream_probe']['error']
 assert s['complete_samples']>0 and s['measurement_errors']==s['guard_samples']==s['peak_study_swap_bytes']==0
 assert min(s['minimum_original_disk_free_bytes'],s['minimum_staging_disk_free_bytes'])>=100*1024**3
 assert s['peak_study_cgroup_bytes']<=8*1024**3 and s['runtime_restoration']['restored']and not s['runtime_restoration']['cleanup_errors']
 assert all(v for v in s['preservation'].values()if isinstance(v,bool))and s['owner_pending_edits_preserved']
 assert s['request_comparison']['not_pure_runtime_causal_comparison_if_messages_differ']and not s['request_comparison']['messages_identical']
 return s
if __name__=='__main__':
 archive=Path(sys.argv[1]);files={}
 with tarfile.open(archive)as t:
  for entry in t:assert entry.isfile()and entry.name not in files;files[entry.name]=t.extractfile(entry).read()
 validate(files);controls={}
 for name,edit in [('fallback_claim_hidden',lambda s:s['native'].update(used_fallback=True)),('missing_actual_native_progress',lambda s:s['recorded_calls'][0].update(actual_progress_frames=0))]:
  bad=copy.deepcopy(files);s=json.loads(bad['summary.json']);edit(s);bad['summary.json']=json.dumps(s).encode();manifest=json.loads(bad['manifest.json']);manifest['summary.json']=sha(bad['summary.json']);bad['manifest.json']=json.dumps(manifest).encode()
  try:validate(bad)
  except AssertionError:controls[name]=True
  else:raise AssertionError('Coherent altered evidence accepted: '+name)
 print(json.dumps({'passed':True,'archive_SHA256':sha(archive.read_bytes()),'files_checked':len(files),'coherently_rehashed_negative_controls_rejected':controls,'scope':'Saved integrity and consistency only; private input/model inference not replayed'},indent=2))
