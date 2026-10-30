# Customising the Advisory OS

Four levels. Stop at whichever level suits you; each one leaves you with a working system.

| Level | Time | You change | Example |
|---|---|---|---|
| 1. Make it yours | 10 min | `practice/` via `/setup` | licence, firm, segments, disclaimer, voice |
| 2. Your documents | 30 min | `templates/` | your firm's FNA sections, review layout, email style |
| 3. Your workflows | 30 min each | `.claude/skills/` | claims follow-up, referral thank-you, seminar invite |
| 4. Your systems | 1 hour | `.claude/settings.json`, connectors | your calendar, mailbox, CRM, extra hooks |

## Level 1: practice files

Each file in `practice/` is plain Markdown. Edit directly or re-run `/setup`. The most important one is `compliance-rules.md`: paste your firm's real disclaimer and house rules there, because `/compliance-check` and every client-facing skill read it.

## Level 2: templates

Skills fill the headings in `templates/`. To use your firm's FNA layout, replace the headings in `templates/fna.md` with the firm's sections, in order. Keep `{{placeholders}}` where Claude should fill something in. Don't rename the files; skills look them up by name.

## Level 3: your own skills

A skill is a folder in `.claude/skills/` with a `SKILL.md`:

```markdown
---
name: claims-chaser
description: Use when the adviser asks to chase a claim or "where is [client]'s claim". Lists open claims and drafts follow-ups.
---

# Claims chaser
1. Read every file named *Claim* in each client's 08_Implementation slot ...
2. ...
```

The `description` decides when Claude uses it, so write it as "Use when ..." with the phrases you'd actually say. The easiest way to make one: describe the workflow to Claude and ask it to "turn this into a skill in .claude/skills". Run it a few times, then tighten the steps.

Rules of thumb:
- One skill, one job. Name the files it reads and the file it writes.
- Say what it must never do (send, delete, invent figures).
- When you correct Claude on the same thing twice, add the correction to the skill.

## Level 4: hooks and connectors

Hooks live in `.claude/settings.json` and run scripts in `.claude/hooks/`. Ideas:

- Block reading a folder of scanned IDs entirely (`PreToolUse` on `Read`).
- Post a daily summary of `logs/activity.md` at session start.
- Warn when a draft mentions a product that isn't on `practice/product-shelf.md`.

Connectors: see [connectors.md](connectors.md).

## A new market

Copy `knowledge/markets/singapore/` to `knowledge/markets/<your-market>/` and rewrite:
- `planning-assumptions.md`: your local rules of thumb for protection, emergency fund, retirement saving
- `regulatory-checklist.md`: your regulator's suitability and disclosure rules
- `glossary.md`: local schemes and terms

Then set `Market` in `practice/profile.md`. Update the ID-number pattern in `.claude/hooks/_common.py` and `scripts/pii_guard.py` to your country's format.
