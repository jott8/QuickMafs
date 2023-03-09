from qm_token import Token
from qm_token_type import TokenType
from functions import str_contains_regex

import re


class Lexer:
    def __init__(self, func_name: str, func_expr: str, func_var: str) -> None:
        self.func_name: str = func_name
        self.func_expr: str = func_expr
        self.func_var: str = func_var

        self.__rm_whitespaces()
        self.tokens: list[Token] = self.__create_tokens()

        print(
            f'\nInput: "{self.func_name}", "{self.func_expr}", "{self.func_var}"\n\n--> {self.func_name}({self.func_var}) = {self.func_expr}\n')

        for token in self.tokens:
            token.print_data()

        print()

    def __rm_whitespaces(self) -> None:
        self.func_expr = self.func_expr.replace(' ', '')

    def __create_tokens(self) -> list[Token]:
        tokens: list[Token] = []
        i = 0

        while i < len(self.func_expr):
            curr: str = self.func_expr[i]

            if (curr == self.func_var):
                tokens.append(Token(curr, TokenType.VARIABLE))
                i += 1
                continue

            elif (str_contains_regex(curr, '[(|)|^]')):
                tokens.append(Token(curr, TokenType.SEPERATOR))
                i += 1
                continue

            elif (str_contains_regex(curr, '[+|-|*|/]')):
                tokens.append(Token(curr, TokenType.OPERATOR))
                i += 1
                continue

            elif (str_contains_regex(curr, '[0-9]')):
                if (i == len(self.func_expr)-1):
                    tokens.append(Token(curr, TokenType.NUMBER))
                    i += 1
                    continue
                else:
                    j = i + 1
                    temp = curr
                    while (str_contains_regex(self.func_expr[j], '[0-9]')):
                        temp += self.func_expr[j]
                        j += 1
                    tokens.append(Token(temp, TokenType.NUMBER))
                    i = j
                    continue

            else:
                i += 1

        return tokens
