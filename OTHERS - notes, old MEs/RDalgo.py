## Lexical analyzer
#
# This is the function for the lexical analyzer. It take the input string and the variable x which is the location of the next token. It then checks if the token is valid an returns the next token and an incremented x to move the position in the input string.
def lex(line,x):
	if x < len(line):
		nextChar = line[x]
	else:
		nextChar = 'EOF'
		nextToken = -1
	if nextChar == '=':
		nextToken = 20
	elif nextChar == '+':
		nextToken = 21
	elif nextChar == '-':
		nextToken = 22
	elif nextChar == '*':
		nextToken = 23
	elif nextChar == '/':
		nextToken = 24
	elif nextChar == '(':
		nextToken = 25
	elif nextChar == ')':
		nextToken = 26
	elif nextChar == 'a':
		nextToken = 11
	elif nextChar == 'b':
		nextToken = 11
	elif nextChar == 'c':
		nextToken = 11
	print "Next token is: " + str(nextToken) + " Next lexeme is: " + nextChar
	return nextToken, x+1

## Rule A -> id = E
#
# This is the function for the rule A -> id = E. iden() is called then lex() to check if the next token is '='. If yes, lex() is called again to get the next token then the function expr(). If an error exists then the error function is called.
def assign(nextToken, line, x):
	print "Enter <A>"
	iden(nextToken)
	nextToken, x = lex(line, x)
	if nextToken == 20:
		nextToken, x = lex(line, x)
		nextToken, x = expr(nextToken, line, x)
	else:
		error()
	if nextToken != -1:
		error()
	else:
		print "Exit <A>"

## Rule E -> TE'
#
# This is the function for the rule E -> TE'. The function term() is called then the function expr() to see that the poduction rule is met. It returns to the function that called it the nextToken and the position 'x' on the input string after going though the functions.
def expr(nextToken, line, x):
	print "Enter <expr>"
	nextToken, x = term(nextToken, line, x)
	nextToken, x = exprP(nextToken, line, x)
	print "Exit <expr>"
	return nextToken, x

## Rule E' -> +TE' | -TE'
#
# This is the function for the rule E' -> +TE' | -TE'. While the next token is either a '+' or a '-', it calls the function lex() then term() to check if the either production rules is matched. It also returns to the function that called it the nextToken and the position 'x' on the input string.
def exprP(nextToken, line, x):
	while (nextToken == 21) or (nextToken == 22):
		nextToken, x = lex(line, x)
		nextToken, x = term(nextToken, line, x)
	return nextToken, x

## Rule T -> FT'
#
# This is the function for the rule T -> FT'. It calls fact() then termP() to check if the following input characters match it's production rule.It returns to the function that called it the nextToken and the position 'x' on the input string.
def term(nextToken, line, x):
	print "Enter <term>"
	nextToken, x = fact(nextToken, line, x)
	nextToken, x = termP(nextToken, line, x)
	print "Exit <term>"
	return nextToken, x

## Rule T' -> *FT' | /FT'
#
# This is the function for the rule T' -> *FT' | /FT'. While the next token is either a '*' or a  '/', it calls lex() and then fact(). It returns to the function that called it the nextToken and the position 'x' on the input string.
def termP(nextToken, line, x):
	while (nextToken == 23) or (nextToken == 24):
		nextToken, x = lex(line, x)
		nextToken, x = fact(nextToken, line, x)
	return nextToken, x

## Rule F -> id | (E)
#
# This is the function for the rule F -> id | (E). First it check which production the nextToken will fit then calls the function or functions that correspond to that production. The error function is called if it doesn't match any of the productions. It returns to the function that called it the nextToken and the position 'x' on the input string.
def fact(nextToken, line, x):
	print "Enter <factor>"
	if nextToken == 11:
		iden(nextToken)
		nextToken, x = lex(line, x)
	elif nextToken == 25:
		nextToken, x = lex(line, x)
		nextToken, x = expr(nextToken, line, x)
		if nextToken == 26:
			nextToken, x = lex(line, x)	
		else:
			error()
	else:
		error()
	print "Exit <factor>"
	return nextToken, x

## Rule id -> a | b | c
#
# This is the function for the rule id -> a | b | c. It checks if the next token encountered is a terminal, otherwise it calls the error function.
def iden(nextToken):
	print "Enter <id>"
	if nextToken == 11:
		print "Exit <id>"
	else:
		error()

## Error
#
# This is the error function. It prints an error message and quits the program after.
def error():
	print "Syntax Error"
	quit()

## Main Function
#
# This is the main function. It takes an input string from the commandline and removes all the whitespaces and then calls the function lex() to get the next token. It then passes it on to the function assign() along with the input string and the location of the token after. The algorithm for the functions that checks the rules were patterned after the ones found in the book Concepts of Programmng Languages. Various modifications have been done in translating from C to python.
def main():
	rawline = raw_input()
	line = ''
	for n in rawline:
		if n != ' ':
			line += n
	x = 0
	nextToken, x = lex(line, x)
	assign(nextToken, line, x)

if __name__ == '__main__':
	main()
