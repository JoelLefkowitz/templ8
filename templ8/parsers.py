import ruamel.yaml
from typing import List
from walkman import get_child_files
from pyimport import path_guard

path_guard("..")
from spec import Spec
from context import Context, ChildContext


def parse_config(config_path: str) -> dict:
    with open(config_path, "r") as stream:
        config = ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)
    return config


def find_specs(template_dir: str) -> dict:
    for spec_file in get_child_files(template_dir, "spec.yml", 1):
        with open(spec_file, "r") as stream:
            spec_dict = ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)
        yield spec_dict


def parse_specs(template_dir: str) -> List[Spec]:
    [
        Spec(spec_file["root_name"], template_dir, [], [], [])
        for spec_file in find_specs(template_dir)
    ]
