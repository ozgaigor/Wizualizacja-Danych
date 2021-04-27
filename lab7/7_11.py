# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. 
# Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. 
# Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?

import numpy as np

a = np.arange(1,13)
print(a)
print("-------------")
b = a.reshape((3,4))
print(b)
print("-------------")
c = a.reshape((4,3))
print(c)
print("-------------")
d = a.reshape((2,6))
print(d)
print("------SPŁASZCZANIE-------")

for a in b.flat:
    print(a)
print("-------------")
for a in c.flat:
    print(a)
print("-------------")
for a in d.flat:
    print(a)