import numpy as np
import matplotlib.pyplot as plt


def C(n):
    fact_n = factorial(n)
    return factorial(2*n)/(factorial(n)*factorial(n+1))

def factorial(n):
    out = 1
    for num in range(n):
        out *= (num + 1)
    return out

plt.plot(range(1000), [C(n) for n in range(1000)])
plt.show()