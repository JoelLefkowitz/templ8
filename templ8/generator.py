from walkmate import get_child_files
from cli import TemplaterOptions, TemplaterScheme
from context import Context
from exceptions import ConfigTypeError
from spec import Spec
from typing import List, Any
from yummy_cereal import AnnotationsParser
import ruamel.yaml


def collect_context(templater_scheme: TemplaterScheme) -> List[Context]:
    config = load_yaml(templater_scheme.config_path)
    
    try:
        context = [Context(name, value) for name, value in config.items()]
    
    except TypeError:
        raise ConfigTypeError()

    return context


def collect_specs(templater_scheme: TemplaterScheme, context: Context) -> List[Spec]:
    spec_parser = AnnotationsParser(Spec)
    return [
        spec_parser(load_yaml(spec_path))
        for template_dir in templater_scheme.template_dirs
        for spec_path in get_child_files(template_dir, match_name="spec.yml")
    ]


def plan_templates(
    templater_scheme: TemplaterScheme,
    templater_options: TemplaterOptions,
    specs: List[Spec],
) -> None:
    pass


def generate_templates(
    templater_scheme: TemplaterScheme,
    templater_options: TemplaterOptions,
    specs: List[Spec],
) -> None:
    pass


def load_yaml(yaml_path: str) -> Any:
    with open(yaml_path, "r") as stream:
        return ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)
