"""Development-only size replay, no inference or publication.

Uses the completed pilot's actual mutations. Private raw old receipt tails are
used only for local tokenizer counts and never copied into output packets.
Current compact context comes from the public baseline, never adjacent scratch
changes. Historical receipt excerpts are already curated and filtered to calls
completed before the original review request.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time
import urllib.request
from review_packet import apply_changes, build_packet, encoded, SYSTEM

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--old-private-root', type=Path, required=True)
    p.add_argument('--old-public-root', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--endpoint', default='http://192.168.86.239:11430')
    args = p.parse_args(); args.output.mkdir(parents=True, exist_ok=True)
    props = json.load(urllib.request.urlopen(args.endpoint + '/props', timeout=10))
    def tokens(text):
        request = urllib.request.Request(args.endpoint + '/tokenize',
            data=json.dumps({'content': text, 'add_special': False}).encode(),
            headers={'Content-Type': 'application/json'})
        start = time.monotonic()
        value = json.load(urllib.request.urlopen(request, timeout=60))
        return len(value['tokens']), round(time.monotonic() - start, 6)
    baseline_root = args.old_public_root / 'source-baseline'
    base = {str(f.relative_to(baseline_root)): f.read_text() for f in baseline_root.rglob('*') if f.is_file()}
    assert len(base) == 40
    rows = []
    for run in sorted((args.old_private_root / 'runs').glob('review-*')):
        records = {}
        for turn in sorted(run.glob('turn*')):
            if (turn/'run.json').exists():
                for file in (turn/'forge-and-review-records/reviews').glob('*-review.json'):
                    records[file.name] = file
        for name, file in sorted(records.items()):
            original = json.loads(file.read_text()); old = original['input']; candidate = old['candidate']
            pub = candidate['publication']; changes = {}
            for item in pub.get('files') or [pub]:
                path = item['path']
                if path in changes: raise ValueError('Duplicate mutation path')
                if item.get('new_path'): raise ValueError('Unsupported rename')
                if item.get('delete'): content = None
                elif 'content' in item: content = item['content']
                else:
                    content = base[path]
                    for edit in item['edits']:
                        assert content.count(edit['old_string']) == 1
                        content = content.replace(edit['old_string'], edit['new_string'], 1)
                changes[path] = content
            # Every review arm in this completed pilot had zero published commits.
            # Confirm actual base from the independent raw-mutation grade.
            phase = original['phase'].rsplit('turn', 1)[1]
            grade = json.loads((args.old_public_root/'runs'/run.name/('turn'+phase)/
                'candidate-reviews'/file.stem/'grade.json').read_text())
            assert grade['prior_successful_commits'] == 0 and grade['materializer_version'] == 2
            for path, context in candidate['source_context'].items():
                assert context['baseline'] == base.get(path), 'Actual base differs from old context'
            public_turn = args.old_public_root/'runs'/run.name/('turn'+phase)
            provenance = {r['id']: r for r in json.loads((public_turn/'native-message-provenance.json').read_text())}
            selected = json.loads((public_turn/'execution-receipts.json').read_text())['receipts']
            observations = []
            for receipt in selected:
                if provenance[receipt['id']]['timestamp'] <= original['start_epoch']:
                    observations.append({'kind': 'historical_observation_not_current_authenticated_execution',
                        'message_id': receipt['id'], 'source_content_sha256': receipt['source_content_sha256'],
                        'command': receipt['command'], 'exit_code': receipt['terminal_exit_code'],
                        'output_excerpt': receipt['output_excerpt'],
                        'shell_status_not_a_test_verdict': receipt.get('shell_status_not_a_test_verdict', False)})
            metadata = {k: v for k, v in pub.items() if k in {'owner','repo','branch_name','head','base','title','body','message'} and isinstance(v,str)}
            metadata['operation'] = candidate['operation']
            context_paths = list(candidate['source_context'])
            docs = [path for path in context_paths if path.endswith('.md')]
            start = time.monotonic()
            packet = build_packet(tasks=old['task_history'], base_revision=grade['actual_base_sha'],
                base=base, changes=changes, context_paths=context_paths, documentation_paths=docs,
                execution=observations[-3:], publication=metadata, max_bytes=2_000_000)
            build_seconds = time.monotonic() - start
            raw = encoded(packet)
            old_text = json.dumps(old, ensure_ascii=False)
            old_tokens, old_tokenize_seconds = tokens(old_text)
            new_tokens, new_tokenize_seconds = tokens(raw.decode())
            output_name = run.name+'-'+name
            (args.output/output_name).write_bytes(raw)
            rows.append({'workflow': run.name, 'phase': int(phase), 'record': name,
                'diagnostic_only_no_publication': True, 'old_packet_sha256': hashlib.sha256(old_text.encode()).hexdigest(),
                'new_packet_sha256': hashlib.sha256(raw).hexdigest(), 'old_bytes': len(old_text.encode()),
                'new_bytes': len(raw), 'fits_32768_byte_budget': len(raw) <= 32768,
                'old_text_tokens_same_current_tokenizer': old_tokens,
                'new_text_tokens_same_current_tokenizer': new_tokens,
                'fits_7500_packet_text_token_target': new_tokens <= 7500,
                'build_seconds': round(build_seconds,6),
                'old_tokenize_seconds': old_tokenize_seconds, 'new_tokenize_seconds': new_tokenize_seconds,
                'historical_observations': len(observations[-3:]),
                'source_paths_changed': sorted(changes), 'source_context_from_actual_base_not_unpublished_workspace': True})
    assert len(rows) == 15
    system_tokens, _ = tokens(SYSTEM)
    result = {'tokenizer_alias': props['model_alias'], 'loaded_context': props['default_generation_settings']['n_ctx'],
              'system_text_tokens': system_tokens, 'model_inference_calls': 0, 'publication_calls': 0,
              'scope': 'Development-only historical size replay. Same current tokenizer for old/new raw JSON text; not rendered chat input, review latency, quality, genuine new test execution, or fresh workflows. Oversized diagnostic packets cannot pass default admission.',
              'rows': rows}
    (args.output/'measurements.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'historical_records': len(rows), 'byte_budget_fits': sum(x['fits_32768_byte_budget'] for x in rows),
        'token_target_fits': sum(x['fits_7500_packet_text_token_target'] for x in rows), 'model_inference_calls': 0}))
if __name__ == '__main__': main()
