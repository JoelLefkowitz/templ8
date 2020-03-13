import os
import pathlib
from subprocess import subprocess, CompletedProcess
from typing import field, List, Mapping, Optional, Union
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader, Template

from pyimport import path_guard

path_guard("..")
from utils import get_child_files
from .context import Context


@dataclass
class FolderRename:
    name: str
    rename: Union[str, Context]

    def replace(self, string: str) -> str:
        return (
            string if string != self.name else self.rename.read
            if isinstance(self.rename, Context)
            else self.rename
        )

    def replace_in_path(self, file_path: str) -> str:
        folder_path, filename = os.path.split(file_path)
        replaced_parts = [self.replace(i) for i in pathlib.Path(folder_path).parts]
        return os.path.join(*replaced_parts, filename)
            

@dataclass
class Callback:
    name: str
    call: List[Union[str, Context]]
    cwd: Optional[str]

    def run(self, output_path: str) -> CompletedProcess:
        call = [i.read if isinstance(i, Context) else i for i in self.call]
        cwd = os.path.join(output_path, self.cwd) if self.cwd else None
        return subprocess.run(call, cwd=cwd)


@dataclass
class Spec:
    root_name: str
    template_dir: str
    context: List[Context]
    folder_renames: List[FolderRename]
    callbacks: List[Callback]

    def check_include(self, config: dict) -> bool:
        names = [self.root_name, *self.dependencies]
        return set(names) <= set(config) and all(config[i] for i in names)

    @property
    def templates(self) -> Tuple[Template, str]:
        root_path = os.path.join(self.template_dir, self.root_name)
        loader = Environment(
            loader=FileSystemLoader(root_path),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )

        for file_path in get_child_files(root_path):
            template = loader.get_template(os.path.relpath(file_path, root_path))
            yield template, file_path

    def resolve_output_path(self, file_path: str, output_dir: str) -> str:
        for rename in self.folder_renames:
            file_path = rename.replace_in_path(file_path)
        return os.path.join(output_dir, file_path)
