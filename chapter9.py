class CapitalIterable:
	def __init__(self,string):
		self.string=string

	def __iter__(self):
		return CapitalIterator(self.string)
class CapitalIterator(object):
	"""docstring for CapitalIerator"""
	def __init__(self, string):
		#super(CapitalIerator, self).__stringt__()
	#	self.arg = argstring
		self.words=[w.capitalize() for w in string.split()]
		self.index=0

	def __next__(self):
		if self.index == len(self.words):
			raise StopIteration()


		word=self.words[self.index]
		self.index+=1
		return word

	def __iter__(self):
		return self
iterable=CapitalIterable('the quick brown fox jumps over the lazy dog')
iterator =iter(iterable)
print(iterable)
print(iterator)
while True:
	try:
		print(next(iterator))
	except StopIteration:
		break
for i in iterable:
	print(i)
input_strings=['1','4','6','8','3000']
output_int=[]
for num in input_strings:
	output_int.append(int(num))
print(output_int)

output_int=[int(num) for num in input_strings]
print(output_int)
output_ints=[int(n) for n in input_strings if len(n)> 0]
print(output_ints)

import sys
print(str(sys.argv))
 