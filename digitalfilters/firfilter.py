"""FIR filter module."""
from digitalfilters.sample import Sample

class FIRFilter:
    """FIR filter class."""
    def __init__(self, coefficients):
        """The sum of the filter coefficients must be equal 1"""
        
        if not isinstance(coefficients, list):
            raise TypeError("The coefficients variable must be a list of numbers")

        if sum(coefficients) != 1:
            raise ValueError("The sum of coefficients must be equal to 1")

        self.coef = coefficients
        self.samples = [0.0] * len(self.coef)

    def AddSample(self, sample):
        """
        AddSample method is used for filter state update.
        It returns filtered sample.
        """
        if not isinstance(sample, Sample):
            raise TypeError("Sample must be instance of Sample")

        self.samples.append(sample.val)

        self.samples.reverse()
        self.samples.pop()
        self.samples.reverse()

        filteredValue = sum([a*b for a, b in zip(self.coef, self.samples)])

        return Sample(sample.t, filteredValue)