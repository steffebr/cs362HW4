import unittest
import Q2avg

class TestCube (unittest.TestCase):
	def test_avg1(self):
		list = [1, 3, 4, 8]
		self.assertEqual(Q2avg.avg(list), 4)

	def test_avg2(self):
		list = []
		self.assertEqual(Q2avg.avg(list), 0)

	def test_avg3(self):
		list = [3]
		self.assertEqual(Q2avg.avg(list), 3)

if __name__ == '__main__':
    unittest.main()