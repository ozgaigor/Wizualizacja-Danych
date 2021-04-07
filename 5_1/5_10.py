import itertools

kombinacje = list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for i in kombinacje:
    print(i)

print('Kombinacje: ', len(kombinacje))