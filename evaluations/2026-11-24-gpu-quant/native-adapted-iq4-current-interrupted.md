# Current IQ4 native attempt: interrupted by disk reserve safeguard

November 27: this fresh coding/Gitea attempt is **incomplete**, with no model-quality
pass or failure assigned. The shared staging filesystem crossed the 100 GiB
reserve during the initial lifecycle-repair turn. The controller stopped its
backend/agent, closed its owned issue and restored the original runtime.

Fourteen requests completed with usage before the interruption. Five later
transport failures follow the intentional backend stop: an incomplete stream,
connection refusal and name-resolution failures during teardown. They are not
independent evidence of a model defect. No coding turn completed, no dependent
docs/feature turn ran, and no continuation rescue was supplied.

The trigger sample records **107,254,538,240 staging bytes free**,
**107,374,182,400 required**, an undershoot of
**119,644,160 bytes**. Sampling every ten seconds can
observe an undershoot before the safeguard acts; do not claim the reserve stayed
continuously intact. At that sample aggregate study cgroups were
5,085,474,816 bytes, PSS 3,249,741,824, study swap zero,
and host available memory 37,663,199,232. This was a disk guard,
not a host-memory or CUDA failure.

Across 127 samples, peak aggregate cgroups were
7,644,172,288 bytes and PSS 3,297,518,592, both within
8 GiB, with no measurement errors or study swap. The supervisor wall time was
**24.27 minutes**; the first turn reached the guard after
**21.12 minutes**. These are interrupted-attempt timings,
not successful task latency or completed-turn benchmarks.

Actual Gitea readback independently verifies an upstream issue, the actor's
personal fork with the correct parent and three commits on its contribution
branch. The final fork head is `4b6aa92fee6642d3fdb88eb87eb27735cf86183b`. The upstream's
40 baseline blobs remain unchanged; no PR was found. Connected MCP independently
confirms issue #1 closed. These partial actions establish real forge use, not
correct source, adequate tests or whole-workflow success.

The [completed IQ4 capacity result](resource-adapted-iq4-current.md) remains valid:
98,304 context, 63/66 reported GPU layers, ubatch64, current C9/fee runtime,
nonthinking temperature.8 and 8,192 output caps. It does not guarantee that the
shared host retains enough disk space for an entire agent workflow.

Independent post-stop audits verify original identities/images/configuration,
running state and alias/context, all 30 retained model metadata, four owner
profile hashes, pending owner source/instructions and Hermes-Codex. Exact owned
containers/network and the exclusively referenced temporary supervisor volume
were removed; the named model-stage volume is preserved. Post-cleanup reserves
again exceed 100 GiB.

No model was downloaded or deleted in this attempt. The backend log is about
10.56 MB and the supervisor's temporary data only 4,553 bytes; those observations
do not explain or attribute the shared-filesystem drop. No unrelated Docker
cache, image or owner data was pruned. Before a fresh trial, review only proven
owned expendable artifacts and establish substantially more headroom. Any retry
must use a fresh fixture/profile/conversation and retain this interruption as a
separate measured attempt.

[Summary](native-adapted-iq4-current-interrupted-summary.json), [sanitized evidence](native-adapted-iq4-current-interrupted-evidence.tar.gz),
[SHA256](native-adapted-iq4-current-interrupted-evidence.sha256), [validation](native-adapted-iq4-current-interrupted-validation.json),
and [privacy scan](native-adapted-iq4-current-interrupted-privacy.json).

```sh
python3 verify_interrupted_iq4_native.py native-adapted-iq4-current-interrupted-evidence.tar.gz
```

The [verifier](verify_interrupted_iq4_native.py) checks saved numeric evidence and
manifest integrity, including the disk threshold and failure chronology. It does
not replay inference, code tests or verify model quality. Raw actor code/messages,
private graders, full profiles, credentials and signing keys are excluded.
