#Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
#wyświetl_dane – drukuje elementy na ekran
#pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
#pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
#policz_sume – liczy sume elementow
#policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
#Stwórz instancję klasy i sprawdź działanie wszystkich metod.

#-------------------------------------------------------------------------------------------------------
class ciagi_arytmetyczne:
    def __init__(self):
        self.elementy = {}
#-------------------------------------------------------------------------------------------------------
    def wyswietl_dane(self):
        for i in sorted(self.elementy.keys()):
            print('a('+str(i)+') = '+str(self.elementy[i]))
        if len(self.elementy) == 0:
            print("")
#-------------------------------------------------------------------------------------------------------
    def pobierz_elementy(self, numer, wartosc):
        self.elementy[numer] = wartosc
#-------------------------------------------------------------------------------------------------------
    def pobierz_parametry(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
#-------------------------------------------------------------------------------------------------------
    def policz_sume(self):
        suma = 0
        for i in self.elementy:
            suma = suma + self.elementy[i]
        return suma
#-------------------------------------------------------------------------------------------------------
    def policz_elementy(self):
        try:
            for i in range(1, self.n+1, 1):
                self.elementy[i] = self.a1+(i-1)*self.r
        except AttributeError:
            print("Brak pierwszej wartosci i roznicy")
#-------------------------------------------------------------------------------------------------------
obiekt = ciagi_arytmetyczne()
obiekt.wyswietl_dane()
obiekt.pobierz_elementy(2, 1)
obiekt.pobierz_elementy(3, 2)
obiekt.pobierz_elementy(4, 3)
obiekt.wyswietl_dane()
print("CIAG ARYTMETYCZNY")
obiekt.pobierz_parametry(2, 2, 20)
obiekt.policz_elementy()
obiekt.wyswietl_dane()
print("Suma wszystkich wyrazow ciagu wynosi ", obiekt.policz_sume())
#-------------------------------------------------------------------------------------------------------