class Point:
	def __init__(self,x,y):
		self.move(x,y)
	def move(self,x,y):
		self.x=x
		self.y=y
	def reset(self):
		self.move(0,0)
point=Point(6,7)
print(point)
print(point.x,point.y)