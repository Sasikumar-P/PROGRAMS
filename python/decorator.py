class author(object):
	def __init__(self,name):
		self.name =  name
	def __call__(self,function):
		function.author=self.name
		return function
@author('Joe')
def func():
	pass

print func.author
