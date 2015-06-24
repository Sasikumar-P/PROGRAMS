class Ttype(object):
	def displayNumType(num):
		print num,'is',
		if isinstance(num, (int, float,long,complex)):
			print 'a number of type:',type(num).__name__
		else:
			print 'not a number at all!!'
