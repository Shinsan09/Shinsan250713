import unittest
from calculate import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_average_normal(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_average([10, 20, 30, 40, 50]), 30)
        self.assertAlmostEqual(calculate_average([1.5, 2.5, 3.5, 4.5, 5.5]), 3.5)

    def test_average_empty(self):
        self.assertEqual(calculate_average([]), 0)

    def test_average_single(self):
        self.assertEqual(calculate_average([42]), 42)

    def test_average_negative(self):
        self.assertEqual(calculate_average([-1, -2, -3, -4, -5]), -3)

if __name__ == '__main__':
    unittest.main()
