class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


Fabian = Pracownik("Fabian", "Bajka", 9000)
Kazimierz = Menadzer("Kazimierz", "Mikulski", 12000)
#------------------------------------------------------------------
print('')
#------------------------------------------------------------------
print(Fabian.przedstaw_sie())
print(Kazimierz.przedstaw_sie())
#------------------------------------------------------------------
print('')
#------------------------------------------------------------------
print('isinstance(Fabian, Osoba):', isinstance(Fabian, Osoba))
print('isinstance(Fabian, Pracownik):', isinstance(Fabian, Pracownik))
print('isinstance(Fabian, Menadzer):', isinstance(Fabian, Menadzer))
#------------------------------------------------------------------
print('')
#------------------------------------------------------------------
print('isinstance(Kazimierz, Osoba):', isinstance(Kazimierz, Osoba))
print('isinstance(Kazimierz, Pracownik):', isinstance(Kazimierz, Pracownik))
print('isinstance(Kazimierz, Menadzer):', isinstance(Kazimierz, Menadzer))
#------------------------------------------------------------------
print('')
#------------------------------------------------------------------
print('issubclass(Pracownik, Osoba):', issubclass(Pracownik, Osoba))
print('issubclass(Menadzer, Osoba):', issubclass(Menadzer, Osoba))
print('issubclass(Osoba, Pracownik):', issubclass(Osoba, Pracownik))
print('issubclass(Osoba, Menadzer):', issubclass(Osoba, Menadzer))
print('issubclass(Menadzer, Pracownik):', issubclass(Menadzer, Pracownik))
print('issubclass(Pracownik, Menadzer):', issubclass(Pracownik, Menadzer))
#------------------------------------------------------------------