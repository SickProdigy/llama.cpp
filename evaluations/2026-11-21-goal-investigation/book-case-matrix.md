# Booksearch public behavior cases

Each row is one conversation; these six cases belong to one bug family. Three already-passing controls are omitted. `ok` is an observed pass, `FAIL`/`ERROR` an observed result, and `not executed` means the case did not run (including syntax failures). Runtime controls have separate labels. No primary success rate is inferred from these correlated inputs.

| Profile | Input | null docs | non-list docs | root array | mixed entries | mapping author | numeric author |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stock-qwen35-q5 | ordinary | ok | FAIL | FAIL | FAIL | FAIL | FAIL |
| stock-qwen35-q5 | bulk-reference | ok | FAIL | FAIL | ok | FAIL | FAIL |
| vibeforged-q4 | bulk-reference | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| gptoss20-mxfp4 | ordinary | ok | ok | ok | FAIL | FAIL | FAIL |
| gptoss20-mxfp4 | bulk-reference | ok | FAIL | FAIL | ok | ok | ok |
| vibeforged-q4 | ordinary | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| qwen36-35b-a3b-udq4xl-cpu24 | ordinary | FAIL | FAIL | ok | ok | FAIL | FAIL |
| qwen36-35b-a3b-udq4xl-cpu24 | bulk-reference | FAIL | ok | FAIL | ok | ok | ok |
| qwen35-27b-dense-udiq3xxs | ordinary | ok | ok | FAIL | FAIL | FAIL | FAIL |
| qwen35-27b-dense-udiq3xxs | bulk-reference | ok | ok | FAIL | FAIL | FAIL | FAIL |
| gptoss20-mxfp4-publisher-low | ordinary | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| gptoss20-mxfp4-publisher-low | bulk-reference | not executed | not executed | not executed | not executed | not executed | not executed |
| stock-qwen35-q5-publisher | ordinary | FAIL | FAIL | FAIL | ok | FAIL | FAIL |
| stock-qwen35-q5-publisher | bulk-reference | ok | ok | FAIL | FAIL | FAIL | FAIL |
| qwen38-27b-hermes-iq3xxs | ordinary | ok | ok | ok | ok | FAIL | FAIL |
| qwen38-27b-hermes-iq3xxs | bulk-reference | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| qwen36-35b-a3b-udq4xl-cpu24-persist-active | bulk-reference | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| qwen36-35b-a3b-udq4xl-cpu24-persist-history | bulk-reference | FAIL | FAIL | ok | ok | FAIL | FAIL |
| qwen3-coder30b-udiq3xxs | ordinary | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |
| qwen3-coder30b-udiq3xxs | bulk-reference | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL |

Observed primary conversations with all nine cases executed: 17. Per-case pass counts in that set: null docs 8/17, non-list docs 6/17, root array 3/17, mixed entries 6/17, mapping author 2/17, numeric author 2/17. These are diagnostic counts, not independent task solve rates.
