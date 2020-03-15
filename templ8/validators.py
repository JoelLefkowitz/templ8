from typing import List
from dataclasses import dataclass
from yummy_cereal import Parser
from pyimport import path_guard

path_guard(".", "..")
from context import Context


@dataclass
class RawSpec(Parser):
    root_name: str
    context_extends: List[str]
    context: List[dict]
    child_context: str
    folder_rename: str
    callbacks: str


@dataclass
class RawChildContext(Parser):
    pass
