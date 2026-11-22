# Compact publication review — experimental primitives

This library is **not installed in the production Hermes profile**. It includes
packet/admission primitives, a trusted Docker test adapter, timed response capture
and an experimental MCP publication adapter. Native workflow integration and
independent fresh-workflow qualification remain separate evaluation stages. See the [staged evaluation](../../evaluations/2026-11-22-compact-review/plan.md).

## Packet

`build_packet()` takes an authoritative text-source inventory, actual base Git
commit, exact proposed mutation, already-issued tasks and explicitly selected
context/documentation paths. It produces complete unified diffs, source hashes,
requested actual-tree context and generic one-hop Python state-writer/callee
context. It never substitutes unpublished adjacent scratch files or includes
owner profiles, raw skill history, private graders, reference fixes or future
prompts. Oversized packets block; nothing is silently cut to fit.

The default limit is 32 KiB of compact JSON. This is a byte bound, not a universal
token count. The controller must measure the actual reviewer tokenizer, rendered chat input
and output reserve; the calibration uses `/apply-template` and `/tokenize` and
checks the backend-reported usage. AST indexing must run in a Python version
compatible with the source. Context retrieval is a heuristic: it does not prove
all relevant dependencies are visible. A reviewer can request more context.

## Execution prerequisite and trust boundary

The **trusted controller**, never the model, chooses required suite IDs/argv,
pinned execution environment and inventory, supplies an isolated execution
callback, and keeps a fresh per-case signing key outside model mounts. The key
must not be reused across independent hosts/controller lifetimes. The test key
in the regression suite is deliberately public and must never be deployed.

`run_suite()` executes that fixed argv, records the actual return code/timeout
and compact output digest/tail, verifies source stability and signs the receipt.
It does not itself provide a sandbox. `DockerExecution` runs the exact proposed
publication snapshot read-only, as UID1000, network-none, without capabilities,
owner credentials, private graders, profile or Docker socket, with CPU/memory/time
bounds. The adapter itself is trusted and needs Docker access. A container hard
kill is a nonzero failed execution; the receipt timeout flag specifically records
a host subprocess timeout, not a diagnosis of every killed child. A callback or inventory supplied by
the model would violate this boundary and provide no execution guarantee.

`admission()` checks authenticated latest receipts for the same source and
runtime, unchanged source/packet, complete requested coverage and an explicit
supported reviewer assessment of tests and documentation. Ordering uses a
monotonic clock; failures/timeouts cannot be hidden by earlier passing runs or
wall-clock ties. Shell pipelines are not registered as suites. The reviewer
must return one bound JSON response without unresolved findings.

These checks establish prerequisites, not correctness. Model-authored tests can
be ineffective, a fixed suite can have poor coverage, and a reviewer can approve
bad code or inaccurate docs. Independent evaluation remains necessary. Even a
signed exit-zero result is not a semantic oracle.

## Tests and historical size replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider hermes-profile/compact-review
```

Part 1 records 19 checks. The expanded suite has 31 checks plus 20 subtests
in the pinned Python 3.14.9 / pytest9.1.1 image. Negative cases cover forged/stale evidence, failing latest tests,
timeouts, source drift, omitted coverage, bad paths, malformed reviews and
missing documentation/test assessments. The positive execution case runs an
actual unittest against its bound temporary source tree.

`measure_historical_packets.py` is an operator-only **development size replay**.
It needs the completed pilot's private original records and public extracted
archive. It sends text only to the existing local `/tokenize` endpoint, with no
model inference or publication. It never publishes old private receipt tails.
Published historical excerpts are filtered to tool messages before the original
review request and labeled as observations, not authenticated new execution.
Diagnostic replay permits measuring oversize packets, while default admission
still refuses them. Historical packets cannot authorize a new publication.

Source inventories currently cover text files only. The Docker adapter decodes
raw UTF-8 bytes without newline translation and rejects symlinks/binary source.
File modes and the actual remote Git tree need independent publication audits.

## Timed transport and publication adapter

`TimedReview` preserves the whole nonstreaming body after caller expiry. Late,
truncated, malformed or non-stop responses cannot authorize publication. Capture
must finish before a calibration case is replayed or its server is removed;
a socket-read timeout is not a universal backend cancellation deadline. An outer
trusted controller must enforce its stage guard and restore the original runtime.
`request_body()` binds a simple JSON schema to the packet ID. Constrained valid
JSON does not establish valid reasoning or supported findings.

`PublicationGate` materializes the actual cumulative MCP payload over the
pristine base and already accepted remote writes, runs the project suite against
that snapshot, and requests review. It does not substitute a local scratch tree.
The outer MCP scope checks ownership, branch, paths and turn lease first; only a
successful matching remote write updates the gate's published state. Signing
keys stay outside actor/test mounts. Never expose this trusted Docker adapter
or its socket through an actor file or command tool.

Full mode requires explicit supported test/docs assessments and no unresolved
findings. `docs_only_control` is an experimental comparison control: genuine
project tests and an external documentation check are common to both arms, while
behavioral/coverage findings are withheld from the control. It is not full review
qualification or a no-review latency measurement. Both modes can still miss bugs
and accept poor tests or false documentation; independent audits are required.
The native MCP adapter completed the first fresh family in [Part 3a](../../evaluations/2026-11-22-compact-review/part3a.md); the second family remains required. Authentic tests and timely reviews still approved task-relevant mistakes.


## Immutable preservation and source context

When `preservation_tests` and its digest are configured, `PublicationGate` requires
both `project` and `preservation` receipts. `DockerExecution` runs the latter with
the original tests mounted read-only over the candidate tests directory, and the
environment identity binds that original-test digest. Rewriting candidate tests
cannot erase this suite. Complete output logs are independently hash-bound.

`build_packet(class_declarations=True)` includes actual static class assignments,
such as settings/metasettings, in generic Python context. It remains optional
and bounded; it does not include every unchanged caller. Part3a exposes the
consequence: an unchanged public reply prefix was absent from review context.
The independent primary grader/reference also missed that path. Passing either
test policy or requested-context coverage does not establish whole-program
coverage, meaningful tests, truthful docs or a correct delivered result.
