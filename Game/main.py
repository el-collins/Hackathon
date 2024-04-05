from fastapi import FastAPI
from routers import inventory, explore

app = FastAPI(title="Adventure Game API")
# Include the routers for the adventure game API
app.include_router(inventory.router, prefix="/inventory", tags=["Player Inventory Management"])
app.include_router(explore.router, prefix="/explore", tags=["Exploring Locations"])