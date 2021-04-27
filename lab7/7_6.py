# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.

import numpy as np

a = np.array( [90,45,180,270,115,30] ).reshape(2,3)

a = np.cos(a)

print(a)