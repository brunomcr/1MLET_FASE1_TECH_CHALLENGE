class Production:
    def __init__(
        self,
        year: str,
        group: str,
        product: str,
        volume: str,  # volume agora é uma string
    ):
        self.year = year
        self.group = group
        self.product = product
        self.volume = volume

    @property
    def year(self) -> str:
        return self._year

    @year.setter
    def year(self, value: str):
        if not value:
            raise ValueError("Year cannot be empty")
        self._year = value

    @property
    def group(self) -> str:
        return self._group

    @group.setter
    def group(self, value: str):
        if not value:
            raise ValueError("Group cannot be empty")
        self._group = value

    @property
    def product(self) -> str:
        return self._product

    @product.setter
    def product(self, value: str):
        if not value:
            raise ValueError("Product cannot be empty")
        self._product = value

    @property
    def volume(self) -> str:
        return self._volume

    @volume.setter
    def volume(self, value: str):
        if not value:
            raise ValueError("Volume cannot be empty")
        self._volume = value

    def __repr__(self) -> str:
        return f"Production(year={self.year}, group={self.group}, product={self.product}, volume={self.volume})"
