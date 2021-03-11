from xtend_built_in import Contact

class Friend(Contact):
	def __init__(self,name, email,phone):
		super().__init__(name,email)
		self.phone=phone

c=Friend("kov","kov@maill",'9090909')
print(c.name)
print(c.phone)

