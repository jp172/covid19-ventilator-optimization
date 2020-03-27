from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .location import Location


@dataclass_json
@dataclass
class City:
    ident: str
    name: str
    position: Location
    population: int
    population_density: int
    state: str
