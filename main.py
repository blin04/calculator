
# TODO: 1. fix parser, 2. choose what tree to construct (parse or ast), 3. create class for tree

from lexer import Lexer
from parser import Parser

if __name__ == '__main__':
    expression = input()

    lexer = Lexer(expression)
    lexer.tokenize()

    print(len(lexer.tokens))

    for t in lexer.tokens:
        print(t)
