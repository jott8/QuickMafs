import re


def str_contains_regex(str: str, reg: str) -> bool:
    return not not re.search(reg, str)
