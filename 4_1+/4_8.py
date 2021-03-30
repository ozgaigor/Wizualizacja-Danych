class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
#-------------------------------------------------------------------------------------------------------
    def __del__(self):
        print("\n")
        print("Zakupy zostały zakończone, wracaj do domu zanim sklep ulegnie autodestrukckji")
#-------------------------------------------------------------------------------------------------------
    def wyświetl_produkt(self):
        print("Nazwa produktu: "+str(self.nazwa_produktu))
        print("Ilość: "+str(self.ilosc))
        print("Jednostka_miary: "+str(self.jednostka_miary))
        print("Cena produktu: "+str(self.cena_jed))

    def ile_produktu(self):
        return str(self.ilosc) +" "+ str(self.jednostka_miary)

    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed
#-------------------------------------------------------------------------------------------------------
obiekt = NaZakupy("Chleb", 1, "szt", 3.3)
obiekt.wyświetl_produkt()

print("Produkt "+str(obiekt.nazwa_produktu), "w ilości " +
      str(obiekt.ile_produktu()), "Koszt wynosi "+str(obiekt.ile_kosztuje()), "złoty.")


