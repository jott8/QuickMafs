from qm_token_type import TokenType


class Token:
    def __init__(self, lexeme: str, type: TokenType) -> None:
        self.lexeme = lexeme
        self.type = type

    def print_data(self):
        print(f'{self.lexeme}: {self.type}')
