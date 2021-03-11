class ContactList(list):
	"""docstring for ClassName"""
	def search(self,name):
		'''return all the contacts that contain the search value
		in their name'''
		matching_contacts=[]
		for contact in self:
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts
class Contact:
	all_contacts=ContactList()
	def __init__(self,name,email):
		self.name=name
		self.email=email
		self.all_contacts.append(self)
c=Contact("John A ","john@gmail")
c=Contact("kyalo Jeez","Kyalo@gmail")
print([c.name for c in Contact.all_contacts.search('Kyalo')])