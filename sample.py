class Sample:
    def __init__(self, time = 0.0, value = 0.0):
        if not isinstance(time) or not isinstance(value):
            raise TypeError("Time and value must be a numbers")

        if time < 0:
            raise ValueError("Time can't be negative")

        self.t = time
        self.val = value