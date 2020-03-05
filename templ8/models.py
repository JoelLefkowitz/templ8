import os
import pathlib
import subprocess

from pyimport import path_guard

path_guard(__file__, "..")
from exceptions import MissingConfig
from utils import get_child_files, inclusive_relpath

from dataclasses import dataclass, field
from typing import List, Tuple, Any, Callable, Dict, Iterator, Union
from jinja2 import Environment, FileSystemLoader, Template


@dataclass
class Context:
    name: str
    default: Any = None

    def __str__(self):
        return f"Context({self.name})"

    def emit_from_config(self, config: dict) -> Tuple[str, Any]:
        if config and self.name in config:
            return self.name, config[self.name]
        elif self.default:
            return self.name, self.default
        else:
            raise MissingConfig(self.name)


@dataclass
class Alias:
    context: Context
    formatter: Callable[[Any], str] = lambda x: str(x).replace("-", "_")

    def __repr__(self):
        return f"Alias for {self.context}"

    def resolve(self, config: dict) -> str:
        name, value = self.context.emit_from_config(config)
        return self.formatter(value)

    def replace_in_path(self, target_name: str, folder_path: str, config: dict) -> str:
        parts = pathlib.Path(folder_path).parts
        replaced = [self.resolve(config) if i is target_name else i for i in parts]
        return os.path.join("", *replaced)


@dataclass
class Callback:
    call: List[Union[str, Alias]]

    def run(self, config: dict, output_dir: str) -> None:
        resolved_call = [
            i.resolve(config) if isinstance(i, Alias) else i for i in self.call
        ]
        subprocess.run(resolved_call, cwd=output_dir)


@dataclass
class Spec:
    root_name: str
    dependencies: List[str] = field(default_factory=list)
    context_set: List[Context] = field(default_factory=list)
    folder_aliases: Dict[str, Alias] = field(default_factory=dict)
    callbacks: List[Callback] = field(default_factory=list)

    def check_condition(self, config: dict) -> bool:
        required_names = [self.root_name] + self.dependencies
        if not config or not all(name in config for name in required_names):
            return False

        else:
            return all(config[name] for name in required_names)

    def load_templates(
        self, config: dict, template_dir: str, output_dir: str
    ) -> Iterator[Tuple[Template, str]]:
        loader = Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )

        root_path = os.path.join(template_dir, self.root_name)
        for file_path in get_child_files(root_path):

            template_path = os.path.relpath(file_path, template_dir)
            template = loader.get_template(template_path)

            rel_file_path = inclusive_relpath(file_path, root_path)
            rel_file_path = self.replace_path_aliases(rel_file_path, config)
            output_path = os.path.join(output_dir, rel_file_path)
            yield template, output_path

    def replace_path_aliases(self, file_path: str, config: dict) -> str:
        folder_path, filename = os.path.split(file_path)

        for target_name, alias in self.folder_aliases.items():
            folder_path = alias.replace_in_path(target_name, folder_path, config)

        return os.path.join(folder_path, filename)
