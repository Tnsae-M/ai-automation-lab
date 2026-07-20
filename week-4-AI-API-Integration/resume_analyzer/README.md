# Resume Analyzer

A Python-based resume evaluation tool that uses the OpenAI API to analyze uploaded resumes and generate a structured assessment. The system reads resume files, extracts relevant details, and returns a professional summary covering candidate identity, target role, resume score, strengths, weaknesses, improvement suggestions, and job-readiness feedback.

## Overview

This project demonstrates how AI can be used to assist with resume screening and professional feedback. It is designed for experimentation, learning, and extension into broader HR or recruitment workflows.

## Features

- Reads resumes from plain text and PDF files
- Sends resume content to an OpenAI model for analysis
- Returns structured output using a Pydantic schema
- Prints a clear terminal report with key evaluation insights
- Includes sample resumes for testing and demonstration

## Project Structure

- `main.py` — entry point that loads resumes from the input folder and runs the analysis
- `analyze_resume.py` — handles the OpenAI request and parses the structured result
- `model.py` — defines the schema for the resume analysis output
- `reader.py` — reads `.txt` and `.pdf` resume files
- `config.py` — loads the OpenAI API key from environment variables
- `input/` — sample resumes used by the project

## Prerequisites

- Python 3.9 or higher
- An OpenAI API key

## Installation

1. Clone the repository and navigate to the project folder.
2. Install the required dependencies:

```bash
pip install openai pydantic pypdf python-dotenv
```

3. Create a `.env` file in the project directory and add your API key:

```env
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the analyzer from the project folder:

```bash
python main.py
```

The script will scan the sample resumes in the input directory and print the analysis results to the terminal.

## Example Output

The generated report includes:

- candidate name
- target job title
- resume score
- programming languages identified
- notable projects
- strengths and weaknesses
- improvement suggestions
- job-readiness verdict

## Notes

- The application currently expects a valid OpenAI API key to be available in the environment.
- The default workflow processes the sample files in the input directory.
- This project can be expanded to save results as JSON, CSV, or to support a web interface.
