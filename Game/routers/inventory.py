from fastapi import APIRouter, Body, HTTPException, status
from models.inventory_models import ItemModel, InventoryModel
from utils.game_utils import add_item_to_inventory, remove_item_from_inventory, player_inventory

router = APIRouter()

@router.post("/add", response_model=InventoryModel)
async def add_item(item: ItemModel = Body(..., example={"name": "Sword"})):
    try:
        add_item_to_inventory(item.name)
        return InventoryModel(inventory=player_inventory)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/remove", response_model=InventoryModel)
async def remove_item(item: ItemModel = Body(..., example={"name": "Sword"})):
    try:
        remove_item_from_inventory(item.name)
        return InventoryModel(inventory=player_inventory)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))