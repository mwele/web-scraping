class Contact:
	all_contacts=[]
	def __init__(self,name,email):
		self.name=name
		self.email=email
		Contact.all_contacts.append(self)
	#print(all_contacts)


class Supplier(Contact):
	def order(self,order):
		print("If this were a real system we would send"
			"'{}' order to '{}'".format(order,self.name))

c=Contact("Some Body","somebody@example.net")
s=Supplier("Sup Plier","supplier@example.net")


print(c.name,c.email,s.name,s.email)
c.all_contacts
print(c.all_contacts)
s.order("I need pliers")
print("________________________________________________")
class ContactList(list):
	def search(self,name):
		"""Return all conatcts that contain the search value  in their name"""
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
c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johna@example.net")
c3 = Contact("John C", "johna@example.net")	
print([c.name for c in Contact.all_contacts.search('John')])
print([] == list())
print(isinstance ([],object))
print("__________________________________________________________")
class LongNameDict(dict):
	def longest_key(self):
		longest=None
		for key in self:
			if not longest or len(key) > len(longest):
				longest=key
		return longest
longkeys = LongNameDict()
longkeys['hello'] = 1
longkeys['longest yet'] = 5
longkeys['hello2'] = 'world'
print(longkeys.longest_key())
print("___________________________________")
class Friend(Contact):
	def __init__(self,name,email,phone):
		super().__init__(name,email)
		self.phone=phone
f=Friend("john","John@gmail.com",8989898)
print(f.name)
print(f.phone)
print(f.email)
print("____________________________")
class BaseClass:
	num_base_calls=0
	def call_me(self):
		print("Calling method on Base Class")
		self.num_base_calls+=1
class LeftSubClass(BaseClass):
	num_left_calls=0
	def call_me(self):
		BaseClass.call_me(self)
		print("Calling method on Left Subclass")
		self.num_left_calls +=1
class RightSubClass(BaseClass):
	num_right_calls=0
	def call_me(self):
		BaseClass.call_me(self)
		print("Clalling method on Right Subclass")
		self.num_right_calls +=1

class Subclass(LeftSubClass,RightSubClass):
	num_sub_calls=0
	def call_me(self):
		LeftSubClass.call_me(self)
		RightSubClass.call_me(self)
		print("Calling method on Subclass")
		self.num_sub_calls +=1
s=Subclass()
print(s.call_me())
print( s.num_sub_calls,s.num_left_calls,s.num_right_calls,s.num_base_calls)

print("_______________________________________")
class BaseClass:
	num_base_calls = 0
	def call_me(self):
		print("Calling method on Base Class")
		self.num_base_calls += 1
class LeftSubclass(BaseClass):
	num_left_calls = 0
	def call_me(self):
		super().call_me()
		print("Calling method on Left Subclass")
		self.num_left_calls += 1
class RightSubclass(BaseClass):
	num_right_calls = 0
	def call_me(self):
		super().call_me()
		print("Calling method on Right Subclass")
		self.num_right_calls += 1
class Subclass(LeftSubclass, RightSubclass):
	num_sub_calls = 0
	def call_me(self):
		super().call_me()
		print("Calling method on Subclass")
		self.num_sub_calls += 1
print( s.num_base_calls,s.num_left_calls,s.num_right_calls,s.num_sub_calls)
class Contact:
	all_contacts = []
	def __init__(self, name='', email='', **kwargs):
		super().__init__(**kwargs)
		self.name = name
		self.email = email
		self.all_contacts.append(self)
class AddressHolder:
	def __init__(self, street='', city='', state='', code='',
	**kwargs):
		super().__init__(**kwargs)
		self.street = street
		self.city = city
		self.state = state
		self.code = code
class Friend(Contact, AddressHolder):
	def __init__(self, phone='', **kwargs):
		super().__init__(**kwargs)
		self.phone = phone


class AudioFile:
	def __init__(self, filename):
		if not filename.endswith(self.ext):
			raise Exception("Invalid file format")
		self.filename = filename	
class MP3File(AudioFile):
	ext = "mp3"
	def play(self):
		print("playing {} as mp3".format(self.filename))
class WavFile(AudioFile):
	ext = "wav"
	def play(self):
		print("playing {} as wav".format(self.filename))
class OggFile(AudioFile):
	ext = "ogg"
	def play(self):
		print("playing {} as ogg".format(self.filename))
ogg = OggFile("myfile.ogg")
ogg.play()
mp3 = MP3File("myfile.mp3")
mp3.play()
#not_an_mp3 = MP3File("myfile.ogg")


print("_________________________________________________________")
from collections.abc import Container
print(Container.__abstractmethods__)
print(help(Container.__contains__))
print("________________________________________________")
class OddContainer:
	def __contains__(self,x):
		if not isinstance(x,int) or not x%2:
			return False
		return True
o=OddContainer()
print(isinstance(OddContainer,Container))
print(issubclass(OddContainer,Container))
#print(1 in OddContainer)
#print(3 in OddContainer)
print("_____________________________________________________")
import abc
class MediaLoader(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def play(self):
		pass
	@abc.abstractproperty
	def ext(self):
		pass
@classmethod
def __subclasshook__(cls, C):
	if cls is MediaLoader:
		attrs = set(dir(C))
		if set(cls.__abstractmethods__) <= attrs:
			return True
	return NotImplemented

class Wav(MediaLoader):
	pass
#x=Wav()
class Ogg(MediaLoader):
	ext='.ogg'
	def play(self):
		pass
y=Ogg()



