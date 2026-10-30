---
name: compare-products
description: Use when the adviser wants proposals or policies compared, says "compare these plans", "term vs IUL", "which is better for", "side by side", or "/compare-products". Builds a side-by-side table from product documents on file, with every figure traced to its page.
argument-hint: "<client name or files...> [--need protection|retirement|legacy|investment]"
---

# Compare products

1. **Collect sources:** the illustrations or brochures named, or every proposal in the client's `04` / `05` slots, plus matching notes in `knowledge/products/`. Read each document; don't rely on memory of the product.
2. **Normalise:** same sum assured, premium term and age where the documents allow. Where they don't, say so instead of adjusting the numbers yourself.
3. **Table:** one column per product, rows: premium (annual, total), premium term, cover by event (death, TPD, CI), guaranteed vs non-guaranteed values at the illustrated rates (state the rates), surrender value at years 5, 10 and 20, charges, flexibility, key exclusions. Each cell cites its page (`p.4`). Missing → `[VERIFY]`.
4. **Fit to the client:** relate each option to the client's need, budget and horizon from the FNA. Include "buy term and invest the difference" or "do nothing" where relevant as a baseline.
5. **No winner by default.** Summarise trade-offs; the adviser makes the recommendation.

Save to `00_Admin and Meeting Notes/YYYY-MM-DD_Product comparison.md` (client) or `knowledge/notes/` (no client). Run `/compliance-check` before it's shown to a client.
