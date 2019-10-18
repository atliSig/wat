import numpy as np
from sequences.base import Base


class A007318(Base):
    def __init__(self, *args, **kwargs):
        super(A007318, self).__init__(*args, **kwargs)

    def compute(self, n=10, *args, **kwargs):
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
