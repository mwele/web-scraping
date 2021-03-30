def linear_search(list,target):
	'''returns the index position of the target if fouund 
	else returns None'''
	for i in range(0,len(list)):
		if list[i] == target:
			return i
	return None
	
def verify(index):
	if index is not None:
		print("Target found at index:",index)
	else:
		print("Target not found in list")
numbers=[1,3,5,5,7,8,9,5,4]
result=linear_search(numbers,1)