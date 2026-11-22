# Compact publication review — experimental primitives

This library is **not installed in the production Hermes profile**. Part 1
implements packet construction and offline admission checks; native transport,
trusted Docker execution integration, timed reviewers and fresh workflows remain
later stages. See the [staged evaluation](../../evaluations/2026-11-22-compact-review/plan.md).

## Packet

`build_packet()` takes an authoritative text-source inventory, actual base Git
commit, exact proposed mutation, already-issued tasks and explicitly selected
context/documentation paths. It produces complete unified diffs, source hashes,
requested actual-tree context and generic one-hop Python state-writer/callee
context. It never substitutes unpublished adjacent scratch files or includes
owner profiles, raw skill history, private graders, reference fixes or future
prompts. Oversized packets block; nothing is silently cut to fit.

The default limit is 32 KiB of compact JSON. This is a byte bound, not a universal
token count. The eventual transport must measure the actual reviewer tokenizer,
rendered chat input and output reserve. AST indexing must run in a Python version
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
It does not itself provide a sandbox: the later adapter must run against the
exact proposed publication snapshot, read-only, without owner credentials,
private graders, profile or Docker socket. A callback or inventory supplied by
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
python3 -m unittest discover -s hermes-profile/compact-review -p 'test_*.py' -v
```

The public evaluation records the same 19 checks in the pinned Python 3.14.9
image. Negative cases cover forged/stale evidence, failing latest tests,
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

Source inventories currently cover text files only. A future adapter must preserve
exact byte/newline content when decoding its inventory, and must reject unsupported
binary mutations rather than claiming they were reviewed.
