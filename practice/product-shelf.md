# Product shelf

<!-- The providers and products you are authorised to recommend. Claude only discusses products listed here,
     and takes their features from the documents in knowledge/products/, never from memory. -->

| Provider | Product | Type | Document on file |
|---|---|---|---|
| {{Insurer A}} | {{Term plan name}} | Term life | `knowledge/products/{{file}}.pdf` |
| {{Insurer B}} | {{IUL / VUL name}} | Universal life | `knowledge/products/{{file}}.pdf` |
| {{Platform}} | {{Managed portfolio}} | Investment | `knowledge/products/{{file}}.md` |

## Rules

- A product not in this table is "not on my shelf"; say so rather than describing it.
- When a product document is older than 12 months, flag it as possibly out of date.
