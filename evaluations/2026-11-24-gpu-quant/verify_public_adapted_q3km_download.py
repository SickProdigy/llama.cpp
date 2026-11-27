"""Verify saved transfer/header consistency; no inference or live owner-state replay."""
from pathlib import Path,PurePosixPath
import json,hashlib,tarfile,sys
p=Path(sys.argv[1]);files={};sha=lambda b:hashlib.sha256(b).hexdigest()
with tarfile.open(p)as t:
 for m in t:
  n=PurePosixPath(m.name);assert m.isfile()and not n.is_absolute()and'..'not in n.parts and m.name not in files and m.size<3*1024**2;files[m.name]=t.extractfile(m).read()
assert sum(map(len,files.values()))<12*1024**2
read=lambda n:json.loads(files[n]);manifest=read('manifest.json');assert set(files)==set(manifest)|{'manifest.json'}
for n,h in manifest.items():assert sha(files[n])==h,n
s=read('summary.json');r=read('observed/receipt.json');c=read('observed/completion.json');policy=read('selection-policy.json');admit=read('admission.json');candidate=policy['candidate'];terminal=read('observed/terminal.json');registration=read('registration.json');comparison=read('header-comparison.json')
assert s['receipt']==r and s['completion']==c and s['not_GPU_fit_or_quality_result']
assert candidate['repo']=='netprojects/Qwen3.8-27B-hermes-adapted-GGUF'and candidate['revision']=='10fdf357f14825c61ad7eb42a932e1f1e4390e8f'and candidate['file']=='Qwen3.8-27B-hermes-Q3_K_M.gguf'
assert candidate['bytes']==r['bytes']==registration['bytes']==13752764064 and candidate['advertised_SHA256']==r['sha256']==registration['expected_SHA256']=='a0c809f93de2bcd813e1b6fbd5c2d1f692821814a4261a316f7c8bca9cf23248'
assert r['passed']and r['full_file_SHA256_verified']and c['passed']and c['download_stream_fullSHA_verified']
assert sha(files['source/download.py'])==r['download_worker_SHA256']==admit['worker_SHA256']==registration['source_SHA256']
assert sha(files['selection-policy.json'])==r['source_selection_SHA256']==admit['selection_SHA256']
assert sha(files['admission.json'])==registration['admission_SHA256']
assert r['transfer_stage_stop_threshold_bytes']==r['transfer_original_stop_threshold_bytes']==101*1024**3
assert r['global_requested_reserve_bytes']==100*1024**3 and r['start_stage_free_after_file_minimum_bytes']==102*1024**3
assert admit['storage']['stage_free_bytes']-r['bytes']==admit['stage_free_after_full_expected_file_bytes']>=102*1024**3
assert admit['storage']['original_free_bytes']>=102*1024**3
assert r['minimum_observed_staging_free_bytes']>=101*1024**3 and min(r['final_staging_free_bytes'],r['original_model_drive_free_bytes'])>=101*1024**3
assert min(c['stage_free_bytes'],c['original_free_bytes'])>=100*1024**3
for key in ['all_three_original_runtime_records_including_full_Codex_unchanged','four_owner_settings_hashes_unchanged','owner_pending_tracked_and_ignored_instructions_unchanged','original_alias_context_unchanged','original30_and_staged_IQ4_metadata_unchanged','exact_terminal_supervisor_and_exclusive_anonymous_volume_removed']:assert c[key]
assert terminal['id']==registration['id']=='3c32f8233af56caeb27df3e3e9620135a74ddb3338a651f21dcaa24182e96d8f'and terminal['state']['Status']=='exited'and not terminal['state']['Running']and terminal['state']['ExitCode']==0 and not terminal['state']['OOMKilled']
assert registration['no_GPU_model_or_actor_calls'];assert '--gpus'not in registration['argv']and registration['argv'][registration['argv'].index('--runtime')+1]=='runc'
headers={}
for n,h in comparison['header_file_SHA256'].items():
 raw=files['headers/'+n];assert sha(raw)==h;item=read('headers/'+n);assert len(item['models'])==1;headers[n]=next(iter(item['models'].values()))
assert len(headers)==4 and len({h['tensor_count']for h in headers.values()})==1 and len({h['tensor_names_and_dimensions_SHA256']for h in headers.values()})==1
assert len({json.dumps(h['metadata']['tokenizer.chat_template'],sort_keys=True)for h in headers.values()})==1
q3=headers['current-adapted-q3km-header-audit.json'];assert q3['file']==r['file']and q3['file_bytes']==r['bytes']and q3['tensor_count']==866 and q3['metadata']['general.file_type']==12
assert comparison['same_tensor_count']and comparison['same_tensor_names_and_dimensions']and comparison['same_chat_template']and comparison['Q3KM_full_file_SHA256']==r['sha256']
assert comparison['Q3KM_actual_download_receipt_SHA256']==sha(files['observed/receipt.json'])
assert read('observed/exclusive-volume.json')['sole_exact_supervisor_reference']
print(json.dumps({'passed':True,'archive_SHA256':sha(p.read_bytes()),'manifest_files':len(manifest),'full_stream_SHA_recorded':True,'actual_header_shapes_templates_consistent':True,'GPU_fit_or_quality_not_tested':True,'scope':__doc__}))
