from openai import OpenAI
from job_data_model import JobSummary
from config import openai_key
client = OpenAI(
  api_key=openai_key
)
SYSTEM_PROMPT="""You are a senior Job Analyst. You are tasked with summarizing job postings into a structured format.
You will be provided with job postings in JSON format. Your task is to extract the relevant information
and return it in a structured format as specified below. If any information is missing, you can leave the field as null."""
def summarize_job(job_text:str)->JobSummary:
    try:
        response=client.responses.parse(
            model="gpt-5.4-mini",
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Job posting data:\n\n{job_text}"}
            ],
            text_format=JobSummary
        )
        return response.output_parsed
    except Exception as e:
        print(f"Failed to summarize job posting: {e}")
        return None