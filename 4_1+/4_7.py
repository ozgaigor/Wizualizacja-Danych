#Stwórz klasę Robot, która będzie sterować ruchami robota. Klasa powinna przechowywać współrzędne x, y, krok 
#(stała wartość kroku dla robota), i powinna mieć następujące metody:
#konstruktor – który nadaje wartość dla x, y i krok
#idz_w_gore(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe 
#wartości współrzędnych x i y
#idz_w_dol(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe 
#wartości współrzędnych x i y
#idz_w_lewo(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe 
#wartości współrzędnych x i y
#idz_w_prawo(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe
#wartości współrzędnych x i y
#pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne robota

#-------------------------------------------------------------------------------------------------------
class Robot:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
#-------------------------------------------------------------------------------------------------------
    def idz_w_gore(self, ile_krokow):
        self.y = self.y + ile_krokow*self.krok
#-------------------------------------------------------------------------------------------------------
    def idz_w_prawo(self, ile_krokow): 
        self.x = self.x + ile_krokow*self.krok
#-------------------------------------------------------------------------------------------------------
    def idz_w_dol(self, ile_krokow): 
        self.y = self.y - ile_krokow*self.krok
#-------------------------------------------------------------------------------------------------------
    def idz_w_lewo(self, ile_krokow): 
        self.x = self.x - ile_krokow*self.krok
#-------------------------------------------------------------------------------------------------------
    def pokaz_gdzie_jestes(self):
        print("Robot znajduje sie na pozycji ("+str(self.x), ", "+str(self.y),")")
#-------------------------------------------------------------------------------------------------------
print("Krok=1\n")
robot = Robot(0, 0, 1)
robot.pokaz_gdzie_jestes()
robot.idz_w_gore(17)
robot.pokaz_gdzie_jestes()
robot.idz_w_prawo(35)
robot.pokaz_gdzie_jestes()
robot.idz_w_dol(21)
robot.pokaz_gdzie_jestes()
robot.idz_w_lewo(37)
robot.pokaz_gdzie_jestes()
#-------------------------------------------------------------------------------------------------------