def no_return():
	print("I am about to raise an exception")
	raise Exception("This is always raised")
	print("This line will never execute")
	return "I won't be returned"
#no_return()

try:
	no_return()
except:
	print("I caught an exception")
print("Excuted after the exception")
def funny_division(divider):
	try:
		return 100/divider
	except ZeroDivisionError:
		return "Zero is not a good Idea"
print(funny_division(0))
print(funny_division(9))
def funny_division2(anumber):
	try:
		if anumber==13:
			raise ValueError("13 is an unlucky number")
		return 100/anumber
	except (ZeroDivisionError,TypeError):
		return "Enter a number other than zero"
for val in (0,"hello",50.0,13):
	print("testing {}:".format(val), end='')
	print(funny_division2(val))
def funny_division3(anumber):
	try:
		if anumber ==13:
			raise ValueError("13 is an unlucky number")
		return 100/anumber
	except ZeroDivisionError:
		return "Enter a number other than zero"
	except TypeError:
		return "Enter a numerical value"
	except ValueError:
		print("No, no , not 13!")
		raise
print(funny_division3(13))
