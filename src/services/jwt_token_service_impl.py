import os
from datetime import timedelta, datetime, UTC
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import encode, decode, ExpiredSignatureError, PyJWTError

from ..domain.interfaces.services import JWTTokenService


SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = os.getenv('JWT_ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('JWT_TOKEN_EXPIRE_MINUTES'))


class JWTTokenServiceImpl(JWTTokenService):
    async def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(UTC) + timedelta(minutes=15)
        to_encode.update({'exp': expire})
        return encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if credentials.scheme.lower() != 'bearer':
                raise HTTPException(status_code=403, detail='Invalid authentication scheme.')
            if not self.__verify_token(credentials.credentials):
                raise HTTPException(status_code=403, detail='Invalid token or expired token.')
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail='Invalid authorization credentials')

    def __verify_token(self, token: str) -> bool:
        try:
            payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token has expired')
        except PyJWTError:
            raise HTTPException(status_code=401, detail='Token is invalid or expired')
        return payload and payload.get('fingerprint') == 'imlet-g43'
