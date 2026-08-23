from pydantic import BaseModel,Field
from typing import List
class LeadModel(BaseModel):
    name:str|None=None
    address:str|None=None
    phone:str|None=None
    website:str|None=None
    # enrichment fields
    email:List[str]|None=None
    social_links:List[str]|None=None
    about:str|None=Field(description="basic information about the buissness",default=None)
