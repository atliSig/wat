import matplotlib.pyplot as plt
import numpy as np

from math import gcd

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

def A002618(n):
    return n*phi(n)

plt.scatter(range(10_000), [A002618(n) for n in range(10_000)], s=1)
plt.show()

