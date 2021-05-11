normal_list=[1,2,4,5,7]
class CustomSeq():
	def __len__(self):
		return 5
	def __getitem__(self,index):
		return "X {0} ".format(index)
class FunkyBackWards(object):
	"""docstring for FunkyBackWards"""
	def __reversed__(self):
		return "BACKWARDS"
for seq in normal_list, CustomSeq(),FunkyBackWards():
	print("\n {}:".format(seq.__class__.__name__), end=" ")
	for item in reversed(seq):
		print(item, end=',')


print("____________________")
import sys
print(sys.getsizeof('a'))

print(sys.getsizeof('aa'))

contents="some file contents"
file=open('filename.txt','w')
file.write(contents)
#file.close()
#file.read()
with open('filename.txt') as file:
	for line in file:
		print(line)

with open("hello.txt",'w') as f:
	f.write('Hello world')
	#f.read()
with open('hello.txt','r') as f:
	f.read()

class Email:
	def __init__(self, from_addr, to_addr, subject, message):
		self.from_addr=from_addr
		self.to_addr=to_addr
		self.subject=subject
		self.message=message
email=Email("a@example.com","b@example.com",
	"You Have Mail!",
	"Here's some mail for you"
	)
template="""
From:<{0.from_addr}>
To:<{0.to_addr}>
Subject:{0.subject}
{0.message}

"""
print(template.format(email))

subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax
print("Sub: ${} Tax: ${} Total: ${total}".format(
subtotal, tax, total=total))
print("Sub: ${:0.2f} Tax: ${:0.2f} "
"Total: ${total:0.2f}".format(
subtotal, tax, total=total))
print("{:.2f}".format(39.54484700000000))

orders = [('burger', 2, 5),
('fries', 3.5, 1),
('cola', 1.75, 3)]
print("PRODUCT QUANTITY PRICE SUBTOTAL")
for product, price, quantity in orders:
	subtotal = price * quantity
	print("{0:7s}{1: ^9d} ${2: <5.2f}${3: >7.2f}".format(
	product, quantity, price, subtotal))
characters = b'\x63\x6c\x69\x63\x68\xe9'
print(characters)
print(characters.decode("latin-1"))
characters = "cliché"
print(characters.encode("UTF-8"))
print(characters.encode("latin-1"))
print(characters.encode("CP437"))
try:
	print(characters.encode("ascii"))
except UnicodeError as e:
	print (e)

print("------------------------------------------")

import re
search_string="hello world"
pattern ="hello world"
match=re.match(pattern,search_string)
if match:
	print("regex matches")
else:
	print("Shit does not match")
try:
	import sys
	pattern=sys.argv[1]
	print(pattern)
	search_string = sys.argv[2]
	match = re.match(pattern, search_string)
	if match:
		template = "'{}' matches pattern '{}'"
	else:
		template = "'{}' does not match pattern '{}'"
	print(template.format(search_string, pattern))
except IndexError as e:
	print(e)


print(re.findall('a.','abacadefagah'))
print(re.findall('a(.)','abacadefagah'))
print(re.findall('(a)(.)','abacadefagah'))

print(re.findall('((a)(.))', 'abacadefagah'))

print(re.findall('s.','tyyyrdsyyjksslgssahdyyysyyyyyyydyyyyyyy'))
print(re.findall('s(.)','tyyyrdsyyjksslgssahdyyysyyyyyyydyyyyyyy'))
import pickle
some_data = ["a list", "containing", 5,
"values including another list",
["inner", "list"]]
with open ("pickle_list",'wb') as file:
	pickle.dump(some_data,file)
	print(file)
with open("pickle_list","rb") as file:
	loaded_data=pickle.load(file)
print(loaded_data)
assert loaded_data==some_data
print(id(loaded_data))
print(id(some_data))

from threading import Timer
import datetime
from urllib.request import urlopen
class UpdatedURL:
	def __init__(self, url):
		self.url = url
		self.contents = ''
		self.last_updated = None
		self.update()
	def update(self):
		self.contents = urlopen(self.url).read()
		self.last_updated = datetime.datetime.now()
		self.schedule()
	def schedule(self):
		self.timer = Timer(3600, self.update)
		self.timer.setDaemon(True)
		self.timer.start()
	def __getstate__(self):
		new_state = self.__dict__.copy()
		if 'timer' in new_state:
			del new_state['timer']
		return new_state
	def __setstate__(self, data):
		self.__dict__ = data
		self.schedule()
u= UpdatedURL("http://news.yahoo.com/")
import pickle
serialized = pickle.dumps(u)
print(serialized)
class FileItem:
	def __init__(self,item):
		self.item=item
f=FileItem("/foo/bar")
print(f.item)

print(magic(f))