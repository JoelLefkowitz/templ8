import os
import sys
import shutil
import ruamel.yaml  # type: ignore
from inspect import cleandoc
from typing import List, Tuple, Any
from docopt import docopt  # type: ignore
from pathlib import Path
from glob import iglob
from jinja2 import Template

from pyimport import path_guard

path_guard(__file__, "..")
from exceptions import OutputDirInvalid, ConfigPathInvalid
from models import Context, Spec, Alias, Callback
from utils import pretty_log


CLI = cleandoc(
    """
    Usage:
      templ8 <config_path> <output_dir> [NAMES ...] [--overwrite --dry-run]

    Options:
      --overwrite
      --dry-run
    """
)

webapp_alias = Alias(Context("name"), lambda x: str(x).replace("-", "_") + "_app")
webserver_alias = Alias(Context("name"), lambda x: str(x).replace("-", "_") + "_server")

SPECS = [
    Spec(
        root_name="common",
        context_set=[
            Context("name"),
            Context("version", "0.1.0"),
            Context("description"),
            Context("author"),
        ],
    ),
    Spec(
        root_name="package",
        context_set=[
            Context("author_email"),
            Context("author_github"),
            Context("github_url"),
            Context("twine_username"),
        ],
        folder_aliases={"src": Alias(Context("name"))},
    ),
    Spec(
        root_name="webapp",
        dependencies=["common"],
        context_set=[Context("github_url"),],
        folder_aliases={"webapp": webapp_alias,},
        callbacks=[
            Callback(
                [
                    "ng",
                    "new",
                    "--routing=true",
                    "--style=scss",
                    webapp_alias,
                    "--directory",
                    webapp_alias,
                ]
            )
        ],
    ),
    Spec(
        root_name="server",
        dependencies=["webapp"],
        folder_aliases={"server": webserver_alias,},
        callbacks=[
            Callback(["django-admin", "startproject", webserver_alias, webserver_alias])
        ],
    ),
]


def entrypoint() -> None:
    arguments = docopt(CLI)
    config_path, output_dir = arguments["<config_path>"], arguments["<output_dir>"]
    options = {
        "overwrite": arguments["--overwrite"],
        "dry-run": arguments["--dry-run"],
        "specified_names": arguments["NAMES"],
    }

    if not os.path.exists(config_path):
        raise ConfigPathInvalid(config_path)

    if os.path.isfile(output_dir):
        raise OutputDirInvalid(output_dir)

    with open(config_path, "r") as stream:
        config = ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)

    main(config, output_dir, options)


def main(config: dict, output_dir: str, options: dict) -> None:
    templates_dir = os.path.dirname(__file__)
    specs = [spec for spec in SPECS if spec.check_condition(config)]
    context_dict = bundle_context(config, specs)

    for spec in specs:
        for template, output_path in spec.load_templates(
            config, templates_dir, output_dir
        ):
            generate_output(template, output_path, context_dict, options)

        for callback in spec.callbacks:
            if options["dry-run"] or options["specified_names"]:
                pretty_log(f"Would callback: {callback.call}")
            else:
                callback.run(config, output_dir)


def bundle_context(config, specs) -> dict:
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
    return context_dict


def generate_output(
    template: Template, output_path: str, context_dict: dict, options: dict
) -> None:
    filename = os.path.basename(os.path.normpath(output_path))

    if options["specified_names"] and filename not in options["specified_names"]:
        pretty_log(output_path + " not in NAMES; skipping")

    elif os.path.exists(output_path) and not options["overwrite"]:
        pretty_log(output_path + " exists; skipping")

    elif options["dry-run"]:
        pretty_log("Would write: " + output_path)

    else:
        Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(template.render(context_dict))
            pretty_log("Generated: " + output_path)
