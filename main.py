import argparse

from enum import Enum


from src.solve import solve
from src.visualize import visualize
from src.evaluate import evaluate
from src.write_out import write_output
from src.objects.instance import Instance
from src.objects.request import Request
from src.objects.hospital import Hospital
from src.helper_functions.read_data import read_objects
from src.schedulers.simple_scheduler import SimpleScheduler


class Scenario(Enum):
    WORST = "worst"
    HIGH = "high"
    NORMAL = "normal"


# this main reads data, solves the scheduling problem, writes json output, and
# will visualize the results sooooon


def main(args):

    if args.scenario not in [s.value for s in Scenario]:
        raise ValueError

    project_instance = Instance()
    project_instance.scenario = args.scenario
    project_instance.hospitals = read_objects("data/hospitals/hospitals.json", Hospital)
    project_instance.requests = read_objects("data/patient_requests/requests.json", Request)
    project_instance.generate_vehicles()
    project_instance.generate_bed_updates()

    print("Start solving")
    solve(project_instance, SimpleScheduler())

    evaluate(project_instance)

    if args.visualize:
        print("Start visualizing")
        visualize(project_instance)

    if args.output:
        write_output(project_instance)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input parameters for the algorithm")
    parser.add_argument("scenario")
    parser.add_argument("-visualize", default = False)
    parser.add_argument("-output", default = True)

    args = parser.parse_args()

    main(args)
