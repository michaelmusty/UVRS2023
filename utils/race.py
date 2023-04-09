"""Race Class"""

import glob
from datetime import datetime
from typing import Any, Dict, List

import pandas as pd  # type: ignore
from loguru import logger

from utils.racer import Racer


class Race:
    def __init__(
        self,
        *,
        dirname: str,
        dirpath: str,
    ):
        self.dirname = dirname  # of the form 03_RaceName_10k_YYYYMMDD
        self.dirpath = dirpath  # absolute path to race csvs

    def get_index(self) -> int:
        """returns index of race 01, 02, 03, etc"""
        return int(self.dirname.split("_")[0])

    def get_index_as_str(self) -> str:
        """returns index of race 01, 02, 03, etc as a string instead of an int"""
        return self.dirname.split("_")[0]

    def get_name(self) -> str:
        """returns name of race CamelCase"""
        return self.dirname.split("_")[1]

    def get_race_distance_used_for_scoring(self) -> str:
        """returns race distance used for scoring from the dirname"""
        return self.dirname.split("_")[2]

    def get_full_name(self) -> str:
        """returns 02_RaceName"""
        # return f"{self.get_index_as_str()}_{self.get_name()}_{self.get_race_distance_used_for_scoring()}"
        return f"{self.get_index_as_str()}_{self.get_name()}"

    def get_datetime_str(self) -> str:
        """returns datetime of race as string"""
        return self.dirname.split("_")[3]

    def get_datetime(self):
        """returns datetime of race as date"""
        dt_str = self.get_datetime_str()
        dt = datetime.strptime(dt_str, "%Y%m%d")
        return dt.date()

    def get_distances(self) -> List[str]:
        """returns race distances for self based on filenames"""
        data_paths = glob.glob(f"{self.dirpath}*.csv")
        distances: List[str] = []
        for data_path in data_paths:
            filename = data_path.split("/")[-1]
            a, b = filename.split(".")
            assert b == "csv"
            assert a in ["5k", "10k", "12k", "7m"]
            distances.append(a)
        return distances

    def get_dataframes(self) -> Dict[str, List[Racer]]:
        """returns pandas dataframes from csvs located in self.dirpath as a dict of the form
        {
            race_distance_1: df_1,
            race_distance_1: df_2,
            ...
        }
        """
        race_distances = self.get_distances()
        data_paths = glob.glob(f"{self.dirpath}*.csv")
        dfs = [pd.read_csv(data_path) for data_path in data_paths]
        assert len(race_distances) == len(dfs)
        return {race_distances[i]: dfs[i] for i in range(len(dfs))}

    def get_racers(self) -> Dict[str, List[Racer]]:
        """returns a dict of racers (Racer objects) for self of the form
        {
            'race_distance_1': List[Racer],
            'race_distance_2': List[Racer],
            ...
        }
        """
        dfs: Dict[str, Any] = self.get_dataframes()
        d: Dict[str, List[Racer]] = {}  # the dict we want to return
        for k in dfs.keys():  # keys are race distances
            df = dfs[k]
            racers: List[Racer] = []
            for i, row in df.iterrows():
                row = row.to_dict()
                if is_valid_row(row):
                    racer = Racer(
                        firstname=row["First Name"],
                        lastname=row["Last Name"],
                        net_time_str=row["Net Time"],
                    )
                    racers.append(racer)
            d[k] = racers
        return d


def is_valid_row(row: Dict) -> bool:
    """determine if we can construct a racer from a row"""
    condition1 = len(row["Net Time"].split(":")) == 3
    condition2 = row["First Name"] is not None
    condition3 = row["Last Name"] is not None
    return condition1 and condition2 and condition3
