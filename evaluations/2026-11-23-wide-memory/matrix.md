# Wider-memory native testing matrix

November 23, 2026. Natural coding tasks and dependent followups; correctness is
audited separately from resource fit, authored tests and actual publication.

| Candidate / family | Initial fix | README followup | Feature followup | Claims / publication audit | Status |
|---|---|---|---|---|---|
| Adapted27B Q4, Spam, conditional recovery | Independent source/behavior pass | Independent docs/preservation pass | Independent source/behavior pass | Real configured Gitea issue/fork/PR and 3 commits; wrong final URL host, stale PR description | Completed, restored and audited; [evidence](native-q4-recovery.md) |
| Adapted27B Q4, fresh Announcer | Automated local/remote checks pass; manual audit pending | Automated local/remote checks pass; manual audit pending | Running | Pending complete independent audit | In progress; no complete quality verdict |
| Adapted27B Q3_K_M | Not run | Not run | Not run | Not run | Header/profile preflight only; full weights/inference pending |
| Devstral Small 2 24B public Q4_K_M | Not run | Not run | Not run | Not run | Architecture/layout/profile preflight only |
| GLM-4.7-Flash public Q4_K | Not run | Not run | Not run | Not run | Scripted client history control passes; actual template/P100/fit/quality pending |

The retained IQ3 has [matched resource observations](resource-baseline-v2.md),
not a new matched native quality score here. Older evaluation cohorts use
different tasks/settings and cannot establish a current precision ranking.
Q3/Q4 [calibration metadata differs](quant-header-preflight/README.md).

The recovered Spam sample resumes a hardware-interrupted partial draft/history;
it is not interchangeable with the fresh Announcer sample. Followups are
dependent stages, not independent reliability trials. All candidates retain
normal memory/approval/persistence policy and the same scoped forge interface;
architecture-specific sampler/template/output/cache needs are recorded.
No winner or autonomous-reliability claim follows from the current small sample.
