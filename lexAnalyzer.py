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
"{", 41
"}", 42
"+", 43
"-", 44
"/", 45
"*", 46
"=", 47
"(", 48
")", 49
"#", 50
",", 51
">=", 52
"<=", 53
"==", 54
">", 55
"<", 56
varname = 100


def lex(nextToken):
    if nextString == 'EOF':
		 = -1
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
    elif (nextString[0] == '\"') and (nextString[-1] == '\"'):
    	nextToken = STRING
    elif (nextString[0] == '\'') and (nextString[-1] == '\''):
    	nextToken = CHAR
    elif nextString == '':
    	nextToken =
    else
        nextToken = varname
    return nextToken
