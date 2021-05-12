import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_excel ('datasets\imiona.xlsx')


zmienna = df.agg({"Rok": ['max']})
zmienna1 = df[(df["Rok"] <= zmienna.values[0][0]) & (df["Rok"] > zmienna.values[0][0]-5)]
zmienna2 = zmienna1.groupby(['Plec']).agg({'Liczba': ['sum']})

wykres = zmienna2.plot.pie(subplots=True, autopct='%.2f %%',fontsize=20, figsize=(6, 6))

plt.title('liczba urodzonych chłopców i dziewczynek w ostatnich 5 latach')
plt.show()