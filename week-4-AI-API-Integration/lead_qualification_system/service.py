from google import genai
from config import gemini_key
from google.genai import types
from lead_qualification_model import Lead
from data import data
client=genai.Client(
    api_key=gemini_key
)
SYSTEM_PROMPT = """You are a strict B2B lead qualification analyst.
Score leads 0-10 based on explicit budget, decision authority, and timeline signals.
If budget_signal is 'no_budget' and score is 2 or below, next_action must be 'disqualify'."""
config=types.GenerateContentConfig(
     system_instruction=SYSTEM_PROMPT,
     response_mime_type="application/json",
                    response_schema=Lead
)
for lead in data:
        try:
            lead_qualifier=client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=f"Analyze the leads inside listed below and qualify them. \n\n Lead Data:\n\n{lead}",
                config=config
            )
            lead_obj=Lead.model_validate_json(lead_qualifier.text)
            if lead_obj.score<=2 and lead_obj.budget_signal=="no_budget":
                lead_obj.next_action="disqualify"
                print(f"  [override] {lead_obj.customer_name}: forced disqualify")
            print(lead_obj)
        except Exception as e:
            print(f"Failed on {lead.get('full_name','unknown')}: {e}")