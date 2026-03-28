#!/usr/bin/env python3
"""
PDF to Markdown Converter using MarkItDown

This script converts PDF files to Markdown format using the MarkItDown library.
"""

import sys
import os
from markitdown import MarkItDown
from pypdf import PdfReader
from langchain_ollama import OllamaLLM


def convert_pdf_to_md(input_pdf_path, output_md_path):
    """
    Convert a PDF file to Markdown format.

    Args:
        input_pdf_path (str): Path to the input PDF file
        output_md_path (str): Path to the output Markdown file

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_pdf_path):
            print(f"Error: Input file '{input_pdf_path}' does not exist.")
            return False

        # Initialize MarkItDown
        md = MarkItDown()

        # Convert PDF to Markdown
        result = md.convert(input_pdf_path)

        # Write the result to output file
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(result.text_content)

        print(f"Successfully converted '{input_pdf_path}' to '{output_md_path}'")
        return True

    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False


def validate_md_file(md_path):
    """
    Perform basic validation on the output Markdown file.

    Args:
        md_path (str): Path to the Markdown file

    Returns:
        bool: True if validation passes, False otherwise
    """
    try:
        if not os.path.exists(md_path):
            print(f"Validation failed: Output file '{md_path}' does not exist.")
            return False

        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.strip():
            print("Validation failed: Output file is empty.")
            return False

        # Basic check for markdown content (look for headers or lists)
        if not any(char in content for char in ['#', '-', '*', '1.']):
            print("Validation failed: Output does not appear to be valid Markdown.")
            return False

        print(f"Validation passed for '{md_path}'")
        return True

    except Exception as e:
        print(f"Validation error: {str(e)}")
        return False


def summarize_first_page_with_ollama(pdf_path):
    """
    Extract text from the first page of the PDF and summarize it using Ollama with llama3.2.

    Args:
        pdf_path (str): Path to the PDF file

    Returns:
        str: Summary of the first page, or None if failed
    """
    try:
        # Extract text from first page
        reader = PdfReader(pdf_path)
        if len(reader.pages) == 0:
            print("No pages found in PDF.")
            return None

        first_page_text = reader.pages[0].extract_text()
        if not first_page_text.strip():
            print("No text found on first page.")
            return None

        # Initialize Ollama LLM
        llm = OllamaLLM(model="llama3.2")

        # Create prompt for summarization
        prompt = f"Summarize the following text from the first page of a datasheet:\n\n{first_page_text}\n\nSummary:"

        # Get summary
        summary = llm.invoke(prompt)
        return summary.strip()

    except Exception as e:
        print(f"Error during summarization: {str(e)}")
        return None


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_md_markitdown.py <input.pdf> <output.md>")
        print("Example: python pdf_to_md_markitdown.py datasheet.pdf datasheet.md")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_md = sys.argv[2]

    success = convert_pdf_to_md(input_pdf, output_md)
    if success:
        # Validate the output
        if validate_md_file(output_md):
            # Summarize the first page
            summary = summarize_first_page_with_ollama(input_pdf)
            if summary:
                print(f"\nFirst Page Summary:\n{summary}")
            else:
                print("Failed to generate summary.")
        else:
            print("Validation failed.")
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()