"""Participant Class"""

from datetime import date, datetime, timedelta
from typing import Dict, List

from loguru import logger

from utils.person import Person
from utils.race import Race
from utils.racer import Racer


class Participant:
    def __init__(
        self,
        *,
        person: Person,
        races: List[Race],  # list of races person participated in
        racers: List[
            Racer
        ],  # list of racers corresponding to the person in each race that person ran
    ):
        self.person = person
        if len(races) > 0:
            self.races = races
        else:
            raise Exception(
                f"a participant cannot be created unless number of races participated in is > 0"
            )
        if len(racers) > 0:
            assert len(racers) == len(races)
            self.racers = racers
        else:
            raise Exception(
                f"a participant cannot be created unless number of of corresponding racers is > 0"
            )

    def age_group(self) -> str:
        """compute age group of participant based on age of self.person at first race in races"""
        assert len(self.races) > 0
        race_dates = [race.get_datetime() for race in self.races]
        return compute_age_group(
            date_of_birth=self.person.date_of_birth(),
            race_date=min(race_dates),
            gender=standardize_gender(self.person.gender),
        )

    def get_corresponding_racer(self, *, race: Race) -> Racer:
        """returns racer corresponding to given race"""
        ind = self.races.index(race)
        return self.racers[ind]


def standardize_gender(gender: str) -> str:
    """F for female and M for male"""
    if gender in ["f", "female", "Female", "F"]:
        return "F"
    elif gender in ["m", "male", "Male", "M"]:
        return "M"
    else:
        raise Exception(f"gender {gender} not recognized")


def compute_age_group(date_of_birth: date, race_date: date, gender: str) -> str:
    """compute age group of individual with given date_of_birth at the time of race_date"""
    assert gender in ["F", "M"]
    age = (
        race_date.year
        - date_of_birth.year
        - ((race_date.month, race_date.day) < (date_of_birth.month, date_of_birth.day))
    )
    assert age > 0
    if age <= 29:
        return f"{gender}029"
    elif age <= 39:
        return f"{gender}3039"
    elif age <= 49:
        return f"{gender}4049"
    elif age <= 59:
        return f"{gender}5059"
    elif age <= 69:
        return f"{gender}6069"
    elif age <= 69:
        return f"{gender}6069"
    elif age <= 120:
        return f"{gender}70+"
    else:
        raise Exception(
            f"is there really someone older than 120 year in the race results?"
        )
