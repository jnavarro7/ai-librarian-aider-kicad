import argparse
import subprocess
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()


def run_cmd(cmd, title, start_msg, done_msg):
    console.print(
        Panel.fit(
            f"[bold cyan]{title}[/bold cyan]\n[white]{' '.join(cmd)}[/white]",
            border_style="cyan",
        )
    )
    with console.status(f"[bold yellow]{start_msg}[/bold yellow]", spinner="dots"):
        subprocess.run(cmd, check=True)
    console.print(f"[bold green]✅[/bold green] {done_msg}\n")


def main():
    parser = argparse.ArgumentParser(description="Run PDF -> Markdown -> JSON/RAG -> symbol pipeline.")
    parser.add_argument("--pdf", required=True, help="Input PDF file")
    parser.add_argument("--md", required=True, help="Output Markdown file")
    parser.add_argument("--json", required=True, help="Output JSON file")
    parser.add_argument("--package", required=True, help='Package name, e.g. "28-pin SSOP"')
    parser.add_argument("--pin-count", type=int, required=True, help="Total number of pins this part has")
    parser.add_argument("--template", required=True, help="KiCad symbol template file")
    parser.add_argument("--out", required=True, help="Final KiCad symbol output file")

    parser.add_argument("--pdf-to-json-md-script", default="pdf_to_json_md.py")
    parser.add_argument("--json-md-rag-script", default="json_md_rag.py")
    parser.add_argument("--generate-symbol-script", default="generate_symbol.py")
    parser.add_argument("--validate", action="store_true", help="Run LLM validation after symbol generation")
    parser.add_argument("--validator-script", default="validate_symbol.py")
    parser.add_argument("--validator-model", default="qwen2.5-coder:14b-instruct-q4_K_M")

    parser.add_argument("--db-step-md", default=None, help="Markdown file to index; defaults to --md")
    parser.add_argument("--query", default=None, help="Optional query for the RAG step, if your script needs it")
    parser.add_argument("--part-number", default=None, help="Optional part number for generate_symbol.py")
    parser.add_argument("--verbose", default="no", choices=["no", "yes"], help="Enable debug messages in pdf_to_json_md.py")
    parser.add_argument("--model", default=None, help="LLM model to pass to pdf_to_json_md.py and generate_symbol.py")

    args = parser.parse_args()

    if args.pin_count <= 0:
        raise ValueError("--pin-count must be greater than 0")

    pdf_path = Path(args.pdf)
    md_path = Path(args.md)
    json_path = Path(args.json)
    db_md_path = Path(args.db_step_md) if args.db_step_md else md_path
    out_path = Path(args.out)

    console.print(Panel.fit("[bold magenta]Pinout Pipeline[/bold magenta]", border_style="magenta"))

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Starting...", total=None)

        progress.update(task, description="📄 Converting PDF to Markdown + JSON...")
        pdf_cmd = [
            sys.executable,
            args.pdf_to_json_md_script,
            str(pdf_path),
            "--verbose",
            args.verbose,
        ]
        if args.model:
            pdf_cmd.extend(["--model", args.model])

        run_cmd(
            pdf_cmd,
            "Convert PDF to Markdown + JSON",
            "Parsing PDF and extracting structured data...",
            "PDF converted to Markdown and JSON successfully.",
        )

        progress.update(task, description="🧠 Running Markdown/JSON RAG extraction...")
        run_cmd(
            [
                sys.executable,
                args.json_md_rag_script,
                str(db_md_path),
                "--json",
                str(json_path),
                "--package",
                args.package,
            ],
            "Run Markdown/JSON RAG extraction",
            "Indexing markdown and building retrieval database...",
            "Retrieval database built successfully.",
        )

        symbol_cmd = [
            sys.executable,
            args.generate_symbol_script,
            str(md_path),
            "--package",
            args.package,
            "--pin-count",
            str(args.pin_count),
            "--template",
            args.template,
            "--out",
            str(out_path),
        ]
        if args.model:
            symbol_cmd.extend(["--model", args.model])
        if args.part_number:
            symbol_cmd.extend(["--part-number", args.part_number])
        if args.validate:
            symbol_cmd.append("--validate")
            symbol_cmd.extend(["--validator-script", args.validator_script])
            symbol_cmd.extend(["--validator-model", args.validator_model])

        progress.update(task, description="🛠️ Generating KiCad symbol...")
        if args.validate:
            run_cmd(
                symbol_cmd,
                "Generate KiCad symbol + Validation",
                "Building symbol and validating output...",
                "KiCad symbol generated and validated successfully.",
            )
        else:
            run_cmd(
                symbol_cmd,
                "Generate KiCad symbol",
                "Building symbol output...",
                "KiCad symbol generated successfully.",
            )

        progress.update(task, completed=1)

    console.print(
        Panel.fit(
            f"[bold green]Complete[/bold green]\nOutput: [white]{out_path}[/white]",
            border_style="green",
        )
    )


if __name__ == "__main__":
    main()