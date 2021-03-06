t_dec = 3 #  @INT
float_dec = 4 # @COKE
char_dec =  5 # @CHIRP
string_dec = 6 # @MSG
bool_dec = 7 # @TRALSE
login = 1 # @LOGIN
logout = 0 # @LOGOUT
if_state = 20 # IF
elseif_state = 21 # ELSEIF
else_state = 22 # ELSE
loop_state = 30 # RT
break_state = 31 # UNFOLLOW
continue_state = 32 # LIKE
exit_state = 33 # BLOCK
exec_state = 34 # FOLLOW
read_state = 10 # REPLY
print_state = 11 # TWEET
return_state = 12 # REPORT
TRUE = 13 # YES
FALSE = 14 # NO
NOT = 15 # '~'
INT = 71
FLOAT = 72
CHAR = 73
STRING = 74
openBrace = 41 # '{'
closeBrace = 42 # '}'
plusSign = 43
minusSign = 44
divSign = 45 # '/'
mulSign = 46
asSign = 47 # =
openParen = 48 # '('
closeParen = 49 # ')'
hashSymbol = 50 # '#'
commaSign = 51 # ',''
lessEqSign = 52 # '<='
greatEqSign = 53 # '>=''
eqSign = 54 # '=='
lesserSign = 55 # '<'
greaterSign = 56 # '>''
VARIABLE = 19
nextString = " "

def isfloat(str):
    try:
        float(str)
    except ValueError:
        return False
    return True

def lex():
    if nextString == 'EOF':
        nextToken = -1
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
    print(nextToken)

def main():
    global nextString
    line = raw_input("Enter: ")
    statement = line.split()
    for lexeme in statement:
        nextString = lexeme
        lex()

if __name__ == '__main__':
	main()
