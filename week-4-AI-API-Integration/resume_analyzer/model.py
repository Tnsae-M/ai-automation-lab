from pydantic import BaseModel,Field
from typing import Literal,List
class Resume(BaseModel):
    resume_score: int=Field(ge=0, le=10, description="A score representing the quality of the resume, ranging from 0 to 10.")
    name: str=Field(description="The candidate's full name")
    target_job:str=Field(description="The type of job the candidate is applying for")
    languages: List[str]=Field(description="List of programming languages the candidate is proficient in.")
    projects:List[str]=Field(max_length=3 , description="List of projects the candidate has done. Choose the top 3")
    strength: List[str]=Field(description="The candidate's key strengths")
    weakness: List[str]=Field(description="The candidate's key weaknesses")
    suggestion:List[str]=Field(description="The actions/steps/methods the candidate can do to improve.")
    job_readiness_verdict: List[str]=Field(description="A final say on wheather this candidate is really ready for the job market. either international freelance, or remote work market, or local work")