#Zdefiniuj funkcję, która oblicza długość
#przeciwprostokątnej, wykorzystując twierdzenie pitagorasa. Proszę podać wartości domyślne dla funkcji

import math

def funkcja(a, b):
    c=a**2+b**2
    if (a**2+b**2>c):
        print("Błąd")
        return "a^2+b^2>c^2"
    elif (a**2+b**2<c):
        print("Błąd")
        return "a^2+b^2<c^2"
    else:
        print("Przeciwprostokątna wynosi: ")
        return c**(1/2)
    
a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))

print(funkcja(a, b))