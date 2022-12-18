import pandas as pd

dataframe1 = pd.read_excel('excelRows.xlsx', sheet_name='Sheet1', header=0)
print(dataframe1.iloc[-1])