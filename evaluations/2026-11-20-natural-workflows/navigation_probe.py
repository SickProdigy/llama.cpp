"""Focused-tool HTTP diagnostic, not the complete Hermes AIAgent runtime.

Uses the real backend and MCP transport with an explicit read-only dispatch gate.
Run old/new reader output separately; preserve all model calls without repair.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import time
import types

from preflight import request, rpc, unpack

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
READS = {"identity", "search_repositories", "repository_info", "list_branches",
         "list_directory", "read_file", "list_issues", "read_issue",
         "list_pull_requests", "read_pull_request"}


def load_plugin(variant):
    path = ROOT / "hermes-profile/gitea-focused/__init__.py"
    if variant == "old":
        source = subprocess.check_output(["git", "-C", str(ROOT), "show", "HEAD:hermes-profile/gitea-focused/__init__.py"], text=True)
    else:
        source = path.read_text(encoding="utf-8")
    module = types.ModuleType("focused_probe")
    exec(compile(source, str(path), "exec"), module.__dict__)
    return module, hashlib.sha256(source.encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variant", choices=["old", "new"], required=True)
    parser.add_argument("--trial", type=int, required=True)
    parser.add_argument("--task", choices=["source", "find"], default="source")
    parser.add_argument("--backend", default="http://192.168.86.239:11430")
    parser.add_argument("--mcp", default="http://192.168.86.239:8289/mcp")
    args = parser.parse_args()
    plugin, source_hash = load_plugin(args.variant)
    props = request(args.backend + "/props")
    bridge_calls = []

    def transport(name, arguments):
        native = name.removeprefix(plugin.PREFIX)
        result = rpc(args.mcp, "tools/call", {"name": native, "arguments": arguments})
        value = unpack(result)
        bridge_calls.append({"name": native, "arguments": arguments, "result": value})
        return value

    bridge = plugin.Bridge(transport, [])
    # Include real write schemas; refuse attempted mutations before any RPC.
    tools = [{"type": "function", "function": schema} for schema in plugin.schemas().values()]
    prompt = {
        "source": "In sickprodigy/nicotineplus-plugins, explain how autospamignore bounds numeric settings and which conversion errors it handles. Base your answer on the code.",
        "find": "Find my SonicRatings repo and tell me what it does.",
    }[args.task]
    system = "You are a repository assistant. The owner's account is sickprodigy; hermes-agent is the automation account. The owner's repositories live on the configured Gitea service. Use evidence from tools and state uncertainty. Do not mutate repositories for read-only requests."
    messages = [{"role": "system", "content": system}, {"role": "user", "content": prompt}]
    report = {"scope": "HTTP tool-loop navigation diagnostic, NOT full Hermes; no local/web tools; no routing-compliance claim", "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "variant": args.variant, "trial": args.trial, "task": args.task, "plugin_sha256": source_hash, "model": props["model_alias"], "context": props["default_generation_settings"]["n_ctx"], "system": system, "prompt": prompt, "tools": tools, "calls": [], "requests": [], "native_calls": bridge_calls}
    output = HERE / ("probe-" + args.task + "-" + args.variant + "-" + str(args.trial) + ".json")
    if output.exists():
        raise SystemExit("Refusing to overwrite an existing trial")
    start = time.monotonic()

    def save():
        report["seconds"] = round(time.monotonic() - start, 3)
        output.write_text(json.dumps(report, indent=2), encoding="utf-8")

    try:
        for _ in range(10):
            if time.monotonic() - start > 180:
                report["stop"] = "time budget"
                break
            body = {"model": props["model_alias"], "messages": messages, "tools": tools,
                    "temperature": 0.2, "top_k": 20, "top_p": 0.95, "min_p": 0.05,
                    "max_tokens": 2048, "stream": False}
            report["requests"].append(body)
            response = request(args.backend + "/v1/chat/completions", body, timeout=180)
            message = response["choices"][0]["message"]
            report.setdefault("responses", []).append(response)
            messages.append(message)
            calls = message.get("tool_calls", [])
            if not calls:
                report["answer"] = message.get("content")
                report["stop"] = "final answer"
                break
            for call in calls:
                name = call["function"]["name"]
                operation = name.removeprefix("gitea_")
                arguments = json.loads(call["function"]["arguments"])
                entry = {"name": name, "arguments": arguments}
                report["calls"].append(entry)
                if not name.startswith("gitea_") or operation not in READS:
                    report["stop"] = "blocked non-read or unknown tool: " + name
                    save()
                    return
                value = bridge.invoke(operation, arguments)
                entry["result"] = value
                messages.append({"role": "tool", "tool_call_id": call["id"], "content": json.dumps(value)})
            save()
        else:
            report["stop"] = "iteration budget"
    except Exception as error:
        report["exception"] = {"type": type(error).__name__, "message": str(error)}
    finally:
        save()
        print(json.dumps({k: report.get(k) for k in ("variant", "trial", "task", "model", "seconds", "stop", "exception", "answer")}), flush=True)


if __name__ == "__main__":
    main()
