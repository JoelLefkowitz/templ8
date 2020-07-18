from dataclasses import dataclass
from typing import List, TypeVar

from templater.context import Context

T = TypeVar("T", bound="PathReplacement")


@dataclass
class PathReplacement:
    name: str
    replacement: str

    @classmethod
    def insert_context(cls, path_replacement: T, context: List[Context]) -> T:
        return cls(
            path_replacement.name,
            Context.parse_string(path_replacement.replacement, context),
        )
