import os
from pathlib import Path
from typing import Any

import ruamel.yaml


def load_yaml(yaml_path: str) -> Any:
    with open(yaml_path, "r") as stream:
        return ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)


def write_file(string: str, output_path: str) -> None:
    Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as stream:
        stream.write(string)


def contains_cache_dir(file_path: str) -> bool:
    return any(cache_dir in file_path for cache_dir in ["__pycache__", ".DS_Store", ".coverage"])
