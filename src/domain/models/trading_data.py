class TradingData:
    def __init__(
        self,
        year: str,
        group: str,
        product: str,
        volume: str,
    ):
        self.year = year
        self.group = group
        self.product = product
        self.volume = volume

    def __repr__(self) -> str:
        return f"TradingData(year={self.year}, group={self.group}, product={self.product}, volume={self.volume})"