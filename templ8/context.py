from pyimport import path_guard

path_guard("..")
from exceptions import MissingConfig

from dataclasses import dataclass
from typing import Any, Callable, Optional


@dataclass
class Context:
    name: str
    config: dict
    default: Optional[Any]

    @property
    def read(self) -> None:
        if self.name not in self.config and self.default is None:
            raise MissingConfig(self.name)
        return self.config[self.name] if self.name in self.config else self.default


@dataclass
class ChildContext(Context):
    name: str
    config: dict
    parent_context: Context
    formatter: Optional[Callable[[str], str]]

    @property
    def read(self) -> None:
        return (
            self.formatter(self.parent_context.read)
            if self.formatter
            else self.parent_context.read
        )
