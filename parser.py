class OpNode:
    """
    class used for representing operation
    nodes in AST
    """
    def __init__(self, left=None, op=None, right=None):
        self.op = op        # operation token
        self.left = left    # node
        self.right = right  # node

    def __str__(self):
        left = str(self.left)
        op = str(self.op)
        right = str(self.right)
        return left + ", " + op + ", " + right

    def __repr__(self):
        left = repr(self.left)
        op = repr(self.op)
        right = repr(self.right)
        return "LEFT: " + left + " | OP: " + op + " | RIGHT: " + right


class NumNode:
    """
    class used for representing number
    nodes in AST
    """
    def __init__(self, token=None):
        # number token
        self.token = token
        self.value = token.value

    def __str__(self):
        return str(self.token)

    def __repr__(self):
        return repr(self.token)


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
        while self.current_token != "EOF":
            print(self.current_token)
            self.nextToken()

    # methods for parsing

    def atom(self):
        # atom = number | lpar expr rpar

        if self.current_token.type == "NUMBER":
            node = NumNode(self.current_token)
            self.accept("NUMBER")
            return node

        elif self.current_token.type == "LPAR":
            self.accept("LPAR")
            node = self.expr()
            self.accept("RPAR")
            return node
        else:
            self.error("Atom")

    def factor(self):
        """
        parsing factors
        factor = atom (pow atom)*
        :return: returns a node of AST (OpNode)
        """

        node = self.atom()

        while self.current_token.type == "POW":
            operation = self.current_token
            self.accept("POW")

            node = OpNode(node, operation, self.factor())

        return node

    def term(self):
        """
        parsing terms
        term = factor ({mul, div}, factor)*
        :return: returns a node of AST (OpNode)
        """

        node = self.factor()

        while self.current_token.type in ("MUL", "DIV"):
            operation = None
            if self.current_token.type == "MUL":
                operation = self.current_token
                self.accept("MUL")
            elif self.current_token.type == "DIV":
                operation = self.current_token
                self.accept("DIV")

            node = OpNode(node, operation, self.factor())

        return node

    def expr(self):
        """
        parsing expressions
        expr = term ({add, sub} term) *
        :return: returns a node of AST (OpNode)
        """
        node = self.term()

        while self.current_token.type in ("ADD", "SUB"):
            operation = None
            if self.current_token.type == "ADD":
                operation = self.current_token
                self.accept("ADD")
            elif self.current_token.type == "SUB":
                operation = self.current_token
                self.accept("SUB")

            node = OpNode(node, operation, self.term())

        return node


def Evaluate(node):
    if type(node) is NumNode:
        return node.value

    left_val = None
    right_val = None

    if node.left is not None:
        left_val = Evaluate(node.left)

    if node.right is not None:
        right_val = Evaluate(node.right)

    if node.op.type == "ADD":
        return left_val + right_val
    elif node.op.type == "SUB":
        return left_val - right_val
    elif node.op.type == "MUL":
        return left_val * right_val
    elif node.op.type == "DIV":
        return left_val / right_val
    elif node.op.type == "POW":
        return left_val ** right_val
    else:
        print("Error: Can't evaluate expression")
        exit()
