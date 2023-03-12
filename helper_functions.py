import re
import time


def str_contains_regex(str: str, reg: str) -> bool:
    return not not re.search(reg, str)


def get_regex_match(str: str, reg: str) -> list[str]:
    return re.findall(reg, str)


def func_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time() - start
        print(f'{func.__name__} took {end} seconds to run')
        return res
    return wrapper
