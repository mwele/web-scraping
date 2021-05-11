class MyClass:
	def method(self):
		return 'instance method called',self
	@classmethod
	def classmethod(cls):
		return 'class method called',cls

	@staticmethod
	def staticmethod():
		return 'staticmethod called'

obj=MyClass()
#print(obj.method())
#print(MyClass.method())
print(obj.classmethod())
print(obj.staticmethod())

print(MyClass.classmethod())
print(MyClass.staticmethod())
print(MyClass.method())