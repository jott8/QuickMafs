from qm_parser import Parser

p = Parser('f', '400-4', 'x')
# p = Parser('f', '4+4*2/(1-5)', 'x')
# p = Parser('f', '30*20', 'x')
# p = Parser('f', '400-4', 'x')
p.calc_postfix()
