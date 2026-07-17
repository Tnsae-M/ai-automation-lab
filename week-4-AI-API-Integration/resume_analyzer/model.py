from pydantic import BaseModel,Field
from typing import Literal,List
class Resume(BaseModel):
    resume_score: int=Field(ge=0, le=10, description="A score representing the quality of the resume, ranging from 0 to 10.")
    name: str=Field(description="The candidate's full name")
    target_job:str=Field(description="The type of job the candidate is applying for")
    languages: List[str]=Field(description="List of programming languages the candidate is proficient in.")
    projects:List[str]=Field(ge=0,le=4,description="List of projects the candidate has done.only top 3 needed.")
    strength: List[str]=Field(description="The candidate's key strengths")
    weakness: List[str]=Field(description="The candidate's key weaknesses")
    suggestion: List[str]=Field(description="Suggestions for improvement.")