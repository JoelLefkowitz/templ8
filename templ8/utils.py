import re
import os
from emoji import emojize
from typing import Any


def pretty_log(msg: str) -> None:
    TOPHAT = emojize(":tophat:", use_aliases=True)
    print(f"{TOPHAT}  {msg}")


def get_child_files(root):
    paths = []
    for rel_root, dirs, files in os.walk(root):
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")

        paths += [os.path.join(rel_root, file) for file in files]
    return paths


def inclusive_relpath(target: str, source: str) -> str:
    return os.path.join(os.path.basename(source), os.path.relpath(target, source))


def underscore_to_camelcase(name: str) -> str:
    return re.sub(r"(?!^)_([a-zA-Z])", lambda m: m.group(1).upper(), name)


def to_app_name(name: str) -> str:
    return str(name).replace("-", "_") + "_app"


def to_camelcase_app_name(name: str) -> str:
    return underscore_to_camelcase(to_app_name(name))


def to_server_name(name: str) -> str:
    return str(name).replace("-", "_") + "_server"
