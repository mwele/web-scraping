class Notebook:
	'''Represent a collection of notes that can be tagged,
	modified, and searched'''
	def __init__(self):
		'''initialized a notebook with an empty list'''
		self.notes=[]
	def new_note(self, memo, tags=''):
		'''create a new note and add it to the list.'''
		self.notes.append(Note(memo,tags))
	def modify_memo(self, note_id,memo):
		'''Find the note with the given id and change its
		memo to the given value'''
		for note in self.notes:
			if note.id ==note_id:
				note.memo =memo
				break
	def modify_tags(self, note_id,tags):
		'''Find the note with the given id and change its tags to the given value.'''
		for note in self.notes:
			if note.id==note_id:
				note.tags=tags
				break
	def search(self,filter):
		'''Find all notes that match the given filter string'''
		return [note for noe in self.notes if note.match(filter)]
n=Notebook()
n.new_note("Hello word")