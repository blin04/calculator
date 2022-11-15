class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = tokens[self.position]

    def nextToken(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def accept(self, token):
        if token != self.current_token:
            # TODO: raise an error here
            print("Invalid syntax used!")
            exit()

        self.nextToken()

    def printTokens(self):
        while self.current_token is not None:
            print(self.current_token)
            self.nextToken()

    # methods for parsing

    def number(self):
        return

    def factor(self):
        return

    def term(self):
        return

    def expr(self):
        return

    # main method that parses the tokens
    def getTree(self):
        return
