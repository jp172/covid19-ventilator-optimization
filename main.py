import argparse

from src.simulate import simulate
from src.visualize import visualize
from src.evaluate import squared_deviation_from_optimal_capacity
from src.compare import compare
from src.write_out import write_output
from src.helper_functions.build_instance import build_instance

from src.schedulers.capacity_coefficient_scheduler import CapacityScheduler

from random import seed
seed(42)


# this main reads data, solves the scheduling problem, writes json output, and visualize the results
def main(args):

    print("reading in instance")
    project_instance = build_instance(args)

    snapshot_list = []
    if args.compare:
        print("Start simulation of both schedulers")
        snapshots_simple, score_simple, snapshots, score = compare(project_instance)
        print("Lower score means better capacity distribution")
        print(f"standard scores {score_simple} > {score} our score ")
        snapshot_list.append(snapshots_simple)
        snapshot_list.append(snapshots)
    else:
        print("Start simulation capacity scheduler")
        snapshots = simulate(project_instance, CapacityScheduler())
        score = squared_deviation_from_optimal_capacity(project_instance)
        snapshot_list.append(snapshots)
        print("Score: ", score)

    if args.visualize:
        print("Start visualizing")
        visualize(project_instance, snapshot_list)

    if args.output:
        print("Writing output")
        write_output(project_instance)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input parameters for the algorithm")
    parser.add_argument("-compare", default=False)
    parser.add_argument("-visualize", default=False)
    parser.add_argument("-output", default=True)

    args = parser.parse_args()

    main(args)
