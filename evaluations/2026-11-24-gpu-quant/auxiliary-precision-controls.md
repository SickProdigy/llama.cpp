# Auxiliary checkpoint controls, November 26

These are direct replays of one saved native compression request, not fresh
coding/Gitea workflow scores. The public retained FableVibes Q4_K_M weights,
98,304 context, seed 20261124 and 8,192 output cap are fixed. Each request forces
uncached prefill, verified by zero actual cached tokens. No model tools or forge
writes are enabled. Private history and generated output remain local.

The current owner-rebuilt backend is b12723-abca69200; the old historical image
is unavailable. All new controls use the same current image. The low-temperature
nonthinking q4-cache replay reproduces the historical bad answer exactly, but
this is not an exact historical-runtime reproduction.

| History and cache | Auxiliary generation | Observation |
|---|---|---|
| Native turns, q4_0 K/V | Original nonthinking | Tool-call markup instead of a checkpoint; 120.09 s / 85 output tokens |
| Native turns, q4_0 K/V | Same sampler, thinking enabled | Repeated completed-actions cycle; 322.09 s / 8,192 tokens, length limit |
| Native turns, q4_0 K/V | Publisher reasoning sampler | Reasoning-only continuation, no answer checkpoint; 105.38 s / 99 tokens |
| History quoted as JSON data, q4_0 K/V | Original nonthinking | Repetitive constraints, later sections absent; 384.15 s / 8,192 tokens, length limit |
| History quoted as JSON data, q4_0 K/V | Same sampler, thinking enabled | Complete section structure, but visible failing tests omitted; 190.61 s / 2,060 tokens |
| Native turns, FP16 K/V | Original nonthinking | Tool-call markup again; 109.40 s / 85 tokens |
| Native turns, FP16 K/V | Same sampler, thinking enabled | Reaches all main sections, then repeats the final log; failing test status omitted; 281.27 s / 8,192 tokens, length limit |
| Native turns, FP16 K/V | Publisher reasoning sampler | Reasoning-only continuation, no answer checkpoint; 104.18 s / 98 tokens |

Changing cache precision visibly changes this reasoning sample, but did not
produce a trustworthy checkpoint. Structural improvement is not a correctness
pass, and the altered JSON wrapping changes tokenization/history presentation.
Neither control changes any earlier coding outcome or establishes a better model.
The wrapped reasoning output's Python version is supported by source history;
it is not counted as a hallucination. The specific omitted status is a visible
13-test run ending with two failures, not an unseen independent grader result.

All three stages confirm 41/41 GPU layers and zero study swap. The q4-cache
stages peak at 8,964 MiB sampled GPU; FP16 peaks at 10,162 MiB. GPU KV grows
from 540 to 1,920 MiB; the backend's compute buffer changes from 229.01 to
50.01 MiB with the cache type. These are measured runtime consequences of
changing cache precision. Aggregate charged cgroups peak at 7,057,166,336 bytes
across the controls; process PSS peaks at 1,406,835,712 bytes. There are 345
five-second samples with no measurement errors or guard triggers; sampling can
miss transient peaks. Whole-host swap is not attributed to the study.

Original container identities, images, configurations and restored alias/context,
all 30 retained model metadata entries, four owner profile hashes, pending owner
repository edits and the separate Codex instance pass postflight checks.
Exact exited supervisors and their backend/network resources are removed.
Disk reserve remains above 100 GiB (106.80 GiB after the FP16 stage).

The [numeric evidence archive](auxiliary-precision-controls-evidence.tar.gz)
contains captured usage/timing, source fingerprints, placement lines and curated
semantic judgments. Check its [SHA256](auxiliary-precision-controls-evidence.sha256)
and run `python3 verify_auxiliary_precision_controls.py auxiliary-precision-controls-evidence.tar.gz`
from this directory. This verifies saved consistency, not private semantic replay.
No production configuration has been changed. No models were downloaded,
quantized or deleted for these controls.
