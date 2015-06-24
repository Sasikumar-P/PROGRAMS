stack = []
def pushit():
	stack.append(raw_input('enter new string:').strip())
def popit():
	if len(stack) == 0:
		print 'cannot pop an item from an empty stack'
	else:
		print 'Removed [','stack.pop()',']'
def viewstack():
	print stack
CMDs={'u':pushit,'o':popit,'v':viewstack}
def showmenu():
	pr="""
	p(U)sh
	p(O)p
	(V)iew
	(Q)uit
Enter choice:"""
	while True:
		while True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except (EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'
			print '\nYou Picked:[%s]'%choice
			if choice not in 'uovq':
				print 'invalid option,try again'
			else:
				break
		if choice=='q':
			break
		CMDs[choice]()
if __name__ =='__main__':
	showmenu() 
