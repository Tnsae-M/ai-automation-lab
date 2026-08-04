from pydantic import BaseModel,Field


class JobSummary(BaseModel):
    title: str
    company: str|None=None
    job_type: str|None=None
    experience_level:str|None=None
    location: str|None=None
    summary: str=Field(..., description="A brief summary of the job posting")