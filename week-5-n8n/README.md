# Week 5: n8n Lead Intake Automation

This folder contains a simple n8n-based workflow for receiving inbound leads, scoring them with an AI model, and routing the result to Telegram.

## Overview

The project demonstrates how to build a lightweight lead intake automation using n8n:

1. A webhook receives a lead submission.
2. An AI model evaluates the lead based on budget, authority, and urgency.
3. The workflow routes the lead to one of three outcomes: schedule a call, nurture, or disqualify.
4. A Telegram message is sent with the qualification result.

## Files in This Folder

- docker-compose.yml
  - Starts an n8n instance in Docker.
- Lead Intake Workflow v0.json
  - Import this workflow into n8n to activate the lead intake automation.

## Prerequisites

Before using this workflow, make sure you have:

- Docker and Docker Compose installed
- A running n8n instance
- An OpenAI API credential configured in n8n
- A Telegram bot credential configured in n8n
- A publicly reachable URL for your webhook (for example, via ngrok)

## Getting Started

### 1. Start n8n with Docker

From this folder, run:

```bash
docker compose up -d
```

Then open:

```text
http://localhost:5678
```

### 2. Update the webhook URL

In docker-compose.yml, replace the placeholder value in the WEBHOOK_URL environment variable with your public ngrok or tunnel URL:

```yaml
environment:
  - N8N_SECURE_COOKIE=false
  - WEBHOOK_URL=https://your-ngrok-url-here.ngrok-free.dev/
```

### 3. Import the workflow

In n8n:

- Open the dashboard
- Click Import from File
- Select Lead Intake Workflow v0.json
- Confirm the credentials and nodes are configured correctly

### 4. Configure credentials

Make sure the workflow has valid credentials for:

- OpenAI account
- Telegram account

### 5. Replace the Telegram chat ID

In the workflow, the Telegram node currently uses a placeholder chat ID:

```text
YOUR_CHATID_HERE
```

Replace this with the actual Telegram chat ID where the alert messages should be delivered.

## Workflow Behavior

The workflow expects an incoming JSON payload similar to:

```json
{
  "name": "John Smith",
  "company": "Acme Marketing",
  "email": "john@acme.com",
  "phone": "+1-555-123-4567",
  "website": "https://acme.com",
  "message": "We need AI automation for lead qualification and appointment booking. Budget around $8,000. We'd like to start this month."
}
```

The webhook path is configured as:

```text
/lead-intake
```

You can test it by sending a POST request to:

```text
https://your-public-url/lead-intake
```

## Example Response

On successful execution, the workflow returns:

```json
{
  "success": true,
  "message": "Lead intaked and routed to agent successfully."
}
```

## Customization Ideas

You can extend this workflow by:

- adding a CRM integration such as HubSpot or Airtable
- storing qualified leads in Google Sheets or a database
- changing the AI prompt to match your business rules
- routing leads to different Telegram channels or Slack alerts

## Notes

- The workflow is intended as a starter example and is not yet production-hardened.
- For local development, using a tunneling service such as ngrok is recommended so the webhook can be reached from n8n.
- Review the workflow nodes and prompts carefully before using it with real lead data.
