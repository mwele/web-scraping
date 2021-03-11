import datetime
last_id=0

class Note:
	'''Represent a note in the notebook. Match against a 
	string in searches and store tags for each note.'''

	def __init__(self,memo,tags=''):
		'''iniialize a note with memo and optimal 
		space-separated tags.Automatically set the note's creation da
		date and a unique ID'''

		self.memo=memo
		sel.tags=tags
		self.creation_date=datetime.date.today()
		global last_id
		last_id+=1
		self.id=last_id
	def match(self,filter):
		'''Determine if this note matches the filter 
		text. Return True if it matches, false otherwise.
		Search is case sensitive and matches both text andd tags'''
		return filter in self.memo or filter in self.tags
	
p=Note()
print(p.match("Hello here"))