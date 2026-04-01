import argparse
import json
import re
from pathlib import Path

import ollama


def build_schema():
    return {
        "type": "object",
        "properties": {
            "SYMBOL_NAME": {"type": "string"},
            "REFERENCE": {"type": "string"},
            "VALUE": {"type": "string"},
            "FOOTPRINT": {"type": "string"},
            "DATASHEET": {"type": "string"},
        },
        "required": ["SYMBOL_NAME", "REFERENCE", "VALUE", "FOOTPRINT", "DATASHEET"],
        "additionalProperties": False,
    }


def extract_json(text):
    text = (text or "").strip()
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return json.loads(text[start : end + 1])
    return json.loads(text)


def parse_part_number(md_text):
    patterns = [
        r"Part number:\s*([A-Za-z0-9._/-]+)",
        r"^\s*#\s*Pinout:\s*([A-Za-z0-9._/-]+)\s*$",
        r"^Part:\s*([A-Za-z0-9._/-]+)\s*$",
    ]
    for pattern in patterns:
        m = re.search(pattern, md_text, re.MULTILINE)
        if m:
            return m.group(1).strip()
    return None


def extract_tables_section(md_text):
    marker = "### Extracted Tables"
    idx = md_text.find(marker)
    if idx == -1:
        return ""
    section = md_text[idx:]
    next_heading = re.search(r"^##\s+", section[1:], re.MULTILINE)
    if next_heading:
        section = section[: next_heading.start() + 1]
    return section.strip()


def parse_package_table(md_text, target_package="28-pin SSOP", pin_count=None):
    lines = md_text.splitlines()
    in_table = False
    table_lines = []

    for line in lines:
        if line.strip().startswith("#### Table 1"):
            in_table = True
            continue
        if in_table and line.strip().startswith("#### Table "):
            break
        if in_table and line.strip():
            table_lines.append(line.rstrip())

    if not table_lines:
        return []

    rows = []
    for line in table_lines:
        if line.strip().startswith("|"):
            cols = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(cols)

    if len(rows) < 4:
        return []

    header_packages = rows[2]

    pkg_col = None
    for i, cell in enumerate(header_packages):
        if target_package.lower() in cell.lower():
            pkg_col = i
            break

    if pkg_col is None:
        return []

    pkg_col = pkg_col - (pkg_col % 2)

    pins = []
    seen = set()

    for row in rows[4:]:
        if len(row) <= pkg_col + 1:
            continue

        pin = row[pkg_col].strip()
        name = row[pkg_col + 1].strip()

        if not pin or not name:
            continue
        if not re.fullmatch(r"\d+", pin):
            continue

        key = (pin, name)
        if key in seen:
            continue
        seen.add(key)

        pins.append(
            {
                "number": pin,
                "name": name,
                "function": name,
                "notes": "",
            }
        )

        if pin_count is not None and len(pins) >= pin_count:
            break

    return pins


def pin_type(function_text):
    f = (function_text or "").lower()
    if any(x in f for x in ["vdd", "vss", "vcc", "gnd", "ground", "power"]):
        return "power_in"
    if "nc" in f or "n/c" in f or "no connect" in f:
        return "passive"
    if "out" in f:
        return "output"
    if "in" in f or "enable" in f:
        return "input"
    return "passive"


def build_pin_block(pins):
    lines = []
    y = 0
    for p in pins:
        lines.append(
            f'    (pin {pin_type(p["function"])} line (at -40 {y:.1f} 0) '
            f'(length 3) (name "{p["name"]}") (number "{p["number"]}"))'
        )
        y -= 2.5
    return "\n".join(lines)


def merge_defaults(meta, part_number, target_package):
    meta = dict(meta or {})
    symbol_name = part_number or meta.get("SYMBOL_NAME") or "UNNAMED_PART"
    meta["SYMBOL_NAME"] = symbol_name
    meta["REFERENCE"] = meta.get("REFERENCE") or "U"
    meta["VALUE"] = meta.get("VALUE") or symbol_name
    meta["FOOTPRINT"] = meta.get("FOOTPRINT") or (target_package or "")
    meta["DATASHEET"] = meta.get("DATASHEET") or "~"
    return meta


def build_context(md_text, part_number, target_package, pins, pin_count):
    tables_section = extract_tables_section(md_text)
    return json.dumps(
        {
            "part_number": part_number,
            "package": target_package,
            "pin_count": pin_count,
            "extracted_tables_section": tables_section,
            "selected_pinout": pins,
        },
        indent=2,
        ensure_ascii=False,
    )


def answer_query(query, context, part_number=None, target_package=None, pin_count=None, ollama_model="llama3.2:latest"):
    schema = build_schema()
    prompt = (
        "You are a helpful electronics datasheet assistant.\n"
        "Generate only metadata for a KiCad symbol.\n"
        "Return only valid JSON matching the schema.\n"
        "Do not invent values.\n"
        "Use the selected markdown package table as the only source for pin/package information.\n"
        "Ignore any other tables or values in the document.\n"
        "Do not use numeric table contents as metadata.\n"
        "If a field is missing, return an empty string.\n"
        "Do not generate pin definitions.\n"
        "The pin list has already been limited to the exact pin count.\n"
        "Do not infer or mention additional pins.\n"
        "If the part number is known, do not leave SYMBOL_NAME, REFERENCE, or VALUE empty.\n"
        "For generic symbols, leave FOOTPRINT empty and use '~' for DATASHEET if unknown.\n\n"
        f"QUERY:\n{query}\n\n"
        f"PART NUMBER:\n{part_number or query}\n\n"
        f"PACKAGE:\n{target_package or ''}\n\n"
        f"TOTAL PIN COUNT:\n{pin_count or ''}\n\n"
        f"CONTEXT:\n{context}\n"
    )

    response = ollama.generate(
        model=ollama_model,
        prompt=prompt,
        format=schema,
        options={"temperature": 0, "num_predict": 300},
    )

    content = ""
    if isinstance(response, dict):
        content = response.get("response") or response.get("content") or ""
    else:
        content = getattr(response, "response", "") or getattr(response, "content", "") or str(response)

    return extract_json(content)


def render_template(template_text, data, pin_block):
    data = dict(data)
    data["PIN_BLOCK"] = pin_block
    for k, v in data.items():
        template_text = template_text.replace(f"{{{{{k}}}}}", str(v))
    return template_text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown_file")
    parser.add_argument("--template", default="templates/symbol_template.kicad_sym")
    parser.add_argument("--out", default="output/generated_symbol.kicad_sym")
    parser.add_argument("--part-number", default=None)
    parser.add_argument("--package", default="28-pin SSOP")
    parser.add_argument("--pin-count", type=int, required=True, help="Total number of pins this part has")
    parser.add_argument("--model", default="llama3.2:latest")
    args = parser.parse_args()

    if args.pin_count <= 0:
        raise ValueError("--pin-count must be greater than 0")

    md_text = Path(args.markdown_file).read_text(encoding="utf-8")
    template_text = Path(args.template).read_text(encoding="utf-8")

    part_number = args.part_number or parse_part_number(md_text)
    pins = parse_package_table(md_text, target_package=args.package, pin_count=args.pin_count)

    if not pins:
        raise ValueError(f"No pins found for package: {args.package}")

    if len(pins) < args.pin_count:
        raise ValueError(
            f"Only found {len(pins)} pins, but --pin-count={args.pin_count}"
        )

    if len(pins) > args.pin_count:
        pins = pins[: args.pin_count]

    context = build_context(md_text, part_number, args.package, pins, args.pin_count)

    meta = answer_query(
        query="Generate KiCad symbol metadata from the selected markdown package table.",
        context=context,
        part_number=part_number,
        target_package=args.package,
        pin_count=args.pin_count,
        ollama_model=args.model,
    )

    meta = merge_defaults(meta, part_number, args.package)
    pin_block = build_pin_block(pins)
    final_text = render_template(template_text, meta, pin_block)

    if "{{" in final_text or "}}" in final_text:
        raise ValueError("Template placeholders were not fully replaced")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(final_text, encoding="utf-8")
    print(f"Wrote symbol to: {args.out}")


if __name__ == "__main__":
    main()