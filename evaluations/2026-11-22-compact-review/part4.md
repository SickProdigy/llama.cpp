# Whole changed-module context did not improve these paired reviews

The four-request posthoc diagnostic is complete. **All four responses approve
both defective historical proposals with no findings.** Whole changed-module
context increases input and observed latency, without improving detection in
these two selected pairs. This is not fresh model qualification, a statistical
reliability estimate, or proof that every context expansion is ineffective.

| Completed proposal | Context | Packet bytes | Actual input tokens | Review seconds | Result |
|---|---|---:|---:|---:|---|
| LocalAI documentation-control initial | Compact | 13,548 | 4,720 | 77.48 | Approve, no findings |
| Same source/evidence | Whole changed module | 24,692 | 7,376 | 91.44 | Approve, no findings |
| LocalAI full-review initial | Whole changed module | 23,512 | 7,092 | 94.86 | Approve, no findings |
| Same source/evidence | Compact | 12,301 | 4,420 | 63.66 | Approve, no findings |

Both snapshots actually deliver 208 characters with a configured limit of 200:
the unchanged public caller adds the username prefix after chunk sizing. Control
also fails to preserve complete inputs in 9 of 18 near/exact-cap cases, while
full preserves all 18. These are independently executed probes against the exact
reviewed snapshots, not deductions from green model-authored tests. All four
reviews label tests adequate; none identifies these defects. Original primary
checks/reference missed the caller path, as already disclosed in Part 3a.

## Registered comparison

The protocol was registered after LocalAI source-audit findings, while the XML
cohort was still running. No diagnostic request starts until both fresh families
finish and the original runtime is restored. It permits exactly four requests,
with no new seed, retry or selected counterexample added after results. Its
private expected audit is unblinded only after calls finish.

Each source gets fresh genuine project and immutable original preservation
execution, with new trusted signing key and matching source/log hashes. The two
variants share the same execution payloads. Compact packets reproduce historical
content except new receipts and packet IDs. The whole-module rule generically
includes every changed production Python module, excluding tests, and removes
redundant related-code excerpts for those files. It does not select a named
caller or insert private graders/references. Here the changed file is
`localai/__init__.py`, so unchanged public delivery code becomes visible.

All calls use the same pinned 27B IQ3_XXS, 98,304 q4 KV context, sampler,
1,024-token output cap, JSON binding, 240-second caller, 32 KiB packet and 10k
rendered input bounds as Part 3. All complete with stop and verified usage;
none times out. Outputs contain 178–200 tokens. There are no actors or actual
publications. Cache/order differ between requests; the latency difference is an
observation from this fixed order, not an independently repeated causal estimate.
Fresh receipt signatures are verified privately; public payloads prove source/log
consistency without exporting keys or MACs.

## Preservation and reproducibility

The original VibeForged runtime is restored and the owned supervisor, backend and
internal network removed. All original container IDs/images/configuration,
profile hashes, 29 model inventory entries, pending owner files and ignored
instructions match; Hermes-Codex's entire snapshot remains unchanged. Model disk
has 123.98 GiB free. No weights are downloaded or removed.

[Archive hash](part4-evidence.sha256), [validation](part4-artifact-validation.json),
[privacy scan](part4-privacy.json), [preservation](part4-preservation.json) and
[summary](part4-summary.json) record the results. Verify the hash, extract the
archive into a new directory, then run:

```bash
python3 verify_part4.py --root /absolute/path/to/extracted
```

The verifier checks every manifested file, rebuilds both compact packets and
both generic whole-module transformations, verifies four complete captures and
binds four execution payloads to actual source/logs. It does not execute tests
or authenticate historical MACs. For real test/probe replay use the isolated
pinned-image mounts in [Part 3a replay](part3a-replay.md), mounting
`cases/CASE/source` at `/workspace` and `checks` at `/checks`. Run project tests
and immutable baseline tests separately; run both supplemental scripts as
`python /checks/check_public_delivery.py /workspace` and
`python /checks/check_exact_fit_preservation.py /workspace`. No credential,
model, socket or native-profile mount is needed for these tests.

## Decision

The compact protocol solves the observed oversized-review/feedback-delivery
problem, but no tested reviewer qualifies as a correctness gate. Real test
execution and honest publication-state checks are useful prerequisites, not
sufficient acceptance criteria. Keep this library experimental and retain human
review. Future work should test actual public delivery boundaries and local versus
remote preservation, rather than accept test counts or a model's approval alone.

The separate wider-memory shortlist is recorded in `MODEL-OPTIONS.md`. Its
candidate fits, speed and quality remain untested under that budget. These
results do not establish that another GPU is needed. The staged compact-review
evaluation is complete with a negative qualification result; the requirement was
to perform and audit the evaluation, not declare a winner despite the evidence.
