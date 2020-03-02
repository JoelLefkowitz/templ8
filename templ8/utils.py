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


def stringer(raw: Any) -> str:
    return str(raw).replace("-", "_")