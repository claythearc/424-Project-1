import re

def lex(identifier: str, symbols: dict,linenum: int) -> tuple:
    keywords = [
        'char',
        'int',
        'main',
        'bool',
        'while'
    ]
    operators = [
        "=",
        "+",
        "*",
        "/",
        "/",
        "<=",
        ">=",
        "==",
        "!="
    ]

    punctuation = [
        ";",
        ",",
        "(",
        ")",
        "{",
        "}",
        "`"
    ]

    boolean = [
        "true",
        "false"
    ]

    quotes = [
        "‘",
        "‘",
        "’"
    ]

    if len(identifier) == 3:  # 3 chars for 'f' and beyond
        if identifier[0] in quotes:
            # this is only reached if the 1st char of the string is not alpha numeric
            if identifier[2] in quotes:
                # this is only reached if the last char if the string is not alpha numeric
                if identifier[1].isalpha():
                    return ("char", identifier[1]), symbols
    if identifier in keywords:
        return ("keyword", identifier), symbols
    if identifier.isalpha():
        symbols[identifier] = symbols.get(identifier, linenum)
        return ("identifier", identifier), symbols
    if identifier.isdigit():
        return ("integer", identifier), symbols
    if identifier.isnumeric():
        return ("digit", identifier), symbols
    if identifier in boolean:
        return ("boolean", identifier), symbols
    if identifier in operators:
        return ("operator", identifier), symbols
    if identifier in punctuation:
        return ("punctuation", identifier), symbols


symtable = {}
out = open("tokens.txt","a+")
out.write("Token Type \t \t Lexeme: \n")
with open('prog.txt','r', encoding="utf-8") as f:
    line = f.readline().strip()
    linenum = 0
    while line != "":
        line = line.split(" ")
        for element in line:
            try:
                NextToken, symtable = lex(element, symtable, linenum)
                out.write(f"{NextToken[0]} \t \t {NextToken[1]} \n")
            except TypeError:
                pass
        line = f.readline().strip()
        linenum += 1

out.write("Symbol Table\n Symbol \t \t Line # \n")
for k,v in symtable.items():
    out.write(f"{k} \t \t {v} \n")
out.close()

