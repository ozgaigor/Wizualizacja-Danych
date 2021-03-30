plik = open("4_1+/4_1.py","r+")


lista = []
for x in range(0,50,4):
    lista += [x]

plik.writelines(str(lista))
plik.close()