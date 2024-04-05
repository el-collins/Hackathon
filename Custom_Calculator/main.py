from fastapi import FastAPI
from router import router

app = FastAPI(title="Custom Calculator API")

app.include_router(router)

