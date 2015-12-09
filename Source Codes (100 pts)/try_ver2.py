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

nextToken = 0
line = " "
ctr = 0

def isfloat(str):
    try:
        float(str)
    except ValueError:
        return False
    return True

def lex():
    if ctr <= len(line):
        nextString = line[ctr]
    if nextString == 'EOF':
        nextToken = EOF
    elif nextString == '@LOGIN':
        nextToken = login
    elif nextString == '@LOGOUT':
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
    ctr += 1;
    print("Next token is: ", nextToken)


## <Program> -> <Declaration> <Main>
#            | <Main>
def Program():
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
                        exit()
    error = True
    print("Error: Invalid Function Declaration")
    exit()

##<Main> -> "LOGIN" <Block> "LOGOUT"
#          | "LOGIN" "LOGOUT"
def Main():
    print("Enter <Main>")
    if (nextToken == login):
        lex()
        Block()
        if (nextToken == logout):
            print("Exit <Main>")
            exit()
    print("Error: Expected LOGIN")
    error = True
    exit()

##<Block> -> <State>                    // Block is made up of statement <State> of the same level
def Block():
    print("Enter <Block>")
    State()
    if (error):
        exit()
    print("Exit <Block>")
    exit()

##<State> -> <Loop> <NewLine> <StatePrime>
#        | <If> <NewLine> <StatePrime>
#        | <Assignment> <NewLine> <StatePrime>
#        | <Call> <NewLine> <StatePrime>
#        | <Printing> <NewLine> <StatePrime>
#        | <Read> <NewLine> <StatePrime>
#        | <Control> <NewLine> <StatePrime>
# We need at tleast one stament inside a block then check for repetitions
def State():
    print("Enter <State>")
    if (nextToken == if_state):
        If()
    elif (nextToken == loop_state):
        Loop()
    elif (nextToken == int_dec or nextToken == char_dec or nextToken == float_dec or nextToken == string_dec or nextToken == bool_dec or nextToken == VARIABLE):
        Assignment()
    elif (nextToken == print_state):
        Printing()
    elif (nextToken == read_state):
        Reading()
    elif (nextToken == call_state):
        Calling()
    elif (nextToken == break_state or nextToken == continue_state or nextToken == exit_state):
        Control()
    else:
        error = True

    if (not error):
        if(nextToken == hashSymbol):
            lex()
            StatePrime()
        else:
            error = True

    if (error):
        exit()
    print("Exit <State>")

##<StatePrime> -> <Loop> <NewLine> <StatePrime>
#        | <If> <NewLine> <StatePrime>
#        | <Assignment> <NewLine> <StatePrime>
#        | <Call> <NewLine> <StatePrime>
#        | <Printing> <NewLine> <StatePrime>
#        | <Read> <NewLine> <StatePrime>
#        | <Control> <NewLine> <StatePrime>
# Basically, nagche-check lng kung may more than one statements
def StatePrime():
    if (nextToken == if_state):
        If()
    elif (nextToken == loop_state):
        Loop()
    elif (nextToken == int_dec or nextToken == char_dec or nextToken == float_dec or nextToken == string_dec or nextToken == bool_dec or nextToken == VARIABLE):
        Assignment()
    elif (nextToken == print_state):
        Printing()
    elif (nextToken == read_state):
        Reading()
    elif (nextToken == call_state):
        Calling()
    elif (nextToken == break_state or nextToken == continue_state or nextToken == exit_state):
        Control()
    else:
        exit()  # Exit lng kung wala ng next statements after the last repitition,
                # no need to lex cuz the nextToken will be checked for a match again outside the function
    if(nextToken == hashSymbol):
        lex()
        StatePrime()
    else:
        error = True

##<Loop> -> "RT" <Boolean> "{" <Block> "}"
def Loop():
    print("Enter <Loop>")
    if (nextToken == loop_state):
        lex()
        Boolean()
        if(nextToken == openBrace):
            lex()
            Block()
            if(nextToken == closeBrace):
                print("Exit <Loop>")
            else:
                error = True
        else:
            error = True
    else:
        error = True
    if(error):
        print("Invalid loop statement")
        exit()
    lex()

##<If> -> "IF" <Boolean> "FOLLOW" "{" <Block> "}" <ElseIf> <Else>
#        | "IF" <Boolean> "FOLLOW" "{" <Block> "}" <Else>
#        | "IF" <Boolean> "FOLLOW" "{" <Block> "}"
def If():
    print("Enter <If>")
    if (nextToken == if_state):
        lex()
        Boolean()
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
                    exit()
    error = True
    print("Error: Invalid IF statement")
    exit()


##<ElseIf> -> "ELSEIF" <Boolean> "FOLLOW" "{" <Block> "}" <Elseif>
def Elseif():
    print("Enter <Elseif>")
    if (nextToken == elseif_state):
        lex()
        Boolean()
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
                    exit()
    error = True
    print("Error: Invalid ELSEIF statement")
    exit()

##<Else> -> "ELSE" <Boolean> "FOLLOW" "{" <Block> "}"
def Else():
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
                    exit()
    print("Error: Invalid ELSE statement")
    exit()

#<Assignment> -> <DType> <Vname> "=" <Vname>
#                | <DType> <Vname> "=" "REPLY"
#                | "@INT" <Vname> "=" <INT>
#                | "@CHIRP" <Vname> "=" <CHAR>
#                | "@COKE" <Vname> "=" <FLOAT>
#                | "@MSG" <Vname> "=" <STRING>
#                | "@TRALSE" <Vname> "=" <BOOL>
#                | <DType> <Vname> "=" "(" <Exp> ")"
def Assignment():
    print("Enter <Assignment>")
    if(nextToken == int_dec):
        lex()
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == INT or nextToken == VARIABLE or nextToken == read_state):
                    lex()
    elif(nextToken == float_dec):
        lex()
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == FLOAT or nextToken == VARIABLE or nextToken == read_state):
                    lex()
    elif(nextToken == char_dec):
        lex()
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == CHAR or nextToken == VARIABLE or nextToken == read_state):
                    lex()
    elif(nextToken == string_dec):
        lex()
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == STRING or nextToken == VARIABLE or nextToken == read_state):
                    lex()
    elif(nextToken == bool_dec):
        lex()
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == BOOL or nextToken == VARIABLE or nextToken == read_state):
                    lex()
    elif(nextToken == openParen):
        lex()
        Exp()
        if(nextToken == closeParen):
            lex()
    else:
        error = True
    if(error):
        print("Error: Invald assignment statement")
        exit()
    else:
        print("Exit <Assignment>")
        return

##<Call> -> <Vname> "(" <Args> ")"
def Call():
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
    print("Invalid")
    exit()

##<Printing> -> "TWEET" <Vname>
#              | "TWEET" <EXP>
#              | "TWEET" <ID>

##<Control> -> "UNFOLLOW" | "LIKE" | "BLOCK"
def Control():
    if (nextToken == break_state or nextToken == continue_state or nextToken == exit_state):
        lex()

##This part is the one we made sa ME
# Copy na lng natin

##<Exp> -> <Term> <ExpPrime>

##<ExpPrime> -> "+" <Term><EspPrime>
#            | "-" <Term><ExpPrime>

##<Term> -> <Fact><TermPrime>

##<TermPrime> -> "*" <Fact><TermPrime>
#            | "/" <Fact><TermPrime>

##<Fact> -> <ID> | <CHAR> | <FLOAT> | "(" <Exp> ")"

##<ID> -> <INT> | <CHAR> | <FLOAT> | <STRING> | <BOOL>

##<Newline> -> "\n" <Newline>

##<Boolean> -> "(" <BooleanCond> ")" | "~" <Boolean>
def Boolean():
    print("Enter <Boolean>")
    if(nextToken == NOT):
        lex()
        Boolean()
        print("Exit <Boolean>")
        return
    elif(nextToken == openParen):
        lex()
        BooleanCond()
        if(nextToken == closeParen):
            lex()
            print("Exit <Boolean>")
            return
        else:
            error = True
    else:
        error = True
        print("Error: Expected is a ~ or a variable name -- basta bool expression")
        exit()

##<BooleanCond> -> <Vname> <BooleanOP> <Vname>
#          | <Vname> <BooleanOP> <Boolean>
#          | <Boolean> <BooleanOP> <Boolean>
#          | <Boolean> <BooleanOP> <VName>
def BooleanCond():
    if (nextToken == vname):
        lex()
        if(nextToken == greatEqSign):
            lex()
            if(nextToken == vname):
                lex()
                return
            else:
                error = True
                exit()
        elif (nextToken == lessEqSign):
            lex()
            if(nextToken == vname):
                lex()
                return
            else:
                error = True
                print("Expected nextToken is  a variable name")
                exit()
        elif (nextToken == eqSign):
            lex()
            if(nextToken == vname):
                lex()
                return
            else:
                error = True
                print("Expected nextToken is  a variable name")
                exit()
        elif (nextToken == lesserSign):
            lex()
            if(nextToken == vname):
                lex()
                return
            else:
                error = True
                print("Expected nextToken is  a variable name")
                exit()
        elif (nextToken == greaterSign):
            lex()
            if(nextToken == vname):
                lex()
                return
            else:
                error = True
                print("Expected nextToken is  a variable name")
                exit()
        else:
            error = True
            print("Error: Expected nextToken is a Logical Operation/tor")
            exit()
    error = True
    print("Error: Expected token is a variable name")
    exit()

##<BooleanOP> -> ">=" | "<=" | "==" | ">" | "<"

##<Dtype> -> "@INT" | "@CHIRP" | "@COKE" | "@MSG" | "@TRALSE"
def Dtype(): #<Dtype> = "@INT" | "@CHIRP" | "@COKE" | "@MSG" | "@TRALSE"
    print("Enter <Dtype>")
    if (nextToken == int_dec or nextToken == float_dec or nextToken == char_dec or nextToken == string_dec or nextToken == bool_dec):
        lex()
        print("Exit <Dtype>")
        return
    print("Error: Expected Data type poeszh")
    exit()

##<Args> -> <Dtype> <Vname> "," <Args>
def Args(): #<Args> -> <Dtype> <Vname> | <Dtype> <Vname>  ", " <Args>
    Dtype()
    if (nextToken == VARIABLE):
        lex()
        if (nextToken == commaSign):
            lex()
            Args()
    return

##<Newline> -> "\n"<Newline> | "\n"

##<Return> -> "REPORT" <ID> | "REPORT" <Vname> | "REPORT" <Exp>
def Return():
    if(nextToken == return_state):
        lex()
        if ((nextToken == INT or nextToken == CHAR or nextToken == FLOAT or nextToken == STRING or nextToken == TRUE or nextToken == FALSE) or nextToken == VARIABLE):
            print("Enter <Return>")
            return
    error = True
    print("Error: Expected return value")
    exit()

def Printing(): #<Printing> -> "TWEET" <Term> #Check this as well
    if (nextToken == printing):
        lex()
        Term()
    else:
        print("Invalid")
        exit()

def Term(): #<Term> -> <Vname> "," <Term> | <ID> "," <Term> | <Vname> | <ID>
    print("Enter <Term>")
    if (nextToken == vname or nextToken == string):
        lex()
        if (nextToken == ","):
            lex()
            Term()
        return
    print("Exit <Term>")
    exit()

## Main Function
def main():
    rawline = raw_input()
    line = rawline.split
    ctr = 0
    error = False
    lex()
    State(line)

if __name__ == '__main__':
	main()
