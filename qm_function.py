from qm_parser import Parser
from helper_functions import calc_postfix_x


class Function:
    def __init__(self, name, expr, var) -> None:
        self.name = name
        self.expr = expr
        self.var = var
        self.func = f'{self.name}({self.var}) = {self.expr}'

        self.p = Parser(expr, func_name=name, func_var=var)
        self.postfix = self.p.postfix_tokens

    def calc(self, x: float) -> float:
        return calc_postfix_x(self.postfix, x, self.var)
