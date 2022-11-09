class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current = tokens[0]

    def nextToken(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.current = self.tokens[self.position]
        else:
            self.current = None

    def accept(self, token):
        if token != self.current:
            return False
        return True

    def printTokens(self):
        while self.current is not None:
            print(self.current)
            self.nextToken()

    # main method that parses the tokens
    def getTree(self):
        return
