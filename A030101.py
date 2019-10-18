import matplotlib.pyplot as plt
import numpy as np

def A030101(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return A030101(n/2)
    else:
        return A030101((n-1)/2) + 2**(np.floor(np.log2(n))+1)

plt.scatter(range(2000), [A030101(n) for n in range(2000)], s=1)
plt.show()