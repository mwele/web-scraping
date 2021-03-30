
class _Tigger:
	def __str__(self):
		return "I'm the only one"
	def roar(self):
		return 'Grrr!'
_instance =None
def Tigger():
	global _instance
	if _instance is None:
		_instance=_Tigger()
	return _instance