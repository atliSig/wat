import matplotlib.pyplot as plt
import numpy as np

def a003188(n):
    return int(bin(n^(n/2))[2:], 2)

plt.plot(range(200), [a003188(n) for n in range(200)])
plt.show()