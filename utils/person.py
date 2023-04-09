"""Person Class"""

from datetime import datetime
from typing import Dict, List

from loguru import logger


def is_date_str(s) -> bool:
    """determine if we can construct a date from s"""
    if type(s) is not str:
        return False
    else:
        splits = [int(x) for x in s.split("/")]
        if len(splits) != 3:
            return False
        else:
            month, day, year = splits
            try:
                datetime(year, month, day)
                return True
            except Exception as e:
                return False


def is_row_valid(row: Dict) -> bool:
    """determine if we can construct a person from a row"""
    condition1 = all(x is not None for x in [row[x] for x in row.keys()])
    condition2 = is_date_str(row["DOB"])
    condition3 = is_date_str(row["Date"])
    # logger.debug(f"row={row}")
    # logger.debug(f"all values not none={condition1}")
    # logger.debug(f"DOB is a date={condition2}")
    # logger.debug(f"Date is a date={condition3}")
    return condition1 and condition2 and condition3


class Person:
    def __init__(
        self,
        *,
        first: str,
        last: str,
        dob_str: str,
        gender: str,
        date_str: str,
    ):
        self.first = first
        self.last = last
        self.dob_str = dob_str
        self.gender = gender
        self.date_str = date_str

    def name(self) -> str:
        """name of person"""
        return f"{self.first} {self.last}"

    def date_of_birth(self):
        """date of birth of person"""
        month, day, year = [int(x) for x in self.dob_str.split("/")]
        return datetime(year, month, day)

    def date_joined(self):
        """date the person joined UVRC"""
        month, day, year = [int(x) for x in self.date_str.split("/")]
        return datetime(year, month, day)

    def __eq__(self, other):
        if isinstance(other, Person):
            return (
                self.name() == other.name()
                and self.date_of_birth() == self.date_of_birth()
            )
        return False
