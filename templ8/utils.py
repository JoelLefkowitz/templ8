import os
from emoji import emojize
from itertools import takewhile, count


def pretty_log(msg: str) -> None:
    tophat = emojize(":tophat:", use_aliases=True)
    print(f"{tophat} {msg} {tophat}")


def pretty_heading(msg: str) -> None:
    heart = emojize(":heart:", use_aliases=True)
    return f"# {heart} {msg} {heart}"


def inclusive_relpath(target: str, source: str) -> str:
    return os.path.join(os.path.basename(source), os.path.relpath(target, source))


def is_tag(string: str) -> bool:
    return string.startswith("<") and string.endswith(">")


def strip_tag(string: str) -> str:
    return string[1:-1]
