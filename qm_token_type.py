from enum import Enum, auto


class TokenType(Enum):
    NUMBER = auto()
    VARIABLE = auto()
    OPERATOR = auto()
    SEPERATOR = auto()
