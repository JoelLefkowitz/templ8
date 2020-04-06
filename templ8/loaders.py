import ruamel.yaml
from typing import List, Any
from walkman import get_child_files
from pyimport import path_guard
from yummy_cereal import (
    Parser,
    AnnotationsParser,
    named_parser,
    list_or_single_parser,
)

from .models import Spec


def load_specs(template_dir: str) -> List[Spec]:
    context_parser = AnnotationsParser()

    folder_renames_parser = AnnotationsParser()

    callbacks_parser = AnnotationsParser()

    spec_parser = AnnotationsParser(
        cls=Spec,
        field_defaults={"template_dir": template_dir},
        child_parsers={"context": None, "folder_renames": None, "callbacks": None,},
    )

    return [
        spec_parser(load_yaml(path))
        for path in get_child_files(template_dir, "spec.yml", 1)
    ]


def load_yaml(path: str) -> Any:
    with open(path, "r") as stream:
        return ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)
