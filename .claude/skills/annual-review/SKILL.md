---
name: annual-review
description: Use when a client's yearly review is due or the adviser says "review pack for", "annual review", "policy review", or "/annual-review". Compares what's on file now with the last review, lists changes, checks goals and drafts recommendations. Draft only.
argument-hint: "\"Client name\" [--year YYYY]"
---

# Annual review

## Read

- Client `CLAUDE.md`, snapshot, the last review in `09_Review History/`, the latest FNA, meeting notes since the last review.
- Current policy documents (`04`), investment statements (`05`), CPF (`03`), estate documents (`06`).

## Build the pack (`templates/review-summary.md`)

1. **What changed:** for each area, last review vs now vs "so what". Include age-related changes (premium step-ups, CPF milestones at 55 and 65, children reaching school or university age).
2. **Protection in force:** every policy, its cover, premium and next renewal date, from documents on file. A policy in the snapshot but with no document gets `[VERIFY]`.
3. **Investments:** value now vs last review, contributions, and any fund or allocation drift. No performance forecasts.
4. **Goals check:** on track / behind / ahead, with the reason.
5. **Gaps and draft recommendations:** re-run the gap method from `/fna` step 3 on current numbers; recommendations follow the `/fna` step 4 rules.
6. **Questions for the client** and **housekeeping** (nominations, will, LPA, contact details, risk profile age).

Save to `09_Review History/YYYY-MM-DD_Annual review DRAFT.md`. Update the snapshot's "Last review / next due" only after the adviser confirms the meeting happened.

In chat: the three biggest changes, the gaps with numbers, and the housekeeping items due.

## Roster mode

`/annual-review --due` lists clients whose next review date in their snapshot falls in the next 60 days, sorted by date. Read-only.
