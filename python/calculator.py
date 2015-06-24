#calculator program 

loop = 1
choice = 0

while loop == 1:
	print "welcome to your calculator"
	print " "
	print "your options are"
	print "1)Addition"
	print "2)Subtraction"
	print "3)Multiplication"
	print "4)Division"
	print "5)Quit calculator.py"
	print " "

        choice =input("enter your choice here")

	if choice == 1:
		add1=input("Add this :")
		add2=input("to this:")
		print add1,"+",add2,"=",add1+add2
	elif choice == 2:
		sub1 = input("subtract this :")
		sub2=input("Form this :")
		print "the result is",sub1-sub2
	elif choice == 3:
		mul1=input("enter first")
		mul2=input("enter second")
		print "multiplication result is ",mul1*mul2
	elif choice == 4:
		div1=input("first number")
		div2=input("seconf number")
		print "division result is",div1/div2
	elif choice==5:
		break
print "thank you for using calculator.py"
