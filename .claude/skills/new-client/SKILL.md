---
name: new-client
description: Use when the adviser has a new client or prospect and says "new client", "set up a folder for", "onboard [name]", or "/new-client". Creates the numbered client folder from the template, a snapshot, a client CLAUDE.md and an intake checklist.
argument-hint: "\"Surname Firstname\" [--couple \"Spouse Name\"] [--business \"Company\"]"
---

# New client

## Steps

1. **Resolve the root.** Read `client_root` in `practice/profile.md` (default `clients/`).
2. **Name the folder** `Surname Firstname`. Couples go under the primary client; a business is `[Business] Company Name`. If a folder with that name (or a close match) exists, stop and show it rather than creating a second one.
3. **Copy `clients/_TEMPLATE/`** to the new folder (all ten numbered slots).
4. **Create `00_Client Snapshot.md`** from `templates/client-snapshot.md`, filling only what the adviser has told you. Everything else stays as a placeholder.
5. **Create the client's `CLAUDE.md`:**

   ```markdown
   # {{Surname Firstname}}
   Household: {{}}
   How they like to communicate: {{}}
   Sensitivities: {{}}
   Notes for Claude: read 00_Client Snapshot.md first; latest meeting notes are in 00_Admin and Meeting Notes/.
   ```
6. **Create `00_Admin and Meeting Notes/YYYY-MM-DD_Intake checklist.md`** listing what to collect before the FNA: ID (masked copy), family details, income and expenses, CPF statement, existing policies, investment statements, will/LPA status, risk profile questionnaire, consent for data collection.
7. **Add the client to `pipeline/prospects.md`** with stage `New` and today's date.
8. Reply with the folder path and the three most useful next steps (usually: send the intake list, book the fact-find, run `/meeting-prep`).

Never create files outside the client root and `pipeline/`.
