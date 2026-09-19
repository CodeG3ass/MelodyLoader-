from fastapi import FastAPI

from app.api.router import router

app = FastAPI(
    title="MelodyLoader API",
    description="Backend API for MelodyLoader.",
    version="0.1.0",
)

app.include_router(router)
