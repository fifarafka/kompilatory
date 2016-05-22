from code_generator import CodeGenerator
from environment import Environment
from scanner import join_tokens, scan
from analyzer import Parser
#from environment import environment
import os

expr = raw_input('expression: ')
tokens = join_tokens(scan(expr))
print("STEP 1")
print("Generated token list: ")
print(tokens)
parser = Parser(tokens)
tree = parser.parse()
print("STEP 2")
print("Parsing token list to binary tree")
print (tree)
code_generator = CodeGenerator(orders_list=[])
code_generator.postorder(tree)
code_generator.orders_list.append('end')
print("STEP 3")
print("Postorder")
print(code_generator.orders_list)
environment = Environment(code_generator.orders_list)
result = environment.count()
print("RESULT: ")
print(result)
