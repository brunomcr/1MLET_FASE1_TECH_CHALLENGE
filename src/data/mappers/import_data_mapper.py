from typing import List

from ..constants import *
from ...domain.models import ImportData


class ImportDataMapper:
    @staticmethod
    def map(data_list: List[dict]) -> List[ImportData]:
        """
        Converts a list of dictionaries to a list of Import objects.

        Args:
            data_list (List[dict]): List of dictionaries containing Import data.

        Returns:
            List[ImportData]: A list of Import objects.
        """
        def convert(db_data) -> ImportData:
            return ImportData(year=db_data.get(COL_YEAR),
                                  product=db_data.get(COL_PRODUCT),  
                                  country=db_data.get(COL_COUNTRY),
                                  weight=db_data.get(COL_WEIGHT),
                                  price=db_data.get(COL_PRICE))
        try:
            return [convert(item) for item in data_list]
        except (ValueError, KeyError) as e:
            print(f"Error converting data: {e}")

