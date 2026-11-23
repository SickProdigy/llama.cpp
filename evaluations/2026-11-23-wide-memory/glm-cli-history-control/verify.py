"""Verify the saved scripted integration evidence, without model inference."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
for name, expected in json.loads((root / 'sha256.json').read_text()).items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected, name
rows = json.loads((root / 'wire-projection.json').read_text())
assert len(rows) == 3
for row in rows:
    assert row['max_tokens'] == 16384
    assert row['chat_template_kwargs'] == dict(enable_thinking=True, clear_thinking=False)
for row in rows[1:]:
    messages = row['assistant_and_tool_messages_only']
    assert any(m.get('reasoning_content') == 'control-reasoning-tool-one' for m in messages)
    tools = [m for m in messages if m['role'] == 'tool']
    assert len(tools) == 1
    result = json.loads(tools[0]['content'])
    assert result['exit_code'] == 0 and result['output'] == 'hermes-glm-history-control'
assert any(m.get('reasoning_content') == 'control-reasoning-final-one'
           for m in rows[2]['assistant_and_tool_messages_only'])
result = json.loads((root / 'result.json').read_text())
assert result['passed'] and all(result['checks'].values())
assert result['model_inference'] is False and result['actual_forge_actions'] is False
print('PASS: saved scripted client-history evidence; no model quality claim')
