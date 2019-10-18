import numpy as np
from matplotlib import pyplot as plt


class Base:
    def __init__(self, id=None, *args, **kwargs):
        self.sequence = np.array([])
        self.compute(*args, **kwargs)
        self.id = id

    def __call__(self, *args, **kwargs):
        self.plot()

    def __str__(self):
        if self.id:
            return str(self.id)
        else:
            ret
    def __repr__(self):
        return self.sequence[]

    def compute(self, *args, **kwargs) -> np.array:
        raise NotImplementedError('foo')

    def plot(self, *args, **kwargs):
        plt.plot(self.sequence)
        plt.show()
