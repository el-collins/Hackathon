from pydantic import BaseModel

class ItemModel(BaseModel):
    name: str

class InventoryModel(BaseModel):
    inventory: list[str]