from fastapi import HTTPException, Depends, APIRouter

from ..di import injector
from ...domain.interfaces.services import JWTTokenService


def get_jwt_service() -> JWTTokenService:
    return injector.get(JWTTokenService)


auth_router = APIRouter()


@auth_router.get("/auth/token", tags=["authentication"], response_model=dict, summary="Generate JWT token.")
async def generate_token(jwt_service: JWTTokenService = Depends(get_jwt_service)) -> dict:
    try:
        # This token is generated with dummy data. In real world, we should pass the user data here.
        token = await jwt_service.create_access_token(data={"fingerprint": "imlet-g43"})
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
