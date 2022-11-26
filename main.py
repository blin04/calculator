
# TODO: evalute tree

from lexer import Lexer
from parser import Parser

if __name__ == '__main__':
    expression = input()

    lexer = Lexer(expression)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    print(parser.tokens)
    start_node = parser.expr()

    print(start_node)
