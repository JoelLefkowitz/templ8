import os
import sys
import ruamel.yaml  # type: ignore
from docopt import docopt, DocoptExit  # type: ignore
from inspect import cleandoc
from operator import itemgetter
from typing import Tuple

from pyimport import path_guard

path_guard("..")
from template_generator import generate_template
from config_generator import generate_config
from exceptions import OutputDirInvalid, ConfigPathInvalid, InvalidCommand


cli = cleandoc(
    """
    Usage:
      templ8 <config_path> <output_dir> [--overwrite | --dry-run] [--no-callbacks] [NAMES ...]
      templ8 generate

    Options:
      --overwrite
      --dry-run
      --no-callbacks
    """
)

template_dir = os.path.join(os.path.dirname(__file__), "templates")


def entrypoint() -> None:
    try:
        arguments = docopt(cli)
    except DocoptExit:
        raise InvalidCommand(sys.argv[1:], cli)

    generate, config_path, output_dir, options = parser(arguments)

    if generate:
        generate_config()

    else:
        with open(config_path, "r") as stream:
            config = ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)

        generate_template(config, template_dir, output_dir, options)


def parser(arguments: dict) -> Tuple[bool, str, str, dict]:

    generate, config_path, output_dir = itemgetter(
        "generate", "<config_path>", "<output_dir>"
        )(arguments)

    if not os.path.exists(config_path):
        raise ConfigPathInvalid(config_path)

    if os.path.isfile(output_dir):
        raise OutputDirInvalid(output_dir)

    options = {
        "overwrite": arguments["--overwrite"],
        "dry-run": arguments["--dry-run"],
        "specified_names": arguments["NAMES"],
        "no_callbacks": arguments["--no-callbacks"],
    }
    return generate, config_path, output_dir, options
