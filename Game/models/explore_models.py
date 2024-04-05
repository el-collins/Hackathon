from pydantic import BaseModel

class LocationModel(BaseModel):
    name: str

class LocationDetailsModel(BaseModel):
    name: str
    description: str
    items: list[str]