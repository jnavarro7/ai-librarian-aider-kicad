# JEDEC References (Package Outlines)

This directory contains references to JEDEC-style package outline guidance used to create and validate KiCad footprints (e.g., SOIC, TSSOP/TSOP, DFN/QFN).

## Important (Copyright / Licensing)
- Do NOT commit third-party standards PDFs here unless redistribution is explicitly permitted.
- Many documents are copyrighted and provided for reference only.
- Prefer storing: (1) links, (2) document identifiers, and (3) internally-authored summaries of the rules we apply.

## Linked References (External)
- CASERM-D (ON Semiconductor) — Package outline / dimensional guidance (reference link):
  - Source: https://www.newark.com/pdfs/techarticles/onSemi/CASERM-D.pdf
  - Note: Copyrighted third-party literature; keep as link only unless approved for redistribution.

## How we use JEDEC-style outlines in this project
- Use the outline documents to confirm the correct package family and the mechanical dimensions to extract:
  - Body length/width (D, E / D1, E1 depending on drawing)
  - Lead pitch (e)
  - Lead span / overall width (E or E2)
  - Lead length and width (L, b)
  - Seating plane / standoff (A1) if relevant

- Prefer this order of precedence:
  1) The part’s datasheet recommended land pattern (if provided)
  2) Part datasheet package drawing dimensions
  3) JEDEC outline reference (as a cross-check)
