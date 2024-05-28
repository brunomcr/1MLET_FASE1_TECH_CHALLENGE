from pydantic import BaseModel


class ExportData(BaseModel):
    country: str
    type: str
    value: str
    weight: str
    year: str

    def __repr__(self) -> str:
        return f"ExportData(year={self.year}, type={self.type}, country={self.country}, weight={self.weight}, price={self.price})"

