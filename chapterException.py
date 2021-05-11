

'''def Divide_by_x():
	x=input("Enter the value of x here:")
	x=int(x)
	try:
		print(x/0)
	except AssertionError as e:
		print(e)
		print("We cannot divide by zilch")

Divide_by_x()'''
import sys
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


try:
	linux_interaction()
except AssertionError as error:
	print(error)
else:
	try:
		with open('file.log') as file:
			read_data=file.read()
	except FileNotFoundError as fnf_error:
		print(fnf_error)
finally:
	print('Cleanig yp, irrespective of any exceptions')


class InvalidWithdrawal(Exception):
	def __init__(self,balance,amount):
		super().__init__("Account doesn't have ${}".format(amount))
		self.amount=amount
		self.balance=balance
	def overage(self):
		return self.amount-self.balance


#raise InvalidWithdrawal(34,67)
try:
	raise InvalidWithdrawal(7,66)
except InvalidWithdrawal as e:
	print("I'm sorry, but your withdrawal is more than your balance by ${}".format(e.overage()))