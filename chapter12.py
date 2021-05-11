import unittest

class CheckNumbers(unittest.TestCase):
	def test_int_float(self):
		self.assertEqual(1,1.0)
	def test_str_float(self):
		self.assertNotEqual(1,"1")
if __name__ == "__main__":
	unittest.main()


from stats import StatsList
import unittest
class TestValidInputs(unittest.TestCase):
	def setUp(self):self.assertEqual(self.stats.mean(), 2.5)
def test_median(self):
	self.assertEqual(self.stats.mean(), 2.5)
def test_median(self):
	self.assertEqual(self.stats.median(), 2.5)
	self.stats.append(4)
	self.assertEqual(self.stats.median(), 3)
def test_mode(self):
	self.assertEqual(self.stats.mode(), [2,3])
	self.stats.remove(2)
	self.assertEqual(self.stats.mode(), [3])
if __name__ == "__main__":
	unittest.main()



def test_int_float():
	assert 1==1.0
