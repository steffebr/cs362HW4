import unittest
import Q3name

class TestCube (unittest.TestCase):
	def test_avg1(self):
		self.assertEqual(Q3name.name("Braylon", "Steffen"), "Braylon Steffen")

	def test_avg2(self):
		self.assertEqual(Q3name.name("", ""), " ")

	def test_avg3(self):
		self.assertEqual(Q3name.name(4, 3), 7)

if __name__ == '__main__':
    unittest.main()