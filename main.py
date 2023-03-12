from qm_parser import Parser

p = Parser('f', 'x^2', 'x')
p.print_data()
p.print_tokens()
p.print_postfix_str()
result = p.calc_postfix_x(3)
print(f'Result: {result}')
