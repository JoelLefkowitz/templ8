import os
import sys
import ruamel.yaml  # type: ignore
from docopt import docopt, DocoptExit  # type: ignore
from inspect import cleandoc
from operator import itemgetter
from typing import Tuple

from pyimport import path_guard

path_guard("..")
from template_generator import generate_templates
from parser import parse_specs, parse_config
from config_creator import create_config
from exceptions import OutputDirInvalid, ConfigPathInvalid, InvalidCommand


cli = cleandoc(
    """
    Usage:
      templ8 create <output_dir>
      templ8 <config_path> <output_dir> [(--overwrite | --dry-run) --no-callbacks NAMES ...]

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

    create_new, config_path, output_dir, options = parse_cli(arguments)

    if create_new:
        create_config(output_dir)

    else:
        config, specs = parse_config(config_path), parse_specs(template_dir)
        print(specs)
        generate_templates(specs, config, output_dir, options)


def parse_cli(arguments: dict) -> Tuple[bool, str, str, dict]:

    create_new, config_path, output_dir = itemgetter(
        "create", "<config_path>", "<output_dir>"
    )(arguments)

    if not create_new and not os.path.exists(config_path):
        raise ConfigPathInvalid(config_path)

    if os.path.isfile(output_dir):
        raise OutputDirInvalid(output_dir)

    options = {
        "overwrite": arguments["--overwrite"],
        "dry-run": arguments["--dry-run"],
        "specified_names": arguments["NAMES"],
        "no_callbacks": arguments["--no-callbacks"],
    }
    return create_new, config_path, output_dir, options


# Remove
entrypoint()
