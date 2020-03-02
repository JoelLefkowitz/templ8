from .exceptions import MissingConfig
from dataclasses import dataclass, field
from typing import List, Tuple, Any, Callable, Dict


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
class Alias:
    context: Context
    formatter: Callable[[Any], str] = lambda x: str(x)

    def resolve(self, config: dict) -> str:
        name, value = self.context.emit_from_config(config)
        return self.formatter(value)


@dataclass
class Spec:
    root_name: str
    context_set: List[Context]
    folder_aliases: Dict[str, Alias] = field(default_factory=dict)

    def check_condition(self, config: dict) -> bool:
        return (
            config[self.root_name] is True
            if config and self.root_name in config
            else False
        )
