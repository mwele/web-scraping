class House:
	def __init__(self,price):
		self._price=price


	@property
	def price(self):
		return self._price
	@price.setter
	def price(self,new_price):
		if new_price > 0 and isinstance(new_price,float):
			self._price=new_price
		else:
			print("Please enter a valid price")
	@price.deleter
	def price(self):
		del self._price

h=House(787)
print(h.price)
h.price=898989.99
print(h.price)
print(help(h))
	#print(h.price)
