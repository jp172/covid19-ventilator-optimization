import json


def write_output(instance, output_file = ""):
    print("hi")
    if output_file:
        json.dump(instance.requests, "data/output/" + output_file)
    else:
        json.dump(instance.requests, "data/output/out")
