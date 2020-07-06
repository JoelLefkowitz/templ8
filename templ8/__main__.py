import os
import sys
from docopt import docopt, DocoptExit  # type: ignore
from inspect import cleandoc
from typing import List
from dataclasses import dataclass
from exceptions import InvalidOutputDir, InvalidCommand, InvalidConfigPath

# TODO Load default context values into config
# TODO Check nominal config is sufficient

cli = cleandoc(
    """
    Usage:
        templ8 <config_path> 
               [--output-dir <output_dir>]
               [--template-dirs <template_dirs>]...
               [--specified-files <specified_files>]... 
               [(--overwrite | --dry-run) --skip-callbacks]

    Options:
      --dry-run
      --overwrite
      --skip-callbacks
    """
)


@dataclass
class TemplaterOptions:
    dry_run: bool
    overwrite: bool
    skip_callbacks: bool


@dataclass
class TemplaterScheme:
    config_path: str
    output_dir: str
    template_dirs: List[str]
    specified_files: List[str]
    options: TemplaterOptions


def entrypoint() -> None:
    try:
        cli_arguments = docopt(cli)
    except DocoptExit:
        raise InvalidCommand(sys.argv[1:], cli)

    config_path = cli_arguments["<config_path>"]
    if not os.path.exists(config_path):
        raise InvalidConfigPath(config_path)

    output_dir = cli_arguments["<output_dir>"] or os.path.dirname(config_path)
    if os.path.isfile(output_dir):
        raise InvalidOutputDir(output_dir)

    options = TemplaterOptions(
        cli_arguments["--overwrite"],
        cli_arguments["--dry-run"],
        cli_arguments["--skip-callbacks"],
    )

    templater_scheme = TemplaterScheme(
        config_path,
        output_dir,
        cli_arguments["<template_dirs>"],
        cli_arguments["<specified_files>"],
        options,
    )


if __name__ == "__main__":
    entrypoint()
