
import math

class Point:
	def move(self,x,y):
		self.x=x
		self.y=y
	def reset(self):
		self.move(0,0)
	def calculate_distance(self,other_point):
		return math.sqrt(
			(self.x-other_point.x)**2+
			(self.y-other_point.y)**2)

p1=Point()
p2=Point()
p1.reset()
p2.move(5,2)
print(p2.calculate_distance(p1))
assert (p2.calculate_distance(p1)==
	p1.calculate_distance(p2))
p1.move(3,4)
print(p1.calculate_distance(p2))
print(p1.calculate_distance(p1))
print('__________________________________________')

class CxPoint:
	def __init__(self,x,y):
		self.move(x,y)
	def move(self,x,y):
		self.x=x
		self.y=y
	def reset(self):
		self.move(0,0)
cp=CxPoint(5,9)
print(cp.x,cp.y)