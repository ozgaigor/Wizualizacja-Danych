import pandas as pd
import xlrd
import openpyxl

df = pd.read_excel(pd.ExcelFile("lab8\imiona.xlsx"), "Arkusz1")

print(df)
