import argparse
import json
import re
from pathlib import Path

import ollama


def build_schema():
    return {
        "type": "object",
        "properties": {
            "ok": {"type": "boolean"},
            "summary": {"type": "string"},
            "issues": {
                "type": "array",
                "items": {"type": "string"},
            },
        },
        "required": ["ok", "summary", "issues"],
        "additionalProperties": False,
    }


def extract_json(text):
    text = (text or "").strip()
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return json.loads(text[start : end + 1])
    return json.loads(text)


def count_pin_lines(symbol_text):
    return len(re.findall(r"\(pin\s+", symbol_text))


def validate_symbol_text(symbol_text, pin_count, model="qwen2.5-coder:14b-instruct-q4_K_M"):
    schema = build_schema()
    prompt = (
        "Validate the KiCad generated symbol for correctness.\n"
        "Check pin count, pin uniqueness, template placeholders, and basic KiCad symbol structure.\n"
        "Return only valid JSON matching the schema.\n"
        "Keep the summary very short.\n"
        "Do not rewrite the symbol.\n\n"
        f"EXPECTED PIN COUNT:\n{pin_count}\n\n"
        f"SYMBOL TEXT:\n{symbol_text}\n"
    )

    response = ollama.generate(
        model=model,
        prompt=prompt,
        format=schema,
        options={"temperature": 0, "num_predict": 200},
    )

    content = ""
    if isinstance(response, dict):
        content = response.get("response") or response.get("content") or ""
    else:
        content = getattr(response, "response", "") or getattr(response, "content", "") or str(response)

    result = extract_json(content)
    if "issues" not in result:
        result["issues"] = []
    if "summary" not in result:
        result["summary"] = ""
    if "ok" not in result:
        result["ok"] = False
    return result


def main():
    parser = argparse.ArgumentParser(description="Validate a generated KiCad symbol using an LLM.")
    parser.add_argument("symbol_file", help="Path to the generated .kicad_sym file")
    parser.add_argument("--pin-count", type=int, required=True, help="Expected total number of pins")
    parser.add_argument("--model", default="qwen2.5-coder:14b-instruct-q4_K_M")
    parser.add_argument("--out", default=None, help="Optional JSON output path")
    args = parser.parse_args()

    symbol_text = Path(args.symbol_file).read_text(encoding="utf-8")
    result = validate_symbol_text(symbol_text, args.pin_count, model=args.model)

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()