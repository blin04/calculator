DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def is_digit(char):
    if char in DIGITS:
        return True
    return False


class Token:

    def __init__(self, token, value):
        self.type = token
        self.value = value

    def __str__(self):
        return self.type + " " + str(self.value)

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


class Lexer:

    def __init__(self, text):
        self.text = text
        self.tokens = []

    def compress(self):
        compressed_text = ""
        for char in self.text:
            if char != " ":
                compressed_text += char

        self.text = compressed_text

    def tokenize(self):
        self.compress()
        size = len(self.text)

        i = 0
        while i < size:
            token = Token("CURRENT", -1)

            if is_digit(self.text[i]) and self.text[i] != '0':
                value = int(self.text[i])

                while i + 1 < size and is_digit(self.text[i + 1]):
                    value *= 10
                    value += int(self.text[i + 1])
                    i += 1

                token.type = "NUMBER"
                token.value = value

            elif self.text[i] == '(':
                token.type = "LPAR"
                token.value = '('

            elif self.text[i] == ')':
                token.type = "RPAR"
                token.value = ')'

            elif self.text[i] == "+":
                token.type = "ADD"
                token.value = '+'

            elif self.text[i] == "-":
                token.type = "SUB"
                token.value = '-'

            elif self.text[i] == "*":
                token.type = "MUL"
                token.value = '*'

            elif self.text[i] == "/":
                token.type = "DIV"
                token.value = '/'
            else:
                print("LexerError: unrecognized symbol")
                exit()

            self.tokens.append(token)
            i += 1
        return self.tokens
