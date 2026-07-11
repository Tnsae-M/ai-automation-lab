from openai import OpenAI
from lead_qualification_model import Lead
from data import data
from config import openai_key  # add this to your config.py

client = OpenAI(api_key=openai_key)

SYSTEM_PROMPT = """You are a strict B2B lead qualification analyst.
Score leads 0-10 based on explicit budget, decision authority, and timeline signals.
If budget_signal is 'no_budget' and score is 2 or below, next_action must be 'disqualify'.
here is an example of lead and output:
lead:
{
    "customer_name": "John Doe",
    "company_size": 500,
    "industry": "Manufacturing",
    "budget_signal": "no_budget",
    "decision_authority": "low",
    "timeline_signal": "long_term"
}
output:
{
    "customer_name": "John Doe",
    "score": 1,
    "intent": "low",
    "budget_signal": "no_budget",
    "next_action": "disqualify"
}
"""

for lead in data:
    try:
        response = client.responses.parse(
            model="gpt-5.4-mini",
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Lead data:\n\n{lead}"}
            ],
            text_format=Lead
        )
        lead_obj = response.output_parsed
        if lead_obj.score <= 2 and lead_obj.budget_signal == "no_budget":
            lead_obj.next_action = "disqualify"
            print(f"  [override] {lead_obj.customer_name}: forced disqualify")
        print(lead_obj)
    except Exception as e:
        print(f"Failed on {lead.get('full_name', 'unknown')}: {e}")