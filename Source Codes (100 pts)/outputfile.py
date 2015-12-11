import time


def HAHAHA(X):
	print "Kaya mo yan"
	print "Oo Kaya mo yan"
	X=0
	
def HIHIHI(Y):
	print "Kaya mo yan"
	print "Oo Kaya mo yan"
	Y=0
	
X=0
Y=32
while (X<4):
	X=(X+1)
	Y=(Y+2)
	print X
	if (X>=Y):
		print "Ahihi"
		
	else :
		Y=X
		HAHAHA(X)
		

	while (X<4):
		X=(X+1)
		Y=(Y+2)
		print X
		if (X>=Y):
			print "Ahihi"
			
		else :
			Y=X
			HAHAHA(X)
			

		
	
print X
HAHAHA(X)
HIHIHI(X)


print "Program exiting in 10s.."
time.sleep(10)