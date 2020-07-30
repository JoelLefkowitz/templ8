import os
import sys
from inspect import cleandoc
from typing import Tuple

from docopt import DocoptExit  # type: ignore
from docopt import docopt

from .exceptions import InvalidCommand, InvalidConfigPath, InvalidOutputDir
from .templater.options import TemplaterOptions
from .templater.scheme import TemplaterScheme

docopts_cli = cleandoc(
    """
    Usage:
        templ8 <config_path> 
               [--output-dir <output_dir>]
               [--template-dirs <template_dirs>]...
               [--specified-files <specified_files>]... 
               [--silent --overwrite --assume-yes --skip-callbacks]

    Options:
      --silent          Supress stdout and assume automatic yes to prompts
      --overwrite       Allow existing files to be overwritten
      --assume-yes      Automatic yes to prompts
      --skip-callbacks  Don't run callbacks
    """
)


def parse_cli() -> Tuple[TemplaterOptions, TemplaterScheme]:
    try:
        cli_arguments = docopt(docopts_cli)
    except DocoptExit:
        raise InvalidCommand(sys.argv[1:], docopts_cli)

    config_path = cli_arguments["<config_path>"]
    if not os.path.exists(config_path) or os.path.isdir(config_path):
        raise InvalidConfigPath(config_path)

    output_dir = cli_arguments["<output_dir>"] or os.path.dirname(config_path)
    if os.path.isfile(output_dir):
        raise InvalidOutputDir(output_dir)

    template_dirs = [
        *cli_arguments["<template_dirs>"],
        os.path.abspath(os.path.join(__file__, "../templates")),
    ]

    templater_scheme = TemplaterScheme(
        config_path, output_dir, template_dirs, cli_arguments["<specified_files>"]
    )

    templater_options = TemplaterOptions(
        cli_arguments["--silent"],
        cli_arguments["--overwrite"],
        cli_arguments["--assume-yes"],
        cli_arguments["--skip-callbacks"],
    )

    return templater_scheme, templater_options
