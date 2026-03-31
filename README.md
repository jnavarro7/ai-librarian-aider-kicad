# ai-librarian-aider-kicad
AI librarian aider for KiCad

## Requirements
- Python 3.x.
- Ollama installed locally.
- An Ollama model pulled locally and available for inference.
- A local Ollama server running before using the pinout pipeline.

Example:

```bash
ollama serve
```

In another terminal, you may also want to verify that your model is available:

```bash
ollama list
```

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

2. Convert the PDF to Markdown.

```bash
python pdf_to_md_markitdown.py "<datasheet-file.pdf>" "<output.md>"
```

3. Add the Markdown file to the vector database.

```bash
python md_rag.py "<output.md>"
```

4. Test the vector database data (optional).

```bash
python query_vector_db_pin_extract.py "extract pinout of example part"
```

5. Get the pinout in Markdown format.

```bash
python pinout_wrapper.py "<PART> <PACKAGE> pinout" --part-number "<EXACT_ORDERING_CODE>" --output "<name>.md"
```

### OPA4182D example

```bash
python pdf_to_md_markitdown.py tmp/opa4182.pdf tmp/opa4182.md
python md_rag.py tmp/opa4182.md
python pinout_wrapper.py "OPA4182 SOIC-14 pinout" --part-number "OPA4182D" --output OPA4182_soic14_pinout.md
```

### Run the pipeline wrapper 

```bash
python pipeline_wrapper.py \
  --pdf tmp/infineon_psoc4.pdf \
  --md tmp/infineon_psoc4.md \
  --json tmp/infineon_psoc4.json \
  --package "28-pin SSOP" \
  --template templates/symbol_template.kicad_sym \
  --out output/psoc4.kicad_sym
```

![Pipeline wrapper demo](images/pipeline_wrapper.gif)