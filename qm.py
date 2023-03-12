from qm_parser import Parser
from helper_functions import str_contains_regex, get_regex_match


# Expression must not contain variable
def calc(expression: str, *kwargs) -> float:
    for _ in range(len(expression)-1):
        if (not str_contains_regex(expression[_], '[0-9+\-*/^()]')):
            return None

    return Parser(expression).calc_postfix()
