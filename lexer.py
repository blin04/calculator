"""
Task of the lexer is to divide expression into tokens,
following some grammar

GRAMMAR:

old grammar
<izraz> = <broj> | <mnozenje> | <sabiranje>
sabiranje = <mnozenje> ( <operator_sabiranja> <mnozenje> )*
mnozenje = <atom> ( <operator_mnozenja> <atom> )*
<atom> = <broj> | <izraz_u_zagradi>
<izraz_u_zagradi> = <izraz>
"""
# TODO: make lexer class
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def skip_blank(text):

    result = ""
    for t in text:
        if t != " ":
            result += t

    return result


def tokenize(expr):
    size = len(expr)
    tokens = []

    expr = skip_blank(expr)

    # going through expression and
    # recognizing tokens

    i = 0
    while i < size:
        if expr[i] in DIGITS and expr[i] != '0':
            tokens.append("NUMBER")

            while i + 1 < size and expr[i + 1] in DIGITS:
                i += 1

        elif expr[i] == "*":
            tokens.append("MUL")

        elif expr[i] == "/":
            tokens.append("DIV")

        elif expr[i] == "+":
            tokens.append("ADD")

        elif expr[i] == "-":
            tokens.append("SUB")
        else:
            print("found invalid token during tokenization")
            return

        i += 1

    return tokens


