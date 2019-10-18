import numpy as np
from sequences.base import Base


class A007318(Base):
    def __init__(self, *args, **kwargs):
        super(A007318, self).__init__(*args, **kwargs)

    def compute(self, n=10, *args, **kwargs):
        # self.sequence = np.array([	1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, 1, 5, 10, 10, 5, 1, 1, 6, 15, 20, 15, 6, 1, 1, 7, 21, 35, 35, 21, 7, 1, 1, 8, 28, 56,
        #                            70, 56, 28, 8, 1, 1, 9, 36, 84, 126, 126, 84, 36, 9, 1, 1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1, 1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1])
        seq = []
        print(args)
        for m in range(n):
            for k in range(m+1):
                seq.append(binom(m, k))

        self.sequence = np.array(seq)


facts = [1]


def binom(n, k):
    return fact(n) // (fact(k) * fact(n - k))


def fact(n):
    if len(facts) > n:
        return facts[n]
    x = facts[-1]
    for i in range(len(facts), n + 1):
        print(i)
        x *= i
        facts.append(x)
    return x


# %%
