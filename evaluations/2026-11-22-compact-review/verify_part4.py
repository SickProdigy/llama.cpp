"""Offline exact context/receipt/capture consistency, not semantic certification."""
from pathlib import Path,PurePosixPath
import argparse,sys,json,hashlib
sys.dont_write_bytecode=True
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);root=p.parse_args().root.resolve()
manifest=json.loads((root/'manifest.json').read_text())['sha256']
for n,h in manifest.items():
 path=PurePosixPath(n);assert not path.is_absolute()and'..'not in path.parts
 assert not any(x in n for x in ['receipt-key','auth.json','.env','state.db'])
 f=root/n;assert f.is_file()and not f.is_symlink()and hashlib.sha256(f.read_bytes()).hexdigest()==h,n
sys.path.insert(0,str(root/'harness/frozen-library'))
from review_packet import source_digest,build_packet,encoded,packet_id
inv=lambda p:{str(f.relative_to(p)):f.read_bytes().decode()for f in p.rglob('*')if f.is_file()}
base=inv(root/'baseline');case_count=0;call_count=0
for case in sorted((root/'cases').iterdir()):
 files=inv(case/'source');digest=source_digest(files)
 receipts=[json.loads((case/(s+'-receipt-payload.json')).read_text())for s in ['project','preservation']]
 for x in receipts:
  assert x['source_digest']==digest and x['returncode']==0 and not x['timed_out']
  assert hashlib.sha256((case/(x['suite_id']+'.log')).read_bytes()).hexdigest()==x['output_sha256']
 mini=json.loads((case/'minimal-packet.json').read_text());whole=json.loads((case/'whole_changed_production_modules-packet.json').read_text());changes={n:files.get(n)for n in set(base)|set(files)if base.get(n)!=files.get(n)}
 rebuilt=build_packet(tasks=mini['tasks'],base_revision=mini['base_revision'],base=base,changes=changes,context_paths=mini['context'].keys(),documentation_paths=mini['documentation_paths'],execution=mini['execution'],publication=mini['publication'],class_declarations=True)
 assert rebuilt==mini and sorted(mini['execution'],key=lambda x:x['suite_id'])==sorted(receipts,key=lambda x:x['suite_id'])
 expected=json.loads(encoded(mini));paths=[x['path']for x in expected['patches']if x['path'].endswith('.py')and not any(y=='tests'or y.startswith('test_')for y in Path(x['path']).parts)]
 for n in paths:expected['context'][n]={'sha256':hashlib.sha256(files[n].encode()).hexdigest(),'content':files[n]}
 expected['related_code_context']=[x for x in expected['related_code_context']if x['path']not in paths]
 expected['context_policy']='Requested actual-tree files, generic local context, and complete actual changed production Python modules; not complete whole-program context';expected['packet_id']=packet_id(expected)
 assert expected==whole
 case_count+=1
for r in sorted((root/'runs').iterdir()):
 result=json.loads((r/'result.json').read_text());packet=json.loads((r/'packet.json').read_text());cap=json.loads((r/'http/capture.json').read_text());req=json.loads((r/'http/request.json').read_text());caller=json.loads((r/'http/caller.json').read_text());raw=(r/'http/response.bin').read_bytes();body=json.loads(raw);metrics=json.loads((r/'input-metrics.json').read_text())
 assert packet==json.loads((root/'cases'/result['case']/(result['variant']+'-packet.json')).read_text())
 assert json.loads(req['messages'][1]['content'])==packet
 assert packet_id(packet)==packet['packet_id'] and cap['parsed_review']['packet_id']==packet['packet_id']
 assert hashlib.sha256(raw).hexdigest()==cap['response_sha256']and len(raw)==cap['captured_bytes']
 assert cap['body_complete']and cap['finish_reason']=='stop' and caller['caller_completed']
 assert json.loads(body['choices'][0]['message']['content'])==cap['parsed_review']
 assert metrics['rendered_tokens']==cap['usage']['prompt_tokens']<=10000
 assert len(encoded(packet))==metrics['packet_bytes']<=32768
 assert req['max_tokens']==1024 and req['seed']==20261122 and caller['caller_limit_seconds']==240
 assert max(x['finished_ns']for x in packet['execution'])<=cap['started_epoch']*1e9
 assert not result['actual_publication'];call_count+=1
assert case_count==2 and call_count==4
print(json.dumps({'passed':True,'manifest_files':len(manifest),'paired_cases_exactly_rebuilt':case_count,'complete_captures_verified':call_count,'fresh_execution_payloads_bound':4,'not_new_execution_or_historic_MAC_authentication':True},indent=2))
