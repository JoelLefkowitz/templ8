import os
import sys
import ruamel.yaml  # type: ignore
from docopt import docopt, DocoptExit  # type: ignore
from inspect import cleandoc
from typing import Tuple, List, Dict

from pyimport import path_guard

path_guard("..")
from generator import generate_templates
from loaders import load_yaml, load_specs
from exceptions import OutputDirInvalid, ConfigPathInvalid, InvalidCommand

# TODO Just record context extends to stay decoupled
# TODO Parse context strings
# TODO Any -> lambda x: x
# TODO common parser pipping
# TODO list parser allow_single=false
# TODO Specified config covered static check ->  static exception
# TODO Specified config covered -> dynamic exception (group templates, context strings)

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
    specs = sum((load_specs(template_dir) for template_dir in template_dirs), [])
    generate_templates(config, specs, output_dir, specified_files, options)


def parse_cli(arguments: dict) -> Tuple[str, str, List[str], List[str], Dict]:
    config_path = arguments["<config_path>"]
    if not os.path.exists(config_path):
        raise ConfigPathInvalid(config_path)

    output_dir = arguments["--output-dir"] or os.path.dirname(config_path)
    if os.path.isfile(output_dir):
        raise OutputDirInvalid(output_dir)

    template_dirs = arguments["<template_dirs>"] or []
    template_dirs.append(os.path.join(os.path.dirname(__file__), "templates"))
    specified_files = arguments["<files>"] or []
    options = {
        "overwrite": arguments["--overwrite"],
        "dry-run": arguments["--dry-run"],
        "no_callbacks": arguments["--no-callbacks"],
    }

    return config_path, output_dir, template_dirs, specified_files, options


if __name__ == "__main__":
    entrypoint()
