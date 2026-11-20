# Primary comparison

| Model | Phase | Grounded read answers | Correct contribution resources | All read-backs and URLs |
|---|---|---:|---:|---:|
| Ministral 3 8B Instruct Q5 control | matched | 0/2 | 1/1 | 0/1 |
| Empero Qwen3.8 distill 9B Q5 | matched | 1/2 | 1/1 | 1/1 |
| LFM2.5 8B-A1B Q5 | matched | 0/2 | 0/1 | 0/1 |
| Gemma 4 E4B Instruct Q5 | matched | 2/2 | 1/1 | 0/1 |
| Ministral 3 8B Reasoning Q5 | matched | 0/2 | 1/1 | 1/1 |
| Same Empero checkpoint Q8 | matched | 1/2 | 1/1 | 1/1 |

# Observed fit and conversation time

| Model | File GB | Loaded context | Cache | Peak GPU MiB | Explain first tool seconds | Full-task seconds |
|---|---:|---:|---|---:|---:|---:|
| Ministral 3 8B Instruct Q5 control | 6.06 | 98,304 | q4_0 | 10,046 | 30.7 | 73.1 |
| Empero Qwen3.8 distill 9B Q5 | 6.64 | 98,304 | q4_0 | 7,368 | 38.5 | 84.4 |
| LFM2.5 8B-A1B Q5 | 6.03 | 98,304 | q4_0 | 6,714 | 24.5 | 13.7 |
| Gemma 4 E4B Instruct Q5 | 5.48 | 98,304 | q4_0 | 4,804 | 24.3 | 101.5 |
| Ministral 3 8B Reasoning Q5 | 6.06 | 98,304 | q4_0 | 10,046 | 29.6 | 96.6 |
| Same Empero checkpoint Q8 | 9.79 | 98,304 | q4_0 | 9,922 | 39.4 | 97.5 |

Each primary row has one sample per task, not a reliability estimate. Public
Q5 and Q8 are two files of one checkpoint. Publisher samplers and larger output
budgets are separate phases in runs.csv/summary.json. Correct resources and
strict completion are distinct. Read grades are conservative whole-answer
checks; see manual-grades.json for unsupported claims despite correct core
summaries. Failed/incomplete full-task elapsed times remain visible.

GB is decimal file size; GPU memory is sampled whole-card MiB every three
seconds. Loaded capacity is not active full-window validation. Conversation
and first-tool times exclude model loading and initial agent/MCP setup; the
conversation includes subsequent inference/tool execution. Publisher probes
reuse a warm backend cache and should not be treated as isolated sampler-speed
comparisons. No CPU/GPU hardware change is made during this cohort.
