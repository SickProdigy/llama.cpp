"""Offline structural/capture verification. Does not rerun or certify project tests."""
from pathlib import Path, PurePosixPath
import argparse,hashlib,json,sys,csv
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);args=p.parse_args();root=args.root.resolve()
manifest=json.loads((root/'manifest.json').read_text())['sha256']
for name,digest in manifest.items():
 path=PurePosixPath(name)
 assert not path.is_absolute() and '..' not in path.parts and '.git' not in path.parts
 assert not any(v in name for v in ['receipt-key','normal-profile','private_checks.py','auth.json','.env','state.db'])
 target=root/name;assert target.is_file() and not target.is_symlink();assert hashlib.sha256(target.read_bytes()).hexdigest()==digest,name
sys.path.insert(0,str(root/'harness/frozen-library'))
from review_packet import encoded,packet_id,source_digest
corpus=json.loads((root/'controls/corpus-private.json').read_text());freeze=json.loads((root/'controls/corpus-freeze.json').read_text())
assert hashlib.sha256((root/'controls/corpus-private.json').read_bytes()).hexdigest()==freeze['corpus_sha256']
def inventory(path):return {str(f.relative_to(path)):f.read_bytes().decode() for f in path.rglob('*') if f.is_file()}
packets={}
for case in corpus['cases']:
 path=root/'cases'/case['case_id'];raw=(path/'packet.json').read_bytes();packet=json.loads(raw)
 assert hashlib.sha256(raw).hexdigest()==case['packet_sha256']==freeze['packet_sha256'][case['case_id']]
 assert packet_id(packet)==packet['packet_id'] and len(encoded(packet))<=32768
 assert source_digest(inventory(path/'source'))==packet['candidate_source_digest']==case['candidate_source_digest']
 base=path/'base' if (path/'base').exists() else root/'source-baseline'
 assert source_digest(inventory(base))==packet['base_source_digest']
 receipt=json.loads((path/'execution-payload.json').read_text());assert receipt['source_digest']==packet['candidate_source_digest']
 assert (receipt['returncode']!=0)==case['execution_blocked']
 packets[case['case_id']]=packet
captures=0;scored=0;warm=0
for path in (root/'runs').glob('*/*/http/capture.json'):
 cap=json.loads(path.read_text());raw=(path.parent/'response.bin').read_bytes();body=json.loads(raw);req=json.loads((path.parent/'request.json').read_text())
 packet=json.loads(req['messages'][1]['content']);assert packet in packets.values()
 assert cap['body_complete'] and not cap.get('error') and hashlib.sha256(raw).hexdigest()==cap['response_sha256']
 assert len(raw)==cap['captured_bytes'] and cap['finish_reason']=='stop'
 assert json.loads(body['choices'][0]['message']['content'])==cap['parsed_review']
 assert cap['parsed_review']['packet_id']==packet['packet_id']
 assert req['max_tokens']==1024 and req['seed']==20261122 and req['chat_template_kwargs']=={'enable_thinking':False}
 assert req['response_format']['json_schema']['schema']['properties']['packet_id']['enum']==[packet['packet_id']]
 caller=json.loads((path.parent/'caller.json').read_text());assert caller['caller_completed'] and caller['caller_limit_seconds']==240
 metrics=json.loads((path.parent.parent/'input-metrics.json').read_text());assert metrics['rendered_tokens']==cap['usage']['prompt_tokens']<=10000
 assert metrics['packet_bytes']==len(encoded(packet))
 captures+=1
 name=path.parent.parent.name
 if name in corpus['scored_order']:scored+=1
 elif name.endswith('-warm-repeat'):warm+=1
assert (captures,scored,warm)==(41,35,5)
control=json.loads((root/'controls/execution-negative-control.json').read_text());assert control['blocked'] and not control['critic_called'] and control['actual_returncode']==1
result={'passed':True,'manifest_files_verified':len(manifest),'source_packets_verified':len(packets),'complete_model_reviews':captures,'scored_reviews':scored,'warm_repeats_excluded':warm,'cache_interference_review_excluded':captures-scored-warm,'failed_suite_control_blocked_without_critic':True,'packet_token_usage_matches_template_measurement':True,'not_a_new_project_test_run':True,'not_semantic_correctness_or_public_MAC_verification':True}
print(json.dumps(result,indent=2))
