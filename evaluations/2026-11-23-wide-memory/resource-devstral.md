# Devstral Small 2 24B public Q4_K_M resource stage

Completed November 24, 2026. The full pinned file completes five resource,
template and tool-history probes at 98,304 context on the P100 using CPU spill.
This is not a coding or Gitea quality pass. Fresh native workflows are separate.

| Probe | Actual input tokens | Output tokens | Seconds | Recorded result |
|---|---:|---:|---:|---|
| Defined lookup tool | 639 | 13 | 19.66 | Correct function and arguments |
| Assistant completion after tool result | 673 | 26 | 6.38 | Completes without another tool call |
| Fresh dependent user followup | 714 | 7 | 2.51 | Exact returned marker |
| Synthetic 16k | 16,055 | 10 | 217.41 | Exact final marker |
| Synthetic 61k | 61,640 | 10 | 856.60 | Exact final marker |

The largest request retains 16,039 cached tokens and processes 45,601 new
tokens; measured server prefill averages 53.53 new tokens/second. These are
complete responses with measured rendered inputs, not cold-prefill benchmarks.
Short markers and one synthetic tool do not demonstrate coding, configured MCP
routing, or long-conversation reliability. Output reserve is 8,192 tokens.

The first declared layout succeeds: non-mapped loading, requested 32 GPU layers,
q4 K/V, one slot, batch512/ubatch128, eight CPU threads, fit disabled, 512 MiB
prompt cache and two context checkpoints. No fallback is used. CPU layers also
retain their KV on CPU in this pinned runtime. Requested placement is recorded;
the verbosity-3 logs do not expose a complete per-tensor allocation inventory.
Backend image is `sha256:7561b4761f849925a728c5ac2bd1f4a649b6a76f24544e7f992b047ad016cec3`,
build `b12627-225a5345b`. Sampler is temperature0.15, top-p1, top-k0, min-p0,
repetition1 and presence0; no Qwen thinking flags are applied.

Across 227 complete samples, peak charged experimental cgroups are **6.563 GiB**,
all-process PSS **5.140 GiB**, and GPU **14,880 MiB**, with at least 1,395 MiB
GPU free. These independent peaks must not be summed. Experiment swap,
measurement-error samples and guard violations are zero. Backend cap is 6.5 GiB,
supervisor cap 512 MiB, aggregate guard 8 GiB, all with no swap allowance.
Cgroup accounting includes charged file cache/shared buffers. Samples do not
prove a continuous additional whole-host allocation bound. Minimum observed
host available memory is 28.78 GiB and disk free 110.085 GiB. Whole-host swap
counters rise 1,266 pages in and 6,906 out; those changes cannot be attributed
to this no-swap experiment.

Loading takes 97.39 seconds after independent full-file hashing and DONTNEED
advice for this specific file. Ambient host activity and cache state are
uncontrolled. The larger CPU share and different architecture/settings prevent
a precision-only or exactly matched speed comparison with the adapted Qwen.

## Two preserved harness failures

Before any Devstral coding actor, the first pilot stops after a valid tool call
because the measurement endpoint omitted the BOS token: measured638 versus
actual639. Measurement now uses `add_special=true`, matching the pinned
[completion tokenization path](https://raw.githubusercontent.com/ggml-org/llama.cpp/225a5345b/tools/server/server-context.cpp),
rather than applying a hardcoded offset. Actual usage and measured counts agree.

The second pilot exposes a noncanonical resource history: a fresh user turn
was inserted after a tool result without first obtaining an assistant completion.
The pinned template rejects it. The corrected probe retains the actual assistant
completion before asking a fresh followup; it fabricates no assistant response.
Both attempts, old controller versions, registrations, preactor amendments,
responses and restoration records are retained in the archive. Neither is a
model-quality or hardware failure. Native tasks, graders, profiles, sampler,
memory limits and layouts are unchanged. There are now five resource requests,
so prior four-probe Q3 timings are not an exactly matched sequence.

## Public file and restoration

- Repository: `unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF`
- Revision: `6e458b8add42681bfd023de5eab93637694aaf82`
- File: `Devstral-Small-2-24B-Instruct-2512-Q4_K_M.gguf`, 14,334,446,752 bytes
- SHA256: `d14ba9edee1bb4c4996a726deb81e49ae81800a3216f0774634238c380aee496`

Anonymous pinned download and independent resource-stage hashing agree.
Only this additional large study file is present; all 29 original model entries
are preserved. At resource-stage completion, independent audits verify the
original service IDs/images/configuration, four profile hashes, owner pending
files/instructions, original Vibe alias/98k context, and unchanged Hermes-Codex
snapshot. Owned resource containers/network are removed; 110.085 GiB is free.
Later native experiments have their own restoration obligations.

[Summary](resource-devstral-summary.json), [archive](resource-devstral-evidence.tar.gz),
[SHA256](resource-devstral-evidence.sha256), [privacy scan](resource-devstral-privacy.json)
and [validation](resource-devstral-validation.json) retain synthetic requests,
complete responses, numerical samples, frozen controls and restoration audits.
No native profiles, private coding tasks/graders, repository source or credentials
are exported.

```sh
python3 evaluations/2026-11-23-wide-memory/verify_candidate_resource.py devstral
```

This checks retained bytes, pins, observations and audit consistency. It does not
rerun inference or certify coding correctness.
