import os


def inclusive_relpath(target: str, source: str) -> str:
    return os.path.join(os.path.basename(source), os.path.relpath(target, source))
