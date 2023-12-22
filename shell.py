from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

while True:
    text = input("DianaScript: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    parser_name = Parser(tokens)
    tree = parser_name.parse()

    print(tree)
