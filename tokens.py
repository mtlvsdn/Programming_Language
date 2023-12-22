class Token:
    def __init__(self, typename, value):
        self.typename = typename
        self.value = value

    def __repr__(self):
        return str(self.value)


class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)


class Float(Token):
    def __init__(self, value):
        super().__init__("FLT", value)


class Variable(Token):
    def __init__(self, value):
        super().__init__("VAR", value)


class Operation(Token):
    def __init__(self, value):
        super().__init__("OPR", value)


class Declaration(Token):
    def __init__(self, value):
        super().__init__("DEC", value)


class Boolean(Token):
    def __init__(self, value):
        super().__init__("BOL", value)


class Comparison(Token):
    def __init__(self, value):
        super().__init__("CMP", value)


class Reserved(Token):
    def __init__(self, value):
        super().__init__("RES", value)