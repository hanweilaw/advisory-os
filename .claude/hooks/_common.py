"""Shared helpers for the Advisory OS hooks. Standard library only."""
import json
import os
import re
import sys

PROJECT_DIR = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()

# NRIC/FIN: prefix letter, 7 digits, checksum letter. Masked form S****567A does not match.
ID_PATTERN = re.compile(r"\b[STFGM]\d{7}[A-Z]\b")


def read_event():
    try:
        return json.load(sys.stdin)
    except ValueError:
        return {}


def client_root():
    """client_root from practice/profile.md, else <project>/clients."""
    default = os.path.join(PROJECT_DIR, "clients")
    profile = os.path.join(PROJECT_DIR, "practice", "profile.md")
    try:
        with open(profile, encoding="utf-8") as f:
            for line in f:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) >= 2 and cells[0] == "client_root":
                    value = cells[1].strip("` ")
                    if not value or value.startswith("{{"):
                        return default
                    if not os.path.isabs(value):
                        value = os.path.join(PROJECT_DIR, value)
                    return os.path.normpath(value)
    except OSError:
        pass
    return default


def inside(path, root):
    try:
        path = os.path.normcase(os.path.abspath(path))
        root = os.path.normcase(os.path.abspath(root))
        return os.path.commonpath([path, root]) == root
    except ValueError:
        return False
