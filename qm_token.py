from enum import Enum, auto


class TokenType(Enum):
    NUMBER = auto()
    VARIABLE = auto()
    OPERATOR = auto()
    PAREN_LEFT = auto()
    PAREN_RIGHT = auto()


class Associativity(Enum):
    LEFT = auto()
    RIGHT = auto()


class Token:
    def __init__(self, lexeme: str, type: TokenType) -> None:
        self.lexeme: str = lexeme
        self.type: TokenType = type

        values = self.__get_values()
        self.precedence = values[0] if values else None
        self.associativity = values[1] if values else None

    def print_data(self) -> None:
        print(f'{self.lexeme}: {self.type}')

    def __get_values(self) -> list:
        if (self.lexeme == '^'):
            return [4, Associativity.RIGHT]
        elif (self.lexeme == '*' or self.lexeme == '/'):
            return [3, Associativity.LEFT]
        elif (self.lexeme == '+' or self.lexeme == '-'):
            return [2, Associativity.LEFT]
        else:
            return None
