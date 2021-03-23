#Wykorzystując poprzedni przykład zdefiniuj funkcję, która będzie liczyć iloczyn elementów ciągu.

import math

def  ciag(a,  q,  i):
    iloczyn = a*((1-q**i)/(1-q))
    return iloczyn
     
print(ciag(1, 5, 10))