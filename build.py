"""script to build dataframe to be consumed by frontend"""

from typing import List

import pandas as pd  # type: ignore
from loguru import logger

from utils.membership import create_people_from_membership_list
from utils.participant import Participant
from utils.participants import get_participants
from utils.person import Person
from utils.race import Race
from utils.races import create_races
from utils.scoring import build_df, build_participation_snapshot

N = 6  # number of top races to use for overall score i.e. maximum score = N*100


def build_email_text(df: pd.DataFrame) -> str:
    df = df[["Individual", "Score", "Race", "Age Group"]]
    df_overall = (
        df.groupby(["Individual", "Age Group"])
        .agg({"Score": {lambda x: x.nlargest(N).sum()}})
        .sort_values(["Age Group", ("Score", "<lambda>")], ascending=[True, False])
    )
    df_overall.columns = df_overall.columns.get_level_values(0)
    df_overall.reset_index(inplace=True)
    age_groups = sorted(df_overall["Age Group"].unique())
    l: List[str] = []  # noqa
    for age_group in age_groups:
        dff = df_overall[df_overall["Age Group"] == age_group].head(3)[
            ["Individual", "Score"]
        ]
        s_by_age_group = f"{age_group}: "
        for row in dff.iterrows():
            individual = row[1].Individual
            score = row[1].Score
            s_by_age_group += f"{individual} ({score}) "
        l.append(s_by_age_group)
    return "\n".join(l)


def main() -> None:
    # setup
    people: List[Person] = create_people_from_membership_list()
    races: List[Race] = create_races()
    logger.info(
        f"BUILDING participants from {len(people)} people and {len(races)} races"
    )
    participants_for_scoring: List[Participant] = get_participants(
        people=people, races=races, for_scoring=True
    )  # participants in races for scoring
    participants_all: List[Participant] = get_participants(
        people=people, races=races, for_scoring=False
    )  # participants in any eligible race

    # build output_data tables
    # location: output_data/tables/df_YYYYMMDDHHMMSS.csv
    logger.info("BUILDING OUTPUT TABLE")
    df = build_df(participants=participants_for_scoring)  # does not filter top races

    # dump participant list
    # build output_data/participation/snapshot_YYYYMMDDHHMMSS.csv
    # build_participation_snapshot(participants=participants_all)
    logger.info("BUILDING PARTICIPATION SNAPSHOT")
    build_participation_snapshot(participants=participants_all)

    # logger text to copy pasta into email update with age group leaders
    logger.info(f"EMAIL TEXT\n{build_email_text(df)}")


if __name__ == "__main__":
    main()
