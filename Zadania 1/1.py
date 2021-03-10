count=0
tekst = input("Twoj tekst: ")
print("{tekst}".format(tekst=tekst))
for i in tekst:
    if(i.isspace()):
        count=count+1
print("Liczba spacji wynosi: ",count)