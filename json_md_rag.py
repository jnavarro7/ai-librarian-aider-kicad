import argparse
import json
import os
import shutil
from pathlib import Path

import ollama
from langchain_community.vectorstores import Chroma
from langchain_core.embeddings import Embeddings as BaseEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def normalize(text):
    return (text or "").lower().replace(" ", "").replace("-", "")


def load_markdown(md_path):
    if not os.path.isfile(md_path):
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        raise ValueError(f"Markdown file is empty: {md_path}")

    return content


def load_json_data(json_path):
    if not os.path.isfile(json_path):
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_text_from_package_pinout(data, target_package=None):
    rows = data.get("package_pinout", [])
    lines = []

    for r in rows:
        pkg = r.get("package", target_package or "")
        if target_package and pkg and normalize(pkg) != normalize(target_package):
            continue

        pin = r.get("package_pin", "")
        signal = r.get("signal", "")
        note = r.get("note", "")

        if pin == "" or pin is None:
            continue

        if note:
            lines.append(f"Pin {pin} ({signal}) [{pkg}] - {note}")
        else:
            lines.append(f"Pin {pin} ({signal}) [{pkg}]")

    return "\n".join(lines).strip()


def chunk_text(text, chunk_size=1200, chunk_overlap=300):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_text(text)


class OllamaEmbeddings(BaseEmbeddings):
    def __init__(self, model="nomic-embed-text"):
        self.model = model
        ollama.pull(model)

    def embed_documents(self, texts):
        embeddings = []
        for text in texts:
            response = ollama.embeddings(model=self.model, prompt=text)
            embeddings.append(response["embedding"])
        return embeddings

    def embed_query(self, text):
        response = ollama.embeddings(model=self.model, prompt=text)
        return response["embedding"]


def reset_vector_db(persist_directory):
    if os.path.isdir(persist_directory):
        shutil.rmtree(persist_directory)


def store_in_vector_db(chunks, persist_directory="./db/vector_db", model="nomic-embed-text", collection_name="pinout_db"):
    embedding_fn = OllamaEmbeddings(model=model)
    vector_db = Chroma.from_texts(
        texts=chunks,
        embedding=embedding_fn,
        persist_directory=persist_directory,
        collection_name=collection_name,
    )
    return vector_db


def run_retrieval_test(vector_db, package, target_pin=None, k=3):
    queries = [
        f"{package} pinout",
        f"{package} P0.0",
        f"{package} VDDA",
    ]
    if target_pin:
        queries.insert(0, f"{package} pin {target_pin}")

    print("\n--- RETRIEVAL TEST ---")
    for q in queries:
        print(f"\nQuery: {q}")
        results = vector_db.similarity_search(q, k=k)
        for i, doc in enumerate(results, start=1):
            preview = doc.page_content[:300].replace("\n", " ")
            print(f"[{i}] {preview}")


def main():
    parser = argparse.ArgumentParser(
        description="Load Markdown and JSON, store in vector DB, and test retrieval"
    )
    parser.add_argument("md_path", help="Path to the Markdown file")
    parser.add_argument("--json", dest="json_file", required=True, help="Path to the JSON file")
    parser.add_argument("--package", required=True, help='Package to filter, e.g. "28-pin SSOP"')
    parser.add_argument("--persist_directory", default="./db/vector_db", help="Chroma persist directory")
    parser.add_argument("--collection_name", default="pinout_db", help="Chroma collection name")
    parser.add_argument("--embed_model", default="nomic-embed-text", help="Ollama embedding model")
    parser.add_argument("--chunk_size", type=int, default=1200)
    parser.add_argument("--chunk_overlap", type=int, default=300)
    parser.add_argument("--test_pin", default="21", help="Optional pin number to test retrieval, e.g. 21")
    parser.add_argument("--no-reset-db", action="store_true", help="Do not delete the existing vector DB before rebuilding")
    args = parser.parse_args()

    md_text = load_markdown(args.md_path)
    print(f"Loaded Markdown file. Length: {len(md_text)} characters")

    data = load_json_data(args.json_file)
    package_text = build_text_from_package_pinout(data, target_package=args.package)
    if not package_text:
        raise ValueError(f"No package_pinout data found in JSON for package: {args.package}")

    chunks = chunk_text(package_text, chunk_size=args.chunk_size, chunk_overlap=args.chunk_overlap)
    print(f"Created {len(chunks)} chunks")

    if not args.no_reset_db:
        reset_vector_db(args.persist_directory)
        print(f"Reset vector database at: {args.persist_directory}")

    vector_db = store_in_vector_db(
        chunks,
        persist_directory=args.persist_directory,
        model=args.embed_model,
        collection_name=args.collection_name,
    )
    print(f"Stored in vector database at: {args.persist_directory}")
    print("Ready for retrieval!")

    run_retrieval_test(vector_db, args.package, target_pin=args.test_pin)


if __name__ == "__main__":
    main()