# Native Hermes compression runtime control

The isolated control completes with a model-produced summary rather than the
native deterministic fallback. This supports a prospective runtime amendment for
unused comparison profiles; it does not change the completed IQ4 coding scores.

The same pinned public IQ4_XS and backend as the [native trial](native-adapted-iq4-beets.md)
run at 65,536 context, 66/66 GPU layers, microbatch64, q4 K/V and automatic fit off.
The experimental configuration explicitly sets auxiliary compression timeout to
5,400 seconds and the native compression inactivity/total guards to5,400 seconds,
and requests llama.cpp prompt progress on both main and auxiliary routes.
The deployed owner profile is unchanged.

A preliminary direct streaming request completes19,912 input tokens in294.64s
with42 actual prompt-progress events. Hermes then invokes its real guarded
`AIAgent._compress_context` facade on a saved prior conversation. Its recorded
streaming request contains26,148 input tokens, nonthinking T0.8/top_p1/top_k0,
seed20261123 and an8,192-token output cap. It produces2,650 output tokens and
56 progress events, finishing in633.84s (10.56minutes). The native result reports
progress, no fallback, and100→30 messages. Source and wire settings are bound in
the [evidence summary](compression-runtime-control-summary.json).

Across189 complete five-second samples, GPU usage peaks at15,788MiB. Aggregate
study cgroups, including charged file cache and helpers, peak at6.550GiB;
aggregate process PSS peaks at2.013GiB. Study swap, guard violations and sample
errors are zero. Minimum free space is110.32GiB on the original model drive and
127.26GiB on the separate owned staging volume. These are sampled measurements,
not continuous peak guarantees or whole-host swap attribution.

The original runtime/default98,304-context alias is restored. Independent checks
confirm all30 retained-model metadata records, four owner-profile hashes,
container identities/configurations, owner pending edits and the complete
Hermes-Codex snapshot are preserved. Owned backend, recorder, worker, supervisor
and network are removed after terminal state is saved. No forge tools or real
forge credentials were available to the compression worker; no issues were opened.

This is a saved-history native compression control, not a complete CLI session,
persisted-session test, semantic summary audit, coding task or publication result.
The new summary request differs from the previous failed request in several
messages as well as the progress flag. Progress and longer timeout settings are
changed together; this is not an exact replay or isolated causal comparison.
Its ten-minute summary cost remains a practical latency limitation. The original
wrong-target Gitea decisions and documentation error preceded compaction.

The [archive](compression-runtime-control-evidence.tar.gz),
[full hash](compression-runtime-control-evidence.sha256), and
[privacy scan](compression-runtime-control-privacy.json) include numeric results,
source, registration and configuration-preflight evidence. Conversation payloads,
generated summary text, full profiles and credentials remain private. Reproduction
requires the pinned retained model/backend/helper, a private input conversation
and an isolated scratch profile; the exported sources document the exact method.
