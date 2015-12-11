import sys
import os
import time
##ROSEY
## Lexemes and Tokens

EOF = -1
tabs = 0
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
fxncall = 23
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
ENDOFSTATE = 50
commaSign = 51
lessEqSign = 52
greatEqSign = 53
eqSign = 54
lesserSign = 55
greaterSign = 56
VARIABLE = 100

nextToken = 0

#Checks if input is floar
def isfloat(str):
    try:
        float(str)
    except ValueError:
        return False
    return True

#LEX PROPER and at the same time, we translate our language to python language and write the code in another py file to be run at the end of the program if no error is found
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
    elif nextString == 'HOOT':
        nextToken = fxncall
    elif nextString == 'IF':
        outfile.write('if ')
        nextToken = if_state
    elif nextString == 'ELSEIF':
        outfile.write('elif ')
        nextToken = elseif_state
    elif nextString == 'ELSE':
        outfile.write('else ')
        nextToken = else_state
    elif nextString == 'RT':
        outfile.write('while ')
        nextToken = loop_state
    elif nextString == 'UNFOLLOW':
        outfile.write('break')
        nextToken = break_state
    elif nextString == 'LIKE':
        outfile.write('continue')
        nextToken = continue_state
    elif nextString == 'BLOCK':
        outfile.write('exit')
        nextToken = exit_state
    elif nextString == 'FOLLOW':
        nextToken = exec_state
    elif nextString == 'REPLY':
        outfile.write('input() ')
        nextToken = read_state
    elif nextString == 'TWEET':
        outfile.write('print ')
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
        outfile.write(nextString)
        nextToken = INT
    elif nextString[0] == '-' and nextString[1:].isdigit():
        outfile.write(nextString)
        nextToken = INT
    elif isfloat(nextString):
        outfile.write(nextString)
        nextToken = FLOAT
    elif (nextString[0] == '\'') and (nextString[-1] == '\'') and (nextString.len() == 1):
        outfile.write(nextString)
        nextToken = CHAR
    elif (nextString[0] == '\"') and (nextString[-1] == '\"'):
        outfile.write(nextString)
        nextToken = STRING
    elif nextString == '{':
        nextToken = openBrace
    elif nextString == '}':
        nextToken = closeBrace
    elif nextString == '+':
        outfile.write(nextString)
        nextToken = plusSign
    elif nextString == '-':
        outfile.write(nextString)
        nextToken = minusSign
    elif nextString == '/':
        outfile.write(nextString)
        nextToken = divSign
    elif nextString == '*':
        outfile.write(nextString)
        nextToken = mulSign
    elif nextString == '=':
        outfile.write(nextString)
        nextToken = asSign
    elif nextString == '(':
        outfile.write(nextString)
        nextToken = openParen
    elif nextString == ')':
        outfile.write(nextString)
        nextToken = closeParen
    elif nextString == '#':
        outfile.write('\n')
        nextToken = ENDOFSTATE
    elif nextString == ',':
        outfile.write(nextString)
        nextToken = commaSign
    elif nextString == '>=':
        outfile.write(nextString)
        nextToken = lessEqSign
    elif nextString == '<=':
        outfile.write(nextString)
        nextToken = greatEqSign
    elif nextString == '==':
        outfile.write(nextString)
        nextToken = eqSign
    elif nextString == '>':
        outfile.write(nextString)
        nextToken = lesserSign
    elif nextString == '<':
        outfile.write(nextString)
        nextToken = greaterSign
    else:
        outfile.write(nextString)
        nextToken = VARIABLE
    print("Next token is: " + str(nextToken))
    print("Next string is: " + nextString)
    del input[0]


### RD PROPER

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

##<Declaration> -> <Dtype> VARIABLE "(" <Args> ")" "{" <Block> <Return>"}"
#                | <Dtype> VARIABLE "(" <Args> ")" "{" <Block> "}"
def Declaration():
    global nextToken
    global tabs
    print("Enter <Declaration>")
    outfile.write('def ')
    Dtype()
    if(nextToken == VARIABLE):
        lex()
        if (nextToken == openParen):
            lex()
            Args()
            if(nextToken == openBrace):
                outfile.write(':\n')
                tabs+=1
                for i in range(tabs):
                    outfile.write('\t')
                lex()
                Block()
                if (nextToken == return_state):
                    lex()
                    Return()
                if(nextToken == closeBrace):
                    tabs-=1
                    outfile.write( '\n' )
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
    print tabs , "haha"
    print("Enter <State>")
    if (nextToken == if_state):
        If()
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
    elif (nextToken == loop_state):
        Loop()
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
    elif (nextToken == int_dec or nextToken == char_dec or nextToken == float_dec or nextToken == string_dec or nextToken == bool_dec or nextToken == VARIABLE):
        Assignment()
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
    elif (nextToken == print_state):
        Printing()
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
    elif (nextToken == read_state):
        lex()
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
    elif (nextToken == fxncall):
        lex()
        Call()
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
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
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
    elif (nextToken == loop_state):
        Loop()
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
    elif (nextToken == int_dec or nextToken == char_dec or nextToken == float_dec or nextToken == string_dec or nextToken == bool_dec or nextToken == VARIABLE):
        Assignment()
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
    elif (nextToken == print_state):
        Printing()
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
    elif (nextToken == read_state):
        lex()
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
    elif (nextToken == fxncall):
        lex()
        Call()
        outfile.write('\n')
        for i in range(tabs):
            outfile.write('\t')
    elif (nextToken == break_state or nextToken == continue_state or nextToken == exit_state):
        Control()
    else:
        return  # Exit lng kung wala ng next statements after the last repitition,
                # no need to lex cuz the nextToken will be checked for a match again outside the function
    if(nextToken == ENDOFSTATE):
        lex()
        StatePrime()

##<Loop> -> "RT" <Condition> "{" <Block> "}"
def Loop():
    global tabs
    global nextToken
    print("Enter <Loop>")
    lex()
    Condition()
    outfile.write(':\n')
    tabs += 1
    for i in range(tabs):
        outfile.write('\t')
    if(nextToken == openBrace):
        lex()
        Block()
        if(nextToken == closeBrace):
            print("Exit <Loop>")
            tabs-=1
            lex()
        else:
            print("Expectetd '}'")
            error()
    else:
        print("Expected '{'")
        error()

##<If> -> "IF" <Condition> "FOLLOW" "{" <Block> "}" <ElseIf> <Else>
#        | "IF" <Condition> "FOLLOW" "{" <Block> "}" <Else>
#        | "IF" <Condition> "FOLLOW" "{" <Block> "}"
def If():
    global nextToken
    global tabs
    print("Enter <If>")
    if (nextToken == if_state):
        lex()
        Condition()
        if (nextToken == exec_state):
            lex()
            if (nextToken == openBrace):
                tabs+=1
                outfile.write(':\n')
                for i in range(tabs):
                    outfile.write('\t')
                lex()
                Block()
                if (nextToken == closeBrace):
                    tabs-=1
                    outfile.write('\n')
                    for i in range(tabs):
                        outfile.write('\t')
                    lex()
                    if (nextToken == elseif_state):
                        Elseif()
                    if (nextToken == else_state):
                        Else()
                    print("Exit <If>")
                    return
        print("Error: Invalid IF statement")
        error()

##<ElseIf> -> "ELSEIF" <Condition> "FOLLOW" "{" <Block> "}" <Elseif>
def Elseif():
    global nextToken
    global tabs
    print("Enter <Elseif>")
    lex()
    Condition()
    if(nextToken == exec_state):
        lex()
        if(nextToken == openBrace):
            tabs+=1
            outfile.write(':\n')
            for i in range(tabs):
                outfile.write('\t')
            lex()
            Block()
            if (nextToken == closeBrace):
                outfile.write('\n')
                tabs-=1
                for i in range(tabs):
                    outfile.write('\t')
                lex()
                if (nextToken == elseif_state):
                    Elseif()
                print("Exit <Elseif>")
                return
    print("Error: Invalid ELSEIF statement")
    error()

##<Else> -> "ELSE" "{" <Block> "}"
def Else():
    global nextToken
    global tabs
    print("Enter <Else>")
    lex()
    tabs+=1
    if(nextToken == openBrace):
        outfile.write(':\n')
        for i in range(tabs):
            outfile.write('\t')
        lex()
        Block()
        if (nextToken == closeBrace):
            tabs-=1
            outfile.write('\n')
            lex()
            print("Exit <Else>")
            return
    print("Error: Invalid ELSE statement")
    error()

#<Assignment> -> <DType> VARIABLE "=" VARIABLE
#                | <DType>  VARIABLE "=" <Reading> # May function na to
#                | "@INT"  VARIABLE "=" INT
#                | "@CHIRP"  VARIABLE "=" CHAR
#                | "@COKE"  VARIABLE "=" FLOAT
#                | "@MSG"  VARIABLE "=" STRING
#                | "@TRALSE"  VARIABLE "=" "YES"
#                | "@TRALSE"  VARIABLE "=" "NO"
#                | <DType>  VARIABLE "=" "(" <Exp> ")"
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
                    lex()
                    return
                elif(nextToken == openParen):
                    lex()
                    Exp()
                    if(nextToken == closeParen):
                        lex()
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
                    lex()
                    return
                elif(nextToken == openParen):
                    lex()
                    Exp()
                    if(nextToken == closeParen):
                        lex()
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
                    lex()
                    return
                elif(nextToken == openParen):
                    lex()
                    Exp()
                    if(nextToken == closeParen):
                        lex()
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
                    lex()
                    return
                elif(nextToken == openParen):
                    lex()
                    Exp()
                    if(nextToken == closeParen):
                        lex()
                        return
    elif(nextToken == bool_dec):
        lex()
        if(nextToken == VARIABLE):
            lex()
            if (nextToken == asSign):
                lex()
                if (nextToken == TRUE or nextToken == FALSE or nextToken == VARIABLE):
                    lex()
                    return
                elif(nextToken == read_state):
                    lex()
                    return
                elif(nextToken == openParen):
                    lex()
                    Exp()
                    if(nextToken == closeParen):
                        lex()
                        return
    elif (nextToken == VARIABLE):
        lex()
        if (nextToken == asSign):
            lex()
            if (nextToken == TRUE or nextToken == FALSE or nextToken == VARIABLE or nextToken == INT or nextToken == FLOAT or nextToken == CHAR or nextToken ==STRING):
                lex()
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


##<Call> ->  VARIABLE "(" <Args> ")"
def Call():
    global nextToken
    print("Enter <Call>")
    lex()
    if (nextToken == openParen):
        lex()
        Args()
        print("Exit <Call>")
        return
    print("Invalid function call")
    error()

##<Printing> -> "TWEET"  VARIABLE
#              | "TWEET" "(" <EXP> ")"
#              | "TWEET" INT
#              | "TWEET" FLOAT
#              | "TWEET" CHAR
#              | "TWEET" STRING
#              | "TWEET" "YES"
#              | "TWEET" "NO"
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
    elif (nextToken == INT or nextToken == FLOAT or nextToken == CHAR or nextToken == STRING or nextToken == TRUE or nextToken == FALSE or nextToken == VARIABLE):
        lex()
        print("Exit <Printing>")
        return
    print("Expected expression, varable or literal")
    error()

##<Reading> - > "REPLY"
def Reading():
    print("Enter <Reading>")
    lex()
    print("Exit <Reading")

##<Control> -> "UNFOLLOW" | "LIKE" | "BLOCK"
def Control():
    global nextToken
    print("Enter <Control>")
    lex()
    print("Exit <Control>")

##This part is the one we made sa ME
# Copy na lng natin

##<Exp> -> <Term> <ExpPrime>
def Exp():
    print "Enter <Exp>"
    Term()
    ExpPrime()
    print "Exit <Exp>"

##<ExpPrime> -> "+" <Term> <ExpPrime>
#            | "-" <Term> <ExpPrime>
def ExpPrime():
    global nextToken
    while (nextToken == plusSign or nextToken == minusSign):
		lex()
		Term() # No need to call ExpPrime since we can just loop it

##<Term> -> <Fact> <TermPrime>
def Term():
	print "Enter <Term>"
	Fact()
	TermPrime()
	print "Exit <Term>"

##<TermPrime> -> "*" <Fact> <TermPrime>
#            | "/" <Fact> <TermPrime>
def TermPrime():
    global nextToken
    while (nextToken == divSign or nextToken == mulSign):
        lex()
        Fact()

##<Fact> -> INT | CHAR | FLOAT | VARIABLE | "(" <Exp> ")"
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

##<Condition> -> "(" <Conditional> ")" | "~" <Condition>
def Condition():
    global nextToken
    print("Enter <Condition>")
    if(nextToken == NOT):
        lex()
        Condition()
        print("Exit <Condition>")
        return
    elif(nextToken == openParen):
        lex()
        Conditional()
        if(nextToken == closeParen):
            lex()
            print("Exit <Condition>")
            return
        else:
            print("Expected ')'")
            error()
    print("Error: Expected is a ~ or a variable name -- basta bool expression")
    error()

##<Conditional> -> VARIABLE <Conditional> VARIABLE
#          | { VARIABLE | INT | CHAR | FLOAT } <CondOp> <Logic>
#          | <Conditional> <CondOp> <Conditional>
#          | <Condition> <CondOp> {VARIABLE | INT | CHAR | FLOAT }
#          | { VARIABLE | INT | CHAR | FLOAT } <CondOp> { VARIABLE | INT | CHAR | FLOAT }
def Conditional():
    global nextToken
    print("Enter <Conditional>")
    if (nextToken == VARIABLE or nextToken == INT or nextToken == CHAR or nextToken == FLOAT):
        lex()
    elif (nextToken == openParen or nextToken == NOT):
        Condition()
        lex()
    else:
        error()
    CondOp()
    if (nextToken == VARIABLE or nextToken == INT or nextToken == CHAR or nextToken == FLOAT):
        lex()
        print("Exit <Conditional>")
        return
    elif (nextToken == openParen or nextToken == NOT):
        Condition()
        lex()
        print("Exit <Conditional>")
        return
    else:
        print("Expected nextToken is a variable name or '(' ")
        error()
    print("Invalid  expression")
    error()

##<CondOP> -> ">=" | "<=" | "==" | ">" | "<"
def CondOp():
    global nextToken
    print("Enter <CondOp>")
    if (nextToken == greatEqSign or nextToken == lessEqSign or nextToken == eqSign or nextToken == lesserSign or nextToken == greaterSign):
        lex()
        print("Exit <CondOp>")
        return
    else:
        print("Expected conditional operator")
        error()

##<Dtype> -> "@INT" | "@CHIRP" | "@COKE" | "@MSG" | "@TRALSE"
def Dtype():
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
        if (nextToken == closeParen):
            lex()
            print("Exit <Args>")
            return
        else:
            print "Expected ')' "
            error()
    error()

##<Return> -> "REPORT" { INT | CHAR | FLOAT | STRING | VARIABLE } | "REPORT" "(" <Exp> ")"
def Return():
    global nextToken
    print("Enter <Return>")
    lex()
    if (nextToken == INT or nextToken == CHAR or nextToken == FLOAT or nextToken == STRING or nextToken == VARIABLE):
        lex()
        print("Exit <Return>")
        return
    elif (nextToken == openParen):
        lex()
        Exp()
        if (nextToken == ")"):
            lex()
            print("Exit <Return>")
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
	global orig

	input = []
	tempLexeme = " "
	print("Reading: " + str(sys.argv[1]) + '.twt')
	try:
		os.remove('outputfile.py')
	except OSError:
		pass
	outfile = open('outputfile.py', 'w')
	outfile.write('import time\n\n\n')
	global outfile
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
	orig = input
	print "\n\nORIG: ", orig, "\n"
	lex()

	Program()
	outfile.write('\n\nprint "Program exiting in 10s.."\ntime.sleep(10)')
	os.system('start python outputfile.py')

if __name__ == '__main__':
	main()
