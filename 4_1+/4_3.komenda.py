with open('4_1+/4_3.py', 'r+') as plik:
    plik.write('Witaj')
    wiersze = plik.readlines()
    plik.close()

print(wiersze)