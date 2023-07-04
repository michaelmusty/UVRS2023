"""
From the home directory of the repository run
```{shell}
python
input_data/race_data_raw/03_SkipsRun_4m_20230618/03_race_data_raw_to_race_data.py
```
"""

import csv
from typing import Dict, List, Tuple

import pandas as pd  # type: ignore
from loguru import logger

path_to_4m_raw = "input_data/race_data_raw/03_SkipsRun_4m_20230618/4m_raw.csv"


def _parse_skips_run_name(name: str) -> Tuple[str, str]:
    """
    X FIRST LAST -> (FIRST, LAST)
    """
    if len(name.split(" ")) == 3:
        x, first, last = name.split(" ")
        assert len(x) == 1
        return (first, last)
    elif len(name.split(" ")) == 2:
        first, last = name.split(" ")
        return (first, last)
    elif len(name.split(" ")) == 4:
        x, first, middle, last = name.split(" ")
        return (first, last)
    else:
        raise Exception(f"name {name} could not be parsed")


def _parse_skips_run_net_time(x: str) -> str:
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
            if row[0] == "Place":
                logger.info(f"skipping row: {row}")
                continue
            logger.info(f"parsing row: {row}")
            first = row[6]
            last = row[7]
            net = _parse_skips_run_net_time(row[4])
            d["First Name"].append(first)
            d["Last Name"].append(last)
            d["Net Time"].append(net)
    df = pd.DataFrame(d)
    logger.info(df)
    df.to_csv(f"input_data/race_data/03_SkipsRun_4m_20230618/{which_race}.csv")


def main():
    _process_path(path_to_4m_raw, "4m")


if __name__ == "__main__":
    main()
