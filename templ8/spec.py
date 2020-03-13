import os
from subprocess import subprocess, CompletedProcess
from typing import field, List, Mapping, Optional
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader, Template

from pyimport import path_guard

path_guard("..")
from utils import get_child_files


@dataclass
class Callback:
    call: List[str]
    cwd: Optional[str]

    def run(self, output_path: str) -> CompletedProcess:
        cwd = os.path.join(output_path, self.cwd) if self.cwd else None
        return subprocess.run(self.call, cwd=cwd)


@dataclass
class Spec:
    root_name: str
    template_dir: str
    dependencies: str
    context: dict
    folder_renames: Mapping[str, str]
    callbacks: Mapping[str, Callback]

    def check_include(self, config: dict) -> bool:
        names = [self.root_name, *self.dependencies]
        return set(names) <= set(config) and all(config[i] for i in names)

    def __iter__(self) -> Template:
        root_path = os.path.join(self.template_dir, self.root_name)
        loader = Environment(
            loader=FileSystemLoader(root_path),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )

        for file_path in get_child_files(root_path):
            yield loader.get_template(os.path.relpath(file_path, root_path))

    # rel_file_path = (
    #     inclusive_relpath(file_path, root_path)
    #     if self.include_root_dir
    #     else os.path.relpath(file_path, root_path)
    # )
    # rel_file_path = self.replace_path_aliases(rel_file_path, config)
    # output_path = os.path.join(output_dir, rel_file_path)

    # def replace_path_aliases(self, file_path: str, config: dict) -> str:
    #     folder_path, filename = os.path.split(file_path)
    #     for target_name, alias in self.folder_aliases.items():
    #         parts = pathlib.Path(folder_path).parts
    #         replaced = [self.resolve(config) if i is target_name else i for i in parts]
    #         return os.path.join("", *replaced)
    #     return os.path.join(folder_path, filename)
