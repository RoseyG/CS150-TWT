#ME1-CS150
#Program: BOTTOM-UP PARSER USING LR-PARSING
#Name:  Mikaela Jun Lenon
#Student Number: 2013-18032
#___________ D E C L A R A T I O N _____________________
nextToken = 0
ID = 11					
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
ID_a  = 12 				#ADDITIONAL VARIABLES USED
ID_b  = 13 				
ID_c  = 14 				
DOLLAR  = 15 			
A = 16					
E = 17					
T = 18 					
F = 19
#Needed for Reductions
VALUE = {1: [A, 6, 'A'], 2: [E, 6, 'E'], 3: [E,6, 'E'], 4: [E, 2, 'E'], 5: [T, 6, 'T'], 6: [T, 6, 'T'], 7: [T, 2, 'T'], 8: [F, 6,'F'], 9: [F, 2, 'F'], 10: [ID, 2, 'id'], 11: [ID, 2, 'id'], 12: [ID, 2, 'id']}
#Needed for Parsing-- Reductions or Shift
table = {ID_a: ['s3', -1, -1, -1, -1, -1, 's3', -1, -1, -1, 's3', -1, 's3', 's3', 's3', 's3', -1, -1, -1, -1, -1, -1], ID_b: ['s4', -1, -1, -1, -1, -1, 's4', -1, -1, -1, 's4', -1, 's4', 's4', 's4', 's4', -1, -1, -1, -1, -1, -1], ID_c: ['s5', -1, -1, -1, -1, -1, 's5', -1, -1, -1, 's5', -1, 's5', 's5', 's5', 's5', -1, -1, -1, -1, -1, -1], DOLLAR: [-1, 'acc', -1, 'r10', 'r11', 'r12', -1, 'r1', 'r4', 'r7', -1, 'r9', -1, -1, -1, -1, -1, 'r2', 'r3', 'r5', 'r6', 'r8'], ASSIGN_OP: [-1, -1, 's6', 'r10', 'r11', 'r12', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],	ADD_OP: [-1, -1, -1, 'r10', 'r11', 'r12', -1, 's12', 'r4', 'r7', -1, 'r9', -1, -1, -1, -1, 's12', 'r2', 'r3', 'r5', 'r6', 'r8'], SUB_OP: [-1, -1, -1, 'r10', 'r11', 'r12', -1, 's13', 'r4', 'r7', -1, 'r9', -1, -1, -1, -1, 's13', 'r2', 'r3', 'r5', 'r6', 'r8'], MULT_OP: [-1, -1, -1, 'r10', 'r11', 'r12', -1, -1, 's14', 'r7', -1, 'r9', -1, -1, -1, -1, -1, 's14', 's14', 'r5', 'r6', 'r8'], DIV_OP: [-1, -1, -1, 'r10', 'r11', 'r12', -1, -1, 's15', 'r7', -1, 'r9', -1, -1, -1, -1, -1, 's15', 's15', 'r5', 'r6', 'r8'], LEFT_PAREN: [-1, -1, -1, -1, -1, -1, 's10', -1, -1, -1,'s10', -1, 's10', 's10', 's10', 's10', -1, -1, -1, -1, -1, -1], RIGHT_PAREN: [-1, -1, -1, 'r10', 'r11', 'r12', -1, -1, 'r4', 'r7', -1, 'r9', -1, -1, -1, -1, 's21', 'r2', 'r3', 'r5', 'r6', 'r8'], A: [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], E: [-1, -1, -1, -1, -1, -1, 7, -1, -1, -1, 16, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],	T: [-1, -1, -1, -1, -1, -1, 8, -1, -1, -1, 8, -1, 17, 18, -1, -1, -1, -1, -1, -1, -1, -1], F: [-1, -1, -1, -1, -1, -1, 9, -1, -1, -1, 9, -1, 9, 9, 19, 20, -1, -1, -1, -1, -1, -1], ID: [2, -1, -1, -1, -1, -1, 11, -1, -1, -1, 11, -1, 11, 11, 11, 11, -1, -1, -1, -1, -1, -1]}

#Getting the tokens of the lexemes to parse
def lex(nextChar):
	global nextToken, cnt
	if nextChar == 'a':
		nextToken = ID_a
	elif nextChar == 'b':
		nextToken = ID_b
	elif nextChar == 'c':
		nextToken = ID_c
	elif nextChar == '(':
		nextToken = LEFT_PAREN
	elif nextChar == ')':
		nextToken = RIGHT_PAREN
	elif nextChar == '+':
		nextToken = ADD_OP	
	elif nextChar == '-':
		nextToken = SUB_OP	
	elif nextChar == '*':
		nextToken = MULT_OP
	elif nextChar == '/':
		nextToken = DIV_OP	
	elif nextChar == '=':
		nextToken = ASSIGN_OP
	elif nextChar == '$':
		nextToken = DOLLAR		
	else:
		print "Syntax Error"
		exit()

def printresult(step, stack, inpt, action):
	string=''
	for m in stack:
		m = str(m)
		string = string + m
	string2=''
	for n in reversed(inpt):
		string2 = string2 + n
	print step, '\t', string, '\t', string2, '\t', action
	

def LR_Parser():
	stack = [0]											#necessary lists, string, counter
	inpt = []
	string = []
	action = ''
	step = 0

	temp = raw_input()									#Getting Input, Storing all non-space character to string list
	for j in temp:
		if ord(j) !=+32: string.append(j)
	string.append('$')

	for k in string:
		lex(k)											#getting token of that element
		
	for i in reversed(string):							#reversed the string so I can pop the "leftmost" easily
		inpt.append(i)
	print 'STEP \t STACK \t\t INPUT \t action'

	#PARSING PROPER
	while(action != 'acc'):
		st_top = stack[-1]								#holds topmost element of stack (rightmost)
		in_top = inpt[-1]								#holds topmost elem of input (lefmost) **reversed 
		lex(in_top)										#getting token of that element
		action = table[nextToken][st_top]				#tracing the action given the nextToken and the top of stack
		if action == -1: 
			print 'Syntax Error'
			exit()
		letter = action[0]								#Determines if Reduction or Shift
		printresult(step, stack, inpt, action)	
		step+=1  
		#EXIT IF DONE
		if(action == 'acc'):	exit()	
		x = 1 											#getting what State (S1, S2, etc)
		num = ''
		while x<len(action):							#necessary for two-digit numbers 
			num = num + action[x]
			x +=1
		num = int(num)	
		#SHIFT
		if(letter == 's'):
			stack.append(in_top)
			inpt.pop(-1)
			stack.append(num)
		#REDUCTION -- check VALUE list above
		elif(letter == 'r'):
			i = 0
			while i < VALUE[num][1]:					#Value[num][1] == numOfEqns * 2
				stack.pop(-1)
				i+=1
			old_top = stack[-1]							#APPENDING THE NONTERMINAL
			stack.append(VALUE[num][2])					#going to
			new_top = table[VALUE[num][0]][old_top]		#new_state
			printresult(step, stack, inpt, new_top)
			step+=1  	
			stack.append(new_top)						#THEN APPENDING THE NEW STATE


LR_Parser()