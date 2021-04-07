def parzyste(lista):
    for i in range(0, len(lista), 2):
        yield lista[i]

parzyste = parzyste([0, 1, 2, 3, 4, 5])
print(next(parzyste), end='/')
print(next(parzyste), end='/')
print(next(parzyste))