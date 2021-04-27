# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

import numpy as np

b = np.arange(1,10).reshape(3,3)
print(b)
for a in b:
   print(a)