import os, sys, shutil
import ruamel.yaml  # type: ignore
from inspect import cleandoc
from typing import List, Tuple, Any
from docopt import docopt  # type: ignore
from pathlib import Path
from glob import iglob
from jinja2 import Environment, FileSystemLoader

import sys

sys.path.append("..")
from .exceptions import OutputDirInvalid, ConfigPathInvalid
from .utils import pretty_log, get_child_files, stringer
from .models import Context, Spec, Alias


CLI = cleandoc(
    """
    Usage:
      template <config_path> <output_dir> [--overwrite --dry-run]

    Options:
      --overwrite
      --dry-run
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
        {"src": Alias(Context("name"), lambda x: stringer(x))},
    ),
    Spec(
        "webapp",
        [Context("github_url"),],
        {
            "app": Alias(Context("name"), lambda x: stringer(x) + "_app"),
            "server": Alias(Context("name"), lambda x: stringer(x) + "_server"),
        },
    ),
]


def entrypoint() -> None:
    arguments = docopt(CLI)
    config_path, output_dir = arguments["<config_path>"], arguments["<output_dir>"]
    options = {"overwrite": arguments["--overwrite"], "dry-run": arguments["--dry-run"]}

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
    context_dict.update(
        {
            folder_name: spec.folder_aliases[folder_name].resolve(config)
            for spec in specs
            for folder_name in spec.folder_aliases
        }
    )

    for spec in specs:

        spec_root = os.path.join(os.path.dirname(__file__), spec.root_name)
        for file in get_child_files(spec_root):

            rel_input_path = os.path.relpath(file, spec_root)
            folder_path, filename = os.path.split(rel_input_path)

            for folder_name in spec.folder_aliases:
                folder_path = folder_path.replace(
                    folder_name, spec.folder_aliases[folder_name].resolve(config)
                )

            output_path = os.path.join(output_dir, folder_path, filename)

            loader = Environment(
                loader=FileSystemLoader(spec_root),
                trim_blocks=True,
                lstrip_blocks=True,
                keep_trailing_newline=True,
            )
            template = loader.get_template(rel_input_path)
            Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)

            if os.path.exists(output_path) and not options["overwrite"]:
                pretty_log(output_path + " exists; skipping")

            elif options["dry-run"]:
                pretty_log("Would write: " + output_path)

            else:
                with open(output_path, "w") as f:
                    f.write(template.render(context_dict))
                    pretty_log("Generated: " + output_path)
