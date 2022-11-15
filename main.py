
# TODO: 1. fix parser, 2. choose what tree to construct (parse or ast), 3. create class for tree

from lexer import Lexer
from parser import Parser

if __name__ == '__main__':
    expression = input()

    lexer = Lexer(expression)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    parser.printTokens()

