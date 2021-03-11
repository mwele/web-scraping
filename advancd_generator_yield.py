'''When the Python yield statement is hit, the program suspends function execution and returns the yielded value to the caller. 
(In contrast, return stops function execution completely.) When a function is suspended, the state of that function is saved. 
This includes any variable bindings local to the generator, the instruction pointer, the internal stack, and any exception handling.'''

def multi_yield():
	yield_str = "This will print the first string"
	yield yield_str
	yield_str = "This will print the second string"
	yield yield_str
multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))
print(next(multi_obj))