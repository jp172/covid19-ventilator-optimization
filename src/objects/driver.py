from typing import Tuple

from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Driver:
    position: Tuple[float]
    shift_start: int
    shift_end: int
