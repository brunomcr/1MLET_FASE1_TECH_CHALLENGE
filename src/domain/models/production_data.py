from pydantic import BaseModel


class ProductionData(BaseModel):
    group: str
    product: str
    volume: str
    year: str

    def __repr__(self) -> str:
        return f"ProductionData(year={self.year}, group={self.group}, product={self.product}, volume={self.volume})"
