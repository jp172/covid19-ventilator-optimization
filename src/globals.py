from enum import Enum


UPDATE_CASES = ["normal_to_corona", "corona_leaves_hosp"]

CAPACITY_SCALAR = 0.25

TARGET_SCORE = 1e4


class ScoreWeight(Enum):
    WEIGHT_OVER_10 = 5
    WEIGHT_OVER_5 = 2
    WEIGHT_OVER_1 = 1


class Scenario(Enum):
    WORST = "worst"
    HIGH = "high"
    NORMAL = "normal"
