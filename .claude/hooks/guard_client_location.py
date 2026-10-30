"""PreToolUse (Write|Edit|MultiEdit|NotebookEdit): client files are never written to a
cloud-synced folder (OneDrive, Dropbox, Google Drive, iCloud, Box ...).

Exit 2 blocks the write and tells Claude why.
"""
import sys

from _common import client_root, inside, is_cloud_synced, read_event

event = read_event()
tool_input = event.get("tool_input") or {}
path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
if not path:
    sys.exit(0)

root = client_root()
if inside(path, root) and is_cloud_synced(root):
    print(
        f"Blocked by the Advisory OS local-only rule: the client folder ({root}) is inside a "
        "cloud-synced folder. Client data must stay on this computer only. Ask the adviser to move "
        "the client folder to a local, non-synced location and update client_root in practice/profile.md.",
        file=sys.stderr,
    )
    sys.exit(2)
sys.exit(0)
