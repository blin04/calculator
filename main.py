
# TODO: evalute tree

from lexer import Lexer
from parser import Parser, Evaluate

if __name__ == '__main__':
    expression = input()

    lexer = Lexer(expression)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    tree = parser.expr()

    print(Evaluate(tree))
