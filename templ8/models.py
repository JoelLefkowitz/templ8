import os
import subprocess

from pyimport import path_guard

path_guard(__file__, "..")
from exceptions import MissingConfig
from utils import get_child_files

from dataclasses import dataclass, field
from typing import List, Tuple, Any, Callable, Dict, Iterator, Union
from jinja2 import Environment, FileSystemLoader, Template


@dataclass
class Context:
    name: str
    default: Any = None

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

    def resolve(self, config: dict) -> str:
        name, value = self.context.emit_from_config(config)
        return self.formatter(value)


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
        spec_root = os.path.join(template_dir, self.root_name)
        loader = Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )

        for file in get_child_files(spec_root):
            rel_input_path = os.path.relpath(file, template_dir)
            folder_path, filename = os.path.split(rel_input_path)

            for folder_name in self.folder_aliases:
                folder_path = folder_path.replace(
                    folder_name, self.folder_aliases[folder_name].resolve(config)
                )

            output_path = os.path.join(output_dir, folder_path, filename)
            template = loader.get_template(rel_input_path)
            yield template, output_path
