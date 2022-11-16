class OpNode:
    """
    class used for representing operation
    nodes in AST
    """
    def __int__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class NumNode:
    """
    class used for representing number
    nodes in AST
    """
    def __int__(self, token):
        self.token = token
        self.value = token.value


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = tokens[self.position]

    def error(self):
        print("ParserError: Invalid syntax used!")
        exit()

    def nextToken(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def accept(self, token_type):
        if token_type != self.current_token.type:
            self.error()

        self.nextToken()

    def printTokens(self):
        while self.current_token is not None:
            print(self.current_token)
            self.nextToken()

    # methods for parsing

    def number(self):
        self.accept("NUMBER")

    def left_par(self):
        self.accept("LPAR")

    def right_par(self):
        self.accept("RPAR")

    def factor(self):
        # factor = number | lpar expr rpar
        token = self.current_token

        if token.type == "NUMBER":
            self.number()
            node = NumNode(token)
            return node

        elif token.type == "LPAR":
            node = self.expr()
            self.right_par()
            return node
        else:
            self.error()

    def term(self):
        return

    def expr(self):
        return

    # main method that parses the tokens
    def getTree(self):
        return
