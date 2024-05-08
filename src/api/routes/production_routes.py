from fastapi import APIRouter, Path
from src.dependencies import get_production_service
from src.domain.responses import GetProductionByYearResponse


production_service = get_production_service()
production_router = APIRouter()


@production_router.get("/production/{year}")
async def get_production_by_year(year: int = Path(None, description="Year: [1970-2022]")) -> GetProductionByYearResponse:
    return await production_service.get_production_by_year(year)
