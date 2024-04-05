from pydantic import BaseModel

class PalindromeRequest(BaseModel):
    text: str


class InterestRequest(BaseModel):
    principal: float
    rate: float
    time: int
