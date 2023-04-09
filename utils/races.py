"""Utilities to help parse race data"""

import glob
import os
from typing import Dict, List

from loguru import logger

from utils.race import Race

PATH_TO_RACES = "input_data/race_data/"


def get_dirname(dirpath: str) -> str:
    """/a/b/c/d/ returns d"""
    split_str = dirpath.split("/")
    return split_str[-2]


def get_dirnames_and_dirpaths(path_to_dir: str) -> Dict[str, List[str]]:
    """returns directory names and absolute paths to those directories for a given path as a dict
    {
        'dirnames': List[str],
        'dirpaths': List[str]
    }
    """
    path = os.path.abspath(path_to_dir)  # absolute path without / at the end
    dirpaths = glob.glob(f"{path}/*/", recursive=True)
    return {"dirnames": [get_dirname(x) for x in dirpaths], "dirpaths": dirpaths}


def create_races() -> List[Race]:
    """builds a list of races (Race objects) from PATH_TO_RACES"""
    d = get_dirnames_and_dirpaths(PATH_TO_RACES)
    races: List[Race] = []
    assert len(d["dirnames"]) == len(d["dirpaths"])
    for i in range(len(d["dirnames"])):
        dirname = d["dirnames"][i]
        dirpath = d["dirpaths"][i]
        assert get_dirname(dirpath) == dirname
        races.append(Race(dirname=dirname, dirpath=dirpath))
    logger.info(f"created {len(races)} races from directories {d['dirnames']}")
    return races
