import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_csv("datasets\zamowienia.csv", header=0, delimiter=";")


zmienna=df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})

print(zmienna)
zmienna.plot()
plt.show()