# Automatic review findings

All fifteen real calls exceeded the 240-second caller deadline. No semantic decision reached the actor. Late findings below are operator analysis, not applied feedback.

| Workflow / turn | Attempt | Known backend s | Strict response | Independent interpretation |
|---|---:|---:|---|---|
| review-beetsbridge-turn0 | 001 | 470.523 | invalid | Prose/fenced approval; unsupported prior-commit assumption; no demonstrated lifecycle/doc error catch. |
| review-beetsbridge-turn0 | 002 | unknown | unknown | Final response capture unavailable; no semantic decision can be recovered. |
| review-beetsbridge-turn1 | 003 | 403.443 | invalid | Prose/revise; misses reload gap and inaccurate README, circular precommit publication requirement. |
| review-beetsbridge-turn1 | 004 | 478.248 | invalid | Prose/approve; misses reload and documentation errors. |
| review-beetsbridge-turn1 | 005 | 342.971 | invalid | Prose/approve; source adjacency confused with actual single-file mutation; no demonstrated correction. |
| review-beetsbridge-turn2 | 006 | 399.672 | valid | Late approve; misses remaining reload gap and inaccurate lifecycle guarantee. |
| review-announcer-turn0 | 001 | 441.738 | valid | Late revise: test clarity/helper naming suggestions. Genuine regression still detects old behavior; no functional defect identified. |
| review-announcer-turn0 | 002 | 381.29 | invalid | Fenced approval rejected by strict whole-response JSON parser. |
| review-announcer-turn0 | 003 | 442.003 | invalid | Fenced revise: naming/style and publication-stage noise, no demonstrated code defect catch. |
| review-announcer-turn1 | 004 | 754.92 | unknown | Only8192 bytes retained after disconnect. Complete decision and API usage unknown; separate server timing retained. |
| review-announcer-turn1 | 005 | 440.008 | valid | Late revise: genuine README-only packaging concern because implementation/tests remain unpublished; also false/soft findings. |
| review-announcer-turn2 | 006 | 572.627 | valid | Late revise: pending publication metadata interpreted as success claim; final answer honestly local-only. No demonstrated code/doc catch. |
| review-arrrequests-turn1 | 001 | 438.244 | invalid | Late decision app is invalid enum and lacks findings. |
| review-arrrequests-turn1 | 002 | 544.75 | valid | Late revise: self-retracted header complaint, false chain exfiltration claim (origin equality transitive), derivative false README criticism. Misses actual HTTPS/doc errors. |
| review-arrrequests-turn1 | 003 | 473.626 | valid | Late revise falsely claims submitted test payload still contains cleanup joins; exact payload contains none. Misses actual HTTPS/doc errors. |

Six strict responses are valid, seven invalid, and two unavailable/incomplete. Validation here is counterfactual: valid late JSON still missed the actual deadline. One output has only an 8192-byte prefix and unknown full decision/API usage. Separate backend timing for that request is retained without substituting it for missing API usage.

Completed caller wait totals 3601.513 seconds. Observed critic backend time totals 6584.063 seconds, a lower bound with 1missing timing record. These are already part of native workflow compute; do not add them to wall time.
