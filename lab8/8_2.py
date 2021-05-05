import pandas as pd
import xlrd
import openpyxl

df = pd.read_excel ('lab8\imiona.xlsx')

#1
print('---------1----------')
print(df[df['Liczba'] > 1000])
print('---------2----------')
#2
print(df[df['Imie'] == 'IGOR'])
print('---------3----------')
#3
print(df.agg({'Liczba': ['sum']}))
print('----------4---------')
#4
ur = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
print(ur.agg({'Liczba': ['sum']}))
print('----------5---------')
#5
print(df.groupby(['Plec']).agg({'Liczba':['sum']}))
print('----------6---------')
#6
print('----------7---------')
#7
Kobiety = df[(df['Plec'] == 'K')]
Kobietymax = df[(df['Plec'] == 'K')].max()
print(Kobiety[(Kobiety['Liczba'] == Kobietymax['Liczba'])])

Mezszcyzni = df[(df['Plec'] == 'M')]
Mezszcyznimax = df[(df['Plec'] == 'M')].max()
print(Mezszcyzni[(Mezszcyzni['Liczba'] == Mezszcyznimax['Liczba'])])
print('--------------------')
