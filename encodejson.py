import json

class User:
	def __init__(self,name,age):
		self.name=name
		self.age=age

user=User('amx',45)

def encode(o):
	if isinstance (o, User):
	 	return{'name':o.name,'age':o.age,o.__class__.__name__:True}
	else:
		raise TypeError('Object of type user is not JSON serializable')
userJSON=json.dumps(user,default=encode,indent=7,sort_keys=True)
print(userJSON)