import os
import pathlib
import subprocess
from typing import List, Optional, Tuple, Union
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader, Template, StrictUndefined
from walkman import get_child_files
from pyimport import path_guard

path_guard(".", "..")
from context import Context


@dataclass
class FolderRename:
    name: str
    rename: Union[str, Context]

    def replace(self, string: str) -> str:
        return (
            string
            if string != self.name
            else self.rename.read
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

    def run(self, output_path: str) -> subprocess.CompletedProcess:
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
            undefined=StrictUndefined,
        )
        for file_path in get_child_files(root_path):
            template = loader.get_template(os.path.relpath(file_path, root_path))
            yield template, file_path

    def resolve_output_path(self, file_path: str, output_dir: str) -> str:
        for rename in self.folder_renames:
            file_path = rename.replace_in_path(file_path)
        return os.path.join(output_dir, file_path)

    def resolve_template(
        self, template: Template, file_path: str, output_dir: str
    ) -> None:
        context_dict = {i: i.read for i in self.context}
        output = template.resolve(context_dict)
        output_path = self.resolve_output_path(file_path, output_dir)

        pathlib.Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(output)
