"""Read-only live transport checks. No credentials or inference; stdlib only."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import time
import urllib.request


def request(url, body=None, timeout=20):
    headers = {"Accept": "application/json, text/event-stream"}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers), timeout=timeout) as response:
        text = response.read().decode()
    if text.lstrip().startswith("{"):
        return json.loads(text)
    for line in text.splitlines():
        if line.startswith("data: "):
            return json.loads(line[6:])
    raise ValueError("No JSON response")


def rpc(url, method, params):
    value = request(url, {"jsonrpc": "2.0", "id": 1, "method": method, "params": params})
    if "error" in value:
        return {"rpc_error": value["error"]}
    return value["result"]


def unpack(result):
    if result.get("isError"):
        return {"error": result.get("content")}
    blocks = result.get("content", [])
    texts = [b["text"] for b in blocks if b.get("type") == "text"]
    if len(texts) == 1:
        try:
            return json.loads(texts[0])
        except ValueError:
            return texts[0]
    return texts or result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", default="http://192.168.86.239:11430")
    parser.add_argument("--mcp", default="http://192.168.86.239:8289/mcp")
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("live-preflight.json"))
    args = parser.parse_args()
    props = request(args.backend + "/props")
    schemas = rpc(args.mcp, "tools/list", {})["tools"]
    report = {
        "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope": "read-only transport diagnostics; no Hermes conversation or model inference",
        "backend": {k: props.get(k) for k in ("model_alias", "model_path", "chat_template_caps")},
        "context": props.get("default_generation_settings", {}).get("n_ctx"),
        "schema_count": len(schemas),
        "schema_sha256": hashlib.sha256(json.dumps(schemas, sort_keys=True).encode()).hexdigest(),
        "checks": [],
    }
    cases = [
        ("root-dot", "get_dir_contents", {"owner": "sickprodigy", "repo": "SonicRatings", "ref": "main", "path": "."}),
        ("root-empty", "get_dir_contents", {"owner": "sickprodigy", "repo": "SonicRatings", "ref": "main", "path": ""}),
        ("root-tree", "get_repository_tree", {"owner": "sickprodigy", "repo": "SonicRatings", "tree_sha": "main", "recursive": False, "per_page": 100}),
        ("source-range", "get_file_contents", {"owner": "sickprodigy", "repo": "nicotineplus-plugins", "ref": "main", "path": "autospamignore/__init__.py", "with_lines": True, "start_line": 1, "end_line": 160}),
    ]
    for label, tool, arguments in cases:
        start = time.monotonic()
        try:
            value = unpack(rpc(args.mcp, "tools/call", {"name": tool, "arguments": arguments}))
            summary = {"type": type(value).__name__}
            if isinstance(value, dict):
                summary["keys"] = sorted(value)
                for key in ("start_line", "end_line", "total_lines", "truncated"):
                    if key in value:
                        summary[key] = value[key]
                if "error" in value:
                    summary["error"] = value["error"]
                if isinstance(value.get("content"), str):
                    content = value["content"]
                    summary["content_chars"] = len(content)
                    try:
                        lines = json.loads(content)
                    except ValueError:
                        lines = None
                    if isinstance(lines, list):
                        summary["returned_lines"] = len(lines)
                        summary["last_line"] = lines[-1].get("line") if lines else None
            elif isinstance(value, str):
                summary["message"] = value[:600]
            report["checks"].append({"case": label, "tool": tool, "arguments": arguments, "seconds": round(time.monotonic() - start, 3), "summary": summary})
        except Exception as error:
            report["checks"].append({"case": label, "transport_error": str(error)})
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
