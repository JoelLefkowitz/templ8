import re
from dataclasses import dataclass
from typing import Any, Generic, List, TypeVar

from exceptions import FailedContextLookup
from models.templater import TemplaterScheme
from utils.files import load_yaml
from utils.tags import untag

T = TypeVar("T")


@dataclass
class Context(Generic[T]):
    name: str
    value: Any

    @staticmethod
    def lookup(name: str, context: List[T], fail_softly=False) -> Any:
        try:
            return next(i for i in context if i.name == name).value

        except StopIteration:
            if fail_softly:
                return None
            else:
                raise FailedContextLookup(name)

    @classmethod
    def parse_string(cls, string: str, context: List[T]) -> str:
        return re.sub(r"<\w+>", lambda x: cls.lookup(untag(x.group()), context), string)

    @classmethod
    def collect_context(cls, templater_scheme: TemplaterScheme) -> List[T]:
        config = load_yaml(templater_scheme.config_path)

        try:
            context = [Context(name, value) for name, value in config.items()]

        except TypeError:
            raise ConfigTypeError()

        return context
