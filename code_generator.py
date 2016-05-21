INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, LPAREN, RPAREN, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', '(', ')', 'EOF'
)


class CodeGenerator(object):
    def __init__(self, orders_list):
        self.orders_list = orders_list

    def postorder(self, tree):
        if type(tree).__name__ == 'BinOp':
            self.postorder(tree.left)
            self.postorder(tree.right)
            if tree.token.type == PLUS:
                self.orders_list.append('add')
            elif tree.token.type == MINUS:
                self.orders_list.append('sub')
            elif tree.token.type == MULTIPLY:
                self.orders_list.append('mul')
            elif tree.token.type == DIVIDE:
                self.orders_list.append('div')
        else:
            self.orders_list.append('\"put %s\"' % tree.value)
