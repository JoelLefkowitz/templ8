from dataclasses import dataclass
from typing import List, Generic, TypeVar

from models.context import Context
T = TypeVar("T")

@dataclass
class PathReplacement(Generic[T]):
    name: str
    replacement: str

    def __repr__(self) -> str:
        return f"Replacement: {self.name}"

    @classmethod
    def insert_context(cls, path_replacement: T, context: List[Context]) -> T:
        cls(path_replacement.name, Context.parse_string(path_replacement.replacement, context))
