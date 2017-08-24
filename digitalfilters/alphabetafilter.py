"""Alpha Beta filter module."""
from digitalfilters.sample import Sample

class AlphaBetaFilter:
    def __init__(self, alpha=1.0, beta=0.0, initialtime=0.0):
        """Alpha Beta filter class."""
        self.alpha = alpha
        self.beta = beta
        self.initialtime = initialtime
        self.lastsample = Sample(initialtime, 0.0)
        self.lastderivative = 0
        self.dt = 0
    
    def Reset(self):
        """Resets filter state"""
        self.lastsample = Sample(self.initialtime, 0.0)

    def AddSample(self, sample):
        """
        AddSample method is used for filter state update.
        It returns filtered sample.
        """
        if not isinstance(sample, Sample):
            raise TypeError("Sample must be instance of Sample class.")
        
        self.dt = sample.t - self.lastsample.t

        if self.dt==0:
            return sample

        estSample = Sample(sample.t, self.lastsample.val)
        error = sample.val - estSample.val
        estSample.val += self.alpha * error
        self.lastderivative += (self.beta * error) / self.dt
        self.lastsample = estSample
        return estSample
