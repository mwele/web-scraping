import unittest
import calc
class TestCalc(unittest.TestCase):
	def test_add(self):
		result =calc.add()
		self.assertEqual(result)
#dir(__str__)		
