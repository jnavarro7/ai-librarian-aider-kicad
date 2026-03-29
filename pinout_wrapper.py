import argparse
import json
import re
from pathlib import Path

import ollama
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings


class OllamaEmbeddings(Embeddings):
    def __init__(self, model="nomic-embed-text"):
        self.model = model
        ollama.pull(model)

    def embed_documents(self, texts):
        return [ollama.embeddings(model=self.model, prompt=t)["embedding"] for t in texts]

    def embed_query(self, text):
        return ollama.embeddings(model=self.model, prompt=text)["embedding"]


def normalize_text(text):
    return re.sub(r"\s+", " ", text or "").strip().lower()


def retrieve_context(query, vector_db, top_k=6, filter=None):
    docs = vector_db.similarity_search(query, k=top_k, filter=filter)
    if not docs:
        return ""
    parts = []
    for i, doc in enumerate(docs, start=1):
        chunk = doc.page_content.strip()
        if chunk:
            parts.append(f"[doc {i}] {chunk}")
    return "\n\n".join(parts)


def filter_relevant_context(context, part_number=None):
    if not context:
        return ""
    if not part_number:
        return context

    pn = normalize_text(part_number)
    parts = context.split("\n\n")
    filtered = [p for p in parts if pn in normalize_text(p)]
    return "\n\n".join(filtered) if filtered else context


def extract_json(text):
    if not text:
        raise ValueError("Empty model output.")
    text = text.strip()
    try:
        return json.loads(text)
    except Exception:
        pass
    match = re.search(r"\{.*\}", text, re.S)
    if match:
        return json.loads(match.group(0))
    raise ValueError("Model output did not contain valid JSON.")


def build_schema():
    return {
        "type": "object",
        "properties": {
            "part_number": {"type": "string"},
            "pins": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "pin": {"type": "string"},
                        "name": {"type": "string"},
                        "function": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["pin", "name", "function"],
                    "additionalProperties": False,
                },
            },
            "source_snippets": {"type": "array", "items": {"type": "string"}},
            "confidence": {
                "type": "string",
                "enum": ["low", "medium", "high"],
            },
            "status": {
                "type": "string",
                "enum": ["found", "partial", "not_found"],
            },
        },
        "required": ["part_number", "pins", "source_snippets", "confidence", "status"],
        "additionalProperties": False,
    }


def answer_query(query, context, part_number=None, ollama_model="llama3.2:latest"):
    schema = build_schema()

    prompt = (
        "You are a helpful electronics datasheet assistant.\n"
        "Extract pin definitions for the specified electronic part from the provided context.\n"
        "Return only valid JSON matching the schema.\n"
        "Do not guess. If data is missing, use status='not_found' and an empty pins array.\n\n"
        f"QUERY:\n{query}\n\n"
        f"PART NUMBER:\n{part_number or query}\n\n"
        f"CONTEXT:\n{context}\n"
    )

    response = ollama.generate(
        model=ollama_model,
        prompt=prompt,
        format=schema,
        options={"temperature": 0, "num_predict": 900},
    )

    content = ""
    if isinstance(response, dict):
        content = response.get("response") or response.get("content") or ""
    else:
        content = getattr(response, "response", None) or getattr(response, "content", "") or str(response)

    return extract_json(content)


def ensure_defaults(result, part_number):
    result["part_number"] = result.get("part_number") or part_number
    result["pins"] = result.get("pins") or []
    result["source_snippets"] = result.get("source_snippets") or []
    result["confidence"] = result.get("confidence") or "low"
    result["status"] = result.get("status") or ("partial" if result["pins"] else "not_found")
    return result


def pins_to_markdown(result):
    part_number = result.get("part_number", "unknown")
    status = result.get("status", "unknown")
    confidence = result.get("confidence", "low")
    pins = result.get("pins", [])
    snippets = result.get("source_snippets", [])

    lines = []
    lines.append(f"# Pinout: {part_number}")
    lines.append("")
    lines.append("## Part info")
    lines.append(f"- Part number: {part_number}")
    lines.append(f"- Status: {status}")
    lines.append(f"- Confidence: {confidence}")
    lines.append(f"- Pin count: {len(pins)}")
    lines.append("")

    lines.append("## Pins")
    lines.append("")
    lines.append("| Pin | Name | Function | Notes |")
    lines.append("|---|---|---|---|")

    if pins:
        for p in pins:
            pin = str(p.get("pin", "")).replace("\n", " ").strip()
            name = str(p.get("name", "")).replace("\n", " ").strip()
            function = str(p.get("function", "")).replace("\n", " ").strip()
            notes = str(p.get("notes", "")).replace("\n", " ").strip()
            lines.append(f"| {pin} | {name} | {function} | {notes} |")
    else:
        lines.append("|  |  |  | No pin data found in context. |")

    if snippets:
        lines.append("")
        lines.append("## Source snippets")
        lines.append("")
        for s in snippets:
            lines.append(f"- {s}")

    return "\n".join(lines) + "\n"


def write_output(text, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query Chroma DB and export pinout as Markdown.")
    parser.add_argument("query", help="Natural-language request, e.g. 'extract pinout of LM358'")
    parser.add_argument("--part-number", default="", help="Exact part number to search for")
    parser.add_argument("--persist-dir", default="./db/vector_db", help="Chroma persistence directory")
    parser.add_argument("--k", type=int, default=6, help="Number of nearest docs to retrieve")
    parser.add_argument("--ollama-model", default="llama3.2:latest", help="Ollama model to use")
    parser.add_argument("--context-max-chars", type=int, default=5000, help="Maximum retrieved context size")
    parser.add_argument("--output", default="pinout.md", help="Output Markdown file")
    args = parser.parse_args()

    search_query = args.part_number.strip() or args.query.strip()
    part_number = args.part_number.strip() or args.query.strip()

    embedding_fn = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma(persist_directory=args.persist_dir, embedding_function=embedding_fn)

    retrieved_context = retrieve_context(search_query, db, top_k=args.k)
    retrieved_context = filter_relevant_context(retrieved_context, part_number=part_number)

    if not retrieved_context:
        result = {
            "part_number": part_number,
            "pins": [],
            "source_snippets": [],
            "confidence": "low",
            "status": "not_found",
        }
        md = pins_to_markdown(result)
        write_output(md, args.output)
        print(md)
        raise SystemExit(0)

    if len(retrieved_context) > args.context_max_chars:
        retrieved_context = retrieved_context[: args.context_max_chars] + "\n..."

    result = answer_query(
        query=args.query,
        context=retrieved_context,
        part_number=part_number,
        ollama_model=args.ollama_model,
    )

    result = ensure_defaults(result, part_number)
    md = pins_to_markdown(result)
    write_output(md, args.output)
    print(md)