import string
alphas=string.letters+'_'
nums=string.digits

print 'welcome to the identifier checker '
myInput=raw_input("enter a identifier to test")
if len(myInput) > 1:
	if myInput[0] not in alphas:
		print ''' invalid ,first symbol must be a alphanumeric'''
	else:
		for otherChar in myInput[1:]:
			if otherChar not in alphas + nums:
				print '''invalid:remaining symbols must be alphanumeric'''
				break
			else:
				print "okay as an identifier"
