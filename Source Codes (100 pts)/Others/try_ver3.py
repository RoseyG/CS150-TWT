#NOTES
    #error yung @INT a = 1 2
    #

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
NEWLINE = 101

global input
line = raw_input()
input = []
statement = line.split()
for lexeme in statement:
    input.append(lexeme)
input.append('EOF')
orig = input
def isfloat(str):
    try:
        float(str)
    except ValueError:
        return False
    return True

def lex():
    global nextToken
    nextString = input[0]
    print "NextString: ", nextString

    if nextString == 'EOF':
        nextToken = -1
    elif nextString == 'LOGIN':
        nextToken = login
    elif nextString == 'LOGOUT':
        nextToken = logout
    elif nextString == '@INT':
        nextToken = int_dec
    elif nextString == '@COKE':
        nextToken = float_dec
    elif nextString == '@CHIRP':
        nextToken = char_dec
    elif nextString == '@MSG':
        nextToken = string_dec
    elif nextString == '@TRALSE':
        nextToken = bool_dec
    elif nextString == 'IF':
        nextToken = if_state
    elif nextString == 'ELSEIF':
        nextToken = elseif_state
    elif nextString == 'ELSE':
        nextToken = else_state
    elif nextString == 'RT':
        nextToken = loop_state
    elif nextString == 'UNFOLLOW':
        nextToken = brake_state
    elif nextString == 'LIKE':
        nextToken = continue_state
    elif nextString == 'BLOCK':
        nextToken = exit_state
    elif nextString == 'FOLLOW':
        nextToken = exec_state
    elif nextString == 'REPLY':
        nextToken = read_state
    elif nextString == 'TWEET':
        nextToken = print_state
    elif nextString == 'REPORT':
        nextToken = return_state
    elif nextString == 'YES':
        nextToken = TRUE
    elif nextString == 'NO':
        nextToken = FALSE
    elif nextString == '~':
        nextToken = NOT
    elif nextString.isdigit():
        nextToken = INT
    elif nextString[0] == '-' and nextString[1:].isdigit():
        nextToken = INT
    elif isfloat(nextString):
        nextToken = FLOAT
    elif (nextString[0] == '\'') and (nextString[-1] == '\''):
        nextToken = CHAR
    elif (nextString[0] == '\"') and (nextString[-1] == '\"'):
        nextToken = STRING
    elif nextString == '{':
        nextToken = openBrace
    elif nextString == '}':
        nextToken = closeBrace
    elif nextString == '+':
        nextToken = plusSign
    elif nextString == '-':
        nextToken = minusSign
    elif nextString == '/':
        nextToken = divSign
    elif nextString == '*':
        nextToken = mulSign
    elif nextString == '=':
        nextToken = asSign
    elif nextString == '(':
        nextToken = openParen
    elif nextString == ')':
        nextToken = closeParen
    elif nextString == '#':
        nextToken = hashSymbol
    elif nextString == ',':
        nextToken = commaSign
    elif nextString == '>=':
        nextToken = lessEqSign
    elif nextString == '<=':
        nextToken = greatEqSign
    elif nextString == '==':
        nextToken = eqSign
    elif nextString == '>':
        nextToken = lesserSign
    elif nextString == '<':
        nextToken = greaterSign
    else:
        nextToken = VARIABLE

    print "NextToken: ", nextToken

    if(nextToken!= 100):
        print ("Next token is " + str(nextToken) + ". Next lexeme is " + nextString + ".")
    del input[0]




##KELLY
def Program():
    print "ENTER <Program>"
    FxnDeclaration()
    Main()
    print "EXIT <Program>"

def FxnDeclaration(): #<FxnDeclaration> -> <Dtype> <VARIABLE> "(" <Args> ")" "{" <Block> "}"
    print "ENTER <FxnDeclaration>"
    if Dtype():
        if(nextToken == VARIABLE):
            if (nextToken == openParen):
                lex()
                Args()
                if (nextToken == closeParen):
                    lex()
                    if(nextToken == openBrace):
                        lex()
                        Block()
                        if(nextToken == closeBrace):
                            lex()
                            print("Exit <FxnDeclaration SUCCESS>")
                            return
    input = orig
    print "EXIT <FxnDeclaration>"
    return

def Dtype(): #<Dtype> = "@INT" | "@CHIRP" | "@COKE" | "@MSG" | "@TRALSE"
    if (nextToken == int_dec or nextToken == float_dec or nextToken == char_dec or nextToken == string_dec or nextToken == bool_dec):
        lex()
        return True
    else:
        return False
        print("Expected: Data Type dapat")
    exit()


def Assignment():
    print("Enter <Assignment>")
    if(nextToken == int_dec):
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == INT or nextToken == VARIABLE or nextToken == read_state):
                    lex()
                    return
    elif(nextToken == float_dec):
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == FLOAT or nextToken == VARIABLE or nextToken == read_state):
                    lex()
                    return
    elif(nextToken == char_dec):
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == CHAR or nextToken == VARIABLE or nextToken == read_state):
                    lex()
                    return

    elif(nextToken == string_dec):
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == STRING or nextToken == VARIABLE or nextToken == read_state):
                    lex()
                    return
    elif(nextToken == bool_dec):
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == BOOL or nextToken == VARIABLE or nextToken == read_state):
                    lex()
                    return
    print("ERROR. NOT THE RIGHT ASSIGNMENT")
    exit()

def Main():
    print("Enter <Main>")
    if (nextToken == login):
        Block()
        lex()
        if (nextToken == logout):
            print("Exit Main")
            return
        else:
            print("Error: Expected LOGOUT ")
            exit()
    print("Error: Expected LOGIN")
    exit()

def Block():
    print("Enter <Block>")
    #if (nextToken == <some tokens that indicate a start of a new line>):
        #return
    Exp()

    #Newline()
    #Block()
    if (nextToken == hashSymbol):
        lex()
        Block()

def Exp():
    print("Enter <Exp>")
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
    print("Exit <Exp>")

def Return():
    print("Enter <Return>")
    if (nextToken == return_state):
        lex()
        if (nextToken == INT or nextToken == CHAR or nextToken == FLOAT or nextToken == STRING or nextToken == TRUE or nextToken == FALSE or nextToken == VARIABLE):
            return
        else:
            print("Error: Expected a variable literal")

def If():
    print("Enter <If>")
    if (nextToken == if_state):
        lex()
        if (nextToken == openParen):
            lex()
            Boolean()
            if (nextToken == closeParen):
                lex()
                if (nextToken == exec_state):
                    lex()
                    if (nextToken == openBrace):
                        lex()
                        Block()
                        if (nextToken == closeBrace):
                            lex()
                            Elseif()
                            Else()
    print("Exit <If>")
def Elseif():
    print("Enter <Elseif>")
    if (nextToken == elseif_state):
        lex()
        if (nextToken == openParen):
            lex()
            Boolean()
            if (nextToken == closeParen):
                lex()
                if(nextToken == exec_state):
                    lex()
                    if(nextToken == openBrace):
                        lex()
                        Block()
                        if (nextToken == closeBrace):
                            lex()
                            Elseif()
    print("Exit <Elseif>")

def Else():
    print("Enter <Else>")
    if (nextToken == else_state):
        lex()
        if (nextToken == openParen): #won't delete yet, pero ELSE na to. i think we should delete this part - Rae
            lex()
            Boolean()
            if (nextToken == closeParen):
                lex()
                if(nextToken == exec_state):
                    lex()
                    if(nextToken == openBrace):
                        lex()
                        Block()
                        if (nextToken == closeBrace):
                            lex()
                            return
        print("Invalid on else")
    #print("Exit <Else>")


def Loop():
    print("Enter <Loop>")
    if (nextToken == loop_state):
        lex()
        if(nextToken == openParen):
            lex()
            Boolean()
            if(nextToken == closeParen):
                lex()
                if(nextToken == openBrace):
                    lex()
                    Block()
                    if(nextToken == closeBrace):
                        #lex() <- madodoble si lex() since nabasa na yung closing brace - Rae
                        print("Exit <Loop>")
                        return
        else:
            print("Invalid on loop")

def Control():
    if (nextToken == break_state or nextToken == continue_state or nextToken == exit_state):
        lex()

##MIKA

#<Assignment> -> <DType> <VARIABLE> "=" <VARIABLE>
#                |<DType> <VARIABLE> "=" "REPLY"
#                |"@INT" <VARIABLE> "=" <INT>
#                | "@CHIRP" <VARIABLE> "=" <CHAR>
#                | "@COKE" <VARIABLE> "=" <FLOAT>
#                | "@MSG" <VARIABLE> "=" <STRING>
#                | "@TRALSE" <VARIABLE> "=" <BOOL>

def Boolean(): #<Boolean> -> <BooleanCond> | "~" <BooleanCond>
    if(nextToken == NOT):
        lex()
        BooleanCond()
    elif(nextToken == VARIABLE):
        BooleanCond()
    else:
        print("Expected is a ~ or a variable name -- basta bool expression")
        exit()
    return

def BooleanCond(): #<BooleanCond> -> <VARIABLE> ">=" <VARIABLE> | <VARIABLE> "<=" <VARIABLE> | <VARIABLE> "==" <VARIABLE> | <VARIABLE> ">" <VARIABLE> | <VARIABLE> "<" <VARIABLE>
    if (nextToken == VARIABLE):
        lex()
        if(nextToken == greatEqSign):
            lex()
            if(nextToken == VARIABLE):
                lex()
                return
            else:
                print("Expected nextToken is  a variable name")
        elif (nextToken == lessEqSign):
                lex()
                if(nextToken == VARIABLE):
                    lex()
                    return
                else:
                    print("Expected nextToken is  a variable name")
        elif (nextToken == eqSign):
                lex()
                if(nextToken == VARIABLE):
                    lex()
                    return
                else:
                    print("Expected nextToken is  a variable name")
        elif (nextToken == lesserSign):
                lex()
                if(nextToken == VARIABLE):
                    lex()
                    return
                else:
                    print("Expected nextToken is  a variable name")
        elif (nextToken == greaterSign):
                lex()
                #LAGAY EXPECTED
                if(nextToken == VARIABLE):
                    lex()
                    return
                else:
                    print("Expected nextToken is  a variable name")
        else:
            print("Expected nextToken is a Logical Operation/tor")
    print("Expected token is a variable name")
    exit()

def Call(): #<Call> -> <VARIABLE> "(" <Args> ")"
    if(nextToken == VARIABLE):
        lex()
        if (nextToken == openParen):
            lex()
            Args()
            if (nextToken == closeParen):
                lex()
                print("Exit <Call>")
                return
    print("Invalid")
    exit()

def Args(): #<Args> -> <Dtype> <VARIABLE> | <Dtype> <VARIABLE>  ", " <Args> | Lambda
    Dtype()
    if (nextToken == VARIABLE):
        lex()
        if (nextToken == commaSign):
            lex()
            Args()
    return

def Printing(): #<Printing> -> "TWEET" <Term> #Check this as well
    if (nextToken == printing):
        lex()
        Term()
    else:
        print("Invalid")
        exit()

def Term(): #<Term> -> <VARIABLE> "," <Term> | <ID> "," <Term> | <VARIABLE> | <ID>
    print("Enter <Term>")
    if (nextToken == VARIABLE or nextToken == string):
        lex()
        if (nextToken == ","):
            lex()
            Term()
        return

    print("Exit <Term>")
    exit()


lex()
Program()
