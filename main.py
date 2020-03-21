import argparse

from enum import Enum

from src.solve import solve
from src.visualize import visualize
from src.schedulers.simple_scheduler import SimpleScheduler


class Scenario(Enum):
    WORST = "worst"
    HIGH = "high"
    NORMAL = "normal"


# this main file should just run a simulation given the following data.
# it should parse the following input specs nicely as arguments


def main(args):

    if args.scenario not in [s.value for s in Scenario]:
        raise ValueError

    hospital_data = "data/hospitals/hospitals.json"
    request_data = "data/patient_requests/patients.json"

    print("Start solving")
    result_data = solve(hospital_data, request_data, SimpleScheduler(), args.scenario)

    if args.visualize:
        print("Start visualizing")
        visualize(result_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input parameters for the algorithm")
    parser.add_argument("scenario")
    parser.add_argument("-visualize", default=False)

    args = parser.parse_args()

    main(args)
