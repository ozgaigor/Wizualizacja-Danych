# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

import numpy as np

a = np.array( [1,11,23,82,12,24,64,4,6] ).reshape(3,3)
b = np.array( [1,11,23,82,12,24,64,4,6,10,11,25,56,53,6,34] ).reshape(4,4)

print("---------------------------------------------")
print("MACIERZ A")
print(a)
print("")
# minimum każdej z kolumn
print("Minimum kolumn:",a.min(axis=0))
# minimum każdego rzędu
print("Minimum rzedu:",a.min(axis=1))

print("---------------------------------------------")
print("MACIERZ B")
print(b)
print("")
# minimum każdej z kolumn
print("Minimum kolumn:",b.min(axis=0))
# minimum każdego rzędu
print("Minimum rzedu:",b.min(axis=1))