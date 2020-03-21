import json


def write(instance, output_file):
    if output_file:
        json.dump(instance.requests, "../data/output/" + output_file)
    else:
        json.dump(instance.requests, "../data/output/out")
