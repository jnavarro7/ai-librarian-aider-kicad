# IPC-7351 References (Land Pattern / Footprint Design)

This directory contains references and internally-authored notes derived from IPC-7351-style guidance for creating SMD land patterns (KiCad footprints).

## Important (Copyright / Licensing)
- Do NOT commit third-party IPC PDFs here unless redistribution is explicitly permitted.
- Prefer storing: (1) links, (2) document identifiers/edition info, and (3) internally-authored summaries of the rules we apply.

## Linked References (External)
- IPC-7351 reference PDF (external link):
  - Source: https://datasheet.datasheetarchive.com/originals/crawler/fancort.com/428761382a93d283e0ca120b5c72d850.pdf
  - Note: Treat as copyrighted third-party material; link for reference only unless approved for redistribution.

## How we use IPC-7351 guidance in this project
- When a component datasheet does not provide a recommended land pattern, use IPC-7351-style rules to derive:
  - pad sizing targets (toe/heel/side fillets)
  - courtyard definition and margin
  - silk clearance guidelines
  - density level selection (if applicable)

- Prefer this order of precedence:
  1) The part’s datasheet recommended land pattern (if provided)
  2) Part datasheet package drawing + manufacturer application notes
  3) IPC-7351-style derived land pattern rules (as a fallback)
