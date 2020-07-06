from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Spec:
    name: str
    extends: str
    required_context: Dict = field(default_factory=dict)

    def typographical_sort(self, other):
        pass

    def parse_spec(self):
        pass
