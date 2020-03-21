import json
from typing import Dict, TypeVar

T = TypeVar("T")


def read_objects(input_file, object_class: T) -> Dict[str, T]:
    objects = dict()
    with open(input_file) as f:
        data = json.load(f)
        for key in data:
            objects[key] = object_class.from_dict(data[key])

    return objects
