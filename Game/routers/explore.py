from fastapi import APIRouter, Path, HTTPException, status
from models.explore_models import LocationModel, LocationDetailsModel
from utils.game_utils import game_locations

router = APIRouter()

@router.get("/{location_name}", response_model=LocationDetailsModel)
async def explore_location(location_name: str = Path(...)):
    location = game_locations.get(location_name)
    if not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Location not found.")
    return LocationDetailsModel(name=location_name, description=location["description"], items=location["items"])