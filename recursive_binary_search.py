def recursive_binary_search(list,target):
	if len(list) == 0:
		return False
	else:
		midpoint=(len(list))//2
		if list[midpoint] == target:
			return True
		else:
			if list[midpoint] < target:
				return recursive_binary_search(list[midpoint+1:],target)
			else:
				return recursive_binary_search(list[:midpoint],target)
'''def verify(index):
	if index is not None:
		print("Target found at index:",index)
	else:
		print("Target not found in list")
numbers=[1,3,5,5,7,8,9,5,4]
result=linear_search(numbers,1)'''
def verify(result):
	print("target found:" ,target)
numbers=[1,2,3,4,5,6,7,8,9]
result=recursive_binary_search(numbers,6)