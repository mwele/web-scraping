
class Contact:
	all_contacts=[]
	def __init__(self,name,email):
		self.name=name
		self.email=email
		Contact.all_contacts.append(self)
	#print(all_contacts)

#c=Contact()
class Supplier(Contact):
	def order(self,order):
		print("if this were a real system we would send" "'{}' order to '{}' ".format (order,self.name))
c=Contact("somebody","somebody@gmail.com")
s=Supplier("supplier","supplier@gmail.com")
print(c.name,c.email)
print(s.name,s.email)
print(c.all_contacts)
print(s.order("I need pliers"))