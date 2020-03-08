import os
import ruamel.yaml  # type: ignore
from docopt import docopt  # type: ignore

from inspect import cleandoc

from pyimport import path_guard; path_guard("..")
from specs import specs
from exceptions import OutputDirInvalid, ConfigPathInvalid


cli = cleandoc(
    """
    Usage:
      templ8 <config_path> <output_dir> [--overwrite | --dry-run] [--no-callbacks] [NAMES ...]

    Options:
      --overwrite
      --dry-run
      --no-callbacks
    """
)

template_dir = os.path.join(os.path.dirname(__file__), "templates")


def entrypoint() -> None:
    arguments = docopt(cli)
    config_path, output_dir = arguments["<config_path>"], arguments["<output_dir>"]
    options = {
        "overwrite": arguments["--overwrite"],
        "dry-run": arguments["--dry-run"],
        "specified_names": arguments["NAMES"],
        "no_callbacks": arguments["--no-callbacks"],
    }

    if not os.path.exists(config_path):
        raise ConfigPathInvalid(config_path)

    if os.path.isfile(output_dir):
        raise OutputDirInvalid(output_dir)

    with open(config_path, "r") as stream:
        config = ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)

    main(config, template_dir, output_dir, options)
