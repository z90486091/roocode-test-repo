import unittest
from math_utils import calculate_pi, create_markov_chain

class TestMathUtils(unittest.TestCase):

    def test_calculate_pi(self):
        """
        Tests the calculate_pi function with a known number of terms.
        """
        self.assertAlmostEqual(calculate_pi(100000), 3.1415826535, places=5)

    def test_create_markov_chain(self):
        """
        Tests the create_markov_chain function with a simple text.
        """
        text = "a cat sat on a mat"
        chain = create_markov_chain(text)
        expected_chain = {
            'a': ['cat', 'mat'],
            'cat': ['sat'],
            'sat': ['on'],
            'on': ['a']
        }
        self.assertEqual(chain, expected_chain)

if __name__ == '__main__':
    unittest.main()
