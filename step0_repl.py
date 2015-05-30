# read
def READ(str):
    return str

# eval
def EVAL(str):
        return str

# print
def PRINT(str):
    return str

# repl
def REPL(str):
    return PRINT(EVAL(READ(str)))

# repl loop
while True:
    try:
        line = input("user> ")
        print(REPL(line))
    except EOFError:
        break

