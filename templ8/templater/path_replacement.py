import os
from dataclasses import dataclass
from typing import List
from typing import TypeVar

from .context import Context

T = TypeVar("T", bound="PathReplacement")


@dataclass
class PathReplacement:
    name: str
    replacement: str

    def replace_in_path(self, file_path: str) -> str:
        head, tail = os.path.split(file_path)
        return os.path.join(
            *[
                self.replacement if component == self.name else component
                for component in os.path.normpath(head).split(os.path.sep)
            ],
            tail
        )

    @classmethod
    def insert_context(cls, path_replacement: T, context: List[Context]) -> T:
        return cls(
            path_replacement.name,
            Context.parse_string(path_replacement.replacement, context),
        )
