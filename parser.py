class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.token = self.tokens[self.index]

    def factor(self):
        if self.token.typename == "INT" or self.token.typename == "FLT":
            return self.token
        elif self.token.value == "(":
            self.move()
            expression = self.boolean_expression()
            return expression
        elif self.token.value == "negat":
            operator = self.token
            self.move()
            output = [operator, self.boolean_expression()]
            return output
        elif self.token.type.startswith("VAR"):
            return self.token
        elif self.token.value == "+" or self.token.value == "-":
            operator = self.token
            self.move()
            operand = self.boolean_expression()
            return [operator, operand]


    # INMULTIRE / IMPARTIRE
    def term(self):
        left_node = self.factor()
        self.move()
        while self.token.value == "*" or self.token.value == "/":
            operator = self.token
            self.move()
            right_node = self.factor()
            self.move()

            left_node = [left_node, operator, right_node]
        return left_node

    # ADUNARE / SCADERE
    def expression(self):
        left_node = self.term()
        while self.token.value == "+" or self.token.value == "-":
            operator = self.token
            self.move()
            right_node = self.term()
            left_node = [left_node, operator, right_node]
        return left_node

    # COMPARATIE
    def comp_expression(self):
        left_node = self.expression()
        while self.token.type == "CMP":
            operator = self.token
            self.move()
            right_node = self.expression()
            left_node = [left_node, operator, right_node]
        return left_node

    def boolean_expression(self):
        left_node = self.comp_expression()
        while self.token.value == "si" or self.token.value == "sau":
            operator = self.token
            self.move()
            right_node = self.comp_expression()
            left_node = [left_node, operator, right_node]
        return left_node

    def parse(self):
        return self.expression()

    def variable(self):
        if self.token.type.startswith("VAR"):
            return self.token

    def statement(self):
        if self.token.type == "DEC":
            self.move()
            left_node = self.variable()
            self.move()
            if self.token.value == "=":
                operation = self.token
                self.move()
                right_node = self.boolean_expression()
                return [left_node, operation, right_node]
            elif self.token.type == "INT" or self.token.type == "FLT" or self.token.type == "OPR" or self.token.value == "negat":




    def move(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.token = self.tokens[self.index]
