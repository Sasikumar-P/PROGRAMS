class Animal:
	def Name(self):
		pass
	def Sleep(self):
		pass
	def MakeNoise(self):
		pass


class 	Dog(Animal):
	def Name(self):
		print " I am a dog"
	def MakeNoise(self):
		print '	Woof'


class Cat(Animal):
	def Name(self):
		print 'I am a cat'
	def MakeNoise(self):
		print 'Meow'
class Lion(Animal):
	def Name(self):
		print "i am a lion"
	def MakeNoise(self):
		print "Roar"


class TestAnimals:
	def PrintName(self,animal):
		animal.Name()
	def GotoSleep(self,animal):
		animal.sleep()
	def MakeNoise(self,animal):
		animal.MakeNoise()
