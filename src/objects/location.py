from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Location:
    lat: float
    lon: float
    time_zone: str = ""  # timezone of the hospital.
    address_line1: str = ""  # first hospital address line
    address_line2: str = ""  # second hospital address line
    city: str = ""  # city of location
    state_province: str = ""  # state or province of location
    postal_code: str = ""  # postal code of location
    country: str = ""  # country of location
