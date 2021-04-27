# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy.

import numpy as np

b = np.arange(1,10).reshape(3,3)
print(b)
for a in b.flat:
   print(a)