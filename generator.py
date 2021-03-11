def my_generator():
	yield 1
	yield 2
	yield 3
g=my_generator()
value =next(g)
print(value)
import cProfile
cProfile.run(value)
''''value =next(g)
print(value)

value =next(g)
print(value)'''

'''If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.

The difference is that while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.'''