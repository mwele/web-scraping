class EvenOnly(list):
	def append(self,integer):
		if not isinstance(integer,int):
			raise TypeError("Only integer can be added")
		if integer %2:
			raise ValueError("Only even numbers can be added")
		super().append(integer)
e=EvenOnly()
#e.append(9)

#e.append(10)
print("_________________")
def no_return():
	print("I am about to raise an exception")
	raise Exception("This is always raised")
	print("This line will never execute")
	return "I won't be returned"
try:
	no_return()
except:
	#print("I caught an Exception")
	pass
print("Executed after the exception")
