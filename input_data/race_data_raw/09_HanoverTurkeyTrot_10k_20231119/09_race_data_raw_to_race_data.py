"""
From the home directory of the repository run
```{shell}
python input_data/race_data_raw/09_HanoverTurkeyTrot_10k_20231119/09_race_data_raw_to_race_data.py
```
"""

import csv
from typing import Dict, List

import pandas as pd  # type: ignore
from loguru import logger

path_to_10k_raw = "input_data/race_data_raw/09_HanoverTurkeyTrot_10k_20231119/10k_raw.csv"
path_to_5k_raw = "input_data/race_data_raw/09_HanoverTurkeyTrot_10k_20231119/5k_raw.csv"


def _parse_net_time(x: str) -> str:
    """
    HH:MM:SS.xx -> HH:MM:SS
    MM:SS.xx -> 00:MM:SS
    """
    logger.info(f"{x} split on ':' {x.split(':')}")
    if len(x.split(":")) == 3:
        h, m, s = x.split(":")
        s = s.split(".")[0]
        return f"{h}:{m}:{s}"
    elif len(x.split(":")) == 2:
        m, s = x.split(":")
        s = s.split(".")[0]
        return f"00:{m}:{s}"
    else:
        raise Exception(f"cannot parse net time: {x}")


def _process_path(path: str, which_race: str):
    """
    takes raw race data and formats it to be consumed by the build script
    """
    d: Dict[str, List[str]] = {
        "First Name": [],
        "Last Name": [],
        "Net Time": [],
    }
    with open(path, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if row[0] == "Name":
                logger.info(f"skipping row: {row}")
                continue
            logger.info(f"parsing row: {row}")
            name = row[0]
            if len(name.split(" ")) != 2:
                logger.error(f"Investigate name: {name}")
            name_splits = name.split(" ")
            first = name_splits[0]
            last = name_splits[-1]
            net = _parse_net_time(row[1])
            d["First Name"].append(first)
            d["Last Name"].append(last)
            d["Net Time"].append(net)
    df = pd.DataFrame(d)
    logger.info(df)
    df.to_csv(f"input_data/race_data/09_HanoverTurkeyTrot_10k_20231119/{which_race}.csv")


def main():
    _process_path(path_to_10k_raw, "10k")
    _process_path(path_to_5k_raw, "5k")


if __name__ == "__main__":
    main()
