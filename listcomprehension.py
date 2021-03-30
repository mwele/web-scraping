input_strings=['3','4','5','45','897','321']
output_strings=[]
for num in input_strings:
	output_strings.append(int(num))
	print(type(output_strings))

l=[int(num) for num in input_strings if len(num)<2]

print(l)
import sys
filename=sys.argv[1]
print(filename)
with open(filename) as file:
	header=file.readline().strip().split('\t')
	contacts=[
			dict(

				zip(header,line.strip().split('\t'))
				)



	]
for contact in contacts:
	print("email:{email}--{last},{first}".format(contact))