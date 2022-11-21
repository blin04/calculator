class OpNode:
    """
    class used for representing operation
    nodes in AST
    """
    def __int__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return

    def __repr__(self):
        return


class NumNode:
    """
    class used for representing number
    nodes in AST
    """
    def __int__(self, token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return

    def __repr__(self):
        return


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = tokens[self.position]

    def error(self, location):
        print("ParserError: Invalid syntax used!")
        print("Called from " + location)
        exit()

    def nextToken(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def accept(self, token_type):
        if token_type != self.current_token.type:
            self.error("Accept")

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
        print(self.current_token.type)

        if self.current_token.type == "NUMBER":
            node = NumNode()
            node.token = self.current_token
            node.value = self.current_token.value
            self.number()
            return node

        elif self.current_token.type == "LPAR":
            node = self.expr()
            self.right_par()
            return node
        else:
            self.error("Factor")

    def term(self):
        """
        parsing terms
        term = factor ({mul, div}, factor)
        :return: returns a node of AST (OpNode)
        """
        node = OpNode()

        print("Trying to parse factor")
        node.left = self.factor()

        while self.current_token.type in ("MUL", "DIV"):
            print("Entered loop")
            if self.current_token.type == "MUL":
                self.accept("MUL")
                node.op = self.current_token
            elif self.current_token.type == "DIV":
                self.accept("DIV")
                node.op = self.current_token

            node.right = self.factor()

        return node

    def expr(self):
        """
        parsing expressions
        expr = term ({add, sub} term) *
        :return: returns a node of AST (OpNode)
        """
        node = OpNode()

        node.left = self.term()

        print("Sucessfully parsed first term")

        while self.current_token.type in ("ADD", "SUB"):
            if self.current_token.type == "ADD":
                node.op = self.current_token
                self.accept("ADD")
            elif self.current_token.type == "SUB":
                node.op = self.current_token
                self.accept("SUB")

        node.right = self.term()

        print("Parsed second term")

        return node

    # main method that parses the tokens
    def getTree(self):
        return
