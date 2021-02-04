import unittest
import Q1cube

class TestCube (unittest.TestCase):
	def test_volume1(self):
		self.assertEqual(Q1cube.cubeVolume(2,3,4), 24)

	def test_volume2(self):
		self.assertEqual(Q1cube.cubeVolume("2","3","4"), 24)

	def test_volume3(self):
		self.assertEqual(Q1cube.cubeVolume(2.5,3,2), 15)

if __name__ == '__main__':
    unittest.main()