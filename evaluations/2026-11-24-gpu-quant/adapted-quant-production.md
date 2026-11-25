# Public adapted27B quantization differences

The saved Q3_K_M, Q4_K_M and IQ4_XS headers have identical866 tensor names/shapes,
identical tokenizer metadata bytes (including token arrays and chat template),
and identical core metadata outside file type and importance-matrix fields.
Their recorded calibration differs:

| Public file | Recorded matrix | Recorded dataset | Entries / chunks |
|---|---|---|---|
| Q3_K_M | `imatrix.gguf` | `imatrix-calib.txt` |496 /150 |
| Q4_K_M | No matrix metadata recorded | Not recorded | Not recorded |
| IQ4_XS | `imatrix.gguf` | `calib-train.txt` |496 /104 |

Missing metadata does not establish that a matrix was never used. Equal filenames
or entry counts do not establish equal matrix contents. Stored tensor-type mixes
also differ; their exact counts and embedding/output types are retained as raw
GGUF type codes. A quantization label does not mean every tensor has that type.
Header agreement does not prove identical unquantized source weights or recover
the producer's commands/calibration contents. These are public production
observations, not a controlled local quantization experiment.

[Comparison and complete pins](adapted-quant-header-comparison.json) bind the
public repository revision, filenames, full advertised SHA256s and exact saved
prefix fingerprints. The Q3/Q4 field fingerprints match the independently saved
[earlier comparison](../2026-11-23-wide-memory/quant-header-preflight/expected.json);
IQ4 prefix/type counts match the separate
[IQ4 reader](adapted-iq4-header-inspection.json). This header check does not repeat
full-file integrity, GPU fit or quality tests.

Reproduce with the three pinned16MiB prefixes in order:

```bash
python3 compare_adapted_quant_headers.py Q3-prefix.bin Q4-prefix.bin IQ4-prefix.gguf
```

Compare `headers`, `comparisons` and `calibration_metadata` against the saved
JSON. The saved artifact separately adds source pins and independent-reader
crosscheck receipts. Full model hashes and measured allocation are in the
resource/native evidence. Different calibration, tensor mixes, actual placement,
context sizes and task histories prevent precision-only attribution; judge the
practical configurations using correctness and latency together.
