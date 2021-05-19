# Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji, 
# tak aby osiągnąć efekt podobny do tego na poniższym zrzucie ekranu.

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 30, 0.1)
s = np.sin(x)
s1 = np.sin(-x)
plt.plot(x, s+2, label='sin(x)')
plt.plot(x, s1, label='sin(x)')
plt.axis([0,20,-1,3])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()


plt.show()

