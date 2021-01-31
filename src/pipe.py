import converter
import ast.parser as parser
from typing import List

def parse_file(file : str):

    with open(file, "r") as fd:
        content = fd.read()
        p = parser.Parser()
        ast = p.parse(content)
        print(ast)

    return ast

def convert_ast(ast):

    return converter.convert(ast)

def handle_exception(exp):

    print(exp)

def pipe(files : List[str]):

    for file in files:

        try:

            ast = parse_file(file)
            ir  = convert_ast(ast)

        except Exception as e:
            handle_exception(e)