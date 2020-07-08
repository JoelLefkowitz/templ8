from dataclasses import dataclass, field
from typing import Generic, List, TypeVar

from exceptions import MissingSpecDependecy
from models.callback import Callback
from models.context import Context
from models.path_replacement import PathReplacement
from models.templater import TemplaterScheme
from toposort import toposort_flatten
from utils.files import load_yaml
from utils.filter import unique_by_key
from walkmate import get_child_files
from yummy_cereal import AnnotationsParser

T = TypeVar("T")


@dataclass
class Spec(Generic[T]):
    name: str
    extends: List[str] = field(default_factory=list)
    required_context: List[Context] = field(default_factory=list)
    path_replacements: List[PathReplacement] = field(default_factory=list)
    callbacks: List[Callback] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"Spec: {self.name}"

    @classmethod
    def select_specs(cls, specs: List[T], context: List[Context]) -> List[T]:
        specified_specs = [
            spec
            for spec in specs
            if Context.lookup(spec.name, context, fail_softly=True) is True
        ]

        dependencies = [
            dependency
            for spec in specified_specs
            for dependency in spec.dependecies(specs)
        ]

        required_specs = unique_by_key(specified_specs + dependencies, lambda x: x.name)

        return cls.topographical_sort(required_specs)

    def dependecies(self, specs: List[T]) -> List[T]:
        if not set(self.extends) <= set([spec.name for spec in specs]):
            raise MissingSpecDependecy(self.name, self.extends, specs)

        return [spec for spec in specs if spec.name in self.extends]

    @staticmethod
    def topographical_sort(specs: List[T]) -> List[T]:
        resolution_order = list(
            toposort_flatten({spec.name: {*spec.extends} for spec in specs})
        )
        return [
            next(spec for spec in specs if spec.name == name)
            for name in resolution_order
        ]

    @classmethod
    def collect_specs(
        cls, templater_scheme: TemplaterScheme, context: List[Context]
    ) -> List[T]:
        spec_parser = AnnotationsParser(
            Spec,
            specified_parsers={
                Context: AnnotationsParser(Context),
                Callback: AnnotationsParser(Callback),
                PathReplacement: AnnotationsParser(PathReplacement),
            },
        )

        all_specs = [
            spec_parser(load_yaml(spec_path))
            for template_dir in templater_scheme.template_dirs
            for spec_path in get_child_files(template_dir, match_name="spec.yml")
        ]

        specs = Spec.select_specs(all_specs, context)
        return specs
