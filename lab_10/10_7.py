import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_excel ('datasets\imiona.xlsx')
wykres2 = df.groupby(['Plec', 'Rok']).agg({'Liczba': 'sum'}).reset_index()
plt.bar(wykres2['Rok'].unique(), wykres2[wykres2['Plec'] == 'M']['Liczba'], label='Mężczyżni', color='blue')
plt.bar(wykres2['Rok'].unique(), wykres2[wykres2['Plec'] == 'K']['Liczba'], label='Kobiety', color='pink',bottom=wykres2[wykres2['Plec'] == 'M']['Liczba'])
plt.xlabel('Rok urodzenia')
plt.ylabel('Ilosc urodzen')
plt.legend()

plt.xticks(wykres2['Rok'].unique(),rotation=90)
plt.show()