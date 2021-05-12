import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_excel ('datasets\imiona.xlsx')


zmienna=df.groupby(['Rok']).agg({'Liczba':['sum']})

print(zmienna)
zmienna.plot()
plt.show()