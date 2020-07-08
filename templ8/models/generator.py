from dataclasses import dataclass, field
from typing import Generic, List, TypeVar

from models.context import Context
from models.spec import Spec
from models.callback import Callback
from models.path_replacement import PathReplacement

T = TypeVar("T")


@dataclass
class Generator(Generic[T]):
    name: str
    context: List[Context] = field(default_factory=list)
    path_replacements: List[PathReplacement] = field(default_factory=list)
    callbacks: List[Callback] = field(default_factory=list)

    @classmethod
    def from_spec(cls, context: List[Context], spec: Spec) -> T:
        return cls(
            name=spec.name,
            context=[],
            path_replacements=[
                PathReplacement.insert_context(path_replacement, context)
                for path_replacement in spec.path_replacements
            ],
            callbacks=[Callback.insert_context(callback, context) for callback in spec.callbacks],
        )
