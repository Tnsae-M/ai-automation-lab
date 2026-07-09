from pydantic import BaseModel,Field
from typing import Literal
class Lead(BaseModel):
    customer_name:str
    score:int=Field(ge=0,le=10)
    intent:Literal["high","medium","low"]
    budget_signal:Literal["has_budget","unclear","no_budget"]
    next_action: Literal["book_call","disqualify","nurture_emails"]