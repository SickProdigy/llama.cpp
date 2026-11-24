# FableVibes Q6: GPU fit, unsuccessful native workflow

November 24, 2026. **Fable Q6 fits the tested GPU configuration, but this fresh
thinking-disabled baseline does not complete the coding/Gitea workflow correctly.**
This is one configuration and one dependent task lineage, not a general verdict
on the checkpoint or evidence that Q4 is better. The Q4 comparison and separately
registered publisher reasoning-mode pair remain pending.

## Exact configuration

Public `tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF`, revision
`9cf910a7ad68dfedcbdfc46ef0fe5003dec07c23`, file
`Qwen3.6-14B-A3B-FableVibes-Q6_K.gguf`, 11,325,370,880 bytes,
SHA256 `7ae56e5003365c568635c14158381df134577877c90ae15f34dbc6de2ca7ffb1`.
The retained file is fully hashed again before native inference.

Pinned backend b12627 / source `225a5345b`, image
`sha256:7561b4761f849925a728c5ac2bd1f4a649b6a76f24544e7f992b047ad016cec3`.
98,304 context, one slot, q4 K/V, two context checkpoints, non-mapped loading,
512 MiB host prompt cache, automatic fit disabled, requested 99 GPU layers.
Actual verbose load confirms **41/41 layers offloaded**, 10,392.38 MiB CUDA model
buffers, 397.85 MiB CUDA-host model buffers and 540 MiB GPU KV cache. This is
mostly GPU-resident inference, with the stated remaining host buffers.

The matched baseline uses temperature .2, top-p .95, top-k 40, min-p 0,
repeat penalty 1, presence penalty 0, seed 20261124 and thinking disabled. Every
captured native HTTP body confirms these settings and an 8192 output cap.
The backend cap is 6656m/no swap; relevant study aggregate guard is 8 GiB.
Each coding turn permits 60 iterations and 10800 seconds, with separate provider
and external guards. No operator continuation or corrective hint is supplied.

The actual full native CLI schema contains 33 tools, normal skills and the scoped
Gitea/workspace plugins. The explicit-subset no-inference transport preflight
has fewer tools; it is not a claim that normal CLI uses only that subset.
The actor has an existing selected checkout and working configured MCP, while
external terminal Git/DNS is blocked by the internal experiment network.
Unrestricted-network performance is not measured.

## Independently audited outcome

| Turn | Minutes | Actual outcome |
|---|---:|---|
| Initial lifecycle repair and contribution | 15.43 | No source/test changes; 51 redundant terminal clone attempts hit blocked DNS; no issue/fork/PR; CLI exit1 |
| Retained README followup | 1.37 | Local README commit, but it describes abandonment of waiting imports that unchanged code does not implement; no publication |
| Retained cancellation feature | 4.26 | Required command missing, existing manual imports broken, authored tests fail collection, no publication; native no-progress stop despite CLI exit0 |

Total coding time is **21.05 minutes**. Read-only repository discovery takes
91.53 seconds separately. The entire supervised GPU stage, including hashing,
load, controls, grading and restoration, takes 26.57 minutes.

The initial source snapshot is byte-identical to all 40 baseline files. Operator
project and immutable-original suites pass, while the independent lifecycle
cases fail. The model has not fixed the defect or authored a regression test.
The selected checkout, exact upstream/base and Beets policy are present in its
actual first coding request; literal presence does not prove attention.

The README-only turn preserves prior lines, but adds contradictory scheduled-work
wording, false waiting-work abandonment and an overbroad manual-import guarantee.
Its local commit `e7b137f1ccfcf48d744da4b8d8ad3fe82dad58db` is not a remote
contribution. An external-terminal DNS failure does not establish that the
working configured Gitea MCP is unreachable.

The feature changes `beetsimport` instead of registering `beetscancel`. It adds
a second metadata parameter enclosed in angle brackets, making it required.
Actual unmodified pinned Nicotine+ 3.3.11 and master dispatcher methods reject
the original single-folder import. Folder paths containing spaces are instead
split into cancellation arguments and also fail. Original and private reference
sources still schedule both correctly under the same dispatcher controls.
The cancellation helpers handle pending timers only; dispatched waiting workers
and the initial stop/reload defect remain. Feature documentation is absent.

The 16 new test methods do not collect in the pinned runtime because their nested
package imports an unavailable `pynicotine` dependency instead of using the
repository's existing fake peers. The same authored tests on the prior
implementation also fail collection, which is **not meaningful regression proof**.
Source review additionally finds an unset `self.tmpdir`, contradictory timer
expectations, and purported cancellation tests calling the import callback.
The original test functions are preserved and all 83 immutable originals pass,
but they miss the independently executed slash-command regressions.

Missing test dependencies are qualified as authored-test setup problems in this
runtime, not proof of a fully installed GUI failure. The missing command, bad
dispatcher behavior and lifecycle defect are established independently. No real
GUI, external beets process or music import is exercised by these controls.

## Memory, context and latency

141 complete samples, no measurement errors or guard triggers:

- Peak sampled GPU: 11,566 MiB.
- Relevant charged cgroups, including cache/helpers: 6.698 GiB.
- All-process PSS: 2.019 GiB; experiment swap: 0 bytes.
- Minimum model-disk reserve: 109.87 GiB.
- Whole-host swap counters move 16,973 input / 76,495 output pages without
  attribution to this experiment. Sampling does not prove continuous whole-host
  allocation bounds.

All 93 captured HTTP responses complete without transport errors. The largest
native prompt is 74,903 tokens; the last complete prompts per coding turn are
53,880 / 62,728 / 74,903. All issued tasks remain literal in subsequent requests,
and the lineage stays one session with no separate compression request.
Native context includes extensive failed-clone history; this is not evidence
of useful whole-window code reasoning. The native generic maximum-iteration
finish instruction adds a user-role message which remains in later history;
it is not an operator resend or private corrective hint.

Backend intervals across read/coding calls range 1.22–77.31 seconds, median 9.19,
sum 1224.94. These include prefill/output/queueing and are not isolated decode
throughput. The first coding request reports zero cached prompt tokens.

## Publication, preservation and reproducible evidence

Independent connected-forge readbacks show no upstream issue or PR and unchanged
upstream main `31e14884e4cc90e3c02f10ca2d562dbfddf7e5b1` in
`chatgpt-codex/hermes-gpuquant-fable-q6-20261124`. Exact fork lookup authenticated
as `hermes-agent` returns 404. There are no owned test issues requiring closure.
No remote default branch changes or merges occur.

Original service identities/images/configuration, alias/context, four profile
files, all 30 retained model metadata entries, owner pending files/instructions
and Hermes-Codex state are independently verified after restoration. Exact owned
containers and network are removed. A later scoped mincore check observes
3,796,992 cached bytes for the inactive Q6 file; advising only that file DONTNEED
reduces the observed resident pages to zero. No model content is modified, and no global cache flush occurs. This poststage observation does not reconstruct historical residency.

The [summary](native-fable-q6-beets-summary.json), sanitized archive and
[positive validation](native-fable-q6-beets-validation.json) retain observed
failures. [Coherent tampering controls](native-fable-q6-beets-verifier-controls.json)
reject wrong source, request and authored-test source bindings. They test the
artifact verifier, not model capability.

```sh
python3 verify_native.py native-fable-q6-beets-evidence.tar.gz
python3 verify_native_controls.py native-fable-q6-beets-evidence.tar.gz
sha256sum -c native-fable-q6-beets-evidence.sha256
```

Private source, requests, profiles, session DBs, graders, references and signing
keys remain local. Public consistency checks do not rerun those private behavior
checks or prove autonomous reliability. The publisher reasoning-enabled
Q4/Q6 comparison is prospective; this baseline is not retrospectively rescued.
