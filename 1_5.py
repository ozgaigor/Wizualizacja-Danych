a = int(input("Podaj liczbe a: "))
print("{a}".format(a=a))

b = int(input("Podaj liczbe b: "))
print("{b}".format(b=b))

c = int(input("Podaj liczbe c: "))
print("{c}".format(c=c))

if a>0 and a<=10 and a > b and b > c:
    print("Oba warunki sa spelnione")
else:
    print("Warunki nie zostaly spelnione")