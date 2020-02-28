from exceptions import MissingConfig
from dataclasses import dataclass
from typing import List, Tuple, Any


@dataclass
class Context:
    name: str
    default: Any = None

    def emit_from_config(self, config: dict) -> Tuple[str, Any]:
        if config and self.name in config:
            return self.name, config[self.name]
        elif self.default:
            return self.name, self.default
        else:
            raise MissingConfig(self.name)


@dataclass
class Spec:
    root_name: str
    context_set: List[Context]

    def check_condition(self, config: dict) -> bool:
        return (
            config[self.root_name] is True
            if config and self.root_name in config
            else False
        )
