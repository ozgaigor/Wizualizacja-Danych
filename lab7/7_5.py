# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.

import numpy as np

a = np.array( [90,45,180,270,115,30] ).reshape(2,3)

a = np.sin(a)

print(a)