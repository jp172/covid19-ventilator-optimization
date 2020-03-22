import json


def write_object_dict(object_dict, output_file):
    with open(output_file, "w") as f:
        object_dict = dict((key, value.to_dict()) for key, value in object_dict.items())
        json.dump(object_dict, f)
