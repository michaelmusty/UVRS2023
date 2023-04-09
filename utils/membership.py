"""Utilities to help parse club membership data"""

import csv
import glob
import os
from itertools import combinations
from math import comb
from typing import Dict, List

import pandas as pd  # type: ignore
from loguru import logger

from utils.person import Person, is_row_valid

PATH_TO_MEMBERSHIP = "input_data/rosters_private"


def get_latest_filename(path_to_dir: str) -> str:
    """returns filename of latest file in a directory with specified path"""
    path = os.path.abspath(path_to_dir)  # absolute path without / at the end
    list_of_filenames = glob.glob(f"{path}/*")
    return max(list_of_filenames, key=os.path.getctime)


# FIXME: this depends on how dates are formatted
def _format_date(x: str) -> str:
    """
    YYYY-MM-DD HH:MM:SS -> MM/DD/YYYY
    OR
    another format -> MM/DD/YYYY
    """
    # parse other formats and redefine x
    dt = pd.to_datetime(x)
    logger.info(f"x_start = {x}")
    x = str(dt.date())
    logger.info(f"{x=}")
    # x is now a string of the form YYYY-MM-DD (isoformat)
    y, m, d = x.split("-")
    # sanity checks
    assert len(y) == 4
    assert int(y) in [2017, 2018, 2019, 2020, 2021, 2022, 2023]
    assert len(m) == 2
    assert int(m) in range(1, 13)
    assert len(d) == 2
    assert int(d) in range(1, 32)
    return f"{m}/{d}/{y}"


def _verify_raw_row(row: List[str]) -> bool:
    if len(row) != 9:
        return False
    if row[0] == "First Name" or row[1] == "Last Name":
        return False
    first = row[0] != ""
    last = row[1] != ""
    dob = row[2] != ""
    gender = row[3] != ""
    date = row[8] != ""
    return first and last and dob and gender and date


def get_latest_membership() -> pd.DataFrame:
    """returns membership list as pandas dataframe with a subset of (nonprivate) columns"""
    d: Dict[str, List[str]] = {
        "First": [],
        "Last": [],
        "DOB": [],
        "Gender": [],
        "Date": [],
    }
    csv_latest = get_latest_filename(PATH_TO_MEMBERSHIP)
    logger.info(f"latest membership list located at {csv_latest}")
    with open(csv_latest, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if _verify_raw_row(
                row
            ):  # FIXME: this all depends on the schema of the leb rec membership csv
                logger.info(
                    f"Adding row to membership data: {row}\n{row[0]} : {row[1]} : {row[2]} : {row[3]} : {row[8]}"
                )
                d["First"].append(row[0])
                d["Last"].append(row[1])
                d["DOB"].append(row[2])
                d["Gender"].append(row[3])
                d["Date"].append(_format_date(row[8]))
            else:
                logger.info(f"No data, skipping: {row}")
    df = pd.DataFrame(d)
    logger.info(df)
    return df
    # below is previous method that fails on some csvs
    # df = pd.read_csv(get_latest_filename(path_to_dir=PATH_TO_MEMBERSHIP))
    # df = df[["First", "Last", "DOB", "Gender", "Date"]]
    # return df.dropna(how="all")


def create_people_from_membership_list() -> List[Person]:
    """builds a list of people (Person objects) from most recent membership list"""
    df = get_latest_membership()  # most recent membership data
    people: List[Person] = []  # a list of people
    for i, row in df.iterrows():
        logger.info(f"building data for row {i} out of {df.shape[0]} rows:\n{row}")
        row = row.to_dict()
        if is_row_valid(row):
            person = Person(
                first=row["First"],
                last=row["Last"],
                dob_str=row["DOB"],
                gender=row["Gender"],
                date_str=row["Date"],
            )
            people.append(person)
            # logger.info(f"Person built for row {i}: {person}")
        # else:
        #     logger.info(f"Person could not be built for row {i}")
    logger.info(f"Created {len(people)} people")
    # dedup
    for p1, p2 in combinations(people, 2):
        if p1 == p2:
            people.remove(p1)
    logger.info(f"After dedup we have {len(people)} people")
    return list(people)
