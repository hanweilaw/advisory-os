---
name: meeting-notes
description: Use after a client meeting, when the adviser pastes rough notes or a transcript, or says "write up the meeting", "notes from today", "record of advice", or "/meeting-notes". Produces structured notes, action items, a record of advice and a draft follow-up email.
argument-hint: "\"Client name\" [<notes file or pasted text>] [--date YYYY-MM-DD]"
---

# Meeting notes

## Input

Pasted notes, a voice-memo transcript, or a file path. If none is given, ask the adviser to paste or dictate. Never invent what was said; anything unclear becomes a question in the notes.

## Output 1: notes (`templates/meeting-notes.md`)

- Summary in 3 to 5 sentences.
- What the client told us: new facts, changes and concerns. Quote the client where wording matters.
- Advice discussed, with the basis and the client's response, including any advice declined.
- Decisions and actions (owner, due date).
- Record of advice in the format the firm requires (`practice/compliance-rules.md`).

Save to `00_Admin and Meeting Notes/YYYY-MM-DD_Meeting notes.md`.

## Output 2: updates to the file

Propose (don't apply silently) changes to `00_Client Snapshot.md` and the client's `CLAUDE.md` for new facts: life events, new dependants, changed income, preferences. Show the diff and apply when the adviser agrees.

## Output 3: follow-up email draft

Using `/client-email` rules: thank them, recap decisions, list next steps with dates, list what you need from them. Save to `00_Admin and Meeting Notes/YYYY-MM-DD_Follow-up email.md`. Never send.

## Output 4: pipeline

Add each adviser action with a due date to `pipeline/follow-ups.md`.

Finish with `/compliance-check` on the record of advice and report flags in chat.
