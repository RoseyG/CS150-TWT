import sys

##ROSEY
EOF = -1
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
call_state = 35
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
ENDOFSTATE = 50
commaSign = 51
lessEqSign = 52
greatEqSign = 53
eqSign = 54
lesserSign = 55
greaterSign = 56
VARIABLE = 100

nextToken = 0

def isfloat(str):
    try:
        float(str)
    except ValueError:
        return False
    return True

def lex():
    global input
    global nextToken
    nextString = input[0]
    if nextString == 'EOF':
        nextToken = EOF
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
        nextToken = ENDOFSTATE
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
    del input[0]
    print("Next token is: " + str(nextToken))
    print("Next string is: " + nextString)


## <Program> -> <Declaration> <Main>
#            | <Main>
def Program():
    global nextToken
    if(nextToken == EOF):
        print("Empty File")
    else:
        print("Enter <Program>")
        if(nextToken == login):
            Main()
        else:
            Declaration()
            if(nextToken == login):
                Main()
        if(nextToken == EOF):
            print("Exit <Program>")


##<Declaration> -> <Dtype> <Vname> "(" <Args> ")" "{" <Block> <Return>"}"
#                | <Dtype> <Vname> "(" <Args> ")" "{" <Block> "}"
def Declaration(): #<Declaration> -> <Dtype> <Vname> "(" <Args> ")" "{" <Block> "}"
    global nextToken
    print("Enter <Declaration>")
    Dtype()
    if(nextToken == vname):
        if (nextToken == openParen):
            lex()
            Args()
            if (nextToken == closeParen):
                lex()
                if(nextToken == openBrace):
                    lex()
                    Block()
                    if (nextToken == return_state):
                        lex()
                        Return()
                    if(nextToken == closeBrace):
                        lex()
                        print("Exit <Declaration>")
                        return
    print("Error: Invalid Function Declaration")
    error()

##<Main> -> "LOGIN" <Block> "LOGOUT"
#          | "LOGIN" "LOGOUT"
def Main():
    global nextToken
    print("Enter <Main>")
    if (nextToken == login):
        lex()
        Block()
        if (nextToken == logout):
            lex()
            print("Exit <Main>")
            return
        else:
            print("Error: Expected LOGOUT")
            error()
    print("Error: Expected LOGIN")
    error()

##<Block> -> <State>                    // Block is made up of statement <State> of the same level
def Block():
    global nextToken
    print("Enter <Block>")
    State()
    print("Exit <Block>")
    return

##<State> -> <Loop> "#" <StatePrime>
#        | <If> "#" <StatePrime>
#        | <Assignment> "#" <StatePrime>
#        | <Call> "#" <StatePrime>
#        | <Printing> "#" <StatePrime>
#        | <Control> "#" <StatePrime>
# We need at tleast one stament inside a block then check for repetitions
def State():
    global nextToken
    print("Enter <State>")
    if (nextToken == if_state):
        If()
    elif (nextToken == loop_state):
        Loop()
    elif (nextToken == int_dec or nextToken == char_dec or nextToken == float_dec or nextToken == string_dec or nextToken == bool_dec or nextToken == VARIABLE):
        Assignment()
    elif (nextToken == print_state):
        Printing()
    elif (nextToken == call_state):
        Calling()
    elif (nextToken == break_state or nextToken == continue_state or nextToken == exit_state):
        Control()
    else:
        print("Expected statement")
        error()
    if(nextToken == ENDOFSTATE):
        lex()
        StatePrime()
        print("Exit <State>")
    else:
        error()

##<StatePrime> -> <Loop> "#" <StatePrime>
#        | <If> "#" <StatePrime>
#        | <Assignment> "#" <StatePrime>
#        | <Call> "#" <StatePrime>
#        | <Printing> "#" <StatePrime>
#        | <Read> "#" <StatePrime>
#        | <Control> "#" <StatePrime>
# Basically, nagche-check lng kung may more than one statements
def StatePrime():
    global nextToken
    if (nextToken == if_state):
        If()
    elif (nextToken == loop_state):
        Loop()
    elif (nextToken == int_dec or nextToken == char_dec or nextToken == float_dec or nextToken == string_dec or nextToken == bool_dec or nextToken == VARIABLE):
        Assignment()
    elif (nextToken == print_state):
        Printing()
    elif (nextToken == call_state):
        Calling()
    elif (nextToken == break_state or nextToken == continue_state or nextToken == exit_state):
        Control()
    else:
        return  # Exit lng kung wala ng next statements after the last repitition,
                # no need to lex cuz the nextToken will be checked for a match again outside the function
    if(nextToken == ENDOFSTATE):
        lex()
        StatePrime()

##<Loop> -> "RT" <Boolean> "{" <Block> "}"
def Loop():
    global nextToken
    print("Enter <Loop>")
    lex()
    Logic()
    if(nextToken == openBrace):
        lex()
        Block()
        if(nextToken == closeBrace):
            print("Exit <Loop>")
            lex()
        else:
            print("Expectetd '}'")
            error()
    else:
        print("Expectedt '{'")
        error()

##<If> -> "IF" <Boolean> "FOLLOW" "{" <Block> "}" <ElseIf> <Else>
#        | "IF" <Boolean> "FOLLOW" "{" <Block> "}" <Else>
#        | "IF" <Boolean> "FOLLOW" "{" <Block> "}"
def If():
    global nextToken
    print("Enter <If>")
    if (nextToken == if_state):
        lex()
        Logic()
        if (nextToken == exec_state):
            lex()
            if (nextToken == openBrace):
                lex()
                Block()
                if (nextToken == closeBrace):
                    lex()
                    if (nextToken == elseif_state):
                        Elseif()
                    if (nextToken == else_state):
                        Else()
                    print("Exit <If>")
                    return
    print("Error: Invalid IF statement")
    error()

##<ElseIf> -> "ELSEIF" <Boolean> "FOLLOW" "{" <Block> "}" <Elseif>
def Elseif():
    global nextToken
    print("Enter <Elseif>")
    if (nextToken == elseif_state):
        lex()
        Logic()
        if(nextToken == exec_state):
            lex()
            if(nextToken == openBrace):
                lex()
                Block()
                if (nextToken == closeBrace):
                    lex()
                    if (nextToken == elseif_state):
                        Elseif()
                    print("Exit <Elseif>")
                    return
    print("Error: Invalid ELSEIF statement")
    error()

##<Else> -> "ELSE" <Boolean> "FOLLOW" "{" <Block> "}"
def Else():
    global nextToken
    print("Enter <Else>")
    if (nextToken == else_state):
        lex()
        Boolean()
        if(nextToken == exec_state):
            lex()
            if(nextToken == openBrace):
                lex()
                Block()
                if (nextToken == closeBrace):
                    lex()
                    print("Exit <Else>")
                    return
    print("Error: Invalid ELSE statement")
    error()

#<Assignment> -> <DType> <Vname> "=" <Vname>
#                | <DType> <Vname> "=" <Reading>
#                | "@INT" <Vname> "=" <INT>
#                | "@CHIRP" <Vname> "=" <CHAR>
#                | "@COKE" <Vname> "=" <FLOAT>
#                | "@MSG" <Vname> "=" <STRING>
#                | "@TRALSE" <Vname> "=" <BOOL>
#                | <DType> <Vname> "=" "(" <Exp> ")"
def Assignment():
    global nextToken
    print("Enter <Assignment>")
    if(nextToken == int_dec):
        lex()
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == INT or nextToken == VARIABLE):
                    lex()
                    return
                elif(nextToken == read_state):
                    Reading()
                    return
    elif(nextToken == float_dec):
        lex()
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == FLOAT or nextToken == VARIABLE):
                    lex()
                    return
                elif(nextToken == read_state):
                    Reading()
                    return
    elif(nextToken == char_dec):
        lex()
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == CHAR or nextToken == VARIABLE):
                    lex()
                    return
                elif(nextToken == read_state):
                    Reading()
                    return
    elif(nextToken == string_dec):
        lex()
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == STRING or nextToken == VARIABLE):
                    lex()
                    return
                elif(nextToken == read_state):
                    Reading()
                    return
    elif(nextToken == bool_dec):
        lex()
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == TRUE or nextToken == FALSE or nextToken == VARIABLE:
                    lex()
                    return
                elif(nextToken == read_state):
                    Reading()
                    return
    elif(nextToken == openParen):
        lex()
        Exp()
        if(nextToken == closeParen):
            lex()
            return
        else:
            print("Expected ')'")
            error()
    print("Error: Invald assignment statement")
    error()

##<Call> -> <Vname> "(" <Args> ")"
def Call():
    global nextToken
    print("Enter <Call>")
    if(nextToken == vname):
        lex()
        if (nextToken == openParen):
            lex()
            Args()
            if (nextToken == closeParen):
                lex()
                print("Exit <Call>")
                return
    print("Invalid function call")
    error()

##<Printing> -> "TWEET" <Vname>
#              | "TWEET" "(" <EXP> ")"
#              | "TWEET" <INT>
#              | "TWEET" <FLOAT>
#              | "TWEET" <CHAR>
#              | "TWEET" <STRING>
#              | "TWEET" <BOOL>
def Printing():
    global nextToken
    print("Enter <Printing>")
    lex()
    if (nextToken == openParen):
        lex()
        Exp()
        if(nextToken == closeParen):
            lex()
            print("Exit <Printing>")
            return
        else:
            print("Error: expected token is ')' ")
            error()
    elif (nextToken == INT or nextToken == FLOAT or nextToken == CHAR or nextToken == STRING or  nextToken == TRUE or nextToken == FALSE or nextToken == VARIABLE):
        lex()
        print("Exit <Printing>")
        return
    else:
        print("Expected expression, varable or literal")
        error()
##<Reading> - > "REPLY"
def Reading():
    print("Enter <Reading>")
    lex()
    print("Exit <Reading")
    return

##This part is the one we made sa ME
# Copy na lng natin

##<Exp> -> <Term> <ExpPrime>
def Exp():
    print "Enter <Exp>"
    Term()
    ExpPrime()
    print "Exit <Exp>"
    return

##<ExpPrime> -> "+" <Term><ExpPrime>
#            | "-" <Term><ExpPrime>
def ExpPrime():
    global nextToken
    while (nextToken == plusSign or nextToken == minusSign):
		lex()
		Term() # No need to call ExpPrime since we can just loop it
    return

##<Term> -> <Fact><TermPrime>
def Term():
	print "Enter <Term>"
	Fact()
	TermPrime()
	print "Exit <Term>"
	return

##<TermPrime> -> "*" <Fact><TermPrime>
#            | "/" <Fact><TermPrime>
def TermPrime():
    global nextToken
    while (nextToken == divSign or nextToken == mulSign):
        lex()
        Fact()
    return

##<Fact> -> <INT> | <CHAR> | <FLOAT> | "(" <Exp> ")"
def Fact():
    global nextToken
    print "Enter <Factor>"
    if (nextToken == INT or nextToken == CHAR or nextToken == FLOAT or nextToken == VARIABLE ):
		lex()
    elif (nextToken == openParen):
        lex()
        Exp()
        if (nextToken == closeParen):
            lex()
        else:
            error()
    else:
        error()
    print "Exit <Factor>"
    return

##<Logic> -> "(" <LogicCond> ")" | "~" <Logic>
def Logic():
    global nextToken
    print("Enter <Logic>")
    if(nextToken == NOT):
        lex()
        Logic()
        print("Exit <Logic")
        return
    elif(nextToken == openParen):
        lex()
        LogicCond()
        if(nextToken == closeParen):
            lex()
            print("Exit <Logic>")
            return
        else:
            print("Expected ')'")
            error()
    else:
        print("Error: Expected is a ~ or a variable name -- basta bool expression")
        error()

##<LogicCond> -> <Vname> <LogicOP> <Vname>
#          | <Vname | INT | CHAR | FLOAT > <LogicOP> <Logic>
#          | <Logic> <LogicOP> <Logic>
#          | <Logic> <LogicOP> <Vname | INT | CHAR | FLOAT >
#          | <Vname | INT | CHAR | FLOAT > <LogicOP> <Vname | INT | CHAR | FLOAT >
def LogicCond():
    global nextToken
    print("Enter <LogicCond>")
    if (nextToken == VARIABLE or nextToken == TRUE or nextToken == FALSE or nextToken == INT or nextToken == CHAR or nextToken == FLOAT):
        lex()
    elif (nextToken == openParen or nextToken == NOT):
        Logic()
        lex()
    else:
        error()
    LogicOp()
    if (nextToken == VARIABLE or nextToken == TRUE or nextToken == FALSE or nextToken == INT or nextToken == CHAR or nextToken == FLOAT):
        lex()
        print("Exit <LogicCond>")
        return
    elif (nextToken == openParen or nextToken == NOT):
        Logic()
        lex()
        print("Exit <LogicCond>")
        return
    else:
        print("Expected nextToken is a variable name or '(' ")
        error()
    print("Invalid Logical/Boolean expression")
    error()

##<LogicOP> -> ">=" | "<=" | "==" | ">" | "<"
def LogicOp():
    global nextToken
    print("Enter <LogicOp>")
    if (nextToken == greatEqSign or nextToken == lessEqSign or nextToken == eqSign or nextToken == lesserSign or nextToken == greaterSign):
        lex()
        print("Exit <LogicOp>")
        return
    else:
        print("Expected boolean operator")
        error()

##<Dtype> -> "@INT" | "@CHIRP" | "@COKE" | "@MSG" | "@TRALSE"
def Dtype(): #<Dtype> = "@INT" | "@CHIRP" | "@COKE" | "@MSG" | "@TRALSE"
    global nextToken
    print("Enter <Dtype>")
    if (nextToken == int_dec or nextToken == float_dec or nextToken == char_dec or nextToken == string_dec or nextToken == bool_dec):
        lex()
        print("Exit <Dtype>")
        return
    print("Error: Expected Data type poeszh")
    error()

##<Args> -> <Dtype> <Vname> "," <Args>
def Args():
    global nextToken
    print("Enter <Args>")
    Dtype()
    if (nextToken == VARIABLE):
        lex()
        if (nextToken == commaSign):
            lex()
            Args()
            print("Exit <Args>")
            return
    error()

##<Return> -> <Return> -> "REPORT" <ID> | "REPORT" <Vname> | "REPORT" "(" <Exp> ")"
def Return():
    global nextToken
    if (nextToken == return_state):
        lex()
        if (nextToken == INT or nextToken == CHAR or nextToken == FLOAT or nextToken == STRING or nextToken == VARIABLE):
            lex()
            print("Enter <Return>")
            return
        elif (nextToken == openParen):
            lex()
            BooleanCond()
            if (nextToken == ")"):
                lex()
                print("Enter <Return>")
                return
    print("Error: Expected return value")
    error()

##Error Function
#
def error():
	print "Syntax Error"
	quit()

##Main Function
#
def main():
    global input
    input = []
    tempLexeme = " "

    print("Reading: " + str(sys.argv[1]) + '.twt')

    try:
        file = open( str(sys.argv[1]) + '.twt' , 'r')
    except:
        print("No such *.twt file exist")
        quit()

    for rawline in file:
        line = rawline.split()
        for lexeme in line:
            if (lexeme[0] == '"' and lexeme[-1] != lexeme[0]):
                tempLexeme = lexeme
                continue
            if (tempLexeme[0] == '"' and tempLexeme[-1] != '"'):
                tempLexeme = tempLexeme + ' ' + lexeme
                if (tempLexeme[0] == tempLexeme[-1]):
                    input.append(tempLexeme)
                    tempLexeme = " "
                    continue
                continue
            input.append(lexeme)

    input.append('EOF')
    lex()
    Program()

if __name__ == '__main__':
	main()
