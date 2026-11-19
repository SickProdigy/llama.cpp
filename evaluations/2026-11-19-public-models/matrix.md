| Model | Public file GB | Grounded reads | Correct workflow | Strict contribution | Contribution seconds | Peak VRAM MiB | First completed tool, explain seconds |
|---|---:|---:|---:|---:|---:|---:|---:|
| VibeForged v2 Q4 control | 8.47 | 1/2 | 1/1 | 1/1 | 70.3 | 9,082 | 41.7 |
| FableVibes Q4 control | 8.47 | 1/2 | 1/1 | 1/1 | 62.8 | 9,082 | 42.1 |
| Ornith 1.5 9B Q5 | 6.47 | 1/2 | 1/1 | 1/1 | 92.8 | 7,368 | 36.8 |
| Ministral 3 8B Q5 | 6.06 | 2/2 | 1/1 | 1/1 | 68.3 | 10,046 | 30.9 |
| Armand Qwen3.5 9B Agent Q5 | 6.47 | 1/2 | 0/1 | 0/1 | 55.0 | 7,368 | 40.7 |
| FlashModel Qwen3.5 9B Q5 | 6.47 | 1/2 | 1/1 | 1/1 | 101.8 | 7,368 | 41.3 |
| GPT-OSS 20B MXFP4 | 12.11 | 1/2 | 1/1 | 1/1 | 64.1 | 12,260 | 32.7 |
| Full Qwen3.6 35B Q4, CPU experts | 22.36 | 1/2 | 1/1 | 1/1 | 154.3 | 11,012 | 131.9 |
| Ministral 3 14B Q4 follow-up | 8.24 | 1/2 | 1/1 | 0/1 | 82.4 | 12,824 | 41.3 |

Primary temperature 0.2, focused Gitea tools, loaded context 98,304. The 14B
row is an adaptive follow-up under matched conditions. One sample per task per
row; repetitions and diagnostics remain separate. GB is decimal file size.
Tool latency includes inference and tool execution, not model-loading time.
Contribution seconds include elapsed time in failed or incomplete attempts.
Strict completion additionally requires all requested read-backs and final URLs.
Read pass requires the whole answer to be grounded; see manual grades for
correct core summaries that still contained unsupported additions.
