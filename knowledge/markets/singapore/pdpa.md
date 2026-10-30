# PDPA rules for the Advisory OS (Singapore)

How the Personal Data Protection Act 2012 applies to the way this OS handles client data. Compiled from public PDPC material as a working checklist; it is not legal advice. Your firm's data protection policy and its Data Protection Officer (DPO) have the final word, and the figures below should be checked against current PDPC guidance at pdpc.gov.sg.

## The house position: client data is local only

Client folders live on this computer, in a folder that no cloud service syncs. They are never stored in, synced to or backed up to OneDrive, Dropbox, Google Drive, iCloud, Box, GitHub, Notion or any other hosted service. The OS enforces this:

| Control | What it does |
|---|---|
| `client_root` check | Session start warns, and writes are blocked, if the client folder sits inside a cloud-synced folder |
| `guard_client_data.py` | Blocks uploads, copies into cloud folders, and Git adds of client files |
| `.gitignore` | Excludes `clients/`, `pipeline/` and `logs/` from Git |
| `scripts/pii_guard.py` | Stops a commit that carries ID numbers, phone numbers or emails |
| Connectors | Never receive client documents (see `docs/connectors.md`) |

**Backups:** use an encrypted external drive kept under your control (e.g. BitLocker or FileVault), not a cloud backup, unless your firm has approved a specific service in writing.

**AI processing:** when Claude reads a client file to work on it, that content is sent to Anthropic for processing. It is not stored as a hosted copy of your folder, but it is still a disclosure to a service provider, possibly outside Singapore. Before using real client data, confirm your firm's policy on AI tools, check the data-handling terms of your Claude plan (commercial plans offer stronger terms than consumer ones), and minimise: work from masked documents and the client snapshot where you can, rather than raw ID scans.

## The obligations, applied

| Obligation | What it means for an adviser | How the OS supports it |
|---|---|---|
| Consent | Get consent before collecting, using or disclosing personal data; record it | Intake checklist starts with the signed consent / PDPA form |
| Purpose limitation | Use data only for purposes a reasonable person would consider appropriate and that were notified | Skills use client data only for that client's advice and servicing |
| Notification | Tell the client why you collect their data | Firm's PDPA notice filed in `01_Identity and Family` |
| Access and correction | Give clients access to their data and correct errors on request, generally within 30 days | `/data-audit --client` lists what you hold on one client |
| Accuracy | Make reasonable effort to keep data accurate and complete | `/annual-review` housekeeping confirms contact and family details |
| Protection | Reasonable security arrangements against unauthorised access, loss or disclosure | Local-only storage, masked IDs, hooks, device encryption |
| Retention limitation | Stop retaining data once it no longer serves a legal or business purpose | `/data-audit` flags inactive clients past your retention period |
| Transfer limitation | Data sent outside Singapore must get comparable protection | No cloud hosting; AI use under firm-approved terms |
| Accountability | Policies, a DPO, staff who know the rules | `practice/compliance-rules.md` holds your firm's policy and DPO contact |
| Data breach notification | Assess a suspected breach promptly; notify PDPC within 3 calendar days of deciding it is notifiable | `/data-breach` walks the steps |

## ID numbers (NRIC / FIN)

PDPC's advisory guidelines restrict collecting full NRIC numbers and copies of the NRIC to cases where the law requires it or where it is necessary to establish identity to a high degree of fidelity. Financial advisers collect them under MAS customer due diligence requirements, so:
- Keep the full number and ID copy only in `01_Identity and Family`, nowhere else.
- Everywhere else (notes, FNAs, emails, snapshots) write it masked: `S****567A`.
- Never send a full ID number by email or messaging app.

## Marketing and the Do Not Call (DNC) Registry

Before a marketing call, SMS or WhatsApp to a Singapore number, check the DNC Registry unless you have the person's clear, documented consent or an ongoing relationship exemption applies. Servicing an existing client's policy is not marketing; selling them a new product can be. Record the DNC check or consent in the prospect's notes.

## Breach: what counts as notifiable

A breach must be notified to PDPC when it results in, or is likely to result in, significant harm to the individuals, or affects 500 or more people. Where significant harm is likely, the affected individuals are notified too. Assess quickly once you suspect a breach (PDPC expects within 30 days). Typical adviser breaches: a lost unencrypted laptop or phone, an email with client documents sent to the wrong person, client files synced to a personal cloud account.

## Retention

Keep client records for as long as your legal and regulatory obligations require (MAS anti-money-laundering rules for financial advisers require customer records to be kept for at least five years after the relationship ends; confirm the period with your firm), then securely delete. Set your period in `practice/compliance-rules.md`.

## Sources to check

- PDPC: Advisory Guidelines on Key Concepts in the PDPA; Advisory Guidelines on the PDPA for NRIC and other National Identification Numbers; Guide on Managing and Notifying Data Breaches (pdpc.gov.sg)
- MAS: notices and guidelines for financial advisers on AML/CFT and record keeping (mas.gov.sg)
- Your firm's data protection policy and DPO
