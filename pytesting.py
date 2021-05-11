

class TestNumbers:
	def test_int_float(self):
		assert 1==1.0
	def test_int_str(self):
		assert 1== "1"
c=TestNumbers()
c
from threading import Thread
class InputReader(Thread):
	def run(self):
		self.line_of_text = input()
print("Enter some text and press enter: ")
thread = InputReader()
thread.start()
count = result = 1
while thread.is_alive():
	result = count * count
	count += 1
print("calculated squares up to {0} * {0} = {1}".format(
count, result))
print("while you typed '{}'".format(thread.line_of_text))
from threading import Thread
import json
from urllib.request import urlopen
import time
CITIES = [
'Edmonton', 'Victoria', 'Winnipeg', 'Fredericton',
"St. John's", 'Halifax', 'Toronto', 'Charlottetown','Quebec City', 'Regina'
]
class TempGetter(Thread):
	def __init__(self, city):
		super().__init__()
		self.city = city
		def run(self):
			url_template = ('http://api.openweathermap.org/data/2.5/''weather?q={},CA&units=metric')
			response = urlopen(url_template.format(self.city))
			data = json.loads(response.read().decode())
			self.temperature = data['main']['temp']
threads = [TempGetter(c) for c in CITIES]
start = time.time()
for thread in threads:
	thread.start()
for thread in threads:
	thread.join()



for thread in threads:
	print("it is °C in {0.city}".format(thread))
print("Got {} temps in {} seconds".format(len(threads), time.time() - start))
from multiprocessing import Process, cpu_count
import time
import os
class MuchCPU(Process):
	def run(self):
		print(os.getpid())
	for i in range(200000000):
		pass
if __name__ == '__main__':
	procs = [MuchCPU() for f in range(cpu_count())]
	t = time.time()
	for p in procs:
		p.start()
	for p in procs:
		p.join()
	print('work took {} seconds'.format(time.time() - t))