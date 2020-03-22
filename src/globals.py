from enum import Enum


UPDATE_CASES = ["normal_to_corona", "corona_leaves_hosp"]

CAPACITY_SCALAR = 0.25

TARGET_SCORE = 1e4

TIMESTEP = 50

BED_UPDATE_PROB = 10

NUMBER_FREE_BEDS = 25

NUMBER_CORONA_BEDS = 5

NUMBER_FREE_CORONA_BEDS = 3

NUMBER_CORONA_PAT_IN_NORMAL_BED = 1


class ScoreWeight(Enum):
    HIGH = 5
    MIDDLE = 2
    LOW = 1
