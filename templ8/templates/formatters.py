import re


def underscore_to_camelcase(name: str) -> str:
    return re.sub(r"(?!^)_([a-zA-Z])", lambda m: m.group(1).upper(), name)


def to_app_name(name: str) -> str:
    return str(name).replace("-", "_") + "_app"


def to_camelcase_app_name(name: str) -> str:
    return underscore_to_camelcase(to_app_name(name))


def to_server_name(name: str) -> str:
    return str(name).replace("-", "_") + "_server"
