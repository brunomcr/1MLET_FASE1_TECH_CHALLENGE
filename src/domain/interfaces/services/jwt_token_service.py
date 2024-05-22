from abc import ABC, abstractmethod


class JWTTokenService(ABC):
    @abstractmethod
    async def create_access_token(self, data: dict) -> str:
        raise NotImplementedError
