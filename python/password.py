passwordlist=['amal1234','amal123','amal12','amal1','amal']

valid = False

count = 3
while count > 0:
	inp = raw_input("enter password")
	for each in passwordlist:
		if inp == each:
			valid =True
			break
	if not valid:
		print "invalid input"
		count -= 1
		continue
	else:
		break
