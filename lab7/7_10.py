# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?

import numpy as np

print("------9x9------")
b = np.arange(1,82).reshape(9,9)
print(b)
print(b.shape)
print("------27x3------")
c = b.reshape((27,3))
print(c)
print(c.shape)
print("------3x27------")
c1 = b.reshape((3,27))
print(c1)
print(c1.shape)
print("------TRANSPOZYCJA------")
d = c.T
print(d)
print(d.shape)
print("------ITEROWANIE WZDŁÓŻ PIERWSZEJ OSI------")
for a in b:
   print(a)
print("------SPŁASZCZANIE------")
for a in b.flat:
    print(a)


# Nasze możliwości to:
#         9x9
#         3x27
#         27x3
#         Transpozycja macierzy
#         Spłaszczanie
#         Iterowanie
# Dlaczego?
#         Kształt macierzy możemy zmieniać wyłączenie względem dzielników rozmiaru macierzy, przykładowo macierz 9x9 ma dzielniki:
#                     1       3       9       27      81
#         Poza tym możemy wykonać operację transpozycji,spłaszczania i iterowania