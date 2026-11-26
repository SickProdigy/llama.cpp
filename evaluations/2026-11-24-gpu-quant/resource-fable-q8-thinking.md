# Fable Q8 capacity on the P100

November26: the public pinned Fable Q8 file completes six capacity requests at
98,304 context. All41 layers are explicitly on GPU with automatic fit disabled.
Peak sampled GPU is14,624MiB (14.28GiB), versus11,566MiB for the retained Q6's
measured layout. GPU model buffers are13,450.91MiB, host model buffers515.31MiB,
GPU KV540MiB and GPU compute229.01MiB. No transformer-layer CPU fallback occurs;
the small host model buffer remains reported separately.

The exact14,655,633,920-byte file passes its pinned full SHA256. Same publisher
revision, tensor names/dimensions and chat template match retained Fable Q4/Q6.
No imatrix metadata is present in these three headers; that does not establish
identical calibration. Q8 tensor production differs from the K quants. The model's
advertised262,144 context has not been measured;98,304 is the tested layout.

| Request | Input tokens | Cached input | Seconds | Observed answer |
|---|---:|---:|---:|---|
| Tool call |291|0|18.21|Correct lookup name/arguments |
| Actual tool result |389|355|2.46|Answer completes without requesting another tool |
| Dependent tool followup |533|508|2.12|Exact returned code |
|16k marker |16,165|0|47.29|Exact marker |
|60k marker |59,935|16,033|156.51|Returns `60000`, missing the required prefix |
|80k marker |79,930|59,803|102.79|Exact marker |

All requests reserve16,384 output tokens; requested input-plus-output fits the
98,304 window. The60k answer is incorrect despite successful inference. This
stage establishes allocation/request compatibility, not perfect retrieval,
reasoning or Gitea/coding quality. The80k request benefits from nearly60k cached
input tokens; its lower latency is not an uncached80k processing benchmark.

Across81 samples with five-second pauses, no measurement errors, guards or study
swap are observed. Charged cgroups peak7,028,101,120 bytes and process PSS
1,921,160,192 bytes; charged file cache is included and is not CPU-layer offload.
Whole-host swap counters move1,992 input/3,660 output pages without study
attribution. Sampling can miss transient peaks. Original/model and staging disk
reserves stay above100GiB throughout.

The first attempt reaches backend readiness but stops before inference because
its verbosity3 logs omit required layer-placement evidence. That operator setup
failure is preserved privately and excluded from model scores. The corrected
registered attempt changes only logging to verbosity5. Both attempts restore the
original runtime and pass preservation checks. Current original IDs/images/config,
alias/context, four profile hashes,30 original model metadata entries,40 owner
source files/pending edits and Codex are preserved; owned backend/network and
terminal supervisors are removed. Final reserves are104.46GiB original drive and
104.47GiB staging. The prior owned IQ4 and all original weights remain present.

A [fresh unused profile preflight](q8-preactor-preflight-summary.json) passes the
actual current SDK/config and native code tool with zero model/forge mutations.
A fresh coding/Gitea workflow using the [corrected recorder](transparent-recorder.md)
is still required. Historical Fable cells use an older Hermes image and recorder;
this capacity result is not evidence of a precision-only quality improvement.

[Observations](resource-fable-q8-thinking-summary.json),
[evidence archive](resource-fable-q8-thinking-evidence.tar.gz),
[SHA256](resource-fable-q8-thinking-evidence.sha256),
[validation](resource-fable-q8-thinking-validation.json).
Saved consistency checks validate placement, source bindings, both reserves and
requested headroom; four manifest-rehashed negative controls are rejected.
They do not rerun inference or private behavior tests.

```sh
python3 verify_q8_resource.py resource-fable-q8-thinking-evidence.tar.gz
sha256sum -c resource-fable-q8-thinking-evidence.sha256
```
