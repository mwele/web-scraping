'''a=int(input("Enter a"))
b=int(input("Enter b"))
print(a+b)'''
def oddNum(l,r):
	for a in range(l,r):
		if a%2 !=0:
			print(a)
		else:
			continue
#if __name__ == '__main__':
	#main()
oddNum(2,1000)
def numend(l,r):
	for a in range(l,r):
		if a%2 !=0:
			print(a,end="")
		else:
			continue
numend(2,1000)