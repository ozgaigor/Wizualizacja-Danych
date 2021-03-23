#Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci: 
#klucz to nazwa produktu a wartość to ilość. Funkcja ma zliczyć ile jest wszystkich produktów w 
#ogóle i zwracać tę wartość.



p = {'coca-cola': 1, 'baton': 2, 'banany': 5, 'ser': 1}
values = p.values()

total = sum(values)

print(total)