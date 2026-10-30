---
name: pipeline
description: Use for the weekly business review, or when the adviser says "who should I follow up", "pipeline", "what's due this week", or "/pipeline". Reads pipeline/ and client snapshots and lists follow-ups due, stalled prospects, reviews due and birthdays. Read-only unless asked to update.
---

# Pipeline

## Read

- `pipeline/prospects.md` and `pipeline/follow-ups.md`
- Each client's `00_Client Snapshot.md` for next review dates (names and dates only; don't load full files)
- Calendar connector, if wired, for meetings already booked

## Report (in chat)

1. **Overdue follow-ups**, oldest first: who, what, how late.
2. **Due this week.**
3. **Stalled prospects:** no movement for 30+ days, with the last stage.
4. **Reviews due in the next 60 days** that aren't booked.
5. **Birthdays and policy anniversaries** in the next 14 days.
6. **One suggestion:** the single highest-value action this week, and why.

Offer to draft the messages with `/client-email`. When the adviser says something is done, tick it in `follow-ups.md` and move the prospect's stage in `prospects.md`.
