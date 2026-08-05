import time
import json
from openai import OpenAI,RateLimitError,APIConnectionError,APITimeoutError
from job_data_model import JobSummary
from config import openai_key
client = OpenAI(
  api_key=openai_key
)
SYSTEM_PROMPT="""You are a senior Job Analyst. You are tasked with summarizing job postings into a structured format.
You will be provided with job postings in JSON format. Your task is to extract the relevant information
and return it in a structured format as specified below. If any information is missing, you can leave the field as null."""
def summarize_job(job_text:dict)->JobSummary|None:
    max_attempt=5
    job=json.dumps(job_text,indent=0)
    for attempt in range(max_attempt):
        try:
            response=client.responses.parse(
                model="gpt-5.4-mini",
                input=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content":job}
                ],
                text_format=JobSummary
            )
            return response.output_parsed
        except (RateLimitError,APIConnectionError,APITimeoutError) as e:
                if attempt !=max_attempt-1:
                    time.sleep(2)
                else:
                    print(f"Job summarzing failed! due to {e}")
                    return None
        except Exception as e:
            print(f"Failed to summarize job posting: {e}")
            return None