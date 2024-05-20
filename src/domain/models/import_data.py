class ImportData:
    def __init__(self, year: int, country: str, quantity: int, value: float):
        self.year = year
        self.country = country
        self.quantity = quantity
        self.value = value

    def __repr__(self) -> str:
        return f"ImportData(year={self.year}, country={self.country}, quantity={self.quantity}, value={self.value})"
