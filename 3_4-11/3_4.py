#Zdefiniuj funkcję, która będzie badać monotoniczność funkcji liniowej:
#y = a x + b
#Funkcja jest rosnąca gdy a>0, malejąca jeżeli a<0, stała gdy a=0 i w zależności od tego będzie wyświetlać odpowiedni komunikat.

import math

def f_liniowa(a, b, x):
    y = a*x+b
    if (a > 0):
        print("Funkcja rosnąca")
        return "a>0"
    elif (a == 0):
        print("Funkcja stała")
        return "a=0"
    else:
        print("Funkcja majeląca")
        return "a<0"

a = int(input("Podaj liczbe a: "))
print("{a}".format(a=a))

b = int(input("Podaj liczbe b: "))
print("{b}".format(b=b))

c = int(input("Podaj liczbe c: "))
print("{c}".format(c=c))

print(f_liniowa(a,b,c))