import unittest
from calculate_pi import calculate_pi

class TestCalculatePi(unittest.TestCase):

    def test_calculate_pi(self):
        """
        Tests the calculate_pi function with a known number of terms.
        """
        self.assertAlmostEqual(calculate_pi(100000), 3.1415826535, places=5)

if __name__ == '__main__':
    unittest.main()
