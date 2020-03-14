import os
from emoji import emojize


def pretty_log(msg: str) -> None:
    tophat = emojize(":tophat:", use_aliases=True)
    print(f"{tophat} {msg} {tophat}")


def pretty_heading(msg: str) -> None:
    heart = emojize(":heart:", use_aliases=True)
    return f"# {heart} {msg} {heart}"


def get_child_files(root):
    paths = []
    for rel_root, dirs, files in os.walk(root):
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")

        paths += [os.path.join(rel_root, file) for file in files]
    return paths


def inclusive_relpath(target: str, source: str) -> str:
    return os.path.join(os.path.basename(source), os.path.relpath(target, source))


def is_tag(string: str) -> bool:
    return string.startswith("<") and string.endswith(">")


def strip_tag(string: str) -> str:
    return string[1:-1]
