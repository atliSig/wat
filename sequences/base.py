import numpy as np
from matplotlib import pyplot as plt


class Base:
    def __init__(self, *args, **kwargs):
        self.sequence = np.array([])
        self.compute(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        self.plot()

    def compute(self, *args, **kwargs):
        raise NotImplementedError('foo')

    def plot(self, *args, **kwargs):
        plt.plot(self.sequence)
        plt.show()
