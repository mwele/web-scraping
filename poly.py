''' In computer science, it describes the concept that objects of different types can be accessed through the same interface.
 Each type can provide its own, independent implementation of this interface.'''
class AudioFile:
	def __init__(self, filename):
		if not filename.endswith(self.ext):
			raise Exception("Invalid file format")
		self.filename = filename
class MP3File(AudioFile):
	ext = "mp3"
	def play(self):
		print("playing {} as mp3".format(self.filename))
class WavFile(AudioFile):
	ext = "wav"
	def play(self):
		print("playing {} as wav".format(self.filename))
class OggFile(AudioFile):
	ext = "ogg"
	def play(self):
		print("playing {} as ogg".format(self.filename))
		
ogg = OggFile("myfile.ogg")
print(ogg.play())