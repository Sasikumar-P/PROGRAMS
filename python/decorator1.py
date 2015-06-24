def author(name):
	def helper(theme):
		theme.author = name
		return theme
	return helper

@author('sasikumar')
def func():
	pass
print func.author
