from pydantic import BaseModel


class ImportData(BaseModel):
    country: str
    type: str
    value: str
    weight: str
    year: str

    def __repr__(self) -> str:
        return f"ImportData(year={self.year}, type={self.type}, country={self.country}, weight={self.weight}, price={self.price})"

