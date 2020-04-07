import ruamel.yaml
from typing import List, Any
from walkman import get_child_files
from pyimport import path_guard
from yummy_cereal import (
    Parser,
    AnotatedFieldsParser,
    named_parser,
    list_or_single_parser,
)

from pyimport import path_guard

path_guard("..")
from models import Spec, Context, ContextString, PathReplacement, Callback


def load_specs(template_dir: str) -> List[Spec]:
    required_context_parser = named_parser(
        list_or_single_parser(
            AnotatedFieldsParser(
                Context, collector_field="default", child_parsers={"default": str},
            )
        )
    )

    path_replacements_parser = named_parser(
        list_or_single_parser(
            AnotatedFieldsParser(PathReplacement, collector_field="replacement")
        ),
        collector_field="replacement",
    )

    callbacks_parser = named_parser(
        list_or_single_parser(AnotatedFieldsParser(Callback, collector_field="call")),
        collector_field="call",
    )

    spec_parser = AnotatedFieldsParser(
        cls=Spec,
        child_parsers={
            "required_context": required_context_parser,
            "required_context_extends": list_or_single_parser(str),
            "path_replacements": path_replacements_parser,
            "callbacks": callbacks_parser,
        },
    )

    for spec_path in get_child_files(template_dir, "spec.yml", 1):
        specs = []
        spec_config = load_yaml(spec_path)
        spec_parser.field_defaults = {"root_path": spec_path}
        specs.append(spec_parser(spec_config))
    return specs


def load_yaml(path: str) -> Any:
    with open(path, "r") as stream:
        return ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)
