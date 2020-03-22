import argparse

from enum import Enum


from src.simulate import simulate
from src.visualize import visualize
from src.evaluate import evaluate
from src.compare import compare
from src.write_out import write_output
from src.helper_functions.build_instance import build_instance
from src.schedulers.capacity_coefficient_scheduler import CapacityScheduler


class Scenario(Enum):
    WORST = "worst"
    HIGH = "high"
    NORMAL = "normal"


# this main reads data, solves the scheduling problem, writes json output, and visualize the results


def main(args):

    if args.scenario not in [s.value for s in Scenario]:
        raise ValueError

    project_instance = build_instance(args)

    if args.compare:
        print("Start simulation of both schedulers")
        _, snapshots = compare(project_instance)
    else:
        print("Start simulation capacity scheduler")
        snapshots = simulate(project_instance, CapacityScheduler())

    evaluate(project_instance)

    if args.visualize:
        print("Start visualizing")
        visualize(project_instance, snapshots)

    if args.output:
        write_output(project_instance)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input parameters for the algorithm")
    parser.add_argument("scenario")
    parser.add_argument("-compare", default=False)
    parser.add_argument("-visualize", default=False)
    parser.add_argument("-output", default=True)

    args = parser.parse_args()

    main(args)
