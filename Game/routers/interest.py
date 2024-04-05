from fastapi import APIRouter, Query
from models.interest_models import InterestModel, InterestResultModel
from utils.interest_utils import calculate_simple_interest

router = APIRouter()

@router.get("/", response_model=InterestResultModel)
async def simple_interest(principal: float = Query(...), rate: float = Query(...), time: int = Query(...)):
    interest = calculate_simple_interest(principal, rate, time)
    return InterestResultModel(interest=interest)