"""
Calculator implementation in python

tokens = lexer(expression)
tree = parser(tokens)
evaluate(tree)

"""
from lexer import tokenize
from parser import Parser

if __name__ == '__main__':
    expression = input()

    tokens = tokenize(expression)
    parser = Parser(tokens)

    parser.printTokens()

    print(tokens)
