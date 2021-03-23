#Napisz funkcję, która będzie sprawdzać czy dwie proste są równoległe czy prostopadłe: Proste dane równaniami:
#y=a1x+b1, y=a2x+b2, są równolegle gdy a1=a2 prostopadłe gdy a1a2=-1

import math

def funkcja(a1, a2, b1, b2, x):
    if (a1 == a2):
        print("Równoległe")
        return "a1=a2"
    elif (a1 * a2==-1):
        print("Prostopadłe")
        return "a1*a2=-1"
    else:
        print("Ani równoległe ani prostopadłe")
        return "Brak odpowiedzi"
    
a1 = int(input("Podaj liczbe a1: "))
print("{a1}".format(a1=a1))

b1 = int(input("Podaj liczbe b1: "))
print("{b1}".format(b1=b1))

a2 = int(input("Podaj liczbe a2: "))
print("{a2}".format(a2=a2))

b2 = int(input("Podaj liczbe b2: "))
print("{b2}".format(b2=b2))

x = int(input("Podaj liczbe x: "))
print("{x}".format(x=x))

print(funkcja(a1, a2, b1, b2, x))