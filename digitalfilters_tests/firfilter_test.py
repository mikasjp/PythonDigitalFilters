"""Unit test for FIRFilter class"""
import unittest
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  
from digitalfilters import Sample
from digitalfilters import FIRFilter

class FIRFilterTest(unittest.TestCase):
    def test(self):
        f = FIRFilter([0.25, 0.25, 0.25, 0.25])
        f.AddSample(Sample(0.0, 0.0))
        f.AddSample(Sample(1.0, 1.0))
        f.AddSample(Sample(2.0, 2.0))
        f.AddSample(Sample(3.0, 4.0))
        f.AddSample(Sample(3.0, 8.0))
        calculatedSample = f.AddSample(Sample(4.0, 2.0))
        print(calculatedSample.val)
        self.assertEqual(4.0, calculatedSample.val)


if __name__ == "__main__":
    unittest.main()