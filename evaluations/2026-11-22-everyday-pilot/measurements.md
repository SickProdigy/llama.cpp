# Recorded measurements

18 of 18 turn snapshots. Correctness and publication outcomes require separate manual audits.

| Workflow | Turn | Wall s | Exit | Prompt tokens | Output tokens | Max recorded input | Reviews | Caller wait s | Critic backend s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| plain-announcer | 0 | 1242.0 | 0 | 458860 | 8484 | 33958 | 0 | 0.0 | 0.0 |
| plain-announcer | 1 | 128.8 | 0 | 142278 | 861 | 36593 | 0 | 0.0 | 0.0 |
| plain-announcer | 2 | 536.8 | 0 | 508143 | 3057 | 51093 | 0 | 0.0 | 0.0 |
| plain-arrrequests | 0 | 1606.7 | 0 | 993451 | 9610 | 48848 | 0 | 0.0 | 0.0 |
| plain-arrrequests | 1 | 458.5 | 0 | 507745 | 2322 | 61885 | 0 | 0.0 | 0.0 |
| plain-arrrequests | 2 | 2117.3 | 137 | ≥1171114 | ≥9690 | 82103 | 0 | 0.0 | 0.0 |
| plain-beetsbridge | 0 | 2022.5 | 126 | 905164 | 13726 | 45683 | 0 | 0.0 | 0.0 |
| plain-beetsbridge | 1 | 413.7 | 0 | 358544 | 2497 | 54482 | 0 | 0.0 | 0.0 |
| plain-beetsbridge | 2 | 2117.5 | 137 | ≥772999 | ≥13702 | 77112 | 0 | 0.0 | 0.0 |
| review-announcer | 0 | 2116.1 | 137 | ≥874558 | ≥6549 | 40464 | 3 | 720.3 | 1265.0 |
| review-announcer | 1 | 1833.8 | 0 | ≥496809 | ≥3969 | 40834 | 2 | 480.2 | 1194.9 |
| review-announcer | 2 | 1055.3 | 0 | 499129 | 4518 | 48570 | 1 | 240.1 | 572.6 |
| review-arrrequests | 0 | 2115.6 | 137 | ≥891146 | ≥12319 | 54666 | 0 | 0.0 | 0.0 |
| review-arrrequests | 1 | 2116.5 | 137 | 1458277 | 6237 | 75585 | 3 | 720.3 | 1456.6 |
| review-arrrequests | 2 | 2117.3 | 137 | ≥687609 | ≥8043 | 82104 | 0 | 0.0 | 0.0 |
| review-beetsbridge | 0 | 2118.3 | 137 | ≥830707 | ≥9461 | 39819 | 2 | 480.2 | 470.5 |
| review-beetsbridge | 1 | 2115.9 | 137 | ≥726304 | ≥4859 | 46475 | 3 | 720.3 | 1224.7 |
| review-beetsbridge | 2 | 2116.9 | 137 | ≥892885 | ≥10003 | 70039 | 1 | 240.1 | 399.7 |

Costs are attributed by request arrival within each native turn. A request may finish after that turn ends; its whole recorded backend time remains attributed to its originating turn. Do not add critic time to wall time, or infer equal compute across arms.

Token figures include repeated/cached prompt tokens and native auxiliary work; they are not unique conversation length or billed cost. Missing usage is unknown, not zero. Max input is the largest recorded request with usage, not a proven peak if requests are incomplete. Critic transport records with the exact frozen reviewer system prompt but absent final metrics are explicitly inferred and incomplete.

Tool, memory and skill counts are cumulative only within the selected physical native session snapshot, not per-turn deltas or sums across compaction ancestors. Native child rotations can change those counts; protocol and checkpoint audits preserve lineage. Zero compacted-row flags do not mean no compression: archive-mode compaction can create a child session instead. Checkpoint backend seconds are already included in native turn costs; do not add them again or infer retention success from a completed summary. VRAM is sampled, not a continuous peak; initial adopted-turn sampling has a documented gap. CPU/RAM/energy were not continuously measured.

No semantic pass or unattended-success conclusion is generated from these measurements.
