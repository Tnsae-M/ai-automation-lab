from google import genai
from google.genai import types
from pydantic import BaseModel
import sys
from config import gemini_key
from typing import List
client = genai.Client(
    api_key=gemini_key
)
class CompanyReport(BaseModel):
    company:str
    summary:str
    risk_level:str
    key_concerns:List[str]

search_tool=types.Tool(google_search=types.GoogleSearch())
config=types.GenerateContentConfig(tools=[search_tool])
try:
    grounded_response= client.models.generate_content(model="gemini-2.5-flash",
                                        contents="Give me a report about mercor AI Job finding platform for ethiopian native freelance aspiring individuals? use the latest information in a range of 2-3 weeks before today,july 8,2026, as a source.",
                                        config=config)
    print(grounded_response.text)
    print("Space between responses! \n \n")
    structured_response= client.models.generate_content(model="gemini-2.5-flash",
                                        contents=f"Extract structured data from this report:\n \n {grounded_response.text}",
                                        config=types.GenerateContentConfig(
                                            response_mime_type="application/json",
                                            response_schema=CompanyReport
                                        ))

    report=CompanyReport.model_validate_json(structured_response.text)
    print(report)
except Exception as ex:
    print(f"Something went wrong when calling API: {ex}")
    sys.exit(1)