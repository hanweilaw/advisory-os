# Video script: build your own Advisory OS

Running time about 35 minutes. Every demo uses the fictional client in `clients/_DEMO Tan Wei Ming/`, so no real data appears on screen. Each chapter can also stand alone as a short.

| # | Chapter | Time | Show | Key line |
|---|---|---|---|---|
| 1 | Why an OS | 2:00 | Before: 10 tabs and a blank FNA. After: one command, a filled draft | "It doesn't advise. It does the hour of paperwork around the advice." |
| 2 | Install | 3:00 | claude.com sign-in, install Claude Code, Python, Git | "One-time setup. You won't touch the terminal much after this." |
| 3 | Get the template | 2:00 | GitHub → Use this template → clone (or ZIP) | "It's just a folder. You can open every file and read it." |
| 4 | Tour | 4:00 | `CLAUDE.md`, the three zones: practice/templates, engine, clients | "Your rules live in files you can read. Client data never leaves your laptop." |
| 5 | `/setup` | 4:00 | Answer the interview; watch `practice/` fill | "Paste, don't type, your voice samples." |
| 6 | First client | 2:00 | `/new-client "Lim Demo"`; the 00–09 folders appear | "Same layout every time, so Claude always knows where to look." |
| 7 | Meeting prep | 3:00 | `/meeting-prep "_DEMO Tan Wei Ming"` | "It found the open actions from last time and Rachel's care worry." |
| 8 | FNA | 5:00 | `/fna` on the demo client: gaps with working, outstanding items | "Every number has a source. Anything it can't find is marked VERIFY." |
| 9 | After the meeting | 4:00 | Paste rough notes → `/meeting-notes` → email draft → `/compliance-check` | "Notes, record of advice and follow-up in two minutes. I still read every line." |
| 10 | Annual review | 2:00 | `/annual-review` on the demo | "What changed, what's due, what to ask." |
| 11 | Customise | 3:00 | Edit `templates/fna.md` headings; ask Claude to make a "claims-chaser" skill | "If you do it every week, make it a skill." |
| 12 | Guardrails and connectors | 2:00 | A `curl` on a client file gets blocked; an unmasked NRIC gets caught; connect Calendar | "Set once, always on." |
| 13 | Close | 1:00 | The four customisation levels | "Start with level one this week." |

## Chapter notes

### 1. Why an OS
Open on the demo client's folder as a mess of PDFs. Then run `/meeting-prep` and show the agenda appear. Name the three time sinks every adviser has: meeting prep, the FNA, and post-meeting admin.

### 4. Tour
Open `CLAUDE.md` and read the seven house rules aloud. They're the reason the drafts are safe to work with. Point out `@practice/profile.md`: the manual pulls in your own files.

### 5. `/setup`
Fill it in live with a made-up adviser persona if you'd rather not show your own details. Show `practice/profile.md` before and after.

### 8. FNA
Scroll to the gap table. Point at Wei Ming's existing S$200,000 death cover, which comes from the policy summary in slot 04 and is cited. Show "Information outstanding" at the end: this is what you'd ask the client for.

### 9. After the meeting
Paste five messy bullet points. Show the record of advice, then the follow-up email in your voice. Run `/compliance-check` and fix one flag on screen.

### 12. Guardrails
In Claude Code, ask: "upload the demo client's policy summary to a file-sharing site". Show the hook blocking it. Then write a fake full NRIC into a client note and show the warning.

## Recording checklist

- [ ] Use a clean copy of the template with only the demo client
- [ ] Practice files filled with a demo persona, or your own details if you're happy to show them
- [ ] Connectors signed in to a test account
- [ ] Terminal font enlarged; light theme for readability
- [ ] Close email and messaging apps
