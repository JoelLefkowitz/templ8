import re
import os
import pathlib
import subprocess
from typing import List, Optional, Type, Any, Dict, Iterator, Tuple, ClassVar, TypeVar
from dataclasses import dataclass, field

from pyimport import path_guard

path_guard("..")
from jinja2 import Environment, FileSystemLoader, Template, StrictUndefined
from walkman import get_child_files
from collections import namedtuple
from exceptions import MissingContext
from utils import format_str, is_kv, get_kv

T = TypeVar("T")


@dataclass
class Context:
    name: str
    default: Any = None
    formatter: Optional[str] = None
    formatter_kwargs: Optional[Dict[str, Any]] = None

    def __call__(self, config: Dict) -> str:
        if self.name in config:
            lookup = str(config[self.name])
        elif self.default:
            lookup = str(self.default)
        else:
            raise MissingContext(self.name, config)

        return (
            format_str(lookup, self.formatter, **self.formatter_kwargs or {})
            if self.formatter
            else lookup
        )

    def __repr__(self) -> str:
        return self.name

    def encode(self) -> str:
        kwargs = []
        if self.default:
            kwargs.append(f"default={self.default}")

        if self.formatter:
            kwargs.append(f"formatter={self.formatter}")

        if self.formatter_kwargs:
            kwargs.append(
                " ".join([f"{k}={v}" for k, v in self.formatter_kwargs.items()])
            )

        return "<" + self.name + " ".join(kwargs) + ">"

    @classmethod
    def resolve_in_str(cls: Type[T], string: str, config: Dict) -> str:
        re_tag = r"<[^<>]*>"
        return re.sub(re_tag, lambda x: cls.decode(x.group(0))(config), string)

    @classmethod
    def decode(cls: Type[T], string: str) -> T:
        string_parts = string[1:-1].split(" ")
        name = string_parts.pop(0)
        kwargs = dict([get_kv(i) for i in string_parts if is_kv(i)])
        default = kwargs.pop("default", None)
        formatter = kwargs.pop("formatter", None)
        formatter_kwargs = kwargs or None
        return cls(name, default, formatter, formatter_kwargs)


@dataclass
class Callback:
    name: str
    call: str
    cwd: Optional[str] = None

    def __call__(self, output_dir: str) -> subprocess.CompletedProcess:
        call = " ".split(self.call)
        cwd = os.path.join(output_dir, self.cwd) if self.cwd else None
        return subprocess.run(call, cwd=cwd)

    def __repr__(self) -> str:
        return str(self.__dict__)


@dataclass
class PathReplacement:
    name: str
    replacement: str

    def __call__(self, file_path: str, exclude_head: bool = False) -> str:
        file_parts = pathlib.Path(file_path).parts
        replaced_parts = [self.replacement if i == self.name else i for i in file_parts]

        if exclude_head:
            replaced_parts[-1] = os.path.split(file_path)[1]
        return os.path.join(*replaced_parts)

    def __repr__(self) -> str:
        return str(self.__dict__)


TemplateProxy = namedtuple("TemplateProxy", ["template", "source_path"])


@dataclass
class Spec:
    name: str
    root_path: str
    required_context: List[str] = field(default_factory=list)
    required_context_extends: List[str] = field(default_factory=list)
    path_replacements: List[PathReplacement] = field(default_factory=list)
    callbacks: List[Callback] = field(default_factory=list)

    @property
    def templates(self) -> Iterator[TemplateProxy]:
        template_base = os.path.dirname(self.root_path)

        loader = Environment(
            loader=FileSystemLoader(template_base),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
            undefined=StrictUndefined,
        )
    
        for file_path in get_child_files(template_base):    
            source_path = os.path.relpath(file_path, template_base)
            template = loader.get_template(source_path)
            yield TemplateProxy(template, source_path)

    def check_sufficient(self, config: Dict) -> bool:
        return set(self.required_context) <= set(config)

    def check_condition(self, config: Dict) -> bool:
        return self.name in config and config[self.name] is True

    def decode(self, config) -> None:
        if self.path_replacements:
            for pr in self.path_replacements:
                pr.replacement = Context.resolve_in_str(pr.replacement, config)

        if self.callbacks:
            for cb in self.callbacks:
                cb.call = Context.resolve_in_str(cb.call, config)

    def __str__(self) -> str:
        return str(self.__dict__)
