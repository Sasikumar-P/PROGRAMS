
n=input("enter the number from counting want to start")
def countdown(n):
	print "couting down from",n
	while n>0:
		yield n
		n-=1
print list(countdown(n))
