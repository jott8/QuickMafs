from qm_token import Token, TokenType

import re
import time
import copy


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


def calc_postfix(postfix_tokens) -> float:
    # TODO check data type in stack
    input_queue: list[Token] = copy.deepcopy(postfix_tokens)
    stack = []

    while (input_queue):
        curr_token = input_queue.pop(0)

        if (curr_token.type == TokenType.NUMBER):
            stack.append(curr_token.lexeme)
        elif (curr_token.type == TokenType.OPERATOR):
            if (len(stack) >= 2):
                str_val1 = stack.pop()
                str_val2 = stack.pop()
                val1 = float(str_val1)
                val2 = float(str_val2)

                stack.append(
                    str(calc_token(curr_token.lexeme, val1, val2)))
            else:
                stack.append(calc_token(
                    curr_token.lexeme, float(stack.pop()), float(input_queue.pop(0).lexeme)))

    return float(stack[0])


def calc_postfix_x(postfix_tokens, x: float, func_var) -> float:
    # TODO check data type in stack
    input_queue: list[Token] = copy.deepcopy(postfix_tokens)
    stack = []

    while (input_queue):
        curr_token = input_queue.pop(0)

        if (curr_token.type == TokenType.NUMBER or curr_token.type == TokenType.VARIABLE):
            stack.append(curr_token.lexeme)
        elif (curr_token.type == TokenType.OPERATOR):
            if (len(stack) >= 2):
                str_val1 = stack.pop()
                str_val2 = stack.pop()

                if (str_val1 == func_var and str_val2 == func_var):
                    val1 = x
                    val2 = x
                elif (str_val1 == func_var):
                    val1 = x
                    val2 = float(str_val2)
                elif (str_val2 == func_var):
                    val1 = float(str_val1)
                    val2 = x
                else:
                    val1 = float(str_val1)
                    val2 = float(str_val2)

                stack.append(
                    str(calc_token(curr_token.lexeme, val1, val2)))
            else:
                stack.append(calc_token(
                    curr_token.lexeme, float(stack.pop()), float(input_queue.pop(0).lexeme)))

    return float(stack[0])


def calc_token(lexeme: str, val1: float, val2: float) -> float:
    if (lexeme == '+'):
        return val1 + val2
    elif (lexeme == '-'):
        return val2 - val1
    elif (lexeme == '*'):
        return val1 * val2
    elif (lexeme == '/'):
        return val2 / val1
    elif (lexeme == '^'):
        return val2**val1
