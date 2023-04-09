"""Racer class"""

from datetime import datetime, timedelta
from typing import List

import pandas as pd  # type: ignore
from loguru import logger

# from utils.race import Race


class Racer:
    def __init__(
        self,
        *,
        # race: Race,
        firstname: str,
        lastname: str,
        net_time_str: str,
    ):
        # self.race = race  # the race that the racer raced
        self.firstname = firstname
        self.lastname = lastname
        self.net_time_str = net_time_str  # net time as a string

    def get_name(self):
        """returns racers full name (fist and last)"""
        return f"{self.firstname} {self.lastname}"

    def get_net_time(self):
        """return net time as timedelta"""
        if len(self.net_time_str.split(".")) > 1:
            # logger.warn(f"{self.name()} has net time {self.net_time_str} with partial seconds for race {self.race}")
            logger.warn(
                f"{self.name()} has net time {self.net_time_str} with partial seconds"
            )
        dt_str = self.net_time_str.split(".")[0]
        assert len(dt_str.split(":")) == 3
        dt = datetime.strptime(dt_str, "%H:%M:%S")
        return timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second)
