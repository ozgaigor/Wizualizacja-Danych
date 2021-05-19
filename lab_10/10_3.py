# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. 
# Dodaj etykiety i legendę do wykresu.

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 30, 0.1)
s = np.sin(x)
c = np.cos(x)
plt.plot(x, s, label='sin(x)')
plt.plot(x, c, label='cos(x)')
plt.axis([0,20,-1,3])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()


plt.show()