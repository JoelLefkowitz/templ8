import os, sys, shutil
import ruamel.yaml  # type: ignore
from inspect import cleandoc
from typing import List, Tuple, Any
from docopt import docopt  # type: ignore
from pathlib import Path
from glob import iglob

from jinja2 import Environment, FileSystemLoader
from exceptions import OutputDirInvalid, ConfigPathInvalid
from utils import pretty_log
from models import Context, Spec


CLI = cleandoc(
    """
    Usage:
      template <config_path> <output_dir> [--overwrite]

    Options:
      --overwrite
    """
)

SPECS = [
    Spec(
        "common",
        [
            Context("name"),
            Context("version", "0.1.0"),
            Context("description"),
            Context("author"),
        ],
    ),
    Spec(
        "package",
        [
            Context("author_email"),
            Context("author_github"),
            Context("github_url"),
            Context("twine_username"),
        ],
    ),
    Spec("webapp", []),
]


def entrypoint() -> None:
    arguments = docopt(CLI)
    config_path, output_dir = arguments["<config_path>"], arguments["<output_dir>"]
    options = {"overwrite": arguments["--overwrite"]}

    if not os.path.exists(config_path):
        raise ConfigPathInvalid(config_path)

    if os.path.isfile(output_dir):
        raise OutputDirInvalid(output_dir)

    with open(config_path, "r") as stream:
        config = ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)

    main(config, output_dir, options)


def main(config: dict, output_dir: str, options: dict) -> None:

    specs = [spec for spec in SPECS if spec.check_condition(config)]
    context_dict = dict(
        [
            context.emit_from_config(config)
            for spec in specs
            for context in spec.context_set
        ]
    )
    context_dict.update({spec.root_name: True for spec in specs})

    for spec in specs:

        spec_root = os.path.join(os.path.dirname(__file__), spec.root_name)
        for file in iglob(spec_root + "/**/*.*", recursive=True):

            file_rel_root = os.path.relpath(file, spec_root)
            output_path = os.path.join(output_dir, file_rel_root)

            loader = Environment(
                loader=FileSystemLoader(spec_root), trim_blocks=True, lstrip_blocks=True
            )
            template = loader.get_template(file_rel_root)
            Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)

            with open(output_path, "w") as f:

                if os.path.exists(output_path) and not options["overwrite"]:
                    pretty_log(output_path + "exists; skipping")

                else:
                    pretty_log("Generated: " + output_path)
                    f.write(template.render(context_dict))

    # Special package action:
    if context_dict["package"]:
        os.rename(os.path.join(output_dir, "src"), os.path.join(output_dir, context_dict["name"]))
