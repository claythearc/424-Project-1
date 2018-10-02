def lex(identifier: str, symbols: dict,linenum: int) -> tuple:
    """ Function for turning the passed word into a lexeme takes 
    the word to check, the symbol table dictionary, and the line number  """
    
    # list of words that define a keyword
    keywords = [
        'char',
        'int',
        'main',
        'bool',
        'while'
    ]
    
    # list of operators
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

    # list of characters that are punctuation
    punctuation = [
        ";",
        ",",
        "(",
        ")",
        "{",
        "}",
        "`"
    ]
    
    # list of words that are booleans
    boolean = [
        "true",
        "false"
    ]

    # list of symbols that are quote marks.
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
    # is the identifier a keyword?
    if identifier in keywords:
        return ("keyword", identifier), symbols
    if identifier.isalpha():
        #is the word all alpha (letters), update the dict, return identifier
        symbols[identifier] = symbols.get(identifier, linenum)
        return ("identifier", identifier), symbols
    if identifier.isdigit():
        # if the identifier is digits, return the integer payload.
        return ("integer", identifier), symbols
    if identifier.isnumeric():
        return ("digit", identifier), symbols
    if identifier in boolean:
        # if the identifier is a boolean, return the identifier
        return ("boolean", identifier), symbols
    if identifier in operators:
        # if the identifier is an operator
        return ("operator", identifier), symbols
    if identifier in punctuation:
        # if the identifier is in the punctuation list.
        return ("punctuation", identifier), symbols


symtable = {} # dictionary for the symbol tables
out = open("tokens.txt","a+") # file handle for the output file
out.write("Token Type \t \t Lexeme: \n")  # write the header.
with open('prog.txt','r', encoding="utf-8") as f:
    # context manager for input file
    line = f.readline().strip()
    linenum = 0
    # while the line isn't empty, pass it into the lex() function.
    while line != "":
        line = line.split(" ")
        for element in line:
            try:
                # get the results from the lex() function.
                NextToken, symtable = lex(element, symtable, linenum)
                out.write(f"{NextToken[0]} \t \t {NextToken[1]} \n")
            except TypeError:
                pass
        line = f.readline().strip()
        linenum += 1
# write the file headers for symbol tables
out.write("Symbol Table\n Symbol \t \t Line # \n")
# for iterate over the dictionary and write the k,v pairs.
for k,v in symtable.items():
    out.write(f"{k} \t \t {v} \n")
out.close()

