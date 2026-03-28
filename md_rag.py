import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import ollama
import argparse

# Step 1: Load Markdown file
def load_markdown(md_path):
    if not os.path.isfile(md_path):
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    if not content:
        raise ValueError(f"Markdown file is empty: {md_path}")

    return content

# Step 2: Chunk the Markdown text
def chunk_text(text, chunk_size=1200, chunk_overlap=300):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Step 3: Embedding adapter for Ollama
from langchain_core.embeddings import Embeddings as BaseEmbeddings

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

# Step 4: Store in Vector DB (Chroma)
def store_in_vector_db(chunks, persist_directory="./db/vector_db", model="nomic-embed-text"):
    embedding_fn = OllamaEmbeddings(model)

    vector_db = Chroma.from_texts(
        texts=chunks,
        embedding=embedding_fn,
        persist_directory=persist_directory,
    )
    vector_db.persist()
    return vector_db

# Main script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load Markdown and store in vector DB")
    parser.add_argument("md_path", help="Path to the Markdown file")
    args = parser.parse_args()
    md_path = args.md_path

    # Load Markdown file
    markdown_text = load_markdown(md_path)
    print(f"Loaded Markdown file. Length: {len(markdown_text)} characters")

    # Chunk the text
    chunks = chunk_text(markdown_text)
    print(f"Created {len(chunks)} chunks")

    # Store in vector DB
    vector_db = store_in_vector_db(chunks)
    print("Stored in vector database. Ready for retrieval!")