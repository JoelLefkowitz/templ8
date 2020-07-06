import re
from typing import Tuple


def is_kv(string: str) -> bool:
    return re.match("\w+=[^=]+", string) is not None


def get_kv(string: str) -> Tuple[str, str]:
    k, v = string.split("=", 1)
    return (k, v)
