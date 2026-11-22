# XML stage replay

Verify `part3b-evidence.tar.gz` against `part3b-evidence.sha256`, extract into a
new directory, and run:

```bash
python3 verify_part3b.py --root /absolute/path/to/extracted
```

The offline verifier checks all manifested bytes, rebuilds eleven packets,
checks eleven complete response captures and nine admissions, binds twelve
local/remote source snapshots to execution logs, and checks four mutant source
and receipt-payload sets. It does not rerun tests, authenticate historical MACs
or certify semantic correctness. Private historical signatures were separately
verified; their keys and MACs are not exported.

Use the pinned image and isolated read-only test mounts described in
[Part 3a replay](part3a-replay.md) for actual project/preservation tests. For XML
primary replay mount extracted `checks` at `/checks` and invoke:

```text
python /checks/private_checks.py /workspace wolfram_errors PHASE
```

Use phase 0/1/2 matching the issued task. Original baseline fails; substitute
`reference/wolfram/__init__.py` into a separate baseline copy to test the reference.
The primary check's WolframError oracle is implementation-specific; inspect the
wrong-attribute and genuine no-result counterexample in the report independently.

`feature-mutations/CASE/source` holds four unpublished posthoc coverage controls,
with exact mutation diffs, actual project/preservation logs, payloads and private
check logs. The LocalAI worker mutant's passing suite is a coverage gap, not a
claim that original published worker code was wrong. Never reuse historical
receipts as authorization or rerun authenticated publication against these arenas.
Native profile/system/memory prompts, raw actor requests, secrets, signing keys
and state databases are deliberately excluded.
