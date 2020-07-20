import subprocess
from dataclasses import dataclass
from typing import List, TypeVar

from .context import Context

T = TypeVar("T", bound="Callback")


@dataclass
class Callback:
    name: str
    call: str

    def __call__(self, cwd: str, capture_output: bool) -> subprocess.CompletedProcess:
        call = self.call.split(" ")
        return subprocess.run(call, cwd=cwd, capture_output=capture_output)

    @classmethod
    def insert_context(cls, callback: T, context: List[Context]) -> T:
        return cls(callback.name, Context.parse_string(callback.call, context))
