import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_excel ('datasets\imiona.xlsx')


zmienna= (df.groupby(['Plec']).agg({'Liczba':['sum']}))

print(zmienna)

wykres = zmienna.plot.bar()
wykres.set_ylabel('Liczba dzieci w milionach')
wykres.set_xlabel('Płeć')
wykres.legend()
plt.title('Liczba dziewczynek i chłopców w latach 2000-2017 ')
plt.show()