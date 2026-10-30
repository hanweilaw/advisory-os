# Compliance rules

<!-- Your firm's and regulator's rules that every client-facing draft must pass.
     /compliance-check reads this file. Replace the examples with your firm's actual requirements,
     and confirm them with your compliance team. -->

## Before recommending

- [ ] A current fact-find exists (dated within {{12}} months) and the client's needs are documented.
- [ ] The client's risk profile is recorded for any investment-linked recommendation.
- [ ] Each recommendation states the basis: the need, the alternatives considered, why this one, costs and key risks.
- [ ] Where the client declines advice or chooses differently, that is recorded.

## In every client-facing document

- [ ] Adviser name, firm and representative number appear: {{name, firm, rep no.}}
- [ ] Standard disclaimer included: "{{Paste your firm's disclaimer here.}}"
- [ ] Projected figures are labelled as illustrations at the stated rates, not guarantees.
- [ ] Past performance statements carry "Past performance is not necessarily indicative of future performance."

## Never write

- "Guaranteed" about any non-guaranteed benefit, return or bonus.
- Manufactured urgency ("price goes up tomorrow", "last chance").
- Comparisons that disparage another product or adviser without a fair basis.
- A client's full ID number, bank account number or medical detail in an email.

## Personal data (PDPA)

Full rules: `knowledge/markets/singapore/pdpa.md`. The non-negotiables:

- **Local only.** Client folders are stored on this computer in a folder no cloud service syncs. Never OneDrive, Dropbox, Google Drive, iCloud, Box, GitHub or Notion.
- **Consent first.** No fact-find data is collected or used before the signed consent / PDPA notice is on file.
- **Minimum data.** Collect only what the advice needs. Full ID numbers and ID copies live only in `01_Identity and Family`; everywhere else they are masked.
- **No sensitive data in messages.** Never put full ID numbers, account numbers or medical details in email or WhatsApp.
- **Marketing.** Check the DNC Registry (or record consent) before marketing calls or messages.
- **Retention.** Keep client records for {{7}} years after the relationship ends, then securely delete.
- **Breach.** Report any suspected breach to {{your DPO's name and contact}} the same day and run `/data-breach`.
- **AI tools.** {{Your firm's policy on using AI tools with client data, in one line.}}
- **Backups.** {{e.g. Encrypted external drive, kept at the office}}. No personal cloud backup of client folders.

## Records to keep

| Event | Record | Where |
|---|---|---|
| Fact-find | FNA, signed | `00_Admin and Meeting Notes` |
| Advice given | Record of advice / basis of recommendation | `00_Admin and Meeting Notes` |
| Implementation | Application, receipts | `08_Implementation` |
| Review | Review summary | `09_Review History` |
| Consent | Signed consent / PDPA notice | `01_Identity and Family` |
| DNC check | Date checked or consent recorded | prospect notes in `00_Admin and Meeting Notes` |
