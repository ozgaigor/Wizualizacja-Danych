#Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
#nazwa_produktu, ilosc, jednostka_miary, cena_jed oraz metody:
#konstruktor – który nadaje wartości
#wyświetl_produkt() – drukuje informacje o produkcie na ekranie
#ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
#ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas 
#funkcja powinna zwrócić wartość 3*2

#-------------------------------------------------------------------------------------------------------
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
#-------------------------------------------------------------------------------------------------------
    def wyświetl_produkt(self):
        print("Nazwa produktu: "+str(self.nazwa_produktu))
        print("Ilość: "+str(self.ilosc))
        print("Jednostka_miary: "+str(self.jednostka_miary))
        print("Cena produktu: "+str(self.cena_jed))
#-------------------------------------------------------------------------------------------------------
    def ile_produktu(self):
        return str(self.ilosc) +" "+ str(self.jednostka_miary)
#-------------------------------------------------------------------------------------------------------
    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed
#-------------------------------------------------------------------------------------------------------
obiekt = NaZakupy("Chleb", 1, "szt", 3.3)
obiekt.wyświetl_produkt()
#-------------------------------------------------------------------------------------------------------
print("Produkt "+str(obiekt.nazwa_produktu), "w ilości " +
      str(obiekt.ile_produktu()), "Koszt wynosi "+str(obiekt.ile_kosztuje()), "złoty.")
print("\n")
#-------------------------------------------------------------------------------------------------------
obiekt = NaZakupy("Baton proteinowy", 2, "szt", 3.99)
obiekt.wyświetl_produkt()
print("Produkt "+str(obiekt.nazwa_produktu), "w ilości " +
      str(obiekt.ile_produktu()), "Koszt wynosi "+str(obiekt.ile_kosztuje()), "złoty.")
#-------------------------------------------------------------------------------------------------------