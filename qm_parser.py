from qm_token import Token, TokenType, Associativity
from functions import str_contains_regex

import copy


class Parser:
    def __init__(self, func_name: str, func_expr: str, func_var: str) -> None:
        self.func_name: str = func_name
        self.func_expr: str = func_expr
        self.func_var: str = func_var

        self.tokens: list[Token] = self.__create_tokens()
        self.postfix_tokens: list[Token] = self.__to_postfix()
        self.print_data()

    def print_data(self) -> None:
        print(
            f'\nInput: "{self.func_name}", "{self.func_expr}", "{self.func_var}"\n\nAs function: {self.func_name}({self.func_var}) = {self.func_expr}\n')

        print('Tokens:')
        for token in self.tokens:
            token.print_data()

        print(f'\nPostfix:\n{self.postfix_str()}\n')

    def __rm_whitespaces(self) -> None:
        self.func_expr = self.func_expr.replace(' ', '')

    # Lexical analysis
    def __create_tokens(self) -> list[Token]:
        tokens: list[Token] = []
        i = 0

        while i < len(self.func_expr):
            curr: str = self.func_expr[i]

            if (curr == self.func_var):
                tokens.append(Token(curr, TokenType.VARIABLE))
                i += 1
                continue

            elif (curr == '('):
                tokens.append(Token(curr, TokenType.PAREN_LEFT))
                i += 1
                continue

            elif (curr == ')'):
                tokens.append(Token(curr, TokenType.PAREN_RIGHT))
                i += 1
                continue

            elif (str_contains_regex(curr, '[+|\-|*|/|^]')):
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
                    while (str_contains_regex(self.func_expr[j], '[0-9]') and j != len(self.func_expr)-1):
                        temp += self.func_expr[j]
                        j += 1
                    tokens.append(Token(temp, TokenType.NUMBER))
                    i = j
                    continue

            else:
                i += 1

        return tokens

    def __shunting_yard(self) -> None:
        pass

    def __to_postfix(self) -> list[Token]:
        # Rules: https://aquarchitect.github.io/swift-algorithm-club/Shunting%20Yard/

        # Input queue -> self.tokens
        # Operator stack
        # Output queue

        # list, pop(0) --> queue
        # list, pop() --> stack

        input_queue: list[Token] = copy.deepcopy(self.tokens)
        output_queue: list[Token] = []
        operator_stack: list[Token] = []

        while (input_queue):
            curr_token = input_queue.pop(0)

            if (curr_token.type == TokenType.OPERATOR):
                if (operator_stack):
                    while (operator_stack[-1].type == TokenType.OPERATOR and ((curr_token.associativity == Associativity.LEFT and curr_token.precedence <= operator_stack[-1].precedence) or (curr_token.associativity == Associativity.RIGHT and curr_token.precedence < operator_stack[-1].precedence))):
                        output_queue.append(operator_stack.pop())
                operator_stack.append(curr_token)
            elif (curr_token.type == TokenType.PAREN_LEFT):
                operator_stack.append(curr_token)
            elif (curr_token.type == TokenType.PAREN_RIGHT):
                while (operator_stack[-1].type != TokenType.PAREN_LEFT):
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()
            else:
                output_queue.append(curr_token)

        while (operator_stack):
            output_queue.append(operator_stack.pop())

        return output_queue

    def calc_postfix(self):
        input_queue: list[Token] = copy.deepcopy(self.postfix_tokens)
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
                        str(self.__calc_token(curr_token, val1, val2)))
                else:
                    stack.append(self.__calc_token(
                        curr_token, float(stack.pop()), float(input_queue.pop(0).lexeme)))

        print(stack[0])

    def __calc_token(self, token: Token, val1: float, val2: float) -> float:
        if (token.lexeme == '+'):
            return val1 + val2
        elif (token.lexeme == '-'):
            return val2 - val1
        elif (token.lexeme == '*'):
            return val1 * val2
        elif (token.lexeme == '/'):
            return val2 / val1

    def postfix_str(self) -> str:
        string = ''

        for pf in self.postfix_tokens:
            string = string + pf.lexeme + ' '

        return string