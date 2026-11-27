# Task-added Fable Q8 retired to restore working headroom

November 27: removed only `Qwen3.6-14B-A3B-FableVibes-Q8_0.gguf` from the isolated
study staging volume: **14,655,633,920 bytes**. A fresh full SHA256 matched the
original owned download receipt before removal; inode, modification time, size,
device, regular-file type and exclusive link were rechecked. The file is absent
from the original 30-model inventory. No original model or useful staged IQ4 was
removed. No owner data, configuration, image or general Docker cache was pruned.

The [current Q8 workflow](native-fable-q8-thinking-cold-beets.md) failed the complete
task requirements, and no measured whole-workflow advantage over retained Q6
justified keeping the larger added artifact. This is a retention decision for the
tested workflow, not a claim that Q8 cannot help any task. Historical evidence and
[pinned source revision](https://huggingface.co/tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF/tree/9cf910a7ad68dfedcbdfc46ef0fe5003dec07c23)
remain available; rerunning Q8 now requires its exact file to be downloaded again.

The immediate staging free-space observation rises to **117.45 GiB**, leaving
about 17.45 GiB above the 100 GiB minimum. The original model filesystem
remains above 100 GiB. Original30 and stagedIQ4 metadata match before/after.
Shared-host use can change those values; every new admission must check again.

This follows the independently audited and
[published disk-guard interruption](native-adapted-iq4-current-interrupted.md).
The next IQ4 run needs a fresh fixture/profile/conversation and separate attempt
label, retaining the interrupted attempt. It must preserve the 100 GiB runtime
guard and establish at least 110 GiB staging free at admission. No new weight was
downloaded as part of this cleanup.

[Retirement receipt](study-owned-q8-retirement.json) and
[known-value privacy scan](study-owned-q8-retirement-privacy.json).
