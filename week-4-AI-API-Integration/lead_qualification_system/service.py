from google import genai
from config import gemini_key
from google.genai import types
from lead_qualification_model import Lead
from data import data
client=genai.Client(
    api_key=gemini_key
)
for lead in data:
        try:
            lead_qualifier=client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=f"Analyze the leads inside listed below and qualify them: \n\n {lead}"
            )
            qualified_leads=client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=f"extract a lead qualifications structured data from this analysis:\n\n{lead_qualifier.text}",
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=Lead
                )
            )
            lead_obj=Lead.model_validate_json(qualified_leads.text)
            if lead_obj.score<=2 and lead_obj.budget_signal=="no_budget":
                lead_obj.next_action="disqualify"
                print(f"  [override] {lead_obj.customer_name}: forced disqualify")
            print(lead_obj)
        except Exception as e:
            print(f"Failed on {lead.get('full_name','unknown')}: {e}")