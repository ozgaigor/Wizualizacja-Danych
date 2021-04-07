class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

#------------------------------------------------------------------
lista = Wspak(['I', 't', 'e', 'r', 'a', 't', 'o', "r"])
#------------------------------------------------------------------
print(end=' ')
print(next(lista), end='/')
print(next(lista), end='/')
print(next(lista), end='/')
print(next(lista), end='/')
print(next(lista), end='/')
print(next(lista), end='/')
print(next(lista), end='/')
print(next(lista))
#------------------------------------------------------------------
print('')
#------------------------------------------------------------------
osoba = Wspak("Pracownik")
#------------------------------------------------------------------
print(end=' ')
print(next(osoba), end='/')
print(next(osoba), end='/')
print(next(osoba), end='/')
print(next(osoba), end='/')
print(next(osoba), end='/')
print(next(osoba), end='/')
print(next(osoba), end='/')
print(next(osoba), end='/')
print(next(osoba))
#------------------------------------------------------------------
