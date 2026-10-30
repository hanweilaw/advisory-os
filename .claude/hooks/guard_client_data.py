"""PreToolUse (Bash): stop commands that would move client files off this machine.

Exit 2 blocks the command and tells Claude why.
"""
import os
import re
import sys

from _common import CLOUD_MARKERS, client_root, read_event

OUTBOUND = re.compile(
    r"\b(curl|wget|scp|sftp|rsync|ftp|nc|rclone|aws\s+s3|gsutil|az\s+storage|gh\s+gist)\b"
)
GIT_FORCE_ADD = re.compile(r"\bgit\s+add\b.*(\s-f\b|--force)")
GIT_PUSH = re.compile(r"\bgit\s+(add|commit|push)\b")
COPY = re.compile(r"\b(cp|mv|rsync|robocopy|xcopy|copy|move|Copy-Item|Move-Item|ditto|tar|zip|7z)\b", re.I)

event = read_event()
command = (event.get("tool_input") or {}).get("command", "")
if not command:
    sys.exit(0)

root = client_root()
names = {"clients/", "clients\\", os.path.basename(root.rstrip("/\\")) + "/"}
mentions_clients = root in command or any(n in command for n in names)

reason = None
lowered = command.lower()
to_cloud = any(m in lowered for m in CLOUD_MARKERS if len(m) > 4)

if mentions_clients and OUTBOUND.search(command):
    reason = "it would send files from the client folder off this machine"
elif mentions_clients and COPY.search(command) and to_cloud:
    reason = "it would copy client files into a cloud-synced folder"
elif mentions_clients and GIT_FORCE_ADD.search(command):
    reason = "it would force client files into Git, which syncs to GitHub"
elif mentions_clients and GIT_PUSH.search(command) and "_TEMPLATE" not in command and "_DEMO" not in command:
    reason = "client files must not be committed or pushed"

if reason:
    print(
        f"Blocked by the Advisory OS client-data guard: {reason}. "
        "Client data stays local (see CLAUDE.md house rule 5). Ask the adviser if they really need this.",
        file=sys.stderr,
    )
    sys.exit(2)
sys.exit(0)
