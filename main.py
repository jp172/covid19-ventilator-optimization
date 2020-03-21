import argparse

from enum import Enum

from src.solve import solve
from src.visualize import visualize
from src.objects.person import Person
from src.objects.hospital import Hospital
from src.helper_functions.read_data import read_objects
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

    hospital_dict = read_objects("data/hospitals/hospitals.json", Hospital)
    person_dict = read_objects("data/patient_requests/patients.json", Person)

    print("Start solving")
    result_data = solve(hospital_dict, person_dict, SimpleScheduler(), args.scenario)

    if args.visualize:
        print("Start visualizing")
        visualize(result_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input parameters for the algorithm")
    parser.add_argument("scenario")
    parser.add_argument("-visualize", default=False)

    args = parser.parse_args()

    main(args)
