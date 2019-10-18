import numpy as np
from matplotlib import pyplot as plt

import abc


class Base(abc.ABC):
    def __init__(self, id=None, *args, **kwargs):
        self.sequence = np.array([])
        self.compute(*args, **kwargs)
        self.id = id

    def __call__(n, self, *args, **kwargs):
        self.compute(n)

    def __str__(self):
        if self.id:
            return str(self.id)
        elif self.sequence.shape[0] != 0:
            stop = min(self.sequence.shape[0], 10)
            return "Sequence for n < {} : {}".format(stop, self.sequence[:stop])

    def __repr__(self):
        return self.sequence

    @abc.abstractmethod
    def compute(self, n, *args, **kwargs):
        return self.sequence

    def show(self, *args, method='plot', **kwargs):
        '''
        Create a MatplotLib
        '''
        getattr(plt,method)(range(len(self.sequence)), self.sequence, **kwargs)
        plt.show()
