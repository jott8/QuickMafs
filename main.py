from qm import calc
from qm_parser import Parser
from qm_function import Function
from helper_functions import calc_postfix, calc_postfix_x


f = Function('f', 'x^2', 'x')
print(f.func)
print(f.calc(3))
