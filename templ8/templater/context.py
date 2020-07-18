import re
from dataclasses import dataclass
from exceptions import FailedContextLookup
from typing import Any, Dict, List, TypeVar

from utils.tags import untag

T = TypeVar("T", bound="Context")


@dataclass
class Context:
    name: str
    value: Any

    @staticmethod
    def lookup(name: str, context: List[T], fail_softly: bool = False) -> Any:
        try:
            return next(i for i in context if i.name == name).value

        except StopIteration:
            if fail_softly:
                return None
            else:
                raise FailedContextLookup(name)

    @staticmethod
    def combine_lists(
        old_context: List[T], new_context: List[T], add_new: bool = True
    ) -> List[T]:

        combined_context = old_context.copy()
        for context in new_context:
            try:
                match = next(i for i in old_context if i.name == context.name)
                match.value = context.value if context.value else match.value

            except StopIteration:
                if add_new:
                    combined_context.append(context)

        return combined_context

    @classmethod
    def from_dict(cls, dct: Dict) -> List[T]:
        return [cls(name=k, value=v or None) for k, v in dct.items()]

    @classmethod
    def parse_string(cls, string: str, context: List[T]) -> str:
        return re.sub(
            r"<\w+>", lambda x: str(cls.lookup(untag(x.group()), context)), string
        )
