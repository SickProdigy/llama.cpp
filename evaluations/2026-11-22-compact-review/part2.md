# Part 2 — reviewers are faster, but none qualifies as a correctness gate

The compact protocol delivers usable responses instead of the previous pilot's
240-second critic timeouts. It does **not** make the reviewers dependable: every
profile misses all four predefined faulty proposals. This is a negative review
qualification result, not a recommendation to deploy an automatic publisher.

| Reviewer/profile | Median review | Range | Predefined faulty proposals detected | Clean controls approved |
|---|---:|---:|---:|---:|
| 27B IQ3_XXS, full GPU | 65.0s | 28.9–79.5s | 0/4 | 2/3 |
| Qwopus4B Q5, full GPU alone | 12.2s | 6.4–18.5s | 0/4 | 1/3 |
| Qwopus4B, 12 GPU layers beside 27B | 38.2s | 25.0–52.2s | 0/4 | 2/3 |
| FableVibes14B-A3B Q4, full GPU alone | 15.8s | 6.9–27.0s | 0/4 | 3/3 |
| FableVibes, 4 GPU layers beside 27B | 57.5s | 28.9–87.1s | 0/4 | 2/3 |

These are seven development cases per profile, not independent population
samples. Three faulty proposals share Arr code. Five identical warm repeats and
one cache-interference repeat are excluded from accuracy and median figures.
A revision/context request is not a detection unless its evidence identifies an
actual defect. A passing project suite, valid JSON or blocked publication is not
proof of correctness.

## Findings checked independently

The frozen faults are lifecycle reload reviving a queued Beets import, rejection
of valid relative redirects, false redirect-limit/relative-redirect documentation,
and missing HTTPS initialization/false certificate-error documentation. All are
missed. Some faulty proposals are blocked for unrelated or false reasons.

FableVibes **alone** finds one additional real test weakness: a purported
scheme-only redirect test also changes the port. Removing the scheme comparison
still leaves **86 tests and two subtests passing**, while a separate isolated
same-host/same-port probe accepts the wrong scheme. This is confirmed supplemental
test-gap detection, not detection of a predefined active-code fault. That reply
also invents the original port and makes unsupported source claims.

The co-resident Fable profile instead raises a plausible missing multi-hop test
concern, but falsely says the same-origin test never makes a second request.
The source explicitly verifies two requests and the redirected request's header.
Its clean Room Announcer response says `revise` with empty findings and positive
test/docs checks. This remains blocked; it is not converted to approval afterward.
Same weights/seed across different offload paths did not produce identical judgments.

The 27B's blocked integer control is a **real cosmetic missing-space nit**, not a
hallucinated fact or behavioral defect. Qwopus falsely claims that supplied
`None`, non-string and decimal-integer-string tests are missing. Other clean-control
blocks demand unrequested documentation specificity. The integer control uses
base-ten integer strings such as `"12"`; it does not promise fractional inputs.
The Room Announcer clean contract covers normal GUI string inputs, not arbitrary
`None` entries. These bounded controls are not general proofs of correctness.

## Protocol and genuine execution

Eight source snapshots and expected outcomes were frozen before inference:
four faulty proposals, three clean controls, and one genuinely failing project
suite. A trusted adapter executed all project suites in the pinned Python 3.14.9 /
pytest 9.1.1 image against the exact read-only candidate, network-none, with no
profile, credentials, private grader or Docker socket in the test container.
Fresh private issuer keys authenticate source/runtime-bound execution receipts.
The failing suite is rejected without asking a critic. Public payloads permit
source replay; private keys are deliberately excluded, so external readers cannot
reverify historical HMACs from the public archive alone.

There are **35 scored reviews, five warm repeats and one cache-interference
review**. All 41 produce complete stop-finished responses within the 240-second
caller deadline. All actual template/tokenizer counts equal backend prompt usage.
Inputs are bounded to 32 KiB and 10,000 rendered tokens; output is capped at 1,024.
The actual scored input range is 1,448–5,645 rendered tokens. Sampling is 0.8,
top-p 1, top-k 0, min-p 0, repeat 1, presence 0, seed 20261122, thinking disabled.
No tools, private checks, reference corrections, future tasks or earlier model
verdicts are supplied to the reviewers.

The pinned backend's JSON-schema wrapper, `/apply-template` and `/tokenize` are
[documented here](https://raw.githubusercontent.com/ggml-org/llama.cpp/d3c3e242c/tools/server/README.md)
and separately checked on every loaded profile. A tiny initial schema preflight
succeeded, then an operator file-hash/JSON-serialization assertion stopped the
first controller **before any scored request**. Its restoration completed.
A new controller/queue corrected the bookkeeping check against the same frozen
inputs; that administrative failure is retained in the evidence.

There are no real 240-second reviewer timeouts in this comparison. Actual loopback
HTTP regression tests separately exercise caller expiry, complete late 40 KB-body
capture, truncated bodies and malformed responses. Late/length-ended responses
cannot authorize publication. This does not prove all slow server failures are
recoverable. A hard-killed project suite is blocked by its nonzero exit; its
receipt timeout flag records host subprocess timeouts rather than diagnosing
every killed child.

The earlier size/timeout comparison changes packet content, output cap and schema
handling together. It is not a causal estimate of packet-size reduction alone.
Historical cases remain development data. Fable supplements were registered after
the first models' poor results, with unchanged inputs; they are not fresh tests.

## Memory, cache and total cost

| Profile | Observed review peak GPU memory | Minimum observed free memory |
|---|---:|---:|
| 27B alone | 12,930MiB | 3,345MiB |
| Qwopus4B alone | 3,554MiB | 12,721MiB |
| 27B + Qwopus12-layer reviewer | 14,710MiB | 1,565MiB |
| FableVibes alone | 8,334MiB | 7,941MiB |
| 27B + Fable4-layer reviewer | 14,178MiB | 2,097MiB |

Both partial-offload profiles meet the predeclared 1,024 MiB startup headroom
requirement. Full-GPU co-residence was not attempted. Solo critic speed therefore
cannot be advertised as the speed of a co-resident reviewer.

Model start/readiness takes roughly 37–62 seconds in the recorded launches. Full SHA
reads warmed OS file cache beforehand; these are **not cold-disk load times**.
The `launch-27b.json` snapshot is the later reload; the event journal retains the
initial 45.6s launch too. One container snapshot must not be mistaken for all launches.

A synthetic 19,216-token actor prefix takes 215.7s to prefill, versus 0.257s with
19,212 tokens cached. After a self-review it **still** has19,212 cached tokens
and 0.285s prefill. The pinned server retained both prompt states: this probe does
not show an actor-cache eviction penalty from self-review. After swapping through
the solo 4B and reloading 27B, the prefix is cold and takes 221.1s. Co-resident 4B
review retains the tested prefix. The 19K cache probe was not repeated for Fable
co-residence; actual native costs must be measured later. Fable's complete
swap-back workflow cost is unmeasured, so its 15.8s solo median is not an end-to-end win.

## Next-stage choice and delivery boundary

No candidate is qualified. For the fresh diagnostic workflows, retain the 27B coder
and use an isolated 27B self-review request with the compact packet, genuine test
gate and 240-second deadline. This chooses the simplest measured path with no
model swaps and retained cache in the 19K probe; it is **not** a claimed accuracy
winner over Fable. Extra models did not establish enough reliable defect detection
to justify a more complex default. Production remains unchanged.

Part 3 will compare full code/test/docs feedback with a control that still requires
genuine execution, immutable public-original preservation tests and an external
documentation check. The original-suite integration is planned for the next
stage and is not claimed as a delivered native check here. Thus it measures the added
behavioral/coverage feedback under common safety controls, not pure no-review
latency. Private independent checks, immutable preservation tests and manual docs /
claim audits determine outcomes. Fresh source context will also include generic
static class declarations so unchanged GUI metadata is visible; this planned
context-policy change is not part of the calibration results above.

The experimental publication adapter is delivered with 30 framework checks plus
20 subtests passing in the pinned native image, but its
native MCP integration is not yet qualified. It materializes the actual cumulative
publication payload rather than substituting a scratch checkout, executes the
real suite, checks rendered input/reserve and binds the verdict to that source.
It cannot make weak tests or a mistaken documentation assessment trustworthy.

Original Hermes/llama.cpp were restored and independently verified after each GPU
controller. Final original IDs/images/configurations, four profile-file hashes,
the inventory and size/mtime metadata of all 29 models match the baseline.
The tested 27B/4B hashes match prior manifests; Fable has a recorded full local
file hash, with its upstream revision unrecovered in this stage. Hermes-Codex's start time
and restart count are unchanged. At least 124 GiB remains free; no model was downloaded,
deleted, trained or quantized. No conclusion about unattended reliability or a need
for different hardware follows from this sample.

[Measurements](part2-measurements.csv), [summary](part2-summary.json), [quality audit](part2-quality.json),
[preservation](part2-preservation.json), [privacy check](part2-privacy.json),
[replay instructions](part2-replay.md), and [staged plan](plan.md).

Fresh-stage setup also created two separate private upstream arenas and seeded
the pristine committed source while calibration ran. Those operator setup commits
are not model publication successes; no fresh model workflow, issue or PR has
yet run. Native profiles and private checks remain outside this evidence archive.
