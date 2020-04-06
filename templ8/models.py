import re
import os
import pathlib
import subprocess
from typing import List, Optional, Any, Dict, Iterator, Tuple, ClassVar
from dataclasses import dataclass, field

from jinja2 import Environment, FileSystemLoader, Template, StrictUndefined
from walkman import get_child_files
from collections import namedtuple
from .exceptions import MissingConfig
from .utils import format_str, is_kv, get_kv


@dataclass
class ContextString:
    string: str
    re_tag: ClassVar[str] = r"<[^<>]*>"

    def __call__(self, config: Dict) -> str:
        return re.sub(
            self.re_tag, lambda x: self.resolve(x.group(0), config), self.string
        )

    def resolve(self, string: str, config: Dict) -> str:
        context = Context.from_string(string)
        return context(config)

    @property
    def tags(self) -> List[str]:
        return [tag[1:-1] for tag in re.findall(self.re_tag, self.string)]


@dataclass
class Context:
    name: str
    default: Any = None
    formatter: Optional[str] = None
    formatter_kwargs: Dict = field(default_factory=dict)

    @staticmethod
    def from_string(string: str) -> Context:
        string_parts = string[1:-1].split(" ")
        name = string_parts.pop()
        kwargs = dict([i.split("=") for i in string_parts if is_kv(i)])
        default = kwargs.pop("default", None)
        formatter = kwargs.pop("formatter", None)
        return Context(name, default, formatter, kwargs)

    def __call__(self, config: Dict) -> str:
        if self.name in config:
            lookup = str(config[self.name])
        elif self.default:
            lookup = str(self.default)
        else:
            raise MissingConfig(self.name, config)

        return (
            format_str(lookup, self.formatter, **self.formatter_kwargs)
            if self.formatter
            else lookup
        )


@dataclass
class Callback:
    name: str
    call: str
    cwd: Optional[str] = None

    def __call__(self, output_dir: str) -> subprocess.CompletedProcess:
        call = " ".split(self.call)
        cwd = os.path.join(output_dir, self.cwd) if self.cwd else None
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


TemplateProxy = namedtuple("TemplateProxy", ["template", "source_path"])


@dataclass
class Spec:
    name: str
    root_path: str
    required_config: List[str]
    path_replacements: List[PathReplacement]
    callbacks: List[Callback]

    @property
    def templates(self) -> Iterator[TemplateProxy]:
        loader = Environment(
            loader=FileSystemLoader(self.root_path),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
            undefined=StrictUndefined,
        )

        for file_path in get_child_files(self.root_path):
            source_path = os.path.relpath(file_path, self.root_path)
            template = loader.get_template(source_path)
            yield TemplateProxy(template, source_path)

    def sufficient_config(self, config: dict) -> bool:
        return set(self.required_config) <= set(config)

    def include(self, config: Dict) -> bool:
        return self.name in config and config[self.name] is True
