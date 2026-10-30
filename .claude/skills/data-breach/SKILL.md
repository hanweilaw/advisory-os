---
name: data-breach
description: Use the moment a personal data breach is suspected: a lost laptop or phone, an email or file sent to the wrong person, client files found in a cloud folder, an account compromise, or when the adviser says "data breach", "I sent this to the wrong client", or "/data-breach". Walks contain, assess, notify, and drafts the internal report. Never contacts PDPC or clients itself.
---

# Data breach response

Calm and fast. The adviser's firm and its DPO lead; this skill organises the facts and drafts. Rules: `knowledge/markets/singapore/pdpa.md`.

## Step 1: Contain (now)

Ask what happened, then give the containment steps that fit, e.g.:
- Wrong recipient: ask the recipient to delete it and confirm in writing; recall the email if the system allows.
- Lost device: remote-lock and wipe; change passwords; note whether the disk was encrypted.
- Files in a cloud folder: stop sync, move the files to the local client folder, delete the cloud copies including the cloud bin and version history, check sharing links.
- Compromised account: change passwords, sign out all sessions, turn on two-factor authentication.

## Step 2: Record the facts

Collect in a short timeline: when it happened, when it was discovered, what data (categories, not the data itself), how many individuals, which clients (by folder name), what containment was done and when. Write it to `00_Admin and Meeting Notes/YYYY-MM-DD_Data incident.md` in each affected client's folder, or to `logs/incidents/YYYY-MM-DD_Data incident.md` (local, gitignored) if several clients are involved.

## Step 3: Assess (with the DPO)

Lay out the two tests from `pdpa.md`:
- **Significant harm:** does the data include ID numbers, financial account details, health information, or anything that could lead to fraud, identity theft or embarrassment?
- **Significant scale:** 500 or more individuals?

State which way each points and why. The adviser and DPO make the call.

## Step 4: Notify (drafts only)

If notifiable: remind the adviser that PDPC must be notified within 3 calendar days of deciding it is notifiable, and affected individuals too where significant harm is likely. Draft:
- an internal report to the DPO (`practice/profile.md` has the contact)
- a plain, factual notification to affected clients: what happened, what data, what was done, what they can do, who to contact

Never send, submit or contact PDPC or clients. Run `/compliance-check` on the client notification.

## Step 5: Prevent

Suggest one or two concrete changes (e.g. turn on disk encryption, a hook that blocks emailing attachments from the client folder) and offer to add them.
