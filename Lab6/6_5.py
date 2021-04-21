import numpy as np

def macierz(n):
    return np.diag(range(n, 0, -1))

print(macierz(3))
