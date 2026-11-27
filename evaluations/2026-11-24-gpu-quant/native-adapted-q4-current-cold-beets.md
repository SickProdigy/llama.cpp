# Current adapted 27B Q4: publication succeeds, behavior fails

November 27: the retained adapted 27B Q4_K_M completes three dependent natural
requests in **84.12 coding minutes**, **88.46 supervisor wall minutes**, with
actual Gitea issue, personal fork and updated PR. The published code fails the
requested lifecycle repair and cancellation feature. CLI success and green
authored tests do not establish correct behavior.

| Turn | Coding minutes | Project | Immutable originals | Independent behavior |
|---|---:|---|---|---|
| Lifecycle repair | 46.22 | 87 pass / 2 subtests | 83 pass / 2 subtests | Fail |
| Documentation | 7.97 | 87 pass / 2 subtests | 83 pass / 2 subtests | Fail |
| Cancellation feature | 29.92 | 92 pass / 2 subtests | 83 pass / 2 subtests | Fail |

All CLI exits are zero, with no external timeout. Grades above use **actual
published fork commits**. MCP edits left the local checkout at baseline; its
green baseline tests are not used to score the published answer. Snapshot source
digests, cloned PR heads, 130 frozen code bindings, exact task hashes and native
session ancestry were verified. All turns share one lineage without compaction.

The [same three literal requests](beets-natural-task-queries.json) ask for a
lifecycle repair, truthful documentation and optional-folder cancellation with
dependent followups. Fresh isolated profile/process/gateway, no preliminary
model read and no private grader feedback were used. Proposed MCP changes passed
ordinary project and immutable-original execution gates before publication;
rejected proposals did not change published source. This measures the friendly
tool/execution-gate workflow, not unrestricted raw MCP. No teacher patch or
corrective hint was supplied.

The initial worker remains unchanged: dispatched jobs and workers waiting for
the serialization lock can still start imports after disable/shutdown/reload.
In a same-object API stress case, resetting the generation counter to zero
introduces a stale callback collision when a fresh same-folder job is queued
after reactivation. This is distinct from ordinary GUI reload behavior. The final cancellation
handler is never registered in `commands`, so the documented `/beetscancel`
cannot be invoked through the plugin. Direct handler calls only cancel pending
timers and cannot cancel already-dispatched waiting work or count those jobs.

The README preserves setup and file-safety guidance, but explicitly allows
serialization-waiting imports to proceed, contrary to the initial request.
It promises logging after disable despite the reporting guard, describes the
generation reset at the wrong lifecycle point, and promises stale-callback
isolation that does not hold. The issue and PR incorrectly claim baseline
disable/shutdown never set stopping or cancelled timers; baseline already did.

Four initial and five feature tests are added. All eight original Beets test
names remain; one original method gains a stopping assertion. The added tests
exercise timers and direct handler methods, missing command registration and
waiting workers. The started-import test completes the import *before* disable,
so does not demonstrate an in-flight import surviving disable. The reload test
does not queue new same-folder work before firing the old callback. Transplanting
authored tests detects prior-source differences, but both initial and final suites
reject the correct reference solely because they require `_generation == 0`.
That is an implementation-detail assertion, not evidence the reference is wrong.

Posthoc boundary observations independently validate a positive correct reference
and baseline negative controls. The candidate misses command registration and
lets the old activation's timer dispatch new same-folder work in that same-object
stress case. These observations
were never actor feedback and do not replace the originally registered grader.
No real music, beets subprocess or GUI was used in these mocked boundary tests.

Actual Gitea publication is a meaningful partial success: the actor created
upstream issue #1, its personal fork and PR #2, then updated the same branch.
Authenticated final readback verifies the fork parent and unchanged 40-blob
upstream baseline. Independent connected MCP readback confirms issue #1 closed
after testing and PR #2 open/unmerged. Final head is
`4abd98fb5252d0ab87ab11cecb4024be64fd4d22` against base
`f9980ddc8aa6809e2f98f3ee95436bdb368e7a3d`. The model's PR is preserved for audit.

Runtime is owner-derived Hermes C9 with pinned test dependencies and llama.cpp
fee/b12723, with corrected transparent recorder. Context 98,304; 56/66 reported
layers on GPU; q4_0 KV; ubatch 128; two cache checkpoints; cache RAM 512 MiB;
fit off/load none; temperature .8/top-p 1/top-k 0; thinking off; main/aux caps
8,192; seed 20261124. Backend memory limit is 6.5 GiB, aggregate study cap 8 GiB,
study swap zero, both disk reserves at least 100 GiB.

All **37/37** requests complete with no backend error, truncation or auxiliary
summary request. Largest prompt is **48,859 tokens**, with full requested output
headroom on every request. This does not prove useful coding at 98k input. Six
earlier [capacity probes](resource-adapted-q4-current.md) separately measure
larger inputs; allocation and task success remain separate results.

474 ten-second samples report zero measurement errors/guards, **15,456 MiB GPU**,
**7,626,006,528 bytes aggregate cgroup**, **5,376,007,168 bytes process PSS**, and
zero study swap. Buffers include 12,787.45 MiB GPU model, **2,982.90 MiB host
model**, 1,512 MiB GPU KV and 216 MiB CPU KV. This is explicit CPU spillover.
Minimum original/staging free space is 111,718,924,288 / 110,908,231,680 bytes.
Sampling can miss transient peaks; timings share the host with other workloads.

The full verified retained file is `Qwen3.8-27B-hermes-Q4_K_M.gguf`,
16,810,714,560 bytes, SHA256
`6512bb1c2595575fc0aed39b7d72a6aaf71084b1164b5d3749f87a6c2a3d3bf3`, from
[netprojects revision 10fdf357](https://huggingface.co/netprojects/Qwen3.8-27B-hermes-adapted-GGUF/tree/10fdf357f14825c61ad7eb42a932e1f1e4390e8f).
Q4 has no recorded importance-matrix metadata; the retained IQ4_XS does. That
production/calibration difference prevents treating the next comparison as
weight precision alone. See capacity evidence for header/placement provenance.

Original runtime identities/settings, all 30 retained model metadata, owner
pending source/instructions and Hermes-Codex are preserved. The supervisor exited
zero, exact owned experimental containers/network were removed, and original
runtime restoration was independently checked. No useful retained model was deleted.

This one task family does not erase earlier positive adapted-Q4 Spam/Announcer
findings, which used different runtime/history. It establishes neither autonomous
reliability nor GPT-5 equivalence. The next registered comparison is the retained
IQ4_XS on this current runtime, starting with measured context/placement admission.
No new download is needed. Higher quantization is not yet a demonstrated winner.

[Sanitized summary](native-adapted-q4-current-cold-beets-summary.json),
[SHA256](native-adapted-q4-current-cold-beets-summary.sha256), and
[consistency validation](native-adapted-q4-current-cold-beets-validation.json)
contain curated observations and private-evidence fingerprints. They exclude raw
messages, private repository source, profiles, credentials and signing keys;
consistency validation is not a public behavioral replay or a model pass.

Methodology qualification, November 27: static inspection of deployed Nicotine+
3.3.11 and the [pinned upstream plugin handler](https://raw.githubusercontent.com/nicotine-plus/nicotine-plus/067f2eeb2666049d06d40b2cd0feb6246dda7d19/pynicotine/pluginsystem.py)
shows enable constructs a fresh plugin object and disable removes its enabled
reference. Same-object `loaded_notification()` reactivation is supplementary API
stress, not direct proof of normal GUI behavior. Registered grader results remain
unchanged; report their cases separately. Q4's missing command registration and
unguarded dispatched/waiting workers do not depend on the generation-collision
case. The [later isolated real-handler controls](native-adapted-iq4-current-r2-cold-beets.md) are now executed against this same actual published source: the fresh-instance timer case passes, while old dispatched/waiting imports still run after disable and the cancel command is absent. Baseline behavior matches expectations and the reference passes all four cases. This uses the real Nicotine+3.3.11 PluginHandler with fake worker/import boundaries, without GUI/media or new model calls; original grades remain unchanged.
