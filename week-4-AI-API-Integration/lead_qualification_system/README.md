# Lead Qualification System

This project demonstrates how to use AI to qualify leads automatically from a sample dataset. It sends each lead entry to the Gemini API, evaluates the lead based on budget, decision authority, and urgency signals, and returns a structured qualification result.

## Overview

The system is designed as a simple, practical example of AI-assisted sales qualification. It uses:

- Python for orchestration
- Pydantic models for structured output
- Google Gemini for lead analysis
- A sample lead dataset for testing and demonstration

## What the system does

For each lead in the sample dataset, the application:

1. Reads the lead details from the dataset
2. Sends the lead to the Gemini model for analysis
3. Produces a structured qualification result with:
   - a score from 0 to 10
   - an intent level
   - a budget signal
   - a recommended next action

## Project structure

- config.py - Loads environment variables and validates API keys
- data.py - Contains sample lead records for qualification
- lead_qualification_model.py - Defines the Pydantic schema for the AI output
- service.py - Sends the leads to the Gemini API and prints the qualification results

## Prerequisites

Make sure you have Python 3.9+ installed.

## Installation

Install the required packages:

```bash
pip install python-dotenv google-genai pydantic
```

## Environment setup

Create a .env file in this folder and add your API keys:

```env
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
```

## Running the project

From this folder, run:

```bash
python service.py
```

The script will process the sample leads and print each qualification result to the terminal.

## Example output

The output includes structured information such as:

```text
customer_name: Abel Tesfaye
score: 8
intent: high
budget_signal: has_budget
next_action: book_call
```

## Notes

- This is a learning-focused example and uses a small sample dataset.
- The current implementation is a one-off script that processes leads and prints results.
- You can extend it later to save results to CSV, JSON, a database, or a CRM integration.

## Future improvements

Possible enhancements include:

- Saving qualified leads to a file or database
- Adding a web interface or API endpoint
- Supporting bulk lead uploads
- Integrating with a CRM tool such as HubSpot or Salesforce
