
# TODO: 1. fix parser, 2. choose what tree to construct (parse or ast), 3. create class for tree

from lexer import Lexer
from parser import Parser

if __name__ == '__main__':
    expression = input()

    lexer = Lexer(expression)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    print(parser.tokens)
    start_node = parser.expr()

    print(start_node.left)
    print(start_node.op)
    print(start_node.right)


