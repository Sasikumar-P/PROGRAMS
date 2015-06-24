class Person():
	def __init__(self,name):
		self.name=name
	
	def Sayhello(self):
		print "hello,my name is",self.name
	
	def __del__(self):
		print "%s says bye",self.name

