---
name: fna
description: Use when the adviser wants to run or draft a fact-find / Financial Needs Analysis, says "do the FNA for", "fact-find", "needs analysis", "what are their gaps", or "/fna". Walks the fact-find from documents on file and the adviser's notes, calculates protection, retirement and education gaps, and drafts the FNA with a basis of recommendation. Draft only.
argument-hint: "\"Client name\" [--from-notes <file>] [--interview]"
---

# FNA

Produces `00_Admin and Meeting Notes/YYYY-MM-DD_FNA DRAFT.md` using `templates/fna.md` (change the slot in `practice/compliance-rules.md` if your firm files FNAs elsewhere).

## Step 1: Gather

Read the client's `CLAUDE.md`, snapshot, intake checklist, and every document in slots 01 to 06. If `--from-notes` is given, read that file too. With `--interview`, ask the adviser for missing fields one section at a time.

## Step 2: Fill sections 1 to 6 and 8 to 9

Only facts that are on file or stated by the adviser. Each figure gets its source in a footnote (`[^1]: 05_Investments and Assets/2026-09-30_Statement.pdf p.2`). Missing items go to section 12, "Information outstanding". Mask ID numbers.

## Step 3: Calculate the gaps (section 7)

Use `knowledge/markets/<market>/planning-assumptions.md` plus any adviser overrides listed there. Show the working for each line (required, existing, gap) so the adviser can check it. Existing cover comes only from policy documents on file; if a policy is mentioned but not on file, count it as `[VERIFY]`, not as cover.

## Step 4: Priorities and recommendations (sections 10 and 11)

- Rank the gaps by the client's stated goals and the size of the gap.
- Draft recommendations only from `practice/product-shelf.md`, with product facts from `knowledge/products/`. For each: the need it meets, alternatives considered (including "do nothing" and lower-cost options), why this one, cost against the budget, key risks.
- Write the basis in a factual, third-person register ("Client wishes to…", "We recommend…"), not the adviser's marketing voice.

## Step 5: Check and hand back

Run the `/compliance-check` rules over the draft. In chat, give: the top three gaps with numbers, the count of outstanding items, and any compliance flags. The adviser reviews and signs; never mark the FNA final.
