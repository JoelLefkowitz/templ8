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
from utils import pretty_log, to_app_name, to_camelcase_app_name, to_server_name


def entrypoint() -> None:
    arguments = docopt(CLI)
    config_path, output_dir = arguments["<config_path>"], arguments["<output_dir>"]
    template_dir = os.path.dirname(__file__)
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

    main(config, template_dir, output_dir, options)


def main(config: dict, template_dir: str, output_dir: str, options: dict) -> None:
    specs = [spec for spec in SPECS if spec.check_condition(config)]
    context_dict = bundle_context(config, specs)

    for spec in specs:
        skipped_any = False
        for template, output_path in spec.load_templates(
            config, template_dir, output_dir
        ):
            success = generate_output(template, output_path, context_dict, options)
            if not success:
                skipped_any = True

        for callback in spec.callbacks:
            if skipped_any:
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
) -> bool:
    filename = os.path.basename(os.path.normpath(output_path))

    if options["specified_names"] and filename not in options["specified_names"]:
        pretty_log(output_path + " not in NAMES; skipping")
        return False

    if os.path.exists(output_path) and not options["overwrite"]:
        pretty_log(output_path + " exists; skipping")
        return False

    if options["dry-run"]:
        pretty_log("Would write: " + output_path)
        return False

    Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(template.render(context_dict))
        pretty_log("Generated: " + output_path)
    return True
