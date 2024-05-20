class ProcessingData:
    def __init__(
        self,
        year: str,
        group: str,
        cultivation: str,
        weight: str,
    ):
        self.year = year
        self.group = group
        self.cultivation = cultivation
        self.weight = weight

    def __repr__(self) -> str:
        return f"ProcessingData(year={self.year}, group={self.group}, cultivation={self.cultivation}, weight={self.weight})"
