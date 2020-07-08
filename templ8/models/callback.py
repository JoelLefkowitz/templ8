import subprocess
from dataclasses import dataclass
from typing import List, Generic, TypeVar

from models.context import Context
T = TypeVar("T")

@dataclass
class Callback(Generic[T]):
    name: str
    call: str

    def __call__(self, output_dir: str) -> subprocess.CompletedProcess:
        call = self.call.split(" ")
        return subprocess.run(call, cwd=output_dir)

    def __repr__(self) -> str:
        return f"Callback: {self.name}"

    @classmethod
    def insert_context(cls, callback: T, context: List[Context]) -> T:
        return cls(callback.name, Context.parse_string(callback.call, context))
