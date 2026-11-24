# Wider-memory native testing matrix

Started November 23, 2026; updated November 24, 2026. Natural coding tasks and dependent followups; correctness is
audited separately from resource fit, authored tests and actual publication.

| Candidate / family | Initial fix | README followup | Feature followup | Claims / publication audit | Status |
|---|---|---|---|---|---|
| Adapted27B Q4, Spam, conditional recovery | Independent source/behavior pass | Independent docs/preservation pass | Independent source/behavior pass | Real configured Gitea issue/fork/PR and 3 commits; wrong final URL host, stale PR description | Completed, restored and audited; [evidence](native-q4-recovery.md) |
| Adapted27B Q4, fresh Announcer | Independent source/behavior pass | README re-enable wording qualification | Independent source/behavior pass | Real issue/fork/PR; PR metadata updated; plugin/full-suite count confusion in final answers | Completed, restored and audited; [evidence](native-q4-fresh.md) |
| Adapted27B Q3, fresh Spam | Incorrect next-message repair despite green tests | Documents unrequested behavior; wrong commit claim | Cooldown scoped pass; original failure persists | Correct real issue/fork/PR, stale PR body | Completed, restored and audited; [evidence](native-q3-spam.md) |
| Adapted27B Q3, fresh Announcer | Independent source/behavior pass; authored replay caveat | Re-enable wording qualification | Independent source/behavior pass | Real issue/fork/PR; stale PR metadata, plugin/project count confusion | Completed, restored and audited; [evidence](native-q3-queue.md) |
| Devstral Small 2 24B public Q4_K_M | Not run | Not run | Not run | Not run | Pinned public download underway; architecture/layout/profile preflight complete |
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
