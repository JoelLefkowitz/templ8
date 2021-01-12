import re
from dataclasses import dataclass
from functools import reduce
from typing import Any
from typing import Dict
from typing import List
from typing import TypeVar

from ..exceptions import FailedContextLookup
from ..utils.tags import untag

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

    @classmethod
    def from_dict(cls, dct: Dict) -> List[T]:
        return [cls(name=k, value=v or None) for k, v in dct.items()]

    @classmethod
    def parse_string(cls, string: str, context: List[T]) -> str:
        return re.sub(
            r"<\w+>", lambda x: str(cls.lookup(untag(x.group()), context)), string
        )

    @staticmethod
    def combine_lists(context_lists: List[List[T]]) -> List[T]:
        return list(
            reduce(
                lambda x, y: Context.fill_list(x, y, add_new=True), context_lists, []
            )
        )

    @staticmethod
    def fill_list(old_list: List[T], new_list: List[T], add_new=False) -> List[T]:
        combined_list = old_list.copy()
        for context in new_list:
            try:
                match = next(i for i in old_list if i.name == context.name)
                match.value = context.value if context.value else match.value

            except StopIteration:
                if add_new:
                    combined_list.append(context)

        return combined_list
