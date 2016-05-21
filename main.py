from code_generator import CodeGenerator
from scanner import join_tokens, scan
from analyzer import Parser
import os

expr = raw_input('expression: ')

tokens = join_tokens(scan(expr))
parser = Parser(tokens)
tree = parser.parse()
code_generator = CodeGenerator(orders_list=[])
code_generator.postorder(tree)
code_generator.orders_list.append('end')
os.system("environment.py %s" % ' '.join(code_generator.orders_list))
