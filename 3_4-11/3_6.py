#Zdefiniuj funkcję, która na podstawie równania okręgu w postaci kanonicznej zwróci długość promienia. Funkcja ma przyjmować 
#argumenty domyślne: Równanie okręgu dane jest wzorem:
#(x-a)2+(y-b)2=r2 gdzie (a,b) to środek okręgu a r to promień okręgu.

import math

def funkcja(a, b, x, y):
        r = (x-a) ** 2 + (y-b) ** 2
        
        print("Promień wynosi: ")
        return r**(1/2)
    
a = int(input("Podaj liczbe a: "))
x = int(input("Podaj liczbe x: "))
b = int(input("Podaj liczbe b: "))
y = int(input("Podaj liczbe y: "))


print(funkcja(a, b, x, y))