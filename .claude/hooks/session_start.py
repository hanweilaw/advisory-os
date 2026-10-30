"""SessionStart: open with what's due, and nudge to run /setup if practice files are unfilled.
Whatever this prints is added to Claude's context for the session."""
import datetime
import os
import re

from _common import PROJECT_DIR, client_root, is_cloud_synced

today = datetime.date.today()
horizon = today + datetime.timedelta(days=7)
lines = []

root = client_root()
if is_cloud_synced(root):
    lines.append(
        f"STOP: the client folder ({root}) is inside a cloud-synced folder. Client data must stay on this "
        "computer only (PDPA, see knowledge/markets/singapore/pdpa.md). Tell the adviser before doing any "
        "client work, and help them move it to a local, non-synced folder. Writes there are blocked."
    )

practice = os.path.join(PROJECT_DIR, "practice")
unfilled = []
for name in sorted(os.listdir(practice)) if os.path.isdir(practice) else []:
    with open(os.path.join(practice, name), encoding="utf-8") as f:
        if "{{" in f.read():
            unfilled.append(name)
if unfilled:
    lines.append(f"Practice files still have placeholders ({', '.join(unfilled)}). Suggest running /setup.")

due = []
followups = os.path.join(PROJECT_DIR, "pipeline", "follow-ups.md")
if os.path.exists(followups):
    with open(followups, encoding="utf-8") as f:
        for line in f:
            if not line.lstrip().startswith("- [ ]"):
                continue
            m = re.search(r"(\d{4}-\d{2}-\d{2})", line)
            if m:
                try:
                    when = datetime.date.fromisoformat(m.group(1))
                except ValueError:
                    continue
                if when <= horizon:
                    tag = "OVERDUE" if when < today else "due"
                    due.append(f"{tag} {line.strip()[6:]}")
if due:
    lines.append(f"Follow-ups due by {horizon.isoformat()}:")
    lines.extend(f"  {d}" for d in due)

if lines:
    print(f"Advisory OS · {today.isoformat()}")
    print("\n".join(lines))
