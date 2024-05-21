class ImportData:
    def __init__(self, year: int, product: str, country: str, weight: str, price: float):
        self.year = year
        self.product = product
        self.country = country
        self.weight = weight
        self.price = price

    def __repr__(self) -> str:
        return f"ImportData(year={self.year}, product={self.product}, country={self.country}, weight={self.weight}, price={self.price})"

