import unittest
import cap

class capital(unittest.TestCase):

	def test1(self):
		name="python"
		result=cap.capfunc(name)
		self.assertEqual(result,'Python')
	def test2(self):
		name="python book"
		result=cap.capfunc(name)
		self.assertEqual(result,'Python book')

if __name__ == '__main__':
	unittest.main()

