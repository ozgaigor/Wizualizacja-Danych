import pandas as pd
import xlrd
import openpyxl

df = pd.read_excel(pd.ExcelFile("Datasets/imiona.xlsx"), "Arkusz1")

print(df)
