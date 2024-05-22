from typing import Optional

from pydantic import BaseModel


class ProcessingData(BaseModel):
    cultivation: Optional[str] = None
    group: Optional[str] = None
    type: str
    weight: str
    year: str

    def __repr__(self) -> str:
        return f"ProcessingData(year={self.year}, group={self.group}, cultivation={self.cultivation}, weight={self.weight})"
