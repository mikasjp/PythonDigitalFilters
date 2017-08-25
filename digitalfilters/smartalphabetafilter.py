"""Smart Alpha Beta filter module."""

from collections import deque
from digitalfilters.sample import Sample
from digitalfilters.alphabetafilter import AlphaBetaFilter

class SmartAlphaBetaFilter:
    """
    Smart Alpha Beta filter class.
    Same as Alpha Beta filter but calculates Alpha and Beta coefficients itself.
    """

    def __init__(self, NoiseVariance, N):
        self.ab = AlphaBetaFilter()
        self.N = N
        self.NoiseVariance = NoiseVariance
        self.SampleMemory = []

    def CalculateVariance(self, l):
        """Calculates the variance of a list."""
        m = sum(l) / len(l)
        return sum([(xi - m)**2 for xi in l]) / len(l)

    def CalculateCoefficients(self):
        """Calculates Alpha and Beta coefficients."""
        raise NotImplementedError("Not implemented yet.")

    def AddSample(self, sample):
        """
        AddSample method is used for filter state update.
        It returns filtered sample.
        """
        self.SampleMemory.append(sample)
        if len(self.SampleMemory) > self.N:
            self.SampleMemory = deque(self.SampleMemory)
        self.CalculateCoefficients()
        return self.ab.AddSample(sample)
