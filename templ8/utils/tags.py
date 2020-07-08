def untag(string: str) -> str:
    return string[1:-1] if is_tag(string) else string


def is_tag(string) -> bool:
    return string.startswith("<") and string.endswith(">")
