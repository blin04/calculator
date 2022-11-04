"""
Calculator implementation in python

tokens = lexer(expression)
tree = parser(tokens)
evaluate(tree)

"""
from lexer import tokenize

if __name__ == '__main__':
    expression = input()

    tokens = tokenize(expression)

    print(tokens)
