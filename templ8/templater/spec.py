import os
from dataclasses import dataclass, field
from exceptions import MissingSpecDependecy
from functools import reduce
from typing import Iterator, List, TypeVar

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from jinja2 import Template as JinjaTemplate
from toposort import toposort_flatten
from walkmate import get_child_files

from templater.callback import Callback
from templater.context import Context
from templater.path_replacement import PathReplacement
from utils.filter import unique_by_name
from utils.files import contains_cache_dir

T = TypeVar("T", bound="TemplaterSpec")
U = TypeVar("U", bound="RawTemplaterSpec")


@dataclass
class Template:
    name: str
    rel_output_path: str
    raw_template: JinjaTemplate


@dataclass
class RawTemplaterSpec:
    name: str
    root_path: str
    extends: List[str] = field(default_factory=list)
    required_context: List[Context] = field(default_factory=list)
    path_replacements: List[PathReplacement] = field(default_factory=list)
    callbacks: List[Callback] = field(default_factory=list)

    def filter_dependencies(self, specs: List[U], include_self=False) -> List[U]:
        if not set(self.extends) <= set([spec.name for spec in specs]):
            raise MissingSpecDependecy(self.name, self.extends, specs)

        direct_depenencies = [
            next(spec for spec in specs if spec.name == name) for name in self.extends
        ]

        recursive_depenencies = [
            dependency
            for spec in direct_depenencies
            for dependency in spec.filter_dependencies(specs, include_self=True)
        ]

        if include_self:
            recursive_depenencies.append(self)

        return unique_by_name(recursive_depenencies)

    @staticmethod
    def topographical_sort(specs: List[U]) -> List[U]:
        topsorted = toposort_flatten({spec.name: {*spec.extends} for spec in specs})
        return sorted(specs, key=lambda spec: topsorted.index(spec.name))


@dataclass
class TemplaterSpec:
    name: str
    root_path: str
    context: List[Context] = field(default_factory=list)
    path_replacements: List[PathReplacement] = field(default_factory=list)
    callbacks: List[Callback] = field(default_factory=list)

    @classmethod
    def from_raw_specs(
        cls, raw_templater_specs: List[RawTemplaterSpec], context: List[Context],
    ) -> List[T]:

        templater_specs = []

        for raw_templater_spec in raw_templater_specs:

            if (
                Context.lookup(raw_templater_spec.name, context, fail_softly=True)
                is True
            ):

                dependencies = raw_templater_spec.filter_dependencies(
                    raw_templater_specs
                )

                required_context = (
                    reduce(
                        lambda x, y: Context.combine_lists(x, y),
                        [dependency.required_context for dependency in dependencies],
                    )
                    if dependencies
                    else []
                )

                given_context = Context.combine_lists(
                    required_context, context, add_new=False
                )

                resolved_path_replacements = [
                    PathReplacement.insert_context(path_replacement, context)
                    for path_replacement in raw_templater_spec.path_replacements
                ]

                resolved_callbacks = [
                    Callback.insert_context(callback, context)
                    for callback in raw_templater_spec.callbacks
                ]

                templater_spec = cls(
                    name=raw_templater_spec.name,
                    root_path=raw_templater_spec.root_path,
                    context=given_context,
                    path_replacements=resolved_path_replacements,
                    callbacks=resolved_callbacks,
                )

                templater_specs.append(templater_spec)

        return templater_specs

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

            if contains_cache_dir(file_path):
                continue

            # TODO Add path replacements
            template_path = os.path.relpath(file_path, self.root_path)

            yield Template(
                name=os.path.basename(template_path),
                rel_output_path=template_path,
                raw_template=loader.get_template(template_path),
            )
