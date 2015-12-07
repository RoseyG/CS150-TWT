##ROSEY
int_dec = 3
float_dec = 4
char_dec =  5
string_dec = 6
bool_dec = 7
login = 1
logout = 0
if_state = 20
elseif_state = 21
else_state = 22
loop_state = 30
break_state = 31
continue_state = 32
exit_state = 33
exec_state = 34
read_state = 10
print_state = 11
return_state = 12
TRUE = 13
FALSE = 14
NOT = 15
INT = 71
FLOAT = 72
CHAR = 73
STRING = 74
openBrace = 41
closeBrace = 42
plusSign = 43
minusSign = 44
divSign = 45
mulSign = 46
asSign = 47
openParen = 48
closeParen = 49
hashSymbol = 50
commaSign = 51
lessEqSign = 52
greatEqSign = 53
eqSign = 54
lesserSign = 55
greaterSign = 56
VARIABLE = 100

##KELLY
def Program():
    FDefns()
    Main()

def FDefns():
    Declaration()
def Main():
    lex()
    if (nextToken == login)
        Block()
        lex()
        if (nextToken == logout)
            print("Exit Main")
            return
        else
            print("Error: Expected LOGOUT ")
            exit()
    print("Error: Expected LOGIN")
    exit()
    
def Block():
    Exp()
    if (nextToken == hashSymbol)
        Block()
    return

def Exp():
    lex()
    if (nextToken == if_state):
        If()
    elif (nextToken == loop_state):
        Loop()
    elif (nextToken == int_dec or nextToken == char_dec or nextToken == float_dec or nextToken == string_dec or nextToken == bool_dec):
        Assignment()
    elif (nextToken == VARIABLE):
        Call()
    elif (nextToken == print_state):
        Printing()
    elif (nextToken == break_state or nextToken == continue_state or nextToken == exit_state):
        Control()
    elif (nextToken == return_state):
        Return()
    else:
        print("Error: Unidentified expression")
        
def Return():
    if (nextToken == return_state):
        lex()
        if (nextToken == INT or nextToken == CHAR or nextToken = FLOAT or nextToken == STRING or nextToken == TRUE or nextToken == FALSE or nextToken == VARIABLE):
            return
        else:
            print("Error: Expected a variable literal")

def If():
    if (nextToken == if_state):
        lex()
        if (nextToken == openParen):
            Boolean()
            lex()
            if (nextToken == closeParen):
                lex()
                if (nextToken == exec_state):
                    lex()
                    if (nextToken == openBrace):
                        Block()
                        lex()
                        if (nextToken == closeBrace):
                            lex()

##MIKA
def Print():
    if (nextToken == printing):


def Term():
    print("Enter <Term>")
	if (nextToken == vname or nextToken == string):
        lex()
        while(nextToken == ","):
            lex()
            Term()
    else:
        print "Error!"
    print "Exit Term>"
        exit()
