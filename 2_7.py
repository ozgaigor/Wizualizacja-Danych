# Napisz pętle, która pobiera liczby od użytkownika i wyświetla ich kwadraty na ekranie. Liczby pobierane są w postaci oddzielonej spacjami.

lista = []

liczba = input("Podaj liczby: ")
liczba = liczba.split()

a = len(liczba)
i = a
for x in range(0, a):
    print(int(liczba[x])**2, end=" ") 