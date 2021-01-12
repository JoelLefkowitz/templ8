from typing import Any
from typing import List


def unique_by_name(item_list: List[Any]) -> List[Any]:
    unique_dict = {i.name: i for i in item_list}
    return list(unique_dict.values())
