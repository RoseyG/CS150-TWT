
global input
input = raw_input()
input = input.replace(" ", "")
input = [input[i] for i in range(len(input))]
input.append('EOF')
inputlength = len(input)
def lex():
        global nexttoken
        #Token list:
        global Identifier, Assign, Add, Sub, Mult, Div, LeftP, RightP, EOF
        Identifier = 11
        Assign = 20
        Add = 21
        Sub = 22
        Mult = 23
        Div = 24
        LeftP = 25
        RightP = 26
        EOF = -1

        i = input[0]
        if( i == 'a') or (i== 'b') or (i == 'c'):
            nexttoken = Identifier
        elif(i == '+'):
            nexttoken = Add
        elif(i == '='):
            nexttoken = Assign
        elif(i == '-'):
            nexttoken = Sub
        elif (i == '/'):
            nexttoken = Div
        elif (i == '*'):
            nexttoken = Mult
        elif (i == '('):
            nexttoken = LeftP
        elif (i == ')'):
            nexttoken = RightP
        elif (i == 'EOF'):
            nexttoken = EOF
        else:
            nexttoken = 100
            print("Invalid Lexeme.")
            exit()
        if(nexttoken!= 100):
            print ("Next token is " + str(nexttoken) + ". Next lexeme is " + i + ".")
        del input[0]
        return
def A():
    print "Enter <A> "
    id()
    if (nexttoken == Assign):
        lex()
        expr()
    else:
        print "Invalid token!"
        exit()
    print "Exit <A> "
    return
def expr():
    print "Enter <expr> "
    term()
    while (nexttoken == Add) or (nexttoken == Sub):
        lex()
        term()
    print "Exit <expr> "
    return

def term():
    print "Enter <term> "
    factor()
    while (nexttoken == Mult) or (nexttoken == Div):
        lex()
        factor()
    print "Exit <term> "
    return

def factor():
    if (nexttoken == LeftP):
        print "Enter <factor> "
        lex()
        expr()
        if (nexttoken == RightP):
            lex()
        else:
            print "Error! "
            exit()
    elif (nexttoken == Identifier):
        id()
    else:
        print "Error! "
        exit()
    print "Exit <factor> "

def id():
    if (nexttoken == Identifier):
        lex()
        print "Enter <id> "
    else:
        print "Error!"
        exit()
    print "Exit <id> "



lex()
A()
