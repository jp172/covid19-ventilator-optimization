from dataclasses import dataclass
from dataclasses_json import dataclass_json

from position import Position


@dataclass_json
@dataclass
class Request:
    filed_at: int
    position: Position
    severity: float
    corona_likelihood: float
