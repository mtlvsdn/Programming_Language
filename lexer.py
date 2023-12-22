from tokens import Integer, Float, Variable, Declaration, Boolean, Reserved, Operation

class Lexer:
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    declarations = ["creeaza"]
    boolean = ["si", "sau", "negat"]
    comparisons = [">", "<", ">=", "<=", "nu egal"]
    #specialCharacters = ["Diana"]
    reserved = ["daca", "daltfel", "altfel", "fa", "cat timp", "Diana"]
    operations = "+-/*^@"
    stopwords = [" "]

    def __init__(self, text):
        self.text = text
        self.index = 0
        self.tokens = []
        self.char = self.text[self.index]
        self.token = None


    def tokenize(self):
        while self.index < len(self.text):
            if self.char in Lexer.digits:
                self.token = self.extract_number()

            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.move()

            elif self.char in Lexer.stopwords:
                self.move()
                continue

            elif self.char in Lexer.letters:
                word = self.extract_word()
                if word in Lexer.declarations:
                    self.token = Declaration(word)
                elif word in Lexer.boolean:
                    self.boolean = Boolean(word)
                elif word in Lexer.reserved:
                    self.token = Reserved(word)
                else:
                    self.token = Variable(word)

            self.tokens.append(self.token)
        return self.tokens

    def extract_word(self):
        word = ""
        while self.char in Lexer.letters and self.index < len(self.text):
            word += self.char
            self.move()
        return word

    def extract_number(self):
        number = ""
        is_float = False
        while (self.char in Lexer.digits or self.char == ".") and (self.index < len(self.text)):
            if self.char == ".":
                is_float = True
            number += self.char
            self.move()
        if is_float is False:
            return Integer(number)
        else:
            return Float(number)

    def move(self):
        self.index += 1
        if self.index < len(self.text):
            self.char = self.text[self.index]