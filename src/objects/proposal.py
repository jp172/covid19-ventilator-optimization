from typing import Dict, List

from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .hospital import Hospital


@dataclass_json
@dataclass
class RankedProposal:
    def __init__(self, proposed_hospitals: List[Hospital]):
        self.proposal_dict: Dict[int, Hospital] = dict()
        sorted_proposals = sorted(
            proposed_hospitals, key=lambda hosp: hosp.capacity_coefficient
        )
        for index, proposal in enumerate(sorted_proposals):
            self.proposal_dict[index] = proposal
