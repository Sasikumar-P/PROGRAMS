filename = raw_input("enter a file name:")

fobj = open(filename,'w')
while True:
	line = raw_input("enter ('.' to quit):")
	if line !='.':
		fobj.write('%s%s'%(line,os.linesep)
	
	
fobj.close()
