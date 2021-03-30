nums=[1,3,4,4]
#i_nums=nums.__iter__()
i_nums=iter(nums)
print(next(i_nums))
print(i_nums)
print(dir(i_nums))
#for num in nums:
#	print(num)

print(dir(nums))
#iterators has a __next__ method in its dir()
# iterator is anumber with a state so that it remembers where it is next
while True:
	try:
		item=next(i_nums)
		print(item)
	except StopIteration:
		break
class MyRange:
	def __init__(self,start,end):
		self.value=start
		self.end=end
	def __iter__(self):
		return self
	def __next__(self):
		if self.value>=self.end:
			raise StopIteration
		current =self.value
		self.value +=1
		return current
numxx =MyRange(1,10)
#
print(next(numxx))
print(next(numxx))
print(next(numxx))
print(next(numxx))
print(next(numxx))
print(next(numxx))
print(next(numxx))
print(next(numxx))
print(next(numxx))
#
# generators are iterators as well but with the __iter__ and __next__ implemented automatically
def my_Range(start,end):
	current=start
	while current < end:
		yield current
		current +=1
numc=my_Range(1,10)
print(next(numc))
print(next(numc))
print(next(numc))
print(next(numc))

#This class we've created is iterable since it has the __iter__ and __next__ 
