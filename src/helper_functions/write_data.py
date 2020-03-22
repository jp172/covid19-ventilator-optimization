import json


def write_dict(output_dict, output_file):
    with open(output_file, "w") as f:
        json.dump(output_dict, f)


def write_objects(object_dict, output_file):
    object_dict = dict((key, value.to_dict()) for key, value in object_dict.items())
    write_dict(object_dict, output_file)
