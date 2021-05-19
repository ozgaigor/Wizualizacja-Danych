# Zmodyfikuj zadanie 1...

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 20, 1)

plt.title('Wykres funkcji f(x) = 1/x dla x [1, 20]')
plt.plot(1/x, 'g:>', label='f(x) = 1/x')
plt.axis([0,20,0,1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()


plt.show()