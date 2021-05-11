import datetime
# store the next available id for all new notes
last_id=0

class Note:
	'''Represent a note in the notebook. Match against a
	string in searches and store tags for each note.'''
	def __init__(self,memo,tags=''):
		'''initialize a note with memo and optional
			space-separated tags. Automatically set the note's
			creation date and a unique id.'''
		self.memo=memo
		self.tags=tags
		self.creation_date=datetime.date.today()
		global last_id
		last_id+=1
		self.id=last_id
	def match(self,filter):
		'''Determine if this note matches the filter
text. Return True if it matches, False otherwise.
Search is case sensitive and matches both text and
tags.'''
		return filter in self.memo or filter in self.tags


class  Notebook:
	"""docstring for  Notebook __init__(self, arg):
		super( Notebook__init__()
		self.arg = arg
		"""
	def __init__(self):
		self.notes=[]
	def new_note(self,memo,tags=''):
		self.notes.append(Note(memo,tags))
	def modify_memo(self,note_id,memo):
		for note in self.notes:
			if note.id==note_id:
				note.memo=memo
				break
	def search(self,filter):
		return [note for note in self.notes if 
				note.match(filter)]
