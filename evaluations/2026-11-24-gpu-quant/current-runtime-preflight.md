# Current owner-runtime compatibility, November26

The rebuilt owner Hermes image has changed prompt building, tool execution,
CLI and MCP-handler sources. The completed cold Fable pair deliberately shares
the prior pinned experimental Hermes image; it must remain labeled with that
runtime and cannot establish behavior on the newer owner stack.

A new isolated evaluation image derives from the exact current owner image and
adds only pytest9.1.1/iniconfig2.3.0/pluggy1.6.0, copied offline from the prior pinned
evaluator. Existing packaging26.3 and Pygments2.21.0 already match and are unchanged.
The owner base layers are an exact prefix; no owner image, container or profile
is replaced. Actual package locations and the pytest root shim are verified;
two preparation-copy errors are corrected before model use and excluded from scores.

The new build passes83 original tests plus2 subtests. Both unused Vibe reasoning
profiles pass actual SDK serialization/sampler/context/timeout checks and native
approved code execution. A separate native plugin/MCP control verifies identity,
repository read and scope-level rejection of a write under a read-only lease.
These controls use zero model inference and zero forge mutations. They establish
compatibility, not model quality or a fix for earlier model mistakes.

The [sanitized provenance/preflight summary](current-runtime-preflight-summary.json)
and [offline Dockerfile](current-runtime-evaluation.Dockerfile) record exact image
pins, selected source fingerprints and test dependency versions. Future scored
cells must prospectively bind this runtime and use fresh state. Do not merge
older/newer runtime scores into a precision-only causal comparison.
