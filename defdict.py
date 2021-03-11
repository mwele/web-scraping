name="pythonists"
d={}
for r in name:
	if r not in d:
		d[r] =1
	else:
		d[r]+=1
print(d)
from collections import defaultdict
d=defaultdict(int)
for r in name:
	d[r]+=1
print(d)