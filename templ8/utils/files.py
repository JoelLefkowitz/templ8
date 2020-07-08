from typing import Any

import ruamel.yaml


def load_yaml(yaml_path: str) -> Any:
    with open(yaml_path, "r") as stream:
        return ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)
