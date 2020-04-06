import os
from emoji import emojize


def pretty_log(msg: str) -> None:
    tophat = emojize(":tophat:", use_aliases=True)
    print(f"{tophat} {msg} {tophat}")


def pretty_heading(msg: str) -> str:
    heart = emojize(":heart:", use_aliases=True)
    return f"{heart} {msg} {heart}"


def inclusive_relpath(target: str, source: str) -> str:
    return os.path.join(os.path.basename(source), os.path.relpath(target, source))
