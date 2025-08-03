import unittest
from hello import calculate_average, greet

class TestHelloFunctions(unittest.TestCase):
    def test_calculate_average_normal(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_average([10, 20, 30]), 20)

    def test_calculate_average_empty(self):
        self.assertEqual(calculate_average([]), 0)

    def test_calculate_average_single(self):
        self.assertEqual(calculate_average([42]), 42)

    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet(""), "Hello, !")

if __name__ == "__main__":
    unittest.main()