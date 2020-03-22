from enum import Enum


class ScoreWeight(Enum):
    OVER_10 = 5
    OVER_5 = 2
    OVER_1 = 1


def evaluate(instance):
    print("the world is saved")
