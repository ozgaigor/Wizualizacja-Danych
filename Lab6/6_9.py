import numpy as np

fibb = np.empty((3, 3), dtype='int')
a = 0
b = 1
for n in range(0, 3, 1):
    for m in range(0, 3, 1):
        fibb[n, m] = b
        b += a
        a = b-a

print(fibb)