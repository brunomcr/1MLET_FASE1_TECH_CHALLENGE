from typing import List
from src.domain import ProductionData
from ..constants import *


class ProductionDataMapper:
    @staticmethod
    def map(data_list: List[dict]) -> List[ProductionData]:
        """
        Converts a list of dictionaries to a list of Production objects.

        Args:
            data_list (List[dict]): List of dictionaries containing production data.

        Returns:
            List[ProductionData]: A list of Production objects.
        """
        def convert(db_data) -> ProductionData:
            return ProductionData(year=db_data.get(COL_YEAR),
                                  group=db_data.get(COL_GROUP),
                                  product=db_data.get(COL_PRODUCT),
                                  volume=db_data.get(COL_VOLUME))
        try:
            return [convert(item) for item in data_list]
        except (ValueError, KeyError) as e:
            print(f"Error converting data: {e}")


