import re
import os
import pathlib
import subprocess
from typing import List, Optional, Any, Dict, Iterator
from dataclasses import dataclass

from jinja2 import Environment, FileSystemLoader, Template, StrictUndefined
from walkman import get_child_files
from exceptions import MissingConfig


@dataclass
class Formatter:
    string: str
    prefix: Optional[str] = None
    suffix: Optional[str] = None

    @property
    def hyphen_to_underscore(self) -> str:
        return str(self.string).replace("-", "_")

    @property
    def underscore_to_hyphen(self) -> str:
        return str(self.string).replace("_", "-")

    @property
    def camelcase(self) -> str:
        return re.sub(r"(?!^)_([a-zA-Z])", lambda m: m.group(1).upper(), self.string)

    @property
    def add_prefix(self) -> str:
        return self.prefix + "_" + self.string if self.prefix else self.string

    @property
    def add_suffix(self) -> str:
        return self.string + "_" + self.suffix if self.suffix else self.string


@dataclass
class Context:
    string: str
    defaults: Optional[Dict] = None

    @property
    def tags(self) -> List[str]:
        re_tag = r"<[^<>]*>"
        return [tag[1:-1] for tag in re.findall(re_tag, self.string)]

    def __call__(self, config: Dict) -> str:
        re_tag = r"<[^<>]*>"
        return re.sub(
            re_tag, lambda x: self.lookup(x.group(0)[1:-1], config), self.string
        )

    def lookup(self, string: str, config: Dict) -> str:
        if string in config:
            return str(config[string])
        elif self.defaults and string in self.defaults:
            return str(self.defaults[string])
        else:
            raise MissingConfig(string, config)


@dataclass
class Callback:
    name: str
    call: str
    cwd: Optional[str] = None

    def __call__(self, output_path: str) -> subprocess.CompletedProcess:
        call = " ".split(self.call)
        cwd = os.path.join(output_path, self.cwd) if self.cwd else None
        return subprocess.run(call, cwd=cwd)


@dataclass
class PathReplacement:
    name: str
    before: str
    after: str

    def __call__(self, file_path: str, exclude_head: bool = False) -> str:
        file_parts = pathlib.Path(file_path).parts
        replaced_parts = [self.after if i == self.before else i for i in file_parts]

        if exclude_head:
            replaced_parts[-1] = os.path.split(file_path)[1]
        return os.path.join(*replaced_parts)


@dataclass
class Spec:
    name: str
    root_path: str
    required_config: List[str]
    path_replacements: List[PathReplacement]
    callbacks: List[Callback]

    @property
    def templates(self) -> Iterator[Template]:
        loader = Environment(
            loader=FileSystemLoader(self.root_path),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
            undefined=StrictUndefined,
        )

        for file_path in get_child_files(self.root_path):
            template = loader.get_template(os.path.relpath(file_path, self.root_path))
            yield template

    def sufficient_config(self, config: dict) -> bool:
        return set(self.required_config) <= set(config)
