"""Unit test for FIRFilter class"""
import unittest
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  
from digitalfilters import Sample
from digitalfilters import AlphaBetaFilter

class AlphaBetaFilterTest(unittest.TestCase):
    def test(self):
        f = AlphaBetaFilter(1.5, 0.5)
        self.assertEqual(0.0, 0.0)


if __name__ == "__main__":
    unittest.main()