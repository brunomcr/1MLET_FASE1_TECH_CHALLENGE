from fastapi import APIRouter

root_router = APIRouter()

@root_router.get("/", tags=["Root"])
async def root():
    return {"message": "Hello 1MLET - Grupo 43"}
