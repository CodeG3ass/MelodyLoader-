from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["General"])
async def root() -> dict[str, str]:
    return {"message": "Welcome to MelodyLoader API"}
