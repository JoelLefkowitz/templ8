import re
import os
from emoji import emojize
from typing import Optional, Tuple
from pyimport import path_guard

path_guard("..")
from exceptions import UnrecognisedFormatter


def pretty_log(msg: str) -> None:
    tophat = emojize(":tophat:", use_aliases=True)
    print(f"{tophat} {msg} {tophat}")


def pretty_heading(msg: str) -> str:
    heart = emojize(":heart:", use_aliases=True)
    return f"{heart} {msg} {heart}"


def inclusive_relpath(target: str, source: str) -> str:
    return os.path.join(os.path.basename(source), os.path.relpath(target, source))


def format_str(
    string: str,
    formatter: str,
    prefix: Optional[str] = None,
    suffix: Optional[str] = None,
):

    if formatter == "hyphen_to_underscore":
        return str(string).replace("-", "_")

    elif formatter == "underscore_to_hyphen":
        return str(string).replace("_", "-")

    elif formatter == "camelcase":
        return re.sub(r"(?!^)_([a-zA-Z])", lambda m: m.group(1).upper(), string)

    elif formatter == "add_prefix":
        return prefix + "_" + string if prefix else string

    elif formatter == "add_suffix":
        return string + "_" + suffix if suffix else string

    else:
        raise UnrecognisedFormatter(string, formatter)


def is_kv(string: str) -> bool:
    return re.match("\w+=[^=]+", string) is not None


def get_kv(string: str) -> Tuple[str, str]:
    k, v = string.split("=", 1)
    return (k, v)
