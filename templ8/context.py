from pyimport import path_guard

path_guard("..")
from exceptions import MissingConfig

from dataclasses import dataclass
from typing import Any, Callable, Optional


@dataclass
class Context:
    name: str
    value: Optional[Any]
    default: Optional[Any]

    def read(self, config: dict) -> None:
        self.value = config[self.name] if self.name in config else self.default
        if self.value is None:
            raise MissingConfig(self.name)


@dataclass
class ChildContext:
    name: str
    parent_context: Context
    value: Optional[Any]
    formatter: Optional[Callable[[str], str]]

    def read(self) -> None:
        return self.formatter(self.parent_context.value) if self.formatter else self.parent_context.value
