import json
person ={"name":"xyxs","age":10,"mail":"xyxs@gmail.com"}

personjson=json.dumps(person,indent=6,sort_keys=True)
print(personjson)
with open('personjson','w') as file:
	json.dump(person,file,indent=4)



#person =json.load(personjson) #json data to python
print(person)