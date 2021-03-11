import random
some_exceptions=[ValueError, TypeError,IndexError,None]
try:
	choice =random.choice(some_exceptions)
	print("raising {}".format(choice))
	if choice:
		raise choice("An error")
except ValueError:
	print("caught a ValueError")
except TypeError:
	print("caught a TypeError")
except Exception as e:
	print("caught some other error: %s" (e.__class__.name))
else:
	print("this code called if there is no Exception")
finally:
	print("This cleanup code is always called")
	