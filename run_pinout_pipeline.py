import argparse
import subprocess
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()


def run_cmd(cmd, title):
    console.print(Panel.fit(f"[bold cyan]{title}[/bold cyan]\n[white]{' '.join(cmd)}[/white]", border_style="cyan"))
    subprocess.run(cmd, check=True)
    console.print(f"[bold green]Done:[/bold green] {title}\n")


def main():
    parser = argparse.ArgumentParser(description="Run PDF -> Markdown -> RAG -> pinout pipeline.")
    parser.add_argument("--pdf", required=True, help="Input PDF file")
    parser.add_argument("--md", required=True, help="Output Markdown file")
    parser.add_argument("--db-step-md", default=None, help="Markdown file to index into vector DB; defaults to --md")
    parser.add_argument("--query", required=True, help='Pinout query, e.g. "OPA4182 SOIC-14 pinout"')
    parser.add_argument("--part-number", required=True, help='Exact ordering code, e.g. "OPA4182D"')
    parser.add_argument("--output", required=True, help="Final pinout Markdown output file")
    parser.add_argument("--pdf-to-md-script", default="pdf_to_md_markitdown.py")
    parser.add_argument("--md-rag-script", default="md_rag.py")
    parser.add_argument("--pinout-script", default="pinout_wrapper.py")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    md_path = Path(args.md)
    db_md_path = Path(args.db_step_md) if args.db_step_md else md_path
    out_path = Path(args.output)

    console.print(Panel.fit("[bold magenta]Pinout Pipeline[/bold magenta]", border_style="magenta"))

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Preparing pipeline...", total=None)

        run_cmd([sys.executable, args.pdf_to_md_script, str(pdf_path), str(md_path)], "Convert PDF to Markdown")
        run_cmd([sys.executable, args.md_rag_script, str(db_md_path)], "Index Markdown in vector DB")
        run_cmd([
            sys.executable,
            args.pinout_script,
            args.query,
            "--part-number",
            args.part_number,
            "--output",
            str(out_path),
        ], "Extract pinout and write Markdown")

        progress.update(task, completed=1)

    console.print(Panel.fit(f"[bold green]Complete[/bold green]\nOutput: [white]{out_path}[/white]", border_style="green"))


if __name__ == "__main__":
    main()