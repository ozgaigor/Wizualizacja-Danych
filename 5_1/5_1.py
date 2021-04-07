class Material:
    def __init__(self, rodzaj, długość, szerokość):
        self.rodzaj = rodzaj
        self.długość = długość
        self.szerokość = szerokość

    def wyświetl_nazwę(self):
        print("Nazwa produktu: "+str(self.rodzaj))
        print("Długość: "+str(self.długość))
        print("Szerokość: "+str(self.szerokość))
#------------------------------------------------------------------
class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyświetl_dane(self):
        print("Rozmiar: "+str(self.rozmiar))
        print("Kolor: "+str(self.kolor))
        print("Dla kogo: "+str(self.dla_kogo))
#------------------------------------------------------------------
class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra

    def wyświetl_dane(self):
        print("Rodzaj swetra: "+str(self.rodzaj_swetra))
#------------------------------------------------------------------
obiekt = Material("Bawełna","110","70")
obiekt.wyświetl_nazwę()
obiekt1 = Ubrania("XL","Czarny","Męski")
obiekt1.wyświetl_dane()
obiekt2 = Sweter("Rozpinany")
obiekt2.wyświetl_dane()
#------------------------------------------------------------------
print("\n")
#------------------------------------------------------------------
obiekt = Material("Len","80","40")
obiekt.wyświetl_nazwę()
obiekt1 = Ubrania("S","Biały","Damski")
obiekt1.wyświetl_dane()
obiekt2 = Sweter("Golf")
obiekt2.wyświetl_dane()
#------------------------------------------------------------------