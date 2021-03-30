from threading import Thread
class Inputreader(Thread):
	def run(self):
		self.line_of_text=input()
print("Enter some text and press enter:")
thread=Inputreader()
thread.run()
count=result=1
while thread.is_alive():
	result=count*count
	count+=1
print("calculated squares up to {0}*{0}".format(count,result))
print("while you typed '{}'".format(thread.line_of_text))