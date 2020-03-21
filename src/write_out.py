import json


def write_output(instance, output_file=""):

    out_data = {}
    for r in instance.requests:
        out_data[r] = instance.requests[r].to_dict()

    of = "out"

    if output_file:
        of = output_file
    with open("data/output/" + of + ".json", "w") as f:
        json.dump(out_data, f)

    print("printed!")
