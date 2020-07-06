import os
import sys
from docopt import docopt, DocoptExit  # type: ignore
from inspect import cleandoc
from typing import List
from dataclasses import dataclass
from cli import docopts_cli, TemplaterOptions, TemplaterScheme
from exceptions import InvalidOutputDir, InvalidCommand, InvalidConfigPath
from generator import collect_context, collect_specs, plan_templates, generate_templates


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
    core_templates_root = os.path.abspath(os.path.join( __file__, "../../"))
    templater_scheme.template_dirs.append(core_templates_root)

    context = collect_context(templater_scheme)
    specs = collect_specs(templater_scheme, context)
    plan_templates(templater_scheme, templater_options, specs)
    generate_templates(templater_scheme, templater_options, specs)


if __name__ == "__main__":
    entrypoint()
