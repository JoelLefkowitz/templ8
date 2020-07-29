import os
from dataclasses import dataclass, field
from typing import Iterator, List, TypeVar

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from jinja2 import Template as JinjaTemplate
from toposort import toposort_flatten
from walkmate import get_child_files

from ..exceptions import MissingSpecDependecy
from ..utils.files import contains_cache_dir
from ..utils.filter import unique_by_name
from .callback import Callback
from .context import Context
from .path_replacement import PathReplacement

T = TypeVar("T", bound="TemplaterSpec")
U = TypeVar("U", bound="RawTemplaterSpec")


@dataclass
class Template:
    name: str
    rel_output_path: str
    raw_template: JinjaTemplate

    def render(self, context: List[Context]) -> str:
        x = {i.name: i.value for i in context}
        return self.raw_template.render({i.name: i.value for i in context})


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
    def filter_dependencies_by_context(
        specs: List[U], context: List[Context]
    ) -> List[U]:
        return unique_by_name(
            [
                individual_spec
                for spec in specs
                for individual_spec in spec.filter_dependencies(
                    specs, include_self=True
                )
                if Context.lookup(spec.name, context, fail_softly=True) is True
            ]
        )

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

        for raw_templater_spec in RawTemplaterSpec.filter_dependencies_by_context(
            raw_templater_specs, context
        ):
            required_context = Context.combine_lists(
                [
                    dependency.required_context
                    for dependency in raw_templater_spec.filter_dependencies(
                        raw_templater_specs, include_self=True
                    )
                ]
            )

            scoped_context = Context.fill_list(
                old_list=required_context, new_list=context
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
                context=scoped_context,
                path_replacements=resolved_path_replacements,
                callbacks=resolved_callbacks,
            )

            templater_specs.append(templater_spec)

        return templater_specs

    @property
    def templates(self) -> Iterator[Template]:
        env = Environment(
            loader=FileSystemLoader(self.root_path, encoding="utf-8"),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
            undefined=StrictUndefined,
        )

        for file_path in get_child_files(self.root_path):

            template_path = os.path.relpath(file_path, self.root_path)

            if (
                contains_cache_dir(file_path)
                or os.path.basename(template_path) == "spec.yml"
            ):
                continue

            rel_output_path = template_path

            for path_replacement in self.path_replacements:
                rel_output_path = path_replacement.replace_in_path(rel_output_path)

            yield Template(
                name=os.path.basename(template_path),
                rel_output_path=rel_output_path,
                raw_template=env.get_template(template_path),
            )
