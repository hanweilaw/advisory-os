---
name: setup
description: Use when an adviser first opens the Advisory OS, or says "set me up", "onboard me", "personalise this", or wants to refresh their practice files. Interviews the adviser and fills the practice/ files. Safe to re-run.
---

# Setup: make the OS yours

Fill `practice/` from a short interview. One question at a time; write each answer to its file as you go so the adviser can stop and resume.

## Step 1: Check what's filled

Read every file in `practice/`. A file still holding `{{...}}` placeholders is unfilled. Tell the adviser in one line what's done and what's left, then continue with the first unfilled item. If everything is filled, ask what they want to change.

## Step 2: The interview (eight questions, each under a minute)

1. **Who are you?** Name, brand, firm, representative number, qualifications, languages. → `profile.md`
2. **Which market and regulator?** Default Singapore / MAS. If another market, note that `knowledge/markets/` needs a pack for it and offer to draft one at the end. → `profile.md`
3. **Where do your client files live?** Keep `clients/` in this folder, or a full path to a synced folder (OneDrive, Google Drive, a vault). → `client_root` in `profile.md`. Never copy client files during setup.
4. **Who do you serve, and how do you work?** Segments, process, how you're paid. → `profile.md`, `services.md`
5. **What do you advise on, and what do you refer out?** → `services.md`
6. **Which providers and products are on your shelf?** A rough list is fine; product documents can be added later to `knowledge/products/`. → `product-shelf.md`
7. **Your compliance requirements.** Ask for the firm's standard disclaimer and any house rules; keep the example checklist items they agree with. → `compliance-rules.md`
8. **Your voice.** Ask them to paste two things they wrote (a client email, a WhatsApp follow-up, a post). They must paste, not type fresh: if they start composing in the chat, stop them and ask for an existing message. Add a 2-3 line summary of their style. → `voice.md`

Also ask their top three priorities for the quarter (each with a number or date) → `profile.md`.

## Step 3: Machine check

- Ask Windows or Mac. On Windows, replace `python3` with `py` in `.claude/settings.json` hook commands (show the diff, then apply).
- Run `git config core.hooksPath .githooks` so the pre-commit PII guard is active, if this folder is a Git repo.

## Step 4: Close

Print three lines:

```
Done. Your OS knows who you are, who you serve and the rules you work under.
Try it: /new-client "Tan Demo" or open clients/_DEMO Tan Wei Ming and run /meeting-prep.
Next: drop your product brochures in knowledge/products/ and your firm's FNA layout into templates/fna.md.
```
