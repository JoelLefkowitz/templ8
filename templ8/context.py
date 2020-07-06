from dataclasses import dataclass
from typing import Any, List, TypeVar, Generic
import re

T = TypeVar("T")


@dataclass
class Context(Generic[T]):
    name: str
    value: Any

    @staticmethod
    def parse_string(string: str, context: List[T]) -> str:
        matches = re.match("<\w+>", string)

        print(matches)

        return string
