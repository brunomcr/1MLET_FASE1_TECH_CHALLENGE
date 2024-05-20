from typing import List
from src.domain import ProcessingData
from ..constants import *


class ProcessingDataMapper:
    @staticmethod
    def map(data_list: List[dict]) -> List[ProcessingData]:
        """
        Converts a list of dictionaries to a list of Processing objects.

        Args:
            data_list (List[dict]): List of dictionaries containing processing data.

        Returns:
            List[ProcessingData]: A list of Processing objects.
        """
        def convert(db_data) -> ProcessingData:
            return ProcessingData(year=db_data.get(COL_YEAR),
                                  group=db_data.get(COL_GROUP),
                                  cultivation=db_data.get(COL_CULTIVATION),
                                  weight=db_data.get(COL_WEIGHT))
        try:
            return [convert(item) for item in data_list]
        except (ValueError, KeyError) as e:
            print(f"Error converting data: {e}")


