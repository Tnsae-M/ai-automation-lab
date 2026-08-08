import time
import json
from google import genai 
from google.genai import types,errors
from job_data_model import JobSummary
from config import gemini_key
client = genai.Client(
  api_key=gemini_key
)
SYSTEM_PROMPT="""You are a senior Job Analyst. You are tasked with summarizing job postings into a structured format.
You will be provided with job postings in JSON format. Your task is to extract the relevant information
and return it in a structured format as specified below. If any information is missing, you can leave the field as null."""
config=types.GenerateContentConfig(
     system_instruction=SYSTEM_PROMPT,
     response_schema=JobSummary,
     response_mime_type="application/json"
)
retryable_status_codes=[500,429,503,504]
max_attempt=5
def summarize_job(job_text:dict)->JobSummary|None:
    job=json.dumps(job_text,indent=0)
    for attempt in range(max_attempt):
        try:
            response=client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=f"Summerize this job: {job}",
                config=config
            )
            job_obj=JobSummary.model_validate_json(response.text)
            return job_obj
        except errors.APIError as e:
                print("Error code:",e.code)
                if attempt !=max_attempt-1 and e.code in retryable_status_codes:
                    time.sleep(2)
                else:
                    print(f"API error! Summarization falied due to {e}")
                    return None
        except Exception as e:
            print(f"Something went wrong: {e}")
            return None