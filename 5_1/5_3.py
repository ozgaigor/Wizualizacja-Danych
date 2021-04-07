class Ksztalty:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __ge__(self, dod):
        if(self.x >= dod.x):
            return True
        else:
            return False

    def __gt__(self, dod):
        if(self.x > dod.x):
            return True
        else:
            return False

    def __le__(self, dod):
        if(self.x <= dod.x):
            return True
        else:
            return False

    def __lt__(self, dod):
        if(self.x < dod.x):
            return True
        else:
            return False


class KwadratowaLiteraL(Kwadrat):

    def obwod(self):
        return 8 * self.x

    def pole(self):
        return 3 * self.x * self.y
#------------------------------------------------------------------
kwadrat1 = Kwadrat(5)
kwadrat2 = Kwadrat(8)
kwadrat3 = Kwadrat(2)
#------------------------------------------------------------------
print('')
#------------------------------------------------------------------
print('Wymiar kwadratu pierwszego: '+str(kwadrat1.x))
print('Wymiar kwadratu drugiego: '+str(kwadrat2.x))
print('Wymiar kwadratu trzeciego: '+str(kwadrat3.x))
#------------------------------------------------------------------
print('__ge__:')
print('Kwadrat1 >= Kwadrat2 : ', kwadrat1 >= kwadrat2)
print('Kwadrat2 >= Kwadrat1 : ', kwadrat2 >= kwadrat1)
print('Kwadrat1 >= Kwadrat3 : ', kwadrat1 >= kwadrat3)
print('Kwadrat3 >= Kwadrat1 : ', kwadrat3 >= kwadrat1)
print('Kwadrat2 >= Kwadrat3 : ', kwadrat2 >= kwadrat3)
print('Kwadrat3 >= Kwadrat2 : ', kwadrat3 >= kwadrat2)
#------------------------------------------------------------------
print('')
#------------------------------------------------------------------
print('__gt__:')
print('Kwadrat1 > Kwadrat2 : ', kwadrat1 > kwadrat2)
print('Kwadrat2 > Kwadrat1 : ', kwadrat2 > kwadrat1)
print('Kwadrat1 > Kwadrat3 : ', kwadrat1 > kwadrat3)
print('Kwadrat3 > Kwadrat1 : ', kwadrat3 > kwadrat1)
print('Kwadrat2 > Kwadrat3 : ', kwadrat2 > kwadrat3)
print('Kwadrat3 > Kwadrat2 : ', kwadrat3 > kwadrat2)
#------------------------------------------------------------------
print('')
#------------------------------------------------------------------
print('__le__:')
print('Kwadrat1 <= Kwadrat2 : ', kwadrat1 <= kwadrat2)
print('Kwadrat2 <= Kwadrat1 : ', kwadrat2 <= kwadrat1)
print('Kwadrat1 <= Kwadrat3 : ', kwadrat1 <= kwadrat3)
print('Kwadrat3 <= Kwadrat1 : ', kwadrat3 <= kwadrat1)
print('Kwadrat2 <= Kwadrat3 : ', kwadrat2 <= kwadrat3)
print('Kwadrat3 <= Kwadrat2 : ', kwadrat3 <= kwadrat2)
#------------------------------------------------------------------
print('')
#------------------------------------------------------------------
print('__lt__:')
print('Kwadrat1 <= Kwadrat2 : ', kwadrat1 < kwadrat2)
print('Kwadrat2 <= Kwadrat1 : ', kwadrat2 < kwadrat1)
print('Kwadrat1 <= Kwadrat3 : ', kwadrat1 < kwadrat3)
print('Kwadrat3 <= Kwadrat1 : ', kwadrat3 < kwadrat1)
print('Kwadrat2 <= Kwadrat3 : ', kwadrat2 < kwadrat3)
print('Kwadrat3 <= Kwadrat2 : ', kwadrat3 < kwadrat2)