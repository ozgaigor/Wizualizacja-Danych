#Zdefiniuj funkcję, która zwraca sumę dowolnego ciągu arytmetycznego. 
#Funkcja niech przyjmuje jako parametry: a1 (wartość początkowa), r (wielkość o ile rosną kolejne elementy) 
#i ile_elementów (ile elementów ma sumować). Ponadto funkcja niech przyjmuje wartości domyślne: a1= 1, r=1, ile=10.

import math

def  ciag(a,  r,  i):
    suma = (i / 2) * (2 * a + (i - 1) * r)
    return suma
     
print(ciag(1, 1, 10))