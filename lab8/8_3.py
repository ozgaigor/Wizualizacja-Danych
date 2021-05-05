import pandas as pd

df = pd.read_csv(r'C:\Programowanie Python\lab8\zamowienia.csv', header=0, delimiter=";")

print("-----1-----")
print(df.Sprzedawca.unique())
print("-----2-----")
print(df.sort_values('Utarg', ascending=False).iloc[:5])
print("-----3-----")
print(df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']}))
print("-----4-----")
