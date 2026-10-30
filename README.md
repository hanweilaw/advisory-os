# Advisory OS

A starter operating system for financial advisers, built on [Claude Code](https://code.claude.com). It turns the work around a client meeting (prep, fact-find, notes, follow-up, annual review, compliance check) into commands you run in plain English, using your own documents, templates and rules.

It is a folder of plain text files. You own it, you can read every rule it follows, and you change it by editing files.

> **Drafts, not decisions.** The OS prepares and checks; you advise, sign and send.
>
> **Client data stays on your computer, never in the cloud.** Client folders live in a local folder that OneDrive, Dropbox, Google Drive, iCloud and Box don't sync, and they are never committed to GitHub. The OS blocks writes to a cloud-synced client folder. PDPA rules are built in (`knowledge/markets/singapore/pdpa.md`). Confirm your firm's policy on AI tools and client data before you put real client files in, and start with the fictional demo client.

## What's inside

```text
advisory-os/
├── CLAUDE.md            the operating manual Claude reads every session
├── practice/            YOU: profile, services, product shelf, compliance rules, voice
├── templates/           YOUR documents: FNA, meeting prep, notes, review, email, snapshot
├── knowledge/           market pack (Singapore example), product notes, your notes
├── clients/             one folder per client, 00–09 slots (local only: never committed, never cloud-synced)
│   ├── _TEMPLATE/
│   └── _DEMO Tan Wei Ming/   fictional client for practice and demos
├── pipeline/            prospects and follow-ups (local only)
├── .claude/
│   ├── skills/          the slash commands
│   ├── agents/          compliance-checker reviewer
│   ├── hooks/           guardrails that run automatically
│   └── settings.json
├── scripts/pii_guard.py pre-commit check for client personal data
└── docs/                customising, connectors, video script
```

## Commands

| Command | What it does |
|---|---|
| `/setup` | Interviews you and fills `practice/` (run this first) |
| `/new-client "Surname Firstname"` | Creates the client folder, snapshot and intake checklist |
| `/meeting-prep "Client"` | Agenda, talking points, questions and watch-outs from the client file |
| `/fna "Client"` | Fact-find, gap calculation and a draft basis of recommendation |
| `/meeting-notes "Client"` | Rough notes or transcript → notes, actions, record of advice, follow-up email |
| `/annual-review "Client"` | Review pack: what changed, cover in force, goals, gaps |
| `/compliance-check <file>` | Checks a draft against your compliance rules |
| `/client-email "Client" <purpose>` | Drafts a message in your voice |
| `/compare-products` | Side-by-side comparison from product documents, every figure cited |
| `/organize-client "Client"` | Sorts a messy folder into the 00–09 slots, nothing deleted |
| `/pipeline` | This week's follow-ups, stalled prospects and reviews due |
| `/data-audit` | PDPA housekeeping: cloud-synced paths, unmasked IDs, missing consent, records past retention |
| `/data-breach` | Step-by-step response to a suspected data breach, with draft notifications |

## Set it up (about 20 minutes)

### 1. Install Claude Code

You need a paid Claude plan (Pro or Max) or an Anthropic Console account. Install Claude Code by following the official guide at [code.claude.com](https://code.claude.com), or use the Claude desktop app. You'll also need:

- **Python 3** for the guardrail hooks: [python.org/downloads](https://www.python.org/downloads/) (on Windows, tick "Add Python to PATH").
- **Git** (Windows: [Git for Windows](https://git-scm.com/download/win), which Claude Code also uses).

Run Claude Code on your own computer (terminal or desktop app) for client work. Cloud sessions such as Claude Code on the web run in a hosted container, so use them only for changes to the template itself, never with client folders.

### 2. Get the template

Either click **Use this template** on GitHub to make your own private copy and clone it, or download the ZIP. Put it in a local folder that no cloud service syncs (not inside OneDrive, Dropbox, Google Drive or iCloud), e.g. `C:\AdvisoryOS` or `~/AdvisoryOS`:

```bash
git clone https://github.com/<you>/advisory-os.git
cd advisory-os
```

### 3. Open it in Claude Code

```bash
claude
```

Claude reads `CLAUDE.md` automatically. The first time, it will ask you to trust the folder and approve the hooks in `.claude/settings.json`.

### 4. Run `/setup`

Answer eight short questions. Paste two things you've written (an email, a WhatsApp message) so drafts sound like you. On Windows, `/setup` switches the hooks from `python3` to `py` for you.

### 5. Try it on the demo client

```text
/meeting-prep "_DEMO Tan Wei Ming"
/fna "_DEMO Tan Wei Ming"
```

### 6. Point it at your real client folders (when you're ready)

Client folders must be on your computer only. Either keep them in `clients/`, or set `client_root` in `practice/profile.md` to a local vault such as `C:\ClientVault`. If your client files are in OneDrive or another cloud service today, move them to the local folder first (and empty the cloud copy, bin and version history), with your firm's agreement.

Before real data goes in:
- Turn on disk encryption (BitLocker on Windows, FileVault on Mac).
- Back up to an encrypted external drive, not a cloud backup.
- Run `/data-audit` and fix anything it flags.

Then run `/organize-client` on one folder and check the plan before approving it.

## Make it yours

See [docs/customising.md](docs/customising.md). In short:

1. **Profile** (`/setup`): who you are, your market and rules.
2. **Documents** (`templates/`): paste your firm's FNA headings and review layout.
3. **Workflows** (`.claude/skills/`): ask Claude "make a skill that ..." for anything you do every week.
4. **Systems** (hooks and connectors): calendar and email. Connectors never receive client documents. See [docs/connectors.md](docs/connectors.md).

Advising outside Singapore? Copy `knowledge/markets/singapore/` to your market, replace its three files, and set `Market` in your profile.

## Guardrails

| Guardrail | How |
|---|---|
| Client folder never in the cloud | Session start warns and `guard_client_location.py` blocks writes if the client folder is inside OneDrive, Dropbox, Google Drive, iCloud or Box |
| Client files never committed | `.gitignore` excludes `clients/`, `pipeline/` and `logs/` (except the template and demo) |
| No uploading client files | `guard_client_data.py` blocks curl, scp, cloud CLIs, copies into cloud folders and forced git adds on client paths |
| Audit trail | `after_write.py` logs every client file Claude writes to `logs/activity.md` |
| ID numbers masked | `after_write.py` stops Claude when an unmasked NRIC/FIN appears in a client file |
| Compliance prompt | client-facing drafts trigger a reminder to run `/compliance-check` |
| PII in commits | `scripts/pii_guard.py` runs before every commit once `/setup` enables it |
| PDPA | consent checked before an FNA, NRIC kept only in slot 01, DNC reminders, `/data-audit`, `/data-breach` |

The hooks are a safety net, not a guarantee. You remain responsible for what leaves your machine.

## Licence

MIT. Use it, change it, share it. See [LICENSE](LICENSE).
