queue={}

def enQ():
	queue.append(raw_input("enter a number appennnd into the queue :").strip())
def deQ():
	if len(queue) == 0:
		print "cannot pop an element form empty queue"
	else:
		print "element remove",'[', 'queue.pop[0]',']'
def viewQ():
	print queue
CMDs ={'e':enQ,'d':deQ,'e':viewQ}
def showmenu():
	pr="""
(E)nqueue
(D)equeue
(V)iew
(Q)uit

Enter your choice: """
	while True:
		while True:
			try:
				choice =raw_input(pr).strip().lower()
			except (EOFError,KeyboardInterrupt,IndexError):
				choice='q'
			if choice not in 'edvq':
				print "invalid option :try again"
			else:
				break
		if choice =='q':
			break
		CMDs[choice]
if __name__ =='__main__':
	showmenu()
