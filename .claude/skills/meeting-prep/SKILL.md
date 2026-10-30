---
name: meeting-prep
description: Use before a client meeting, when the adviser says "prep me for [client]", "meeting tomorrow with", "agenda for", or "/meeting-prep". Reads the client folder and builds an agenda, talking points, questions and watch-outs. Saves a draft to the client's admin folder.
argument-hint: "\"Client name\" [--date YYYY-MM-DD] [--purpose first|fna|recommendation|review|claim]"
---

# Meeting prep

## Inputs

- Client name (find the folder under `client_root`), meeting date and purpose. If the calendar connector is wired and no client is named, list today's and tomorrow's client meetings and ask which to prep.

## Read, in this order

1. The client's `CLAUDE.md` and `00_Client Snapshot.md`
2. The two most recent files in `00_Admin and Meeting Notes/` (open actions, promises made)
3. The latest FNA and review (`09_Review History/`)
4. Policy and investment documents relevant to the purpose
5. `practice/services.md` for what's in scope

## Build the prep (template: `templates/meeting-agenda.md`)

- **Since we last met:** changes visible on file (new documents, birthdays that change premiums or CPF rules, renewals, maturities), each with its source file.
- **Open actions** from the last meeting, with who owes what.
- **Agenda** sized to the meeting length (default 60 minutes).
- **Talking points:** each tied to a file. No product claims without a document; mark `[VERIFY]` otherwise.
- **Questions to ask:** gaps in the fact-find, life changes to confirm.
- **Bring / send before:** forms, illustrations, documents to request.
- **Watch-outs:** sensitivities from the client's `CLAUDE.md`, compliance points (e.g. replacement of an existing policy needs disclosure).

Save to `00_Admin and Meeting Notes/YYYY-MM-DD_Meeting prep.md`. In chat, reply with the agenda and the top three watch-outs only.
