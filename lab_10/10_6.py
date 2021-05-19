# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8. 
# Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów stosowne etykiety. 
# Poustawiaj różne kolory dla wykresów.

# 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.
# 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla 
#            każdego roku z osobna. Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
# 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.

import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_excel ('datasets\imiona.xlsx')
#----------------------------------------------------------------------------------------
wykres = df.groupby(['Plec']).agg({'Liczba': 'sum'}).reset_index()
wykres2 = df.groupby(['Plec', 'Rok']).agg({'Liczba': 'sum'}).reset_index()
wykres3 = df.groupby(['Rok']).agg({'Liczba': 'sum'}).reset_index()
#----------------------------------------------------------------------------------------
plt.subplot(1, 3, 1)
plt.bar(wykres['Plec'], wykres['Liczba'], color=['orange', 'green'])
plt.xlabel('Plec')
plt.ylabel('Ilosc urodzen w mln.')
#----------------------------------------------------------------------------------------
plt.subplot(1, 3, 2)
plt.plot(wykres2['Rok'].unique(), wykres2[wykres2['Plec'] == 'K']['Liczba'], label='Kobiety', color='blue')
plt.plot(wykres2['Rok'].unique(), wykres2[wykres2['Plec'] == 'M']['Liczba'], label='Mężczyżni', color='pink')
plt.xlabel('Rok urodzenia')
plt.ylabel('Ilosc urodzen')
plt.legend()
#----------------------------------------------------------------------------------------
plt.subplot(1, 3, 3)
plt.bar(wykres3['Rok'], wykres3['Liczba'],color='magenta')
plt.xlabel('Rok urodzenia')
plt.ylabel('Ilosc urodzen')
#----------------------------------------------------------------------------------------
plt.show()
