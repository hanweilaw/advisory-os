---
name: compliance-check
description: Use before any client-facing document is final, or when the adviser says "check this", "is this compliant", "compliance check", or "/compliance-check". Checks a draft against practice/compliance-rules.md and the market regulatory checklist, and lists exact fixes. Never rewrites silently.
argument-hint: "<file path or pasted draft>"
---

# Compliance check

## Rules to apply, in order of precedence

1. `practice/compliance-rules.md` (the firm's rules win)
2. `knowledge/markets/<market>/regulatory-checklist.md` and `knowledge/markets/<market>/pdpa.md`
3. The house rules in `CLAUDE.md` (no invented product facts, masked IDs, drafts only)

## Checks

- **Mechanical:** full ID numbers, account numbers, phone numbers or emails of third parties; the words "guaranteed", "risk-free", "sure", "no-brainer"; urgency phrases; missing disclaimer, rep number or illustration caveat.
- **Substance:** every recommendation has a need, alternatives, reason, cost and risks; product facts trace to a document on file; replacement of an existing policy carries the switching disclosure; risk profile on file for investment advice.
- **Tone:** respectful, no pressure, no disparaging comparisons.
- **PDPA:** only the personal data the document needs; no full ID numbers outside `01_Identity and Family`; no medical or account details in anything sent by email or messaging; a third party's data (e.g. a family member) only where needed for the advice; marketing messages have a DNC check or consent on file.

For a long or high-stakes document, hand the substance checks to the `compliance-checker` agent so the review isn't anchored on the draft's own reasoning.

## Output

A table in chat:

| # | Issue | Where (quote) | Rule | Fix |
|---|---|---|---|---|

Then one line: `PASS`, `PASS WITH FIXES` or `FAIL`. Offer to apply the fixes; apply only on the adviser's yes. This check supports the adviser's own review; it is not a sign-off by the firm's compliance function.
