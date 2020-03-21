from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .position import Position


@dataclass_json
@dataclass
class Hospital:
    ident: str
    nbr_free_beds: int
    nbr_free_corona_beds: int
    position: Position
