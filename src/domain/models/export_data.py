from pydantic import BaseModel


class ExportData(BaseModel):
    country: str
    quantity: str
    type: str
    value: str
    year: str

    def __repr__(self) -> str:
        return f"ExportData(year={self.year}, country={self.country}, quantity={self.quantity}, value={self.value})"
