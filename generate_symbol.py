import argparse
import json
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
        return json.loads(text[start:end + 1])
    return json.loads(text)

def parse_pin_table(md_text):
    pins = []
    in_table = False
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith("| Pin |"):
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table:
            if not line.startswith("|"):
                break
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 4 and cols[0].isdigit():
                pins.append({
                    "number": cols[0],
                    "name": cols[1],
                    "function": cols[2],
                    "notes": cols[3],
                })
    return pins

def pin_type(function_text):
    f = function_text.lower()
    if "power" in f or "ground" in f or f in {"vcc", "vdd", "vss", "gnd"}:
        return "power_in"
    if "output" in f:
        return "output"
    if "input" in f or "enable" in f:
        return "input"
    return "passive"

def build_pin_block(pins):
    lines = []
    y = 0
    for p in pins:
        lines.append(
            f'    (pin {pin_type(p["function"])} line (at -40 {y} 0) '
            f'(length 3) (name "{p["name"]}") (number "{p["number"]}"))'
        )
        y -= 2.5
    return "\n".join(lines)

def answer_query(query, context, part_number=None, ollama_model="llama3.2:latest"):
    schema = build_schema()
    prompt = (
        "You are a helpful electronics datasheet assistant.\n"
        "Generate only metadata for a KiCad symbol.\n"
        "Return only valid JSON matching the schema.\n"
        "Do not guess. Use empty strings if data is missing.\n\n"
        f"QUERY:\n{query}\n\n"
        f"PART NUMBER:\n{part_number or query}\n\n"
        f"CONTEXT:\n{context}\n"
    )

    response = ollama.generate(
        model=ollama_model,
        prompt=prompt,
        format=schema,
        options={"temperature": 0, "num_predict": 500},
    )

    content = response.get("response") if isinstance(response, dict) else getattr(response, "response", "")
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
    parser.add_argument("--model", default="llama3.2:latest")
    args = parser.parse_args()

    md_text = Path(args.markdown_file).read_text(encoding="utf-8")
    template_text = Path(args.template).read_text(encoding="utf-8")

    pins = parse_pin_table(md_text)
    context = json.dumps({"markdown": md_text, "pins": pins}, indent=2)

    meta = answer_query(
        query="Generate KiCad symbol metadata from this pinout markdown.",
        context=context,
        part_number=args.part_number,
        ollama_model=args.model,
    )

    pin_block = build_pin_block(pins)
    final_text = render_template(template_text, meta, pin_block)

    if "<pin_block>" in final_text or "{{PIN_BLOCK}}" in final_text:
        raise ValueError("Template placeholders were not fully replaced")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(final_text, encoding="utf-8")

if __name__ == "__main__":
    main()