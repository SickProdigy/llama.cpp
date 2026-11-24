# Fresh adapted27B Q3 Spam workflow: incorrect repair

Completed, restored and independently audited November 24, 2026. **This workflow
fails the requested repair despite green project tests, correct Gitea publication
and a useful cooldown feature.** It is a quality failure in this sample, not a
loading, memory or runtime-compatibility failure. The separate fresh Announcer
workflow remains in progress; no general model or precision ranking follows.

The [pinned public Q3](resource-q3.md) uses the measured 98,304-context layout:
requested `-ngl 99`, non-mapped loading, q4 K/V, one slot, 512 MiB prompt cache,
two context checkpoints, backend6.5GiB/no swap and aggregate8GiB guard. Native
main/compression output reserve is8,192, temperature0.8, thinking off. Normal
native memory/approval/persistence policy is retained with scoped forge tools
and a visible project-test publication gate. A separate read-only control is
not resumed into the fresh coding conversation. The three coding turns share
one lineage; no private grader results or corrective audit findings reach it.

| Stage | Actor time | Project / original tests | Independent result |
|---|---:|---:|---|
| Initial enforcement repair | 20.60 min | 88 / 83 | Requested next-message behavior fails in both scopes |
| README followup | 2.37 min | 88 / 83 | Documents unrequested immediate-hook behavior; original failure persists |
| Rule cooldown feature | 12.44 min | 95 / 83 | New cooldown checks pass; inherited repair still fails |

Two immutable-original subtests also pass at every stage. Local and independently
cloned remote source digests match for all three publications. All three frozen
independent checker exit codes are1 because the initial repair remains wrong;
the final checker separately passes the cooldown-specific cases. Green authored
tests and a green evidence-consistency verifier do not turn this into a task pass.

## Why the repair is wrong

The request is to ignore the user's **next qualifying message** after enforcement
is enabled while their rolling count remains above threshold. The actor leaves
the original incoming-message callback unchanged and adds a `settings_updated`
hook that acts immediately when directly called. The original trigger latch still
prevents the requested next-message action. Frozen public-callback checks
reproduce that failure for both per-room and combined-room counting.

All pre-existing module AST is unchanged except the added hook in the initial
patch. Five new unittest methods directly call that hook; all five fail against
the original source because the hook is absent (`AttributeError`). They do not
exercise the requested next-message regression. The existing test AST is
preserved. The posthoc AST helper initially recognized only top-level functions;
a documented analysis correction handles unittest methods, without changing or
repeating the retained test executions.

Separate immutable-fixture controls show that, **if the new hook is called**, it
ignores newly exempt users/buddies and repeats an ignore plus notification for an
already-ignored user under an active clock. Those guard checks exist in the
original message path but are absent from the hook. Its claimed no-renotification
test uses timestamps1..3 without holding the clock at invocation, so counters
expire and the active pending case is never tested. Actual Nicotine+ framework
invocation of this newly named hook is not established by these unit tests; the
primary next-message failure does not depend on assuming any hook API.

The final source retains the same callback, hook and action method. The cooldown
feature itself uses a bounded1..3600/default60 monotonic timestamp per rule/room/
user, bypasses suppression when enforcing, and clears selected/all timestamps on
reset. Its independent scoped checks pass. Of seven added tests, three reject
prior permanent suppression through behavior, two reset tests fail prior source
on a missing private timestamp dictionary, and two also pass prior source.
The authored independence case never changes rule and changes room after the
interval; source inspection and separate checks cover the actual contract.

## Actual publication and reporting

The actor creates upstream issue1, its verified personal fork
`hermes-agent/hermes-wide-q3-20261123`, branch
`wide-spam-q3-enforcement-switch`, and upstream PR2 with three commits. Parent and
fork-main identity are independently verified; upstream main is independently
confirmed unchanged at `93f7d0429ce3acd9479e47fefd2563a76ffc5181`.
Final head is `0ba615b6e66dce47159a84194c88a7affd5c2773`.
The issue is verified closed after the run; the PR remains open and unmerged.
Operator-seeded upstream setup is not actor credit.

Additional claim errors remain: the initial answer/PR body call19 plugin tests
the full suite (actual project88), the README answer claims published commit
`f67fe137` instead of actual documentation commit
`1391152a7780e08d95ed1c63ecd09f7e2ce2a5ee`, and final PR title/body retain the
initial fix/five tests/19-count without documenting the cooldown feature. Final
answer26 is the correctly measured plugin-file count; full project is95.
Initial configured-host issue/PR URLs are correct.

## Resource and environment observations

All57 HTTP bodies complete without transport errors; largest completed prompt is
**62,241 tokens**. Across237 complete samples, peak charged cgroups are
**6.919 GiB**, all-process PSS **2.382 GiB**, and GPU **14,946 MiB**. Own experiment
swap, measurement-error samples and guard events are zero. These independent
peaks must not be summed. Global swap counters increase4,156 pages in and41,225
out, which cannot be attributed to this no-swap experiment. Sampling is not a
continuous whole-host peak proof; transient helper accounting has limits.

Coding actor time totals **35.41 min**, excluding the separate223.27s read
control. First coding HTTP is146.56s/13,734 prompt tokens. HTTP median24.35s,
maximum180.63s; these include prompt processing/generation and are not isolated
decode speed. Cache/host activity is uncontrolled. Q4 Spam was a conditional
recovery with different history, so these timings do not establish a causal
precision comparison. Public Q3/Q4 calibration metadata also differs.

Web searches encounter DNS failures in the isolated internal actor network;
extraction separately reports a URL security block with exact cause unproven.
Those service failures are environment limitations, not intrinsic reasoning
failures. Local source, tests and configured Gitea remain usable. No live network
or prompt change is made. The demonstrated unchanged message path and hook guard
omissions are established independently from local source/behavior. A GitHub
SDK-documentation lookup is not itself wrong-forge publication.

Original service IDs/images/configuration, four profile hashes, owner pending
files/instructions, original29 model metadata and entire Hermes-Codex snapshot
are independently verified preserved/restored before the Announcer stage starts.
The owned Spam containers and empty network are independently verified removed.
Minimum observed disk reserve is110.50GiB; after restoration110.69GiB is free.
This historical restoration is not a claim that no later GPU stage is running.

## Retained evidence and limits

[Summary](native-q3-spam-summary.json), [sanitized archive](native-q3-spam-evidence.tar.gz),
[SHA256](native-q3-spam-evidence.sha256), [privacy scan](native-q3-spam-privacy.json)
and [validation](native-q3-spam-validation.json) retain measurements, source
fingerprints, project/original-suite logs and scoped audit/publication projections.
Raw native prompts/responses, profiles/databases, full private project source,
primary graders, independent grader logs and credentials remain local.

```sh
python3 evaluations/2026-11-23-wide-memory/verify_candidate_native.py q3 spam_enforcement
```

The verifier checks saved consistency and explicitly retains observed independent
exits `[1,1,1]`. It does not rerun private behavior checks or certify correctness.
Unit/fake-peer tests do not replace a live Nicotine+ GUI/network trial. One fresh
family and its dependent followups are not independent reliability trials.
See the [matrix](matrix.md) for remaining candidates and the separate Announcer
outcome. No winner or autonomous-reliability claim is made.
