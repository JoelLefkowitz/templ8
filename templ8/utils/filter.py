from typing import Any, Callable, List


def unique_by_key(
    item_list: List[Any], key_function: Callable[[Any], Any]
) -> List[Any]:
    unique_dict = {key_function(i): i for i in item_list}
    return list(unique_dict.values())
