import argparse
import ollama
from langchain_community.vectorstores import Chroma
from langchain_core.embeddings import Embeddings


class OllamaEmbeddings(Embeddings):
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


def retrieve_context(query, vector_db, top_k=4, filter=None):
    docs = vector_db.similarity_search(query, k=top_k, filter=filter)
    if not docs:
        return ""
    context_parts = []
    for i, doc in enumerate(docs, start=1):
        context_parts.append(f"[doc {i}] {doc.page_content.strip()}")
    return "\n\n".join(context_parts)


def answer_query(prompt, query, context, ollama_model="llama2", max_tokens=512):
    system_prompt = (
        "You are a helpful electronics datasheet assistant. "
        "Extract the pin definitions (pin number or name and signal/function) for the specified electronic part from the context. "
        "If the context lacks pin information, respond with 'Pin data not found in context'."
    )

    stuffed_prompt = (
        f"{system_prompt}\n\n"
        f"CONTEXT:\n{context}\n\n"
        f"INSTRUCTION:\n{query}\n\n"
        f"PIN DEFINITIONS:"
    )

    response = ollama.generate(
        model=ollama_model,
        prompt=stuffed_prompt,
        options={"max_tokens": max_tokens},
    )

    if isinstance(response, (list, tuple)):
        response = response[-1] if response else {}

    if isinstance(response, dict):
        return response.get("content", response.get("stdout", ""))

    # Ollama may return object with .content
    content = getattr(response, "content", None)
    if content is not None:
        return content

    return str(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query a persisted Chroma vector DB and answer with Ollama.")
    parser.add_argument("query", help="Query string or prompt")
    parser.add_argument("--persist-dir", default="./db/vector_db", help="Chroma persistence directory")
    parser.add_argument("--k", type=int, default=4, help="Number of nearest docs to retrieve")
    parser.add_argument("--ollama-model", default="llama3.2:latest", help="Ollama model to use for answer generation")
    parser.add_argument("--context-max-chars", type=int, default=1500, help="Maximum total characters from retrieved context")
    args = parser.parse_args()

    embedding_fn = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma(persist_directory=args.persist_dir, embedding_function=embedding_fn)

    retrieved_context = retrieve_context(args.query, db, top_k=args.k)
    if not retrieved_context:
        print("No relevant context found in vector DB.")
        raise SystemExit(0)

    if len(retrieved_context) > args.context_max_chars:
        retrieved_context = retrieved_context[: args.context_max_chars] + "\n..."

    try:
        answer = answer_query(args.query, args.query, retrieved_context, ollama_model=args.ollama_model)
    except Exception as exc:
        # Provide a helpful message for model resolution errors.
        import ollama as _ollama

        if hasattr(_ollama, "list"):
            avail = _ollama.list()
            models = [m.model for m in avail.models]
        else:
            models = []
        raise RuntimeError(
            f"Ollama generation failed with {exc!r}.\n"
            f"Available Ollama models: {models}\n"
            f"Try --ollama-model with one of the available models."
        )

    print("\n--- Retrieved context ---\n")
    print(retrieved_context)
    print("\n--- Model answer ---\n")
    print(answer)
