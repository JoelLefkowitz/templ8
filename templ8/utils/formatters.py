import re


def hyphen_to_underscore(string: str) -> str:
    return str(string).replace("-", "_")


def underscore_to_hyphen(string: str) -> str:
    return str(string).replace("_", "-")


def camelcase(string: str) -> str:
    return re.sub(r"(?!^)_([a-zA-Z])", lambda m: m.group(1).upper(), string)


def add_prefix(string: str, prefix: str) -> str:
    return prefix + "_" + string if prefix else string


def add_suffix(string: str, suffix: str) -> str:
    return string + "_" + suffix if suffix else string
