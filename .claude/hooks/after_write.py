"""PostToolUse (Write|Edit): audit-log client file writes, catch unmasked ID numbers,
and remind about /compliance-check on client-facing drafts."""
import datetime
import json
import os
import sys

from _common import ID_PATTERN, PROJECT_DIR, client_root, inside, read_event

event = read_event()
path = (event.get("tool_input") or {}).get("file_path", "")
if not path:
    sys.exit(0)

root = client_root()
if not inside(path, root):
    sys.exit(0)

rel = os.path.relpath(path, root)
client = rel.split(os.sep)[0]
stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
log_dir = os.path.join(PROJECT_DIR, "logs")
os.makedirs(log_dir, exist_ok=True)
with open(os.path.join(log_dir, "activity.md"), "a", encoding="utf-8") as log:
    log.write(f"- {stamp} · {client} · {event.get('tool_name', 'Write')} · {rel}\n")

try:
    with open(path, encoding="utf-8", errors="ignore") as f:
        text = f.read()
except OSError:
    sys.exit(0)

found = sorted(set(ID_PATTERN.findall(text)))
if found:
    print(
        f"{rel} contains {len(found)} unmasked ID number(s). "
        "Mask each to the last 4 characters (e.g. S****567A) before continuing.",
        file=sys.stderr,
    )
    sys.exit(2)

name = os.path.basename(path).lower()
if any(k in name for k in ("email", "fna", "review", "comparison", "proposal")):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": f"{rel} is client-facing: run /compliance-check on it before the adviser shares it.",
        }
    }))
sys.exit(0)
