from typing import List
from src.domain import Production
from ..constants import *


class ProductionMapper:
    @staticmethod
    def map(data_list: List[dict]) -> List[Production]:
        """
        Converts a list of dictionaries to a list of Production objects.

        Args:
            data_list (List[dict]): List of dictionaries containing production data.

        Returns:
            List[Production]: A list of Production objects.
        """

        production_list = []
        for item in data_list:
            try:
                year = item.get(COL_YEAR)
                if not year:
                    raise ValueError("Year is missing")

                group = item.get(COL_GROUP)
                if not group:
                    raise ValueError("Group is missing")

                product = item.get(COL_PRODUCT)
                if not product:
                    raise ValueError("Product is missing")

                volume = item.get(COL_VOLUME, "0")
                if not volume:
                    raise ValueError("Volume is missing")

                production_list.append(
                    Production(year=year, group=group, product=product, volume=volume)
                )
            except (ValueError, KeyError) as e:
                print(f"Error converting data: {e}")

        return production_list


