from pydantic import BaseModel

class InterestModel(BaseModel):
    principal: float
    rate: float
    time: int

class InterestResultModel(BaseModel):
    interest: float