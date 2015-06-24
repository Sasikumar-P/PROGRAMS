class deprecated():
	def __init__():
		pass
	def __call___(func):
		func=func
		count=0
		return wrapper
	def wrapper(*args,**kwargs):
		count+=1
		if count == 1:
			print func.__name__,'is deprecated'
		return func(*args,**kwargs)

@deprecated
def f():
	pass

print 'f()'
