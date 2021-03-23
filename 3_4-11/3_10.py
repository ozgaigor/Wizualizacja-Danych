#Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci: 
#klucz to nazwa produktu a wartość to ilość. Funkcja ma zliczyć ile jest wszystkich produktów w 
#ogóle i zwracać tę wartość.



def ile(**suma):
    return sum([int(value) for value in suma.values()])

print(ile(picie=2,baton=3,banan=5))