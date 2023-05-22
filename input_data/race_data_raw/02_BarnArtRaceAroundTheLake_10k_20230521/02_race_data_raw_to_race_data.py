"""
From the home directory of the repository run
```{shell}
python
input_data/race_data_raw/02_BarnArtRaceAroundTheLake_10k_20230521/02_race_data_raw_to_race_data.py
```
"""

import csv
from typing import Dict, List, Tuple

import pandas as pd  # type: ignore
from loguru import logger

path_to_5k_raw = (
    "input_data/race_data_raw/02_BarnArtRaceAroundTheLake_10k_20230521/5k_raw.csv"
)
path_to_10k_raw = (
    "input_data/race_data_raw/02_BarnArtRaceAroundTheLake_10k_20230521/10k_raw.csv"
)


def _parse_barn_art_name(name: str) -> Tuple[str, str]:
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


def _parse_barn_art_net_time(x: str) -> str:
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
            if row[1] == "Place":
                logger.info(f"skipping row: {row}")
                continue
            logger.info(f"parsing row: {row}")
            first, last = _parse_barn_art_name(row[3])
            logger.info(f"row[9] = {row[9]} | {type(row[9])}")
            net = _parse_barn_art_net_time(row[9])
            d["First Name"].append(first)
            d["Last Name"].append(last)
            d["Net Time"].append(net)
    df = pd.DataFrame(d)
    logger.info(df)
    df.to_csv(
        f"input_data/race_data/02_BarnArtRaceAroundTheLake_10k_20230521/{which_race}.csv"
    )


def main():
    _process_path(path_to_5k_raw, "5k")
    _process_path(path_to_10k_raw, "10k")


if __name__ == "__main__":
    main()
