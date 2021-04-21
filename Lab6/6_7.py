import numpy as np

def macierz(n):




    a = np.diag([2 for x in range(n)])
    for i in range(1, n):
        wektor = [2+(2*i) for x in range(n-i)]
        a += np.diag(wektor, i)
        a += np.diag(wektor, -i)
    return a

print(macierz(5))