# Adapted 27B IQ4_XS capacity check

The pinned public IQ4_XS completes all five capacity probes at **65,536 context**.
Both 98,304-context layouts fail CUDA allocation (microbatches 128 and64); these
are fit exclusions, not coding-quality failures. No CPU-layer fallback was tried.
The selected layout requests99 GPU layers, microbatch64, q4_0 KV and fit off.
Resource logs do not enumerate every tensor: native verbose placement remains a
required gate before the actor starts.

The 16,152-token input takes226.314 seconds. The 51,942-token input takes598.859
seconds and returns `capacity-check-52000`;16,084 input tokens were cached from
the preceding probe. These are operational request timings, not isolated decode
benchmarks. Its nine-token completion is too short to establish normal generation
speed. The short tool call, actual tool-result answer and dependent-history marker
also pass. This is not coding or Gitea qualification.

176 complete samples record15,788MiB peak device use,7,051,190,272 bytes aggregate
charged cgroups (6.567GiB, includes cache/helpers),2,360,057,856 bytes process PSS
(2.198GiB), zero study swap and no resource guard triggers. The original model
filesystem stays above110.455GiB free and staging above125.086GiB. These sampled
measurements do not prove continuous whole-host bounds or zero host allocations.
Inactive selected-file pages are evicted before each layout, not globally flushed.

The original services/default98k alias, four owner configuration hashes, all30
retained model metadata entries, owner pending edits and the unchanged Codex
container snapshot pass independent restoration checks. The exact completed
supervisor is removed. A prior registration-binding harness failure happened
before model loading and is preserved separately without a model score.

The [summary](resource-adapted-iq4-summary.json), [protocol](iq4-resource-protocol.json),
[full evidence](resource-adapted-iq4-evidence.tar.gz) and [SHA256](resource-adapted-iq4-evidence.sha256)
include both failed layouts and the selected layout. Run `python3 verify_iq4_resource.py
resource-adapted-iq4-evidence.tar.gz`; the saved positive and three coherently
modified negative controls pass. Public quantization/imatrix pins remain in the
[candidate record](prospective-adapted-iq4-xs.json). A fresh dependent coding/Gitea
trial at the measured64k layout is next; no everyday winner is selected.
