# Napisz skrypt, który odczytuje liczby od użytkownika i umieszcza je na liście. Wykorzystaj pętle while.

lista=[]
a=0
while(a!=3):
    liczba=input("podaj liczbe: ")
    lista.append(liczba)
    a+=1

print (lista)