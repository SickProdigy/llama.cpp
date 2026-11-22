"""Offline source/receipt-payload/capture consistency; not semantic certification."""
from pathlib import Path,PurePosixPath
import argparse,json,hashlib,sys
sys.dont_write_bytecode=True
p=argparse.ArgumentParser();p.add_argument('--root',required=True,type=Path);root=p.parse_args().root.resolve()
m=json.loads((root/'manifest.json').read_text())['sha256']
for n,h in m.items():
 q=PurePosixPath(n);assert not q.is_absolute()and'..'not in q.parts
 assert not any(x in n for x in ['receipt-key','normal-profile','auth.json','.env','state.db'])
 f=root/n;assert f.is_file()and not f.is_symlink()and hashlib.sha256(f.read_bytes()).hexdigest()==h,n
sys.path.insert(0,str(root/'harness/frozen-library'))
from review_packet import source_digest,build_packet,packet_id,encoded
inv=lambda p:{str(f.relative_to(p)):f.read_bytes().decode()for f in p.rglob('*')if f.is_file()}
base=inv(root/'baseline');packets=0;captures=0;grades=0;admitted=0
for r in sorted((root/'reviews').glob('*/*')):
 source=inv(r/'source');digest=source_digest(source)
 receipts=[json.loads(f.read_text())for f in r.glob('*receipt-payload.json')]
 for x in receipts:
  assert x['source_digest']==digest
  log=r/('project.log'if x['suite_id']=='project'else'preservation.log');assert hashlib.sha256(log.read_bytes()).hexdigest()==x['output_sha256']
 if(r/'packet.json').exists():
  packet=json.loads((r/'packet.json').read_text());assert packet_id(packet)==packet['packet_id'];assert packet['candidate_source_digest']==digest;assert packet['base_source_digest']==source_digest(base)
  changes={n:source.get(n)for n in set(base)|set(source)if base.get(n)!=source.get(n)}
  rebuilt=build_packet(tasks=packet['tasks'],base_revision=packet['base_revision'],base=base,changes=changes,context_paths=packet['context'].keys(),documentation_paths=packet['documentation_paths'],execution=packet['execution'],publication=packet['publication'],class_declarations=True)
  assert rebuilt==packet,r
  assert sorted(receipts,key=lambda x:x['suite_id'])==sorted(packet['execution'],key=lambda x:x['suite_id'])
  packets+=1
 if(r/'http/capture.json').exists():
  cap=json.loads((r/'http/capture.json').read_text());raw=(r/'http/response.bin').read_bytes();body=json.loads(raw);req=json.loads((r/'http/request.json').read_text());met=json.loads((r/'input-metrics.json').read_text());caller=json.loads((r/'http/caller.json').read_text())
  assert json.loads(req['messages'][1]['content'])==packet
  assert hashlib.sha256(raw).hexdigest()==cap['response_sha256']and len(raw)==cap['captured_bytes']
  assert cap['body_complete']and cap['finish_reason']=='stop'
  assert json.loads(body['choices'][0]['message']['content'])==cap['parsed_review']
  assert cap['parsed_review']['packet_id']==packet['packet_id']
  assert met['rendered_tokens']==cap['usage']['prompt_tokens']<=10000
  assert met['packet_bytes']==len(encoded(packet))<=32768
  assert req['max_tokens']==1024 and req['seed']==20261122 and caller['caller_limit_seconds']==240
  assert max(x['finished_ns']for x in receipts)<=cap['started_epoch']*1e9
  captures+=1
 if(r/'admitted.json').exists():
  a=json.loads((r/'admitted.json').read_text());assert a['source_digest']==digest and a['packet_id']==packet['packet_id'];assert all(x['returncode']==0 and not x['timed_out']for x in receipts);assert caller['caller_completed'];admitted+=1
for r in(root/'runs').glob('*/turn*/*grade'):
 g=json.loads((r/'grade.json').read_text());assert source_digest(inv(r/'source'))==g['source_digest']
 for suite in ['project','preservation']:
  x=json.loads((r/(suite+'-receipt-payload.json')).read_text());assert x['source_digest']==g['source_digest'];assert hashlib.sha256((r/(suite+'.log')).read_bytes()).hexdigest()==x['output_sha256'];assert x['returncode']==g[suite+'_exit']
 grades+=1
mutants=0
for r in sorted((root/'feature-mutations').iterdir()):
 if not r.is_dir():continue
 result=json.loads((r/'result.json').read_text());digest=source_digest(inv(r/'source'))
 assert digest==result['mutant_source_digest']
 for suite in ['project','preservation']:
  receipt=json.loads((r/(suite+'-receipt-payload.json')).read_text())
  assert receipt['source_digest']==digest
  assert receipt['returncode']==result[suite+'_exit']
  assert hashlib.sha256((r/(suite+'.log')).read_bytes()).hexdigest()==receipt['output_sha256']
 assert result['target_new_assertion_failure_in_mutant'] and not result['mutant_was_published']
 mutants+=1
assert mutants==4
assert grades==12
print(json.dumps({'passed':True,'mutant_sources_and_execution_payloads_verified':mutants,'manifest_files_verified':len(m),'exact_source_packets_rebuilt':packets,'complete_captures_verified':captures,'admissions_verified':admitted,'local_and_actual_remote_grades_bound':grades,'not_new_project_test_run_or_semantic_correctness':True,'historic_MACs_require_private_issuer_keys':True},indent=2))
