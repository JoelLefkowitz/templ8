import os
import sys
import ruamel.yaml  # type: ignore
from docopt import docopt, DocoptExit  # type: ignore
from inspect import cleandoc
from typing import Tuple, List, Dict, Any
from walkman import get_child_files
from pyimport import path_guard

path_guard("..")
from generator import generate_templates
from exceptions import InvalidOutputDir, InvalidCommand, InvalidConfigPath
from models import Spec, Context
from parsers import spec_parser


cli = cleandoc(
    """
    Usage:
      templ8 <config_path> [--output-dir=<output_dir>] [--template-dirs <template_dirs>]... [--files <files>]... [(--overwrite | --dry-run) --no-callbacks]

    Options:
      --overwrite
      --dry-run
      --no-callbacks
    """
)


def entrypoint() -> None:
    try:
        arguments = docopt(cli)
    except DocoptExit:
        raise InvalidCommand(sys.argv[1:], cli)

    config_path, output_dir, template_dirs, specified_files, options = parse_cli(
        arguments
    )

    config = load_yaml(config_path)
    specs = load_specs(template_dirs)

    # TODO Load default context values into config
    # TODO Check nominal config is sufficient
    specs = [spec for spec in specs if spec.check_condition(config)]
    for spec in specs:
        spec.decode(config)
    generate_templates(config, specs, output_dir, specified_files, options)


def parse_cli(arguments: dict) -> Tuple[str, str, List[str], List[str], Dict]:
    config_path = arguments["<config_path>"]
    if not os.path.exists(config_path):
        raise InvalidConfigPath(config_path)

    output_dir = arguments["--output-dir"] or os.path.dirname(config_path)
    if os.path.isfile(output_dir):
        raise InvalidOutputDir(output_dir)

    template_dirs = arguments["<template_dirs>"] or []
    template_dirs.append(os.path.join(os.path.dirname(__file__), "templates"))
    specified_files = arguments["<files>"] or []
    options = {
        "overwrite": arguments["--overwrite"],
        "dry-run": arguments["--dry-run"],
        "no_callbacks": arguments["--no-callbacks"],
    }

    return config_path, output_dir, template_dirs, specified_files, options


def load_specs(template_dirs: List[str]) -> List[Spec]:
    specs = []
    for template_dir in template_dirs:
        for spec_path in get_child_files(template_dir, "spec.yml", 1):
            spec_config = load_yaml(spec_path)
            spec_parser.field_defaults = {"root_path": spec_path}
            spec = spec_parser(spec_config)
            specs.append(spec)
    return specs


def load_yaml(path: str) -> Any:
    with open(path, "r") as stream:
        return ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)


if __name__ == "__main__":
    entrypoint()
