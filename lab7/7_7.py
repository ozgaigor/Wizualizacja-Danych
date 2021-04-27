# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.

import numpy as np
print("-----------SINUS-----------")
a = np.array( [90, 45, 180, 270, 115, 30] ).reshape(2,3)

a = np.sin(a)

print(a)
print("-----------COSINUS-----------")
b = np.array( [60, 30, 150, 220, 110, 80] ).reshape(2,3)

b = np.cos(b)

print(b)
print("-----------SUMA-----------")
print(a+b)