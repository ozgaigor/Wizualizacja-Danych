import random

macierz = [[random.randint(1,50) for x in range(4)] for n in range(4)]
# print(macierz)
for wiersz in macierz:
    print(wiersz)

przekatna = [macierz[x][x] for x in range(4)]
print(przekatna)