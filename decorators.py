

def start_end_decorator(func):


	def wrapper():
		print('start')
		func()
		print('end')
	return wrapper
@start_end_decorator
def print_name():
	print('John')
print_name()