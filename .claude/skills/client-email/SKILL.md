---
name: client-email
description: Use when the adviser wants a message drafted to a client, says "draft an email to", "WhatsApp message for", "follow up with", or "/client-email". Writes in the adviser's voice from practice/voice.md, with no sensitive data. Draft only, never sent.
argument-hint: "\"Client name\" <purpose> [--whatsapp]"
---

# Client email

1. Read `practice/voice.md` and match its register: greeting, sentence length, sign-off.
2. Read the client's `CLAUDE.md` for how they like to be addressed and any sensitivities, and the latest meeting notes for context.
3. Draft with `templates/client-email.md`: why I'm writing, what happens next (dated list), what I need from you. `--whatsapp` makes it short, no subject line, no list longer than three items.
4. Never include: full ID or account numbers, medical details, projected returns without the illustration caveat, pressure or urgency.
5. Run the mechanical checks from `/compliance-check`.
6. Save to `00_Admin and Meeting Notes/YYYY-MM-DD_<purpose> email.md` and show the draft in chat. If an email connector is wired, offer to save it as a draft in the mailbox. Never send.
