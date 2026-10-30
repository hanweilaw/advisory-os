#!/usr/bin/env python3
"""Pre-commit PII guard: block commits that carry client personal data.

Pattern checks: NRIC/FIN numbers, Singapore mobile numbers, email addresses.
Optional name check: a local list of client names, one per line, kept OUTSIDE
this repo and pointed to by the ADVISORY_OS_NAMES environment variable.

Usage:
    python3 scripts/pii_guard.py --staged      # what the pre-commit hook runs
    python3 scripts/pii_guard.py FILE [FILE...]
Exit 0 = clean, 1 = PII found.
"""
import os
import re
import subprocess
import sys

PATTERNS = {
    "ID number": re.compile(r"\b[STFGM]\d{7}[A-Z]\b"),
    "SG mobile": re.compile(r"(?<![\d.])(?:\+65[\s-]?)?[89]\d{3}[\s-]?\d{4}(?![\d.])"),
    "email": re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"),
}
# Addresses that are fine to commit (placeholders, docs).
EMAIL_ALLOW = re.compile(r"@(example\.(com|org)|users\.noreply\.github\.com|anthropic\.com)$")
SKIP_SUFFIXES = (".png", ".jpg", ".jpeg", ".gif", ".pdf", ".xlsx", ".docx", ".zip")


def load_names():
    path = os.environ.get("ADVISORY_OS_NAMES", "")
    if not path or not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [n.strip() for n in f if len(n.strip()) > 3]


def staged_files():
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True, check=True,
    ).stdout
    return [p for p in out.splitlines() if p]


def scan(path, names):
    hits = []
    if path.lower().endswith(SKIP_SUFFIXES):
        return [f"{path}: binary file, not scanned; confirm it holds no client data"]
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except OSError:
        return hits
    for no, line in enumerate(lines, 1):
        for label, rx in PATTERNS.items():
            for m in rx.finditer(line):
                if label == "email" and EMAIL_ALLOW.search(m.group(0)):
                    continue
                hits.append(f"{path}:{no}: {label} '{m.group(0)}'")
        lowered = line.lower()
        for name in names:
            if name.lower() in lowered:
                hits.append(f"{path}:{no}: client name '{name}'")
    return hits


def main(argv):
    names = load_names()
    files = staged_files() if argv[1:] == ["--staged"] else argv[1:]
    findings = [h for p in files for h in scan(p, names)]
    blocking = [h for h in findings if "binary file" not in h]
    for h in findings:
        print(h)
    if blocking:
        print(f"\nPII guard: {len(blocking)} finding(s). Commit blocked. Remove or mask them, then commit again.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
