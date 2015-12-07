int_dec = 3
float_dec = 4
char: "@CHIRP", 5
string: "@MSG", 6
bool: "@TRALSE", 7
login: "@LOGIN", 1
logout: "@LOGOUT", 0
if: "IF", 20
elseif: "ELSEIF", 21
loop: "RT", 30
break: "UNFOLLOW", 31
continue: "LIKE", 32
exit: "BLOCK", 33
exec: "FOLLOW", 34
read: "REPLY", 10
print: "TWEET", 11
return: "REPORT", 12
true: "YES", 13
no: "NO", 14
INT: 71
FLOAT: 72
CHAR: 73
STRING: 74
BOOL: 75
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
	elif nextString == '':
		nextToken =
    elif nextString == '':
    		nextToken =
    elif nextString == '':
    		nextToken =
    elif nextString == '':
    		nextToken =
    return nextToken
