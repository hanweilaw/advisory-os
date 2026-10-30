# Knowledge

Reference material Claude reads before answering product or regulation questions. Everything here is either public or written by you; client documents never go here.

| Folder | Holds |
|---|---|
| `markets/<country>/` | A market pack: planning assumptions, regulatory checklist, local terms. Singapore ships as the example. |
| `products/` | Product summaries, brochures and policy wordings for your shelf (`practice/product-shelf.md`). |
| `notes/` | Your own notes: market views, case studies, objection handling. |

**Adding a market:** copy `markets/singapore/`, rename it, replace the content, and set `Market` in `practice/profile.md`.

**Adding a product:** drop the PDF in `products/`, then ask Claude: "summarise this into products/<name>.md using the product note format", and add a row to `practice/product-shelf.md`.
