def sq_numbers(nums):
	sqs=[]
	for i in nums:
		sqs.append(i*i)
	return sqs
sqd=sq_numbers(range(0,100))
print(sqd)
def sq_nubers(nums):
	for i in nums:
		yield(i*i)
sqx=sq_nubers([1,1,1,3,5,8,9])
for num in sqx:
	print(num)
print(list(sqx))
import memory_profiler as mem_profile
import random
import time
names=['John ', 'corey','Adam','Steve','Rick','Thomas']
majors=['math','Engineering','Compsci','Arts','Business']

print('Memory(Before):{} Mb'.format(mem_profile.memory_usage()))
def people_list(num_people):
	result=[]
	for i in range(num_people):
		person={

		'id':i,
		'name':random.choice(names),
		'major':random.choice(majors)
		}
		result.append(person)
	return result
def people_generator(num_people):
	for i in range(num_people):
		person={
		'id':i,
		'name':random.choice(names),
		'major':random.choice(majors)
		}
		yield person


t1=time.perf_counter()
people=people_list(1000000)
t2=time.perf_counter()


print("Memory (after) : {}mb".format(mem_profile.memory_usage()) )
print('Took {} seconds'.format(t2-t1))
'''The function time.clock() has been removed,
 after having been deprecated since Python 3.3: use time.perf_counter() or time.process_time()
  instead, depending on your requirements,
   to have well-defined behavior.'''
