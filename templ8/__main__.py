import os
import sys

from cli import docopts_cli
from docopt import DocoptExit, docopt  # type: ignore
from exceptions import (
    ConfigTypeError,
    InvalidCommand,
    InvalidConfigPath,
    InvalidOutputDir,
)
from models.context import Context
from models.generator import Generator
from models.spec import Spec
from models.templater import TemplaterOptions, TemplaterScheme


def entrypoint() -> None:
    try:
        cli_arguments = docopt(docopts_cli)
    except DocoptExit:
        raise InvalidCommand(sys.argv[1:], cli)

    config_path = cli_arguments["<config_path>"]
    if not os.path.exists(config_path) or os.path.isdir(config_path):
        raise InvalidConfigPath(config_path)

    output_dir = cli_arguments["<output_dir>"] or os.path.dirname(config_path)
    if os.path.isfile(output_dir):
        raise InvalidOutputDir(output_dir)

    templater_options = TemplaterOptions(
        cli_arguments["--overwrite"],
        cli_arguments["--dry-run"],
        cli_arguments["--skip-callbacks"],
    )

    templater_scheme = TemplaterScheme(
        config_path,
        output_dir,
        cli_arguments["<template_dirs>"],
        cli_arguments["<specified_files>"],
        options=templater_options,
    )

    # TODO Ensure this is correct when packaging
    core_templates_root = os.path.abspath(os.path.join(__file__, "../../"))
    templater_scheme.template_dirs.append(core_templates_root)

    context = Context.collect_context(templater_scheme)
    specs = Spec.collect_specs(templater_scheme, context)
    generators = [Generator.from_spec(context, spec) for spec in specs]
    x = 1

if __name__ == "__main__":
    entrypoint()
