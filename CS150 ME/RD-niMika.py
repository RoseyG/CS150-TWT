#ME1-CS150
#Program: RD ALGORITHM
#Name:  Mikaela Jun Lenon
#Student Number: 2013-18032

#___________ D E C L A R A T I O N _____________________

global my_list
nextToken = 0
cnt = 0
IDENT  = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

#_____________F U N C T I O N S _______________________

def lex(nextChar):
	global nextToken
	if nextChar == 'a' or nextChar == 'b' or nextChar == 'c':
		nextToken = IDENT
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
	else:
		nextToken = -1
#		print "token for ", nextChar, " not found."

	print "Next Token is ", nextToken, ". Next Lexeme is ", nextChar

def A(): #A -> id = E
	global cnt
	print "ENTER <A>"
	id()
	if(cnt + 1 < len(my_list)):
		cnt+=1
		lex(my_list[cnt])
		if nextToken == ASSIGN_OP:		#if equal to =
			cnt+=1
			lex(my_list[cnt])
			E()					#GO TO E()
		else: 
			print "Error. Expected =  : given ", my_list[cnt]
			exit()
	print "EXIT <A>"

def id():
	global cnt
	print "ENTER <id>"		
	if cnt + 1 < len(my_list):
		if nextToken != IDENT:				
			print "Error. Expected a, b, or c : given ", my_list[cnt] 
			exit()
	print "EXIT <id>"

def E():
	global cnt
	print "ENTER <E>"
	T()
	if(cnt + 1 < len(my_list)):
		while nextToken == ADD_OP or nextToken == SUB_OP: 	#--> + 
			cnt+=1
			lex(my_list[cnt])
			T()
	print "EXIT <E>"
	
def T():
	global cnt
	print "ENTER <T>"
	F()
	if(cnt + 1 < len(my_list)):
		cnt+=1
		lex(my_list[cnt])
		while nextToken == MULT_OP or nextToken == DIV_OP: #--> *
			cnt+=1
			lex(my_list[cnt])
			F()
			cnt+=1
			lex(my_list[cnt])
	print "EXIT <T>"
	
def F():
	global cnt
	print "ENTER <F>"
	if(cnt + 1 <len(my_list)):
		if nextToken == LEFT_PAREN: #--> (
			cnt = cnt+1
			lex(my_list[cnt])
			E()
			if nextToken != RIGHT_PAREN:
				print "ERROR. Expected ) : given ", my_list[cnt]
				exit()
		elif nextToken == IDENT: 
			id()
		else:
			print "ERROR. Expected (, a, b, or c : given ", my_list[cnt]
			exit()
	print "EXIT <F>"	

#_______MAIN_________

inpt = raw_input("What's the input? ") 
my_list = []
for j in inpt: 
	if(ord(j)!=32): 	my_list.append(j) #ERROR DAPAT
my_list.append('EOF')	

lex(my_list[0])
A()