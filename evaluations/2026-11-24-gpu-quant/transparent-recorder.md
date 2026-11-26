# Recorder correction: preserve backend HTTP errors

November26: the experiment's original recorder converted all backend HTTP errors
into a generic502 HTML response, discarding their original status/body. This
observation layer changes agent behavior when those errors occur. The recorded
Vibe Q6 final turn has23 backend400 context errors presented to Hermes as502.
Its final turn is therefore recorder-confounded, not an unqualified model score.
The earlier lifecycle defects and test failures are independently measured and
precede the overflow; this correction does not turn them into passes.

A separate prospective recorder preserves backend HTTP status, response bytes,
Content-Type and Retry-After, records error response hashes, and keeps genuine
connection failures on the generic502 path. The frozen old recorder/protocols,
original owner runtime and old model results are unchanged. Future actor stages
must explicitly bind the new source; no current actor has used it yet.

The [actual current Hermes SDK/classifier control](transparent-recorder/preflight.json)
runs without inference, credentials, Gitea or external networking. A synthetic
loopback backend returns400 context overflow,429 rate limit and503 overload for
both streaming-request and nonstreaming-request modes. The old recorder produces
six InternalServerError502 results classified as server_error, with no compression
recommendation. The corrected recorder preserves all six statuses/bodies:
400 becomes BadRequestError/context_overflow with should_compress=true;429 becomes
RateLimitError/rate_limit;503 remains InternalServerError/overloaded. Retry-After
survives. Successful JSON and streamed SSE content/usage also pass. Recorded
error-body hashes match the actual captured bytes.

This proves error recognition reaches native recovery classification, not that a
real overflowing session will recover or generate a faithful summary. The
repetitive8,192-token summaries remain model failures. Another long actor test
still needs measured capacity, fresh profiles and explicit source registration.

The [impact inventory](transparent-recorder/error-impact.json) checks the listed
11 native GPU-quant stages and seven older wide-memory stages. Only Vibe Q6
reasoning has recorded HTTPError entries in this set (23). The successful slow
27B Q4 fresh workflows have none. Other recorded errors include broken pipes,
an incomplete read and a DNS failure; these are not treated as erased400s. The
inventory does not reconstruct absent bodies or cover every historical experiment.

Reproduce the synthetic control with the existing qualified local image (its
Docker derivation is described in [current-runtime qualification](current-runtime-preflight.md)):

```sh
docker run --rm --runtime runc --network none --read-only \
  --cap-drop ALL --memory 1g --memory-swap 1g --cpus 1 \
  --tmpfs /tmp:rw,size=128m,mode=1777 \
  --mount type=bind,source="$PWD/evaluations/2026-11-24-gpu-quant/transparent-recorder",target=/state,readonly \
  -e NVIDIA_VISIBLE_DEVICES=void -e PYTHONDONTWRITEBYTECODE=1 \
  --entrypoint python \
  sha256:c9b40eb8dea441cba7ded2e6589e5c011545ffc1ec76a0dc736f8e399d8f947b \
  /state/preflight_transparent_llm_recorder.py
```

The image must already exist locally; this command does not fetch a replacement
Hermes version. [Source hashes](transparent-recorder/sha256.json) bind the public
old/new recorder and control. The controlled token counts reproduce the observed
overflow message but do not submit the private original conversation.
