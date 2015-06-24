fname = raw_input("enter filename: ")
print "attempt to opened the file for reading "
try:
	fobj = open(fname,'r')
except IOError, e:
	print "*** file open error",e
else:
	for eachLine in fobj:
		print eachLine,
	fobj.close()
