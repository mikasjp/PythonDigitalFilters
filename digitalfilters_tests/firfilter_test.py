"""Unit test for FIRFilter class"""
import unittest
import sys

sys.path.append("..")
import digitalfilters as df

class FIRFilterTest(unittest.TestCase):
    def test(self):
        f = df.FIRFilter([0.25, 0.25, 0.25, 0.25])
        f.AddSample(df.Sample(0.0, 0.0))
        f.AddSample(df.Sample(1.0, 1.0))
        f.AddSample(df.Sample(2.0, 2.0))
        f.AddSample(df.Sample(3.0, 4.0))
        calculatedSample = f.AddSample(df.Sample(4.0, 8.0))
        self.assertEqual(3.75, calculatedSample.val)