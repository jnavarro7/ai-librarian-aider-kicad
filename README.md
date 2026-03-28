# ai-librarian-aider-kicad
AI librarian aider for KiCad

## Setup Python virtual environment

1. Navigate to the project directory:

```bash
cd ai-librarian-aider-kicad
```

2. Make setup script executable (one-time):

```bash
chmod +x setup_venv.sh
```

3. Run setup script (default env: `.venv`):

```bash
./setup_venv.sh
```

4. Activate virtual environment:

```bash
source .venv/bin/activate
```

5. Confirm installed packages:

```bash
pip list
```

6. Run your script:

```bash
python pdf_to_md_rag.py
```

### Optional

- Custom env folder:

```bash
./setup_venv.sh myenv
source myenv/bin/activate
```

## Process

1. Get a part datasheet in PDF format. 
2. Convert PDF to Markdown
    python pdf_to_md_markitdown.py "datasheet path"
3. Add .md to vector database (RAG)
    python md_rag.py ".md file path"
4. Test vector DB
    python query_vector_db_pin_extract.py "extract pinout of example part"

