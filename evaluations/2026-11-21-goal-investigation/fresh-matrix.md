# Fresh real-source matrix

These are completed sessions, not a final reliability ranking. Each ordinary/bulk cell is one fresh conversation, not repeated IID trials. Defect counts exclude three already-passing controls. Passing means more than code cases: tests, actual publication, honesty and followup are reviewed separately.

| Profile | Context | Ordinary defects /6 | Bulk defects /6 | Verified PR sessions / completed | Peak VRAM MiB | Native persistence |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Stock Qwen3.5 9B Q5, .2 | 262144 | 1 | 2 | 1/2 | 9712 | False |
| VibeForged Q4, .2 | 262144 | 0 | 0 | 2/2 | 10462 | False |
| GPT-OSS20B MXFP4, .2 | 131072 | 3 | 4 | 0/2 | 12572 | False |
| Qwen3.6 35B Q4, CPU24, .6 | 98304 | 2 | 4 | 1/2 | 11012 | False |
| Qwen3.5 27B IQ3XXS, .6 | 98304 | 2 | 2 | 1/2 | 13398 | False |
| GPT-OSS20B MXFP4, T1/low | 131072 | 0 | source error | 0/2 | 12572 | False |
| Stock Qwen3.5 9B Q5, publisher .6 | 262144 | 1 | 2 | 2/2 | 9712 | False |
| Qwen3.8 Hermes27B IQ3XXS, .8 | 98304 | 4 | 0 | 1/2 | 13094 | True |
| 35B CPU24, persisted active reference | 98304 | n/a | 0 | 0/1 | 11012 | True |
| 35B CPU24, persisted historical reference | 98304 | n/a | 2 | 1/1 | 11012 | True |
| Qwen3-Coder 30B IQ3XXS, .7 | 98304 | 0 | 0 | 0/2 | 15350 | True |

A verified PR includes the retained followup and does not imply a correct patch or first-turn publication. CSV stage fields distinguish those. Edited-test status uses the actual published tree when available; local results remain in a separate field. Trial elapsed includes agent/workspace startup, copying and independent grading; backend weight load/download are outside that per-trial clock. Agent elapsed is provided separately. Fresh sessions can reuse exact server prefixes; timings are not controlled cold-start benchmarks. VRAM is observed device usage. See [per-run results](fresh-results.csv) for independently checked code, edited/original tests, portability, actual remote outcomes and elapsed time. The 35B original bulk run is context/runtime-affected: its store-less SDK caller lacked message UIDs and the compactor replayed the full active reference packet. Native replay controls also reproduce duplication with UIDs when the summary carrier has tool calls; persistence alone is not a complete fix. Preserve its observed code/test/time outcomes without treating it as a clean normal-persistence comparison.

The historical-reference fixture and native-persistence controls use separate labels and source revisions. They do not replace old failures. Model-specific contexts and samplers differ; this is a practical configuration comparison, not an isolated weight/precision effect.
