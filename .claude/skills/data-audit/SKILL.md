---
name: data-audit
description: Use for PDPA housekeeping, monthly or when the adviser says "data audit", "PDPA check", "are my client files safe", "what data do we hold on [client]", or "/data-audit". Checks that client data is local only, IDs are masked, consent is on file and old records are flagged for deletion. Read-only; reports in chat.
argument-hint: "[--client \"Client name\"]"
---

# Data audit

Read-only. Report in chat only; never write the findings (which name clients) into a file outside the client root.

## Roster mode (default)

1. **Location.** Resolve `client_root` from `practice/profile.md`. Report whether it, or this OS folder, sits inside a cloud-synced folder (OneDrive, Dropbox, Google Drive, iCloud, Box). Any hit is the first line of the report, marked STOP.
2. **Git.** Run `git status --short --ignored` and `git ls-files` and confirm nothing under the client root, `pipeline/` or `logs/` is tracked. Run `python3 scripts/pii_guard.py` over tracked files (`git ls-files`).
3. **Unmasked IDs.** Search the client root for full NRIC/FIN numbers (pattern `[STFGM]\d{7}[A-Z]`) outside `01_Identity and Family`. List file paths and counts only; never print the numbers.
4. **Consent.** For each client folder, check `01_Identity and Family` or the intake checklist for a consent / PDPA document. List folders without one.
5. **Retention.** Read the retention period from `practice/compliance-rules.md`. List client folders whose newest file is older than that period, as candidates for the adviser to review for secure deletion. Never delete anything.
6. **Stray copies.** Look for client documents outside the client root within this OS folder (e.g. a PDF in `knowledge/` or the project root).

Output: a table of check · result · what to do, with STOP items first. End with one line: `CLEAN`, `FIX` or `STOP`.

## One client (`--client`)

For a client's access or correction request: list every file held for that client, by slot, with dates, and the categories of personal data each holds (identity, contact, financial, health, family). The adviser uses this to answer the request, generally within 30 days. Don't copy the contents into the reply.
